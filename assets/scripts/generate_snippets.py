# python3 generate_snippets.py ../../mint.json

import json
import sys

def generate_ahk(mint_file_path):
    # Read the redirects from mint.json
    with open(mint_file_path, 'r') as file:
        data = json.load(file)
        redirects = data['redirects']
        #print(redirects)

    # Open snippets_links.ahk in write mode to overwrite its contents
    with open('snippets_links.ahk', 'w') as file:
        for redirect in redirects:
            print(redirect)
            source = redirect['source']
            print(source)
            destination = redirect['destination']
            file.write(f"::{source}/::\n")
            file.write(f"SendInput {destination}\n")
            file.write("return\n\n")

    print("snippets_links.ahk file has been generated successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_ahk.py <path_to_mint.json>")
    else:
        mint_file_path = sys.argv[1]
        generate_ahk(mint_file_path)
