#!/usr/bin/env python3

import json
import pathlib


def check_exist_json_file(p_fname):
    """
    Function check that file exists
    :param p_fname: json filename
    :return: True or False
    """
    if pathlib.Path(p_fname):
        return True
    else:
        return False


def load_dict_from_json_file(p_fname):
    """
    Function transform json to dict
    :param p_fname: json filename
    :return: dict of json or ["Error"]
    """
    try:
        with open(p_fname, 'r') as f_json:
            decode_json = json.load(f_json)
        f_json.close()
    except (ValueError, KeyError, TypeError):
        decode_json = ["Error"]
    return decode_json


def print_dict_from_json(p_dict):
    """
    Print json dict to console
    :param p_dict: json dict
    :return:
    """
    for person_item in p_dict['person']:
        if person_item['kind'] == 'man:':
            print("Род: мужчина")
        else: print("Род: женщина")
        for info_item in person_item['info']:
            print("Фамилия:", info_item['surname'])
            print("Имя:", info_item['name'])
            if info_item['married']:
                print("Гражданин был женат/замужем")
            else:
                print("Гражданин не был женат/замужем")
            if info_item['children'] > 0:
                print("У гражданина есть дети")
            else:
                print("У гражданина нет детей")
        print("--------")


def write_dict_to_json_file(p_fname, p_dict):
    """

    :param p_fname:
    :param p_dict:
    :return:
    """
    add_to_p_dict = {"type": "human", "kind": "woman", "info": [{"surname": "Петрова", "name": "Алена", "married": False, "children": 1}]}
    p_dict['person'].append(add_to_p_dict)
    try:
        with open(p_fname, 'w') as f_json:
            json.dump(p_dict, f_json, indent=2, ensure_ascii=False)
        f_json.close()
    except (ValueError, KeyError, TypeError):
        pass


def main():
    """
    Main function
    :return:
    """
    file_name = 'person.json'

    if check_exist_json_file(file_name):
        dict_json = load_dict_from_json_file(file_name)
        if dict_json != ["Error"]:
            print("Вывод содержимого входного json-файла:")
            print_dict_from_json(dict_json)
            write_dict_to_json_file(file_name, dict_json)
        else:
            print("Cодержимое входного json-файла не может быть распечатано из-за возникшей ошибки!")


if __name__ == '__main__':
    main()
