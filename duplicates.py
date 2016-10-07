import os
import sys


def get_duplicates_files(file_path_1, file_path_2):
    if not os.path.exists(file_path_1) and not os.path.exists(file_path_2):
        return None

    map_files_dir = {}
    for file_path in [file_path_1, file_path_2]:
        for root, _, files in os.walk(file_path):
            for name in files:
                path_file = os.path.join(root, name)
                size = os.path.getsize(path_file)
                new_name = "File '{0}' with size {1} bytes".format(name, size)
                if new_name not in map_files_dir:
                    map_files_dir[new_name] = [path_file]
                else:
                    map_files_dir[new_name].append(path_file)
    return map_files_dir


def print_duplicated_file_names(map_files_dir):
    print("Duplicated files: ")
    for names, list_of_paths in map_files_dir.items():
        if len(list_of_paths) >= 2:
            print("\n{} is duplicated:".format(names))
            for path in list_of_paths:
                print("{}".format(path))


if __name__ == '__main__':
    file_path1 = sys.argv[1]
    file_path2 = sys.argv[2]
    duplicated_files = get_duplicates_files(file_path1, file_path2)
    print_duplicated_file_names(duplicated_files)
