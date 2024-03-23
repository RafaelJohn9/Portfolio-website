#!/usr/bin/python3

import json
import base64

# Read the image and encode it to base64
with open("./travelkenya.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

# Create a dictionary with the required data
data = {
    "name": "Travel Kenya",
    "url": "https://travel-kenya-mauve.vercel.app/",
    "image": encoded_string,
    "description": "Plan your dream vacation and discover the wonders of Kenya's diverse landscapes, wildlife, and culture. Immerse yourself in the rich history, vibrant traditions, and breathtaking scenery. Whether you're an adventure seeker or a nature enthusiast, Kenya has something extraordinary to offer."
}

# Write the data to a JSON file
with open("./travel_kenya.json", "w") as json_file:
    json.dump(data, json_file)