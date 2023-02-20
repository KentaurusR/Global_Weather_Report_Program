import requests

# API endpoint URL
endpoint_url = "https://api.thecatapi.com/v1/images/search"

# We need to set up the parameters for our API
params = {
    "limit": 1,
    "size": "full"
}

# Now, we need to send our API request
response = requests.get(endpoint_url, params=params)

# Now, we check the response status code
if response.status_code == 200:
    data = response.json()
    # If the response is okay, we will be able to retrieve the JSON data

    # Now, we want to retrieve the image URL from the JSON data
    if 'url' in data[0]:
        image_url = data[0]['url']
        print(f"Here's your random cat image: {image_url}")
        # The 'f' makes this a formatted string, it allows you to embed expression inside string literals using curly braces {}

else:
    print("The API request failed.")