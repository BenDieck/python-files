import os
import pandas
import sys

def handle_csv(current_file_name):
    current_data_frame = pandas.read_csv(current_file_name)
    print(current_data_frame.head())

def handle_py(current_file_name):
    with open(os.path.join(path, current_file_name)) as source_file:
        source_text = source_file.read()
        source_as_list = source_text.splitlines()
        line_count = 0
        for source_line in source_as_list:
            line_count += 1
            print(f"{line_count} {source_line}")
            if line_count >= 5:
                break
def handle_txt(current_file_name):
    with open(os.path.join(path, current_file_name)) as source_file:
        source_text = source_file.read()
        source_as_list = source_text.splitlines()
        for line_no, source_line in enumerate(source_as_list):
            print(source_line)
            if line_no >= 10:
                break

# region handle multiple file types
def handle_file(current_path, file_to_handle):
    current_file_name = os.path.join(current_path, file_to_handle)
    print(f"------- File {current_file_name} ---------")
    if file_to_handle.endswith('.csv'):
        handle_csv(current_file_name)
    elif file_to_handle.endswith('.py') :
        handle_py(current_file_name)
    elif file_to_handle.endswith('.txt'):
        handle_txt(current_file_name)
    else:
        print(f"Cannot handle file {file_to_handle}")

path = os.getcwd() if len(sys.argv) == 1 else sys.argv[1] 
print('The current path is', path)

listing = [file for file in os.listdir(path) if file.endswith('.csv') or file.endswith('.py') or file.endswith('.txt')]
listing = sorted(listing, key=str.lower)
for each_file in listing:
    handle_file(path, each_file)

# endregion
