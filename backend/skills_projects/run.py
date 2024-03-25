#!/usr/bin/env python3

"""
Its used to run the api
"""
# project/run.py
from api.v1.app import app

if __name__ == '__main__':
    app.run(debug=True)
