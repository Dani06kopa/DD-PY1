import json

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.json"

def csv_to_list_dict(input_f) -> list[dict]:
    results = []
    rows = []
    date = []
    with open(input_f,'r') as f:
        i = 0
        headers = f.readline()
        for lines in f:
            #print(lines)
            rows += lines.split('\n')
            #print(rows)
        for i in rows:
            date += i.split(',')
            #print(date)
        headers = headers.split(',')
        headers[len(headers)-1] = headers[len(headers)-1][:-1]
    col = 0
    col1 = 0
    for i in date:
        if i == '':
            col += 1
        else:
            col1 += 1
    col1 = int(col1/col)
    k = i*col1
    for i in range(col):
        new = []
        k = i*col1
        if i>0:
            k += i
        new= {H:D for H,D in zip(headers,date[k:])}
        results.append(new)
    #print (results)
    return results


if __name__ == '__main__':
    print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
