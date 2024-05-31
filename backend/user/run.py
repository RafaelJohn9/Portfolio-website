#!/usr/bin/env python3
"""Official script to run this microservice"""
# run_gunicorn.py
import os
from dotenv import load_dotenv
from subprocess import run


# Load environment variables from .env file
load_dotenv('.env')

# Run Gunicorn with your application
run(["gunicorn", "-b", "0.0.0.0:5000", "--chdir", "./api/v1", "app:app"])
