import os
import time
import glob
import re
import shutil


def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")


def get_root_folder():
    root_dir = input('What folder do you want to organize?\n')
    return root_dir


def get_file_paths(root_dir):
    file_paths_filtered = []
    files = glob.iglob('**/*.*', root_dir=root_dir, recursive=True)

    for file in files:
        if re.search('[.](jpg|rw2|mp4)$', file, re.IGNORECASE):
            full_path = os.path.join(root_dir, file)
            file_paths_filtered.append(full_path)
    return file_paths_filtered


def set_output_path(root_folder, file):
    modified_time = os.path.getmtime(file)
    time_struct = time.gmtime(modified_time)
    year = time_struct.tm_year
    month = time.strftime('%m_%b', time_struct)
    return f"{root_folder}\\{year}\\{month}"


def copy_to_path(input_file_paths):
    progress_bar(0, len(input_file_paths))
    for index, file_path in enumerate(input_file_paths):
        out_path = set_output_path('E:\\Photos', file_path)
        try:
            if not os.path.exists(os.path.join(out_path, file_path.split('\\')[-1])):
                os.makedirs(out_path, exist_ok=True)
                shutil.copy2(file_path, out_path)
            progress_bar(index+1, len(input_file_paths))
        except Exception as e:
            print(f"Warning!! file copy failed: {e}")
    print("\nFiles copied successfully!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dir_2copy = get_root_folder()
    input_files = get_file_paths(dir_2copy)
    copy_to_path(input_files)
