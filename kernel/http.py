import requests

# HTTP requests for the Kobash Kernel.

def get_online_string(website):
    return requests.get(website).text

