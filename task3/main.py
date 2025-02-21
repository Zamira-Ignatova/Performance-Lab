import sys
import json

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def fill_values(tests, values_dict):
    for test in tests:
        if 'id' in test:
            test_id = test['id']
            if test_id in values_dict:
                test['value'] = values_dict[test_id]
        if 'values' in test:
            fill_values(test['values'], values_dict)


def main():
    if len(sys.argv) != 4:
        print("Please enter the arguments in the following order: python <script_name>.py <values.json> <tests.json> <report.json>")
        return

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    values_data = read_json(values_file)
    tests_data = read_json(tests_file)

    values_dict = {item['id']: item['value'] for item in values_data['values']}
    fill_values(tests_data['tests'], values_dict)
    save_json(tests_data, report_file)
    print(f"The results is in the: {report_file}")


if __name__ == "__main__":
    main()
