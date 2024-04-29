""" Homework 8 """
import os


dir_name = os.path.dirname(__file__)
source_file = 'test_file.csv'
result_file = 'salaries_uah.csv'
source_file_path = os.path.join(dir_name, 'test_folder', source_file)
result_file_path = os.path.join(dir_name, 'test_folder', result_file)
exchange_rate_usd_to_uah = 39.16

with open(source_file_path) as infile_r, open(result_file_path, 'w') as outfile_w:
    header = infile_r.readline()
    outfile_w.write(header)
    for line in infile_r:
        processed_line = line.split(",")
        for i in range(1, len(processed_line)):
            salary_usd = int(processed_line[i])
            salary_uah = salary_usd * exchange_rate_usd_to_uah
            processed_line[i] = str(round(salary_uah, 2))
        converted_line = ','.join(processed_line)
        outfile_w.write(converted_line + "\n")


def display_file_contents(file_path, filename, currency):
    print(f'{filename} file content with salary in {currency}:')
    with open(file_path) as file:
        print(file.read())


display_file_contents(source_file_path, source_file, "$")
print('-' * 100)
display_file_contents(result_file_path, result_file, "UAH")
