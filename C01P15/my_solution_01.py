def gas_stations(distance, tank_size, stations):
    result = []

    len_stations = len(stations)

    stations_km = stations[:]
    print(stations)


    for km in range(1,len_stations):
        stations_km[km] = stations[km] - stations[km-1]

    print(stations_km)

    tank_size_temp = tank_size
    index = 0
    temp_i = 0




    for i, dis in enumerate(stations_km):

        print(f'tank size: {tank_size_temp}, distance: {dis}')


        if tank_size_temp > dis:
            temp_i = i
            tank_size_temp -= dis
        else:
            result.append(stations[temp_i])
            print(f'result: {result}')
            tank_size_temp = tank_size
            tank_size_temp -= dis


    return result




tests = [
    (320, 90, [50, 80, 140, 180, 220, 290], [80, 140, 220, 290]),
    # (390, 80, [70, 90, 140, 210, 240, 280, 350], [70, 140, 210, 280, 350]),
    # (100, 50, [10, 20, 30, 40, 50, 60, 70, 80, 90, 150], [40, 80]),
    # (100, 50, [10, 90], [])
    ]

for dis, tank, stations, expected in tests:
    result = gas_stations(dis, tank, stations)

    print(result, result == expected)