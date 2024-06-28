


#python3 replace_strings.py config_internal_links_replacements.txt /home/franc/Github/test-mintlify/ --exclude_dirs /home/franc/Github/test-mintlify/assets /home/franc/Github/node_modules


# python3 replace_strings.py config_strings.txt /home/franc/Github/test-mintlify/ --exclude_dirs /home/franc/Github/test-mintlify/assets

# python replace_strings.py config.txt /path/to/search/directory --exclude_dirs /path/to/search/directory/exclude1 /path/to/search/directory/exclude2 --extensions .md

# The script will load the configuration file, recursively search the specified directory for *.mdx and *.json files, exclude specified directories from the search, and replace the specified strings within those files.

import os
import argparse

def load_config(config_file):
    replace_map = {}
    with open(config_file, 'r') as f:
        for line in f:
            search, replace = line.strip().split('\t')
            replace_map[search] = replace
        #print(replace_map)
    return replace_map

def replace_in_file(file_path, replace_map):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    original_content = content

    for search, replace in replace_map.items():
        content = content.replace(search, replace)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Replaced strings in: {file_path}')
    #else:
        #print(f'No changes made to: {file_path}')

def replace_in_files(root_dir, replace_map, exclude_dirs, extensions):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Remove directories that need to be excluded from the search
        dirnames[:] = [d for d in dirnames if os.path.join(dirpath, d) not in exclude_dirs]

        for filename in filenames:
            if any(filename.endswith(ext) for ext in extensions):
                file_path = os.path.join(dirpath, filename)
                replace_in_file(file_path, replace_map)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Recursively search and replace strings in specified file extensions based on a tab-delimited config file.")
    parser.add_argument('config_file', type=str, help="Path to the tab-delimited config file.")
    parser.add_argument('root_dir', type=str, help="Root directory to start the search from.")
    parser.add_argument('--exclude_dirs', nargs='*', default=[], help="List of directories to exclude from the search, separated by spaces.")
    parser.add_argument('--extensions', nargs='+', default=['.mdx', '.json', '.yml'], help="List of file extensions to include in the search, separated by spaces.")

    args = parser.parse_args()

    replace_map = load_config(args.config_file)
    exclude_dirs = [os.path.abspath(d) for d in args.exclude_dirs]
    replace_in_files(os.path.abspath(args.root_dir), replace_map, exclude_dirs, args.extensions)
