#!/usr/bin/env python3

import json
from json_creation import save_skills

def delete_skill():
    with open('skills.json', 'r') as f:
        skills = json.load(f)
    for i, skill in enumerate(skills):
        print(f"{i+1}. {skill['name']}")
    while True:
        try:
            skill_to_delete = int(input("Enter the number of the skill you want to delete: ")) - 1
            if skill_to_delete < 0 or skill_to_delete >= len(skills):
                raise ValueError("Invalid input. Please enter a number corresponding to a skill.")
            break
        except ValueError as e:
            print(e)
    del skills[skill_to_delete]
    save_skills(skills)
    print("Skill deleted successfully.")
    
    
if __name__ == "__main__":
    delete_skill()