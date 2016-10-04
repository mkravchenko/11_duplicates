import os
import sys

map_of_deleted_files = {}


def are_files_duplicates(file_path_1, file_path_2):
    if not os.path.exists(file_path_1) and not os.path.exists(file_path_2):
        return None

    map_files_dir1 = get_map_of_files_and_delete_duplicates(file_path_1)
    map_files_dir2 = {}
    for root, _, files in os.walk(file_path_2):
        for name in files:
            path_file = os.path.join(root, name)
            size = os.path.getsize(path_file)
            if name in map_files_dir1.keys():
                if size == map_files_dir1[name]:
                    map_of_deleted_files[path_file] = size
                    os.remove(path_file)
            elif name in map_files_dir2:
                if size == map_files_dir2[name]:
                    map_of_deleted_files[path_file] = size
                    os.remove(path_file)
            else:
                map_files_dir2[name] = size


def get_map_of_files_and_delete_duplicates(file_path):
    map_files_dir1 = {}
    for root, _, files in os.walk(file_path):
        for name in files:
            path_file = os.path.join(root, name)
            size = os.path.getsize(path_file)
            if name not in map_files_dir1.keys():
                map_files_dir1[name] = size
            else:
                map_of_deleted_files[path_file] = size
                os.remove(path_file)
    return map_files_dir1


def print_duplicated_file_names(list_of_names):
    total_size = 0
    if list_of_names:
        print("Duplicated files was removed(file name, size):\n ")
        for name, size in list_of_names.items():
            total_size += size
            print(name, str(size) + " bates")
        print("\nTotal size is: {} bytes".format(total_size))
    else:
        print("Nothing to delete!")


if __name__ == '__main__':
    file_path1 = sys.argv[1]
    file_path2 = sys.argv[2]
    are_files_duplicates(file_path1, file_path2)
    print_duplicated_file_names(map_of_deleted_files)
