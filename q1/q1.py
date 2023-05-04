import csv


with open('2022_Seoul_Temp.csv', 'r', encoding='cp949') as f:
    data = csv.reader(f)
    next(data)  
    avg_temp = []
    min_temp = []
    max_temp = []
    for row in data:
        if row[2] == '' or row[3] == '' or row[4] == '':
            continue
        else:
            avg_temp.append(float(row[2]))
            min_temp.append(float(row[3]))
            max_temp.append(float(row[4]))
    avg_temp_mean = round(sum(avg_temp) / len(avg_temp), 2)
    min_temp_min = round(min(min_temp), 2)
    max_temp_max = round(max(max_temp), 2)
    print(f"Average Temperature : {avg_temp_mean} Celsius")
    print(f"Average Minimum Temperature: {min_temp_min} Celsius")
    print(f"Average Maximum Temperature: {max_temp_max} Celsius")

    
