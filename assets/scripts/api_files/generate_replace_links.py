import json

# Load the JSON file
with open('../../../mint.json', 'r') as file:
    data = json.load(file)

# Open the output text file in write mode
with open('config_internal_links_replacements.txt', 'w') as output_file:
    # Iterate through each redirect in the array
    for redirect in data.get('redirects', []):
        source = redirect.get('source', '')
        destination = redirect.get('destination', '')

        # Modify the source as specified
        modified_source = source.replace('/', '(', 1).replace('/', ':') + ' '

        # Write to the output file
        output_file.write(f"{modified_source}\t({destination}\n")

print("Redirects have been processed and written to redirects_output.txt")
