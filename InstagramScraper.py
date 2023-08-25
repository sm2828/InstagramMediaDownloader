import instaloader
import os
import requests
import time

# Create an Instaloader instance
L = instaloader.Instaloader()

# Set user agent for requests
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

# Prompt the user for the Instagram username
username = input("Enter the Instagram username: ")

# Load the profile
profile = instaloader.Profile.from_username(L.context, username)

# Create a directory to save downloaded media
media_folder = username + "_media"
if not os.path.exists(media_folder):
    os.mkdir(media_folder)

# Iterate through the profile's posts
for post in profile.get_posts():
    try:
        media_url = None
        if post.typename == 'GraphSidecar':
            for index, sidecar_node in enumerate(post.get_sidecar_nodes()):
                if sidecar_node.is_video:
                    media_url = sidecar_node.video_url
                else:
                    media_url = sidecar_node.display_url
                if media_url:
                    response = requests.get(media_url, headers=headers)
                    if response.status_code == 200:
                        extension = "mp4" if sidecar_node.is_video else "jpg"
                        filename = os.path.join(media_folder, f"{post.date_utc}_{post.owner_username}_{index+1}.{extension}")
                        with open(filename, "wb") as media_file:
                            media_file.write(response.content)
                        print("Downloaded:", media_url)
                    else:
                        print("Failed to download:", media_url)
                    time.sleep(1)  
        else:
            if post.is_video:
                media_url = post.video_url
            else:
                media_url = post.url + "media/?size=l"
            if media_url:
                response = requests.get(media_url, headers=headers)
                if response.status_code == 200:
                    extension = "mp4" if post.is_video else "jpg"
                    filename = os.path.join(media_folder, f"{post.date_utc}_{post.owner_username}.{extension}")
                    with open(filename, "wb") as media_file:
                        media_file.write(response.content)
                    print("Downloaded:", media_url)
                else:
                    print("Failed to download:", media_url)
                time.sleep(1)  
    except Exception as e:
        print("Error:", e)

print("Download completed.")
