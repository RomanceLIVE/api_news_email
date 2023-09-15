import requests

topic = "tesla"
api_key = "a693352cfdda4fe78f4cc555a67c4ba1"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2023-08-14&sortBy=publishedAt&apiKey={api_key}&language=en"

# Make request
request_url = requests.get(url)

# Check if the request was successful
if request_url.status_code != 200:
    print("Error: Failed to fetch data from the API.")
    print(f"Status code: {request_url.status_code}")
    print(f"Response content: {request_url.text}")
    exit(1)

# Get data in dictionary format
content = request_url.json()

# Print the entire content to understand its structure
print(content)

# Rest of your code to process the response and send emails...
