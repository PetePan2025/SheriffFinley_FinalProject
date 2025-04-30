# File Name : main.py
# Student Name: Peter Phan, Peyton Bock
# email:  phanpv@mail.uc.edu, bockps@mail.uc.edu
# Assignment Number: Assignment Final Project
# Due Date:   5/01/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Write a program to decrypt a two files to uncover a provided UC location, movie title,
#                                       and movie quote.Then display what was decrypted and a photo of the location
# Brief Description of what this module does. Develop programs based on problem descriptions and pseudo-code
# Citations: Gemini: https://gemini.google.com/app
# Chatgpt: chat.com
# Anything else that's relevant:

from locationPackage.location import LocationDecrypter
from moviePackage.movie import MovieDecrypter
from groupimagePackage.groupimage import show_group_photo

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
    # --- Step 2: Decrypt the movie title ---
    movie_key = "gavGFv10Swqor9DHsLKPBkxN14rXEWj1PigAC8Dor-8="
    movie_file = "data/TeamsAndEncryptedMessagesForDistribution.json"
    team_name = "Sheriff Finley"

    movie_decrypter = MovieDecrypter(movie_key)
    decrypted_movie = movie_decrypter.decrypt_movie_title(movie_file, team_name)
    print(f"Decrypted Movie Title: {decrypted_movie}")

    show_group_photo()

