def gas_stations(distance, tank_size, stations):
    
    if tank_size > distance:
        return []

    result = []

    stations_km = []

    for station in stations:
        if distance > station:
            stations_km.append(station)

    # print(stations_km)

    len_stations = len(stations_km)

    if stations_km:

        stations_km.append(distance - stations_km[-1])


        for km in range(1,len_stations):
            stations_km[km] = stations[km] - stations[km-1]


        tank_size_temp = tank_size


        for stop in range(len_stations):
            tank_size_temp -= stations_km[stop]


            if tank_size_temp > stations_km[stop + 1]:
                pass
            elif tank_size < stations_km[stop + 1]:
                return []
            else:
                result.append(stations[stop])
                tank_size_temp = tank_size
    else:
        return stations_km


    return result




tests = [
    (320, 90, [50, 80, 140, 180, 220, 290], [80, 140, 220, 290]),
    (390, 80, [70, 90, 140, 210, 240, 280, 350], [70, 140, 210, 280, 350]),
    (100, 50, [10, 20, 30, 40, 50, 60, 70, 80, 90, 150], [40, 80]),
    (100, 101, [200], []),
    (100, 50, [200], []),
    (100, 50, [10, 90], [])
    ]

for dis, tank, stations, expected in tests:
    result = gas_stations(dis, tank, stations)

    print(result, result == expected)