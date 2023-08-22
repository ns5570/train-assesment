import requests
import json

def get_numbers(urls):
    numbers = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            numbers.extend(response.json()["numbers"])
    return sorted(list(set(numbers)))

def main():
    """The main function."""
    urls = [
        "http://20.244.56.144/numbers/primes",
        "http://20.244.56.144/numbers/fibo",
        "http://20.244.56.144/numbers/odd",
        "http://20.244.56.144/numbers/rand"
    ]
    
    numbers = get_numbers(urls)
    print(json.dumps({"numbers": numbers}))

if _name_ == "_main_":
    main()