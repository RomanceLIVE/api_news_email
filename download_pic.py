import requests

url = "https://banner2.cleanpng.com/20180712/cos/kisspng-learning-to-program-using-python-programming-langu-tic-tac-toe-logo-5b47098b6cd292.0915139615313821554458.jpg"

try:
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP errors
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    # You can handle the error here, e.g., exit the program or provide a message.

with open("image.jpg", "wb") as file:
    file.write(response.content)

# wb = write binary, to use on the image