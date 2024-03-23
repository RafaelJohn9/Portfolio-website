#!/usr/bin/env python3
import os
import json
import base64

class Skill:

    def __init__(self, name, images, direct_link, level, description):
        self.name = name
        self.images = images
        self.direct_link = direct_link
        self.level = level
        self.description = description
        self.status = self.set_status()

    def set_status(self):
        if self.level <= 2:
            return 'beginner'
        elif self.level <= 4:
            return 'intermediate'
        elif self.level <= 6:
            return 'advanced'
        elif self.level <= 8:
            return 'proficient'
        else:
            return 'native'

    def __repr__(self):
        return f"Skill(name={self.name}, images={self.images}, direct_link={self.direct_link}, level={self.level}, status={self.status}, description={self.description})"

    def __str__(self):
        return f"Skill {self.name} with direct link {self.direct_link} and level {self.level}"

    def to_dict(self):
        return {
            'name': self.name,
            'images': self.images,
            'direct_link': self.direct_link,
            'level': self.level,
            'status': self.status,
            'description': self.description
        }




def get_images(directory):
    images = os.listdir(directory)
    # Convert the third word in the image name to integer and sort
    images.sort(key=lambda img: int(img.split('-')[-1].split('.')[0]))

    encoded_images = {}
    for image in images:
        size = image.split('-')[-1].split('.')[0]  # Extract size from the image name
        with open(os.path.join(directory, image), 'rb') as img_file:
            encoded_image = base64.b64encode(img_file.read()).decode('utf-8')
            encoded_images[size] = encoded_image
            print(f"Key: {size}, Image: {image}")
    return encoded_images


def format_name(name):
    words = name.split('_')
    return ' '.join(word.capitalize() for word in words)

def get_skills():
    skills = []
    base_dir = './images'
    for dir_name in os.listdir(base_dir):
        formatted_name = format_name(dir_name)
        images = get_images(os.path.join(base_dir, dir_name))
        while True:
            try:
                level = int(input(f"Enter the level of skill {formatted_name} (name of the skill) from 1-10: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 10.")
        while True:
            try:
                description = input(f"Give a little description of the skill {formatted_name}: ")
                if not description:
                    raise ValueError("Description cannot be empty.")
                break
            except ValueError as e:
                print(e)
        while True:
            try:
                direct_link = input(f"Enter the direct link for the skill {formatted_name}: ")
                if not direct_link:
                    raise ValueError("Direct link cannot be empty.")
                break
            except ValueError as e:
                print(e)
        skill = Skill(formatted_name, images, direct_link, level, description)
        skills.append(skill.to_dict())
        save_skills(skills)  # Save skills to JSON after each skill is added
    return skills

def save_skills(skills):
    with open('skills.json', 'w') as f:
        json.dump(skills, f, indent=4)


if __name__ == "__main__":
    skills = get_skills()
    save_skills(skills)
