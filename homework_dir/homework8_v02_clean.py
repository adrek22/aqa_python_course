""" Homework 8 """
import os

dir_name = os.path.dirname(__file__)
source_file = 'test_file.csv'
result_file = 'salaries_uah.csv'
source_file_path = os.path.join(dir_name, 'lesson8_test_folder', source_file)
result_file_path = os.path.join(dir_name, 'lesson8_test_folder', result_file)

exchange_rate_usd_to_uah = 39.16

with open(source_file_path) as infile_r, open(result_file_path, 'w') as outfile_w:
    source_file_data = infile_r.readlines()
    for line in source_file_data:
        if line.startswith(','):
            outfile_w.write(line)
        else:
            processed_line = line.split(",")
            for item in processed_line:
                try:
                    salary_usd = int(item)
                    salary_uah = salary_usd * exchange_rate_usd_to_uah
                    outfile_w.write("," + str(round(salary_uah, 2)))
                except ValueError:
                    outfile_w.write(item)
            outfile_w.write("\n")

with open(source_file_path) as infile_r, open(result_file_path) as outfile_r:
    source_file_data = infile_r.read()
    print(f'File {source_file} content with salary in $:\n{source_file_data}')
    print('-' * 100)  # Separator for better visualisation
    result_file_data = outfile_r.read()
    print(f'File {result_file} content with salary in UAH:\n{result_file_data}')
