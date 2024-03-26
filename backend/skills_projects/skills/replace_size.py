#!/usr/bin/env python3
"""
Fixes the problem with images not properly named
"""
import json
import collections

def replace_size():
    with open('./skills.json', 'r') as f:
        data = json.load(f)

    for item in data:
        images = item.get('images', {})
        sorted_images = collections.OrderedDict()

        # Convert keys to integers and sort
        size_keys = ['sm', 'md', 'lg', 'xl', '2xl']
        for i, key in enumerate(sorted(map(int, images.keys()))):
            if i < len(size_keys):
                sorted_images[size_keys[i]] = images[str(key)]
            else:
                print(f"Warning: No size key for index {i}. Skipping.")

        # Replace the old 'images' dictionary with the new one
        item['images'] = sorted_images

    # Save the JSON back to the file
    with open('./skills.json', 'w') as f:
        json.dump(data, f, indent=4)

replace_size()