def calculate_temperature_difference():
    import csv
    f = open('2022_Seoul_Temp.csv', 'r', encoding='cp949')
    data = csv.reader(f)
    header = next(data) 

    max_diff = -9999 
    min_diff = 9999 
    max_date = '' 
    min_date = '' 

    for row in data:
        if '' in row: 
            continue
        date = row[0]
        low_temp = float(row[3])
        high_temp = float(row[4])
        diff = round(high_temp - low_temp, 2)

        if diff > max_diff:
            max_diff = diff
            max_date = date
        if diff < min_diff:
            min_diff = diff
            min_date = date

    f.close()

    print(f"Day with the Largest Temperature Variation:  {max_date}")
    print(f"Temperature Variation: {max_diff} Celsius ")
    print(f"Day with the Smallest Temperature Variation:  {min_date}")
    print(f"Temperature Variation: {min_diff} Celsius ")

if __name__ == "__main__":
    calculate_temperature_difference()
