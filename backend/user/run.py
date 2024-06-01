#!/usr/bin/env python3
"""Official script to run this microservice"""
# run_gunicorn.py
import os
from dotenv import load_dotenv
from subprocess import run


# Load environment variables from .env file
load_dotenv('.api_keys.env')

# Run Gunicorn with your application
<<<<<<< Updated upstream
run(["gunicorn", "-b", "0.0.0.0:5000", "--chdir", "./api/v1", "app:app"])
=======
run(["gunicorn", "-b ",  " 0.0.0.0:5000 " " --chdir " "./api/v1 "," app:app "])
>>>>>>> Stashed changes
