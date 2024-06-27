import os

# bash command:
# python3 rename_files.py config.txt /home/franc/Github/test-mintlify/api-reference
# python rename_files.py config.txt /path/to/search/directory

def load_config(config_file):
    rename_map = {}
    with open(config_file, 'r') as f:
        for line in f:
            search, replace = line.strip().split('\t')
            rename_map[search] = replace
            #print(rename_map)
    return rename_map

def rename_files(root_dir, rename_map):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            print(filename)
            if filename in rename_map:
                old_path = os.path.join(dirpath, filename)
                new_path = os.path.join(dirpath, rename_map[filename])
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} -> {new_path}')

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Rename files based on a tab-delimited config file.")
    parser.add_argument('config_file', type=str, help="Path to the tab-delimited config file.")
    parser.add_argument('root_dir', type=str, help="Root directory to start the search from.")

    args = parser.parse_args()

    rename_map = load_config(args.config_file)
    rename_files(args.root_dir, rename_map)
