#!/usr/bin/env python3

import json
from json_creation import Skill, get_images, save_skills, format_name
import os
import sys



def add_skill(directory):
    try:
        formatted_name = format_name(directory)
        images = get_images(os.path.join('./images', directory))
    except Exception as e:
        print(f"Error occurred while formatting name or getting images: {e}")
        return

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

    try:
        skill = Skill(formatted_name, images, direct_link, level, description)
        with open('skills.json', 'r') as f:
            skills = json.load(f)
        skills.append(skill.to_dict())
        save_skills(skills)
    except Exception as e:
        print(f"Error occurred while creating skill or saving skills: {e}")


if __name__ == "__main__":
    print("Make sure your dir containing images has 5 images else change this requirement in the source code")
    print("Your dir should be located inside ./images")
    print("Then pass  your dir name as the second argument  as you execute this script")
    add_skill(sys.argv[1])
