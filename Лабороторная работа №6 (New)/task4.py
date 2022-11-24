import json

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.json"

def csv_to_list_dict(input_f) -> list[dict]:
    results = []
    with open(input_f,'r') as f:
        headers = f.readline()
        headers = headers.split(',')
        headers[len(headers)-1] = headers[len(headers)-1][:-1]
        for i in f:
            row = i.split(',')
            row[len(row)-1] = row[len(row)-1][:-1]
            new = {H:D for H,D in zip(headers,row)}
            results.append(new)

    return results

if __name__ == '__main__':
    print(json.dumps(csv_to_list_dict(INPUT_FILE), indent = 4))
