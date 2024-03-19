""" Homework 8 """
import os

dir_name = os.path.dirname(__file__)
# dir_name = os.path.abspath('') -> not stable usage if run form root working directory
# print(dir_name)

file_source = 'test_file.csv'
# file_path_source = dir_name + '/lesson8_test_folder/' + file_source
file_path_source = os.path.join(dir_name, 'lesson8_test_folder', file_source)
with open(file_path_source) as file_source_opened_r:
    file_source_data = file_source_opened_r.readlines()
    print(file_source_data)

dollar_change_course = 39

file_result = 'salaries_uah.csv'
file_path_result = dir_name + '/lesson8_test_folder/' + file_result
# file_path_result = os.path.join(dir_name, 'lesson8_test_folder', file_result)
with open(file_path_result, 'w') as file_result_opened_w:
    for line in file_source_data:
        if line.startswith(','):
            file_result_opened_w.write(line)
        else:
            print(line.split(","))
            processed_line = line.split(",")
            for item in processed_line:
                print(item)
                try:
                    item = int(item)
                    item *= dollar_change_course
                    file_result_opened_w.write("," + str(item))
                except ValueError:
                    file_result_opened_w.write(item)
            file_result_opened_w.write("\n")

with open(file_path_result) as file_result_opened_r:
    file_result_data = file_result_opened_r.read()
    print(file_result_data)
