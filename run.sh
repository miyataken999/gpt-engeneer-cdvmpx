#!/bin/bash

# Install dependencies
python -m pip install -r requirements.txt

# Run tests in parallel
python -m pytest tests/test_line_converter.py & 
python -m pytest tests/test_google_chat_formatter.py & 
python -m pytest tests/test_main.py &

# Wait for all tests to finish
wait
