# 11_duplicates

This script searching, deleting and printing duplicate files from two directories and their child directories.<br />
In result user will have only one copy of file.<br /><br />

Rules of deleting files:<br />
1. Files will be deleted if they have same names(and extends) and same sizes.<br />
2. All duplicated files will be deleted in every directory and their child directories.<br />
Example (input directories dir1.1 and dir2.1):<br />
dir1.1->child_dir2.1->chid_dir3.1<br />
dir2.1->child_dir2.2->chid_dir2.3<br />
3. Files must be closed.<br />

# How to run:<br />
1. Run the script:<br />
python duplicates.py \<path_to_first_folder\> \<path_to_second_folder\><br />
2. Program will print the path and size(in bytes) for every deleted file <br />
or if duplicates not exists will print: "Nothing to delete!"


