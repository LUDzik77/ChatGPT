package org.example;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import java.util.UUID;

public class AddUUIDNamesToFiles {
    public static void main(String[] args) {

        String sourceDirectoryPath = "getUUIDnames";
        String destinationDirectoryPath = "createdUUIDnames";
        createDirectoryIfNotExists(sourceDirectoryPath);
        createDirectoryIfNotExists(destinationDirectoryPath);

        File sourceDirectory = new File(sourceDirectoryPath);
        File[] files = sourceDirectory.listFiles();

        if (files != null) {
            for (File file : files) {
                if (file.isFile()) {
                    // Generate a unique UUID
                    String uuid = UUID.randomUUID().toString();
                    String originalFileName = file.getName();
                    String fileExtension = getFileExtension(originalFileName);
                    String newFileName = originalFileName.replaceFirst("\\.", "__UUID__" + uuid + ".");
                    Path sourceFilePath = file.toPath();
                    Path destinationFilePath = new File(destinationDirectoryPath, newFileName).toPath();

                    try {
                        Files.move(sourceFilePath, destinationFilePath, StandardCopyOption.REPLACE_EXISTING);
                        System.out.println("Moved: " + originalFileName + " to: " + newFileName);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }
        }

        System.out.println("All files have been processed.");
    }

    private static void createDirectoryIfNotExists(String directoryPath) {
        File directory = new File(directoryPath);
        if (!directory.exists() && !directory.mkdirs()) {
            System.err.println("Failed to create directory: " + directoryPath);
        }
    }

    private static String getFileExtension(String fileName) {
        int lastIndex = fileName.lastIndexOf('.');
        if (lastIndex > 0) {
            return fileName.substring(lastIndex);
        }
        return "";
    }
}
