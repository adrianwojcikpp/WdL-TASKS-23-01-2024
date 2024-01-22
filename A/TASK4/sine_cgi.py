#!/bin/python3.10
import json
import time
import math
import cgi

# Set the content type to JSON
print("Content-Type: application/json")
print()

# Get the current timestamp
timestamp = int(time.time())

# Calculate the sine wave value with a frequency of 600 seconds
frequency = 1 / 600  # Frequency in Hz
sine_wave_value = math.sin(2 * math.pi * frequency * timestamp)

# Map the sine wave value from the range [-1, 1] to [0, 1]
normalized_value = (sine_wave_value + 1) / 2

# Create the JSON structure
json_data = {
    "timestamp": timestamp,
    "value": normalized_value
}

# Print the JSON structure
print(json.dumps(json_data))
