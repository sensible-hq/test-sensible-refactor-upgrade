# python3 check_redirs.py ../../mint.json

import requests
import json
import sys

def load_redirects(json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            return [redirect['source'] for redirect in data['redirects']]
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return []

def check_redirects(base_path, sources):
    results = []
    for source in sources:
        url = base_path + source
        try:
            response = requests.get(url, allow_redirects=True, timeout=5)
            results.append((url, response.url, response.status_code))
        except requests.exceptions.RequestException as e:
            results.append((url, None, str(e)))
    return results

def main(json_file_path):
    base_path = "https://sensible.mintlify.app"
    sources = load_redirects(json_file_path)
    urls = [base_path + source for source in sources]

    # Check redirects for the list of URLs
    results = check_redirects(base_path, sources)

    # Write the results to a text file
    with open("redirect_results.txt", "w+") as file:
        for result in results:
            file.write(f"{result}\n")

    print("Results have been written to redirect_results.txt")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_redirs.py <path_to_mint.json>")
    else:
        json_file_path = sys.argv[1]
        main(json_file_path)
