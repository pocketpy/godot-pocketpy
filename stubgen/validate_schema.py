import json
import os
from dataclasses import asdict
from .schema import load_extension_api

def compare_files(file1, file2):
    with open(file1, 'r', encoding='utf-8') as fp1, \
         open(file2, 'r', encoding='utf-8') as fp2:
        json1 = json.load(fp1)
        json2 = json.load(fp2)
        print(f'Compare directly using dict: {json1==json2}')
        json1_byte = json.dumps(json1, ensure_ascii=False).encode('utf-8')
        json2_byte = json.dumps(json2, ensure_ascii=False).encode('utf-8')
        print(f'Compare directly using bytes: {json1_byte==json2_byte}')
        line = 0
        fp1.seek(0)
        fp2.seek(0)
        for line1, line2 in zip(fp1, fp2):
            line += 1
            if line1 != line2:
                print(f'{line} is different')
                return
        print('No difference found')


def remove_none_values(obj):
    if isinstance(obj, dict):
        new_dict = {}
        for key, value in obj.items():
            if value is not None:
                new_value = remove_none_values(value)
                new_dict[key] = new_value
        return new_dict
    elif isinstance(obj, list):
        return [remove_none_values(item) for item in obj]
    else:
        return obj


if __name__ == '__main__':
    filepath = 'godot-cpp/gdextension/extension_api.json'
    all_in_one = load_extension_api(filepath)
    cleared_none = remove_none_values(asdict(all_in_one))
    with open('tmp.json', 'w', encoding='utf-8', newline='') as fp:
        json.dump(cleared_none, fp, indent='\t', ensure_ascii=False)
        fp.write('\n')

    compare_files('tmp.json', filepath)
    os.remove('tmp.json')