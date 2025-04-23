# File Name : location.py
# Student Name: Peter Phan
# email:  phanpv@mail.uc.edu
# Assignment Number: Assignment Final Project
# Due Date:   5/01/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Write a program to decrypt a two files to uncover a provided UC location, movie title,
#                                       and movie quote.Then display what was decrypted and a photo of the location
# Brief Description of what this module does. Develop programs based on problem descriptions and pseudo-code
# Citations: Gemini: https://gemini.google.com/app
# Anything else that's relevant:

import json
import os

class LocationDecrypter:
    def __init__(self, english_text_file):
        """
        Initializes the LocationDecrypter with the path to the English text file.

        Args:
            english_text_file (str): Path to the text file containing the word list.
        """
        self.english_text_file = english_text_file
        self.word_list = self._load_word_list()

    def _load_word_list(self):
        """Loads the word list from the English text file."""
        try:
            filepath = os.path.join("data", self.english_text_file)
            with open(filepath, 'r') as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            print(f"Error: English text file not found at {filepath}")
            return []
        except Exception as e:
            print(f"An error occurred while loading the word list: {e}")
            return []

    def decrypt_location(self, encrypted_data_file):
        """
        Decrypts the location data from a JSON file using indices associated with "Norman Dale".

        Args:
            encrypted_data_file (str): Path to the JSON file containing encrypted location data.

        Returns:
            str: The decrypted location string, or None if an error occurs.
        """
        if not self.word_list:
            return None

        try:
            filepath = os.path.join("data", encrypted_data_file)
            with open(filepath, 'r') as f:
                encrypted_data = json.load(f)
                if isinstance(encrypted_data, dict) and "Norman Dale" in encrypted_data:
                    indices = encrypted_data["Norman Dale"]
                    decrypted_location_parts = []
                    for index_str in indices:
                        try:
                            index = int(index_str)
                            if 0 <= index < len(self.word_list):
                                decrypted_location_parts.append(self.word_list[index])
                            else:
                                print(f"Warning: Index {index} out of bounds in {self.english_text_file}.")
                                return None
                        except ValueError:
                            print(f"Warning: Invalid index '{index_str}' found in encrypted data.")
                            return None
                    return " ".join(decrypted_location_parts)
                else:
                    print("Error: Unexpected structure in encrypted location data.")
                    return None

        except FileNotFoundError:
            print(f"Error: Encrypted data file not found at {filepath}.")
            return None
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in {filepath}.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred during location decryption: {e}")
            return None