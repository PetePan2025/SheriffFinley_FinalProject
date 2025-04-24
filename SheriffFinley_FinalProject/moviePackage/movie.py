# File Name : movie.py
# Student Name: Peyton Bock
# email:  bockps@mail.uc.edu
# Assignment Number: Assignment Final Project
# Due Date:   5/01/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Write a program to decrypt a two files to uncover a provided UC location, movie title,
#                                       and movie quote.Then display what was decrypted and a photo of the location
# Brief Description of what this module does. Develop programs based on problem descriptions and pseudo-code
# Citations: ChatGPT: chat.com
# Anything else that's relevant:
from cryptography.fernet import Fernet
import json

class MovieDecrypter:
    def __init__(self, key: str):
        self.fernet = Fernet(key.encode())

    def decrypt_movie_title(self, filepath: str, team_name: str) -> str:
        with open(filepath, 'r') as file:
            encrypted_data = json.load(file)
        encrypted_message = encrypted_data.get(team_name)[0]
        decrypted_bytes = self.fernet.decrypt(encrypted_message.encode())
        return decrypted_bytes.decode()

