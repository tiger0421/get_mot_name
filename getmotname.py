import os
import re

def main():
    input_path = "./rireki.txt"

    with open(input_path) as f:
        grep_lines = [line.strip() for line in f if len(re.findall(r'SJ_\D*\d{4,8}.mot', line, re.IGNORECASE)) > 0]

    result_dict = {}
    for line in grep_lines:
        mot_name = re.findall(r'SJ_\D*\d{4,8}.mot', line, re.IGNORECASE)[0]
        mot_update_date = re.findall(r'\d{4,8}', line)[0]
        ref_name = re.sub(r'\d{4,8}.mot', '', mot_name)

        if(ref_name in result_dict):
            if(dict_is_new(result_dict[ref_name], line)):
                continue

        result_dict[ref_name] = line

    for result in result_dict.values():
        print(result)


def get_update_date(line):
    mot_update_date = re.findall(r'\d{4,8}', line)[0]
    return mot_update_date


def dict_is_new(result_dict_line, new_line):
    return get_update_date(result_dict_line) > get_update_date(new_line)


if __name__ == '__main__':
    main()
