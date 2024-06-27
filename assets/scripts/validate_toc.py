# python3 validate_toc.py /home/franc/Github/test-mintlify/ /home/franc/Github/test-mintlify/mint.json


import os
import json

def load_navigation(mint_file):
    with open(mint_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data.get('navigation', [])

def check_paths(navigation, repo_root):
    valid_links = []
    invalid_links = []

    for group in navigation:
        for page in group.get('pages', []):
            file_path = os.path.join(repo_root, f"{page}.mdx")
            if os.path.isfile(file_path):
                valid_links.append(page)
            else:
                invalid_links.append(page)

    return valid_links, invalid_links

def log_results(valid_links, invalid_links):
    with open('valid_links.log', 'w+', encoding='utf-8') as file:
        for link in valid_links:
            file.write(f"Valid link: {link}.mdx\n")

    with open('invalid_links.log', 'w+', encoding='utf-8') as file:
        for link in invalid_links:
            file.write(f"Invalid link: {link}.mdx\n")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Check if MDX files listed in mint.json exist in the repository.")
    parser.add_argument('repo_root', type=str, help="Root directory of the GitHub repository.")
    parser.add_argument('mint_file', type=str, help="Path to the mint.json file.")

    args = parser.parse_args()

    navigation = load_navigation(args.mint_file)
    valid_links, invalid_links = check_paths(navigation, args.repo_root)
    log_results(valid_links, invalid_links)

    print(f"Valid links logged to valid_links.log")
    print(f"Invalid links logged to invalid_links.log")
