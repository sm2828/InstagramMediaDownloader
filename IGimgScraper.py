import instaloader
import os
import requests

# Create an Instaloader instance
L = instaloader.Instaloader()

# Replace with the Instagram username you want to download from
username = ''

# Load the profile
profile = instaloader.Profile.from_username(L.context, username)

# Create a directory to save downloaded images
image_folder = username + "_images"
if not os.path.exists(image_folder):
    os.mkdir(image_folder)

# Iterate through the profile's posts
for post in profile.get_posts():
    try:
        if post.typename == 'GraphSidecar':  # Check if the post has multiple images
            for index, sidecar_node in enumerate(post.get_sidecar_nodes()):
                image_url = sidecar_node.display_url
                response = requests.get(image_url)
                if response.status_code == 200:
                    filename = os.path.join(image_folder, f"{post.date_utc}_{post.owner_username}_{index+1}.jpg")
                    with open(filename, "wb") as img_file:
                        img_file.write(response.content)
                    print("Downloaded:", image_url)
                else:
                    print("Failed to download:", image_url)
        else:
            image_url = post.url + "media/?size=l"  # Get the image URL
            response = requests.get(image_url)
            if response.status_code == 200:
                filename = os.path.join(image_folder, f"{post.date_utc}_{post.owner_username}.jpg")
                with open(filename, "wb") as img_file:
                    img_file.write(response.content)
                print("Downloaded:", image_url)
            else:
                print("Failed to download:", image_url)
    except Exception as e:
        print("Error:", e)

print("Download completed.")
