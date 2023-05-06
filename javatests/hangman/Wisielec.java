package org.example;
import java.util.List;
import java.util.Random;
import java.util.Arrays;
import java.util.Scanner;

public class Wisielec {
    List<String> words = List.of("cat", "dog", "cow");
    String word;
    char[] userWord;
    int lives = 3;

    //System.out.println("game starts");
    public void play() {
        Scanner scanner = new Scanner(System.in);

        Random random = new Random();
        //random.nextInt(bound: 4)
        word = words.get(random.nextInt(words.size()));
        //arrays need to have declared length
        userWord = new char[word.length()];
        Arrays.fill(userWord, '_');

        System.out.println(userWord);

        while(!gameEnded()) {
            System.out.println(userWord);
            System.out.println();
            System.out.println("Next letter please --> ");
            System.out.println("Remaining lifes: " + lives);
            // we do check the user  input validity this time
            char letter = scanner.nextLine().charAt(0);
            checkLetter(letter);
        }
        scanner.close();

        if (lives ==0) {
            System.out.println("Game Over!");
        } else {
            System.out.println("You did it!");
        }
    }
    private void checkLetter(char letter) {
        //System.out.println(letter);
        boolean foundLetter = false;
        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == letter) {
                userWord[i] = letter;
                foundLetter = true;
            }
        }
        if (!foundLetter) {
            System.out.println("Not in the word :( ");
            lives--;
        }
    }
    private boolean gameEnded() {
        return lives ==0 || word.equals(String.valueOf(userWord));
    }
}
