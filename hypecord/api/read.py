import requests

# Fetch JSON data from URL
url = 'http://api.icey.fr/keys/api.json'
response = requests.get(url)
data = response.json()

# Read 5 letter string from user input
key = input("Enter the 5 letter string: ")

# Check if the key exists in the JSON data
if key in data:
    # If the key exists, print the activation code
    print(f"Activation code for {key}: {data[key]['activation']}")
else:
    # If the key doesn't exist, print an error message
    print(f"Error: {key} is not a valid key.")
