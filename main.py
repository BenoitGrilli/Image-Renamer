import os
import json

# Path to the JSON and images folders
json_folder = "json"
images_folder = "images"

# Loop through each file in the JSON folder
for filename in os.listdir(json_folder):
    if filename.endswith(".json"):
        # Open the JSON file
        with open(os.path.join(json_folder, filename), "r") as f:
            json_data = json.load(f)
            # Get the DNA and UID from the JSON
            dna = json_data["dna"]
            uid = json_data["uid"]
            # Construct the old and new filenames for the image
            old_filename = os.path.join(images_folder, f"{dna}.png")
            new_filename = os.path.join(images_folder, f"{uid}.png")
            # Rename the file
            os.rename(old_filename, new_filename)
