import glob
import os
import re
import shutil
import time


def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = "█" * int(percent) + "-" * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")


def get_root_folder():
    root_dir = input("[Source] Path to the folder with the files:\n").strip()
    return root_dir


def get_file_paths(root_dir):
    file_paths_filtered = []
    files = glob.iglob("**/*.*", root_dir=root_dir, recursive=True)

    for file in files:
        if re.search("[.](jpg|rw2|mp4)$", file, re.IGNORECASE):
            full_path = os.path.join(root_dir, file)
            file_paths_filtered.append(full_path)
    return file_paths_filtered


def set_output_folder():
    output_dir = input("[Destination] Path where the files will be copied and organized:\n").strip()
    return rf"{output_dir}"


def set_output_path(root_folder, file):
    modified_time = os.path.getmtime(file)
    time_struct = time.gmtime(modified_time)
    year = time_struct.tm_year
    month = time.strftime("%m_%b", time_struct)
    return os.path.join(root_folder, str(year), month)


def copy_to_path(input_file_paths):
    if not input_file_paths:
        print("No files to copy")
        return

    output_folder = set_output_folder()
    progress_bar(0, len(input_file_paths))
    for index, file_path in enumerate(input_file_paths):
        out_path = set_output_path(output_folder, file_path)
        try:
            os.makedirs(out_path, exist_ok=True)
            dest_path = os.path.join(out_path, os.path.basename(file_path))
            if not os.path.exists(dest_path):
                shutil.copy2(file_path, dest_path)
            progress_bar(index + 1, len(input_file_paths))
        except Exception as e:
            print(f"Warning!! file copy failed: {e}")
    print("\nFiles copied successfully!")


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    dir_2copy = get_root_folder()
    input_files = get_file_paths(dir_2copy)
    copy_to_path(input_files)
