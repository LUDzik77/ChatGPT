using System;

namespace PasswordGenerator
{
    class Program
    {
        static void Main(string[] args)
        {
            // Set up the character sets for the password
            string lowercaseChars = "abcdefghijklmnopqrstuvwxyz";
            string uppercaseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            string numericChars = "0123456789";
            string specialChars = "!@#$%^&*()_+-=[]{}|;:,.<>?";

            // Combine the character sets into one string
            string allChars = lowercaseChars + uppercaseChars + numericChars + specialChars;

            // Get the length of the password from the user
            Console.Write("Enter the length of the password: ");
            int passwordLength = int.Parse(Console.ReadLine());

            // Generate a random password using the character sets
            Random random = new Random();
            char[] passwordChars = new char[passwordLength];
            for (int i = 0; i < passwordLength; i++)
            {
                int index = random.Next(allChars.Length);
                passwordChars[i] = allChars[index];
            }
            string password = new string(passwordChars);

            // Display the password to the user
            Console.WriteLine("Your password is: " + password);
            Console.ReadLine();
        }
    }
}