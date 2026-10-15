# Import required libraries
import requests
from datetime import datetime
import sys

# GitHub API URL
api_url = "https://api.github.com/users/octocat"

# Send GET request to the API
response = requests.get(api_url)

# Check if the API request was successful
if response.status_code == 200:

    # Convert API response into Python dictionary
    data = response.json()

    # Extract required information
    username = data["login"]
    user_id = data["id"]
    public_repos = data["public_repos"]
    followers = data["followers"]

    # Record current date and time
    fetch_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get current Python version
    python_version = sys.version.split()[0]

    # Display extracted information
    print("======================================")
    print("Student Information API Tracker")
    print("======================================")
    print("API Request Successful!")
    print()
    print("Username              :", username)
    print("User ID               :", user_id)
    print("Public Repositories   :", public_repos)
    print("Followers Count       :", followers)
    print("Fetch Date & Time     :", fetch_time)
    print("Python Version        :", python_version)

    # Save information into api_log.txt
    with open("api_log.txt", "w") as file:
        file.write("GitHub API Data Log\n")
        file.write("-------------------\n")
        file.write(f"Username: {username}\n")
        file.write(f"User ID: {user_id}\n")
        file.write(f"Public Repositories: {public_repos}\n")
        file.write(f"Followers Count: {followers}\n")
        file.write(f"Fetch Date & Time: {fetch_time}\n")
        file.write(f"Python Version: {python_version}\n")

    print()
    print("Data saved successfully to api_log.txt")

    # Read and display saved data
    print()
    print("Saved Data:")
    print("-----------")

    with open("api_log.txt", "r") as file:
        saved_data = file.read()

    print(saved_data)

else:
    print("API request failed.")
    print("Status Code:", response.status_code)