import csv

def find_busiest_and_least_used_lines(passengers):
    f = open('202303_Seoul_Subway.csv', encoding='utf-8')
    data = csv.reader(f)
    for row in data:
        line_name = row[1]
        if line_name not in passengers:
            continue
        passengers[line_name] += int(row[4]) + int(row[5])
    f.close()
    
    sorted_passengers = sorted(passengers.items(), key=lambda x: x[1], reverse=True)

    most_used_lines = sorted_passengers[:2]
    least_used_lines = sorted_passengers[-2:]

    print('1st Busiest Line: {}({})'.format(most_used_lines[0][0], most_used_lines[0][1]))
    print('2nd Busiest Line: {}({})'.format(most_used_lines[1][0], most_used_lines[1][1]))

    print('\n1st Least used Line: {}({})'.format(least_used_lines[0][0], least_used_lines[0][1]))
    print('2nd Least used Line: {}({})'.format(least_used_lines[1][0], least_used_lines[1][1]))

if __name__ == "__main__":
    passengers = {'1호선': 0, '2호선': 0, '3호선': 0, '4호선': 0, '5호선': 0,
                  '6호선': 0, '7호선': 0, '8호선': 0, '9호선': 0}
    find_busiest_and_least_used_lines(passengers)
