using System;
using System.IO;
using System.Text.RegularExpressions;

class Program
{
    static void Main(string[] args)
    {
        // Get the directory path from the command-line arguments
        if (args.Length == 0)
        {
            Console.WriteLine("Usage: FileRenamer <directory_path>");
            return;
        }
        string directoryPath = args[0];

        // Get a list of files in the directory
        string[] files = Directory.GetFiles(directoryPath);

        // Iterate through each file and rename it
        foreach (string file in files)
        {
            // Get the current file name and extension
            string fileName = Path.GetFileNameWithoutExtension(file);
            string extension = Path.GetExtension(file);

            // Create a regular expression pattern to match the file name
            string pattern = "^.*\\d{3}$"; // Match any file name that ends with three digits
            Regex regex = new Regex(pattern);

            // Check if the file name matches the pattern
            if (regex.IsMatch(fileName))
            {
                // Generate a new file name
                string newFileName = fileName.Substring(0, fileName.Length - 3) + "_renamed" + extension;
                string newPath = Path.Combine(directoryPath, newFileName);

                // Rename the file
                File.Move(file, newPath);
                Console.WriteLine("Renamed {0} to {1}", file, newFileName);
            }
        }
    }
}