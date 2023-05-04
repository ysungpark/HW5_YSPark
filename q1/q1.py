import csv

def calculate_temperature():
    f = open('2022_Seoul_Temp.csv', 'r', encoding='cp949')
    data = csv.reader(f)
    next(data)
    count = 0
    avg_temp_total = 0
    min_temp_min = 99999999
    max_temp_max = -9999999

    for row in data:
        if row[2] == '' or row[3] == '' or row[4] == '':
            continue
        else:
            avg_temp_total += float(row[2])
            min_temp_min = min(min_temp_min, float(row[3]))
            max_temp_max = max(max_temp_max, float(row[4]))
            count += 1

    avg_temp_mean = round(avg_temp_total / count, 2)
    min_temp_min = round(min_temp_min, 2)
    max_temp_max = round(max_temp_max, 2)

    print(f"Average Temperature : {avg_temp_mean} Celsius")
    print(f"Average Minimum Temperature: {min_temp_min} Celsius")
    print(f"Average Maximum Temperature: {max_temp_max} Celsius")

if __name__ == "__main__":
    calculate_temperature()
