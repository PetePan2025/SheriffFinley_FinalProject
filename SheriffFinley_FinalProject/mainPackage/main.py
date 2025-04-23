# File Name : main.py
# Student Name: Peter Phan,
# email:  phanpv@mail.uc.edu, 
# Assignment Number: Assignment Final Project
# Due Date:   5/01/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Write a program to decrypt a two files to uncover a provided UC location, movie title,
#                                       and movie quote.Then display what was decrypted and a photo of the location
# Brief Description of what this module does. Develop programs based on problem descriptions and pseudo-code
# Citations: Gemini: https://gemini.google.com/app
# Anything else that's relevant:

from locationPackage.location import LocationDecrypter

if __name__ == "__main__":
    encrypted_location_file = "EncryptedGroupHints Spring 2025.json"
    english_words_file = "UCEnglish.txt"

    # --- Step 1: Decrypt the location ---
    location_decoder = LocationDecrypter(english_words_file)
    decrypted_location = location_decoder.decrypt_location(encrypted_location_file)
    if decrypted_location:
        print(f"Decrypted Location: {decrypted_location}")
    else:
        print("Failed to decrypt the location.")
