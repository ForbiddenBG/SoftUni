from os import walk

files_by_ext = {}
for _, _, files in walk("."):
    for file in files:
        extension = file.split(".")[-1]
        if extension not in files_by_ext:
            files_by_ext[extension] = []
        files_by_ext[extension].append(file)

with open("report.txt", "w") as output:
    for extension, files in sorted(files_by_ext.items()):
        output.write(f".{extension}\n")
        for file in sorted(files):
            output.write(f"--- {file}\n")


# from os import listdir, path
#
#
# def traverse_dir(current_path, files_by_ext):
#     for element in listdir(current_path):
#         if path.isdir(path.join(current_path, element)):
#             traverse_dir(path.join(current_path, element), files_by_ext)
#         else:
#             extension = element.split(".")[-1]
#             if extension not in files_by_ext:
#                 files_by_ext[extension] = []
#             files_by_ext[extension].append(element)
#
#
# files_by_ext = {}
# traverse_dir('.', files_by_ext)
#
# for ext, files in sorted(files_by_ext.items()):
#     print(f".{ext}")
#     for file in sorted(files):
#         print(f"--- {file}")
