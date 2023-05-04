import csv

def subway_info():
    f = open('202303_Seoul_Subway.csv', 'r', encoding='utf-8')
    data = csv.reader(f)
    next(data)

    subway_dict = {}
    for row in data:
        line = row[1]
        if line not in ['1호선', '2호선', '3호선', '4호선']:
            continue

        subway_dict.setdefault(line, [])

        subway_dict[line].append((row[3], int(row[4]) + int(row[5])))

    for line, stations in subway_dict.items():
        busiest_station = None
        busiest_count = 0
        least_busy_station = None
        least_busy_count = float('inf')

        for station, count in stations:
            if count > busiest_count:
                busiest_station = station
                busiest_count = count
            if count < least_busy_count:
                least_busy_station = station
                least_busy_count = count
                
        print(f"{line}:")
        print(f"Busiest Station: {busiest_station} ({busiest_count}명)")
        print(f"Least used Station: {least_busy_station} ({least_busy_count}명)")
        print()
        


    f.close()

if __name__ == "__main__":
    subway_info()
