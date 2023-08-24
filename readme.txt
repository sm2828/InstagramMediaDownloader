# Instagram Image Downloader

This is a Python script that allows you to download images from an Instagram user's profile. The script uses the `instaloader` library for interacting with Instagram and the `requests` library for downloading images.

## Prerequisites

Before running the script, make sure you have the following:

- Python (3.6 or higher) installed on your system.
- Required libraries installed using the following command:

## Usage

1. Clone this repository to your local machine.

2. Open the script `download_images.py` in a text editor.

3. Replace the `username` variable with the Instagram username from which you want to download images.

4. Run the script using the following command:

5. The script will create a folder named `username_images` in the same directory and save the downloaded images there.

## Note

- The script handles both single-image posts and posts with multiple images (carousels).
- Images are saved with filenames containing the post's date, username, and index (for multiple-image posts).
- If there is a video in the post, it will download the thumbnail image of the video.

## Disclaimer

This script is provided for educational and personal use only. Please ensure that you respect copyright and intellectual property rights when using downloaded content.

Feel free to use, modify, and share the script as you like!

---

Author: Sean Neville
