# File Name : groupimage.py
# Student Name: Justin Ganduri
# email: gandurpn@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 5/01/2025
# Course #: IS4010-001
# Semester: Spring 2025
# Brief Description: Stylish display of the team group photo with custom decoration
# Citations: ChatGPT + matplotlib documentation

from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def show_group_photo():
    try:
        image_path = os.path.join("data", "Final Project 1.jpg")
        img = Image.open(image_path)

        # Create figure and axis
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.imshow(img)
        ax.axis('off')  # Hide axis ticks

        # Title with style
        plt.title(" Final Project- Sheriff Finley Team ", fontsize=16, fontweight='bold', pad=20, color='#1A237E')

        # Optional: Add a border/frame
        border = patches.Rectangle(
            (0, 0), 1, 1, transform=ax.transAxes,
            linewidth=6, edgecolor='#283593', facecolor='none'
        )
        ax.add_patch(border)

        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print(f"Error: File not found at {image_path}")
    except Exception as e:
        print(f"Error displaying photo: {e}")
