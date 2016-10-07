import os
import sys


def are_files_duplicates(file_path_1, file_path_2):
    if not os.path.exists(file_path_1) and not os.path.exists(file_path_2):
        return None

    map_files_dir = {}
    for file_path in [file_path_1, file_path_2]:
        for root, _, files in os.walk(file_path):
            for name in files:
                path_file = os.path.join(root, name)
                size = os.path.getsize(path_file)
                naw_name = name + "#" + str(size)
                if naw_name not in map_files_dir.keys():
                    map_files_dir[naw_name] = [{"path": path_file}, {"size": size}, []]
                elif name in map_files_dir.keys() and size != map_files_dir[name][1]["size"]:
                    map_files_dir[naw_name] = [{"path": path_file}, {"size": size}, []]
                else:
                    map_files_dir[naw_name][2].append(path_file)
    return map_files_dir


def print_duplicated_file_names(map_files_dir):
    if map_files_dir:
        print("Duplicated files: ")
        for key, name in map_files_dir.items():
            if name[2]:
                file_name = key.split("#")[0]
                print("\nFile: " + file_name + " with size " + str(name[1]["size"])
                      + " bates is duplicated:")
                print(name[0]["path"])
                for path in name[2]:
                    print(path)
    else:
        print("Nothing to delete!")


if __name__ == '__main__':
    file_path1 = sys.argv[1]
    file_path2 = sys.argv[2]
    m = are_files_duplicates(file_path1, file_path2)
    print_duplicated_file_names(m)
