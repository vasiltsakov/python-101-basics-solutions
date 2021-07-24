def in_range(x, y, matrix):
    min_x = 0
    max_x = len(matrix)
    min_y = 0
    max_y = len(matrix[0])

    in_range = x >= min_x and x < max_x and y >= min_y and y < max_y

    return in_range

def friends_configuration_layout(friends_configuration):

    fri_con_layout = {}

    fri_con_layout[friends_configuration[0]] = (0,0)

    for friend in range(1, len(friends_configuration)):

        name, position, relative_to = friends_configuration[friend]

        if position == "A":
            x, y = fri_con_layout[relative_to]
            fri_con_layout[name] = (-1 + x, 0 + y)
        elif position == "B":
            x, y = fri_con_layout[relative_to]
            fri_con_layout[name] = (1 + x, 0 + y)
        elif position == "R":
            x, y = fri_con_layout[relative_to]
            fri_con_layout[name] = (0 + x, 1 + y)
        elif position == "L":
            x, y = fri_con_layout[relative_to]
            fri_con_layout[name] = (0 + x, -1 + y)

    return fri_con_layout


def stranger_forms(cinema_layout, friends_configuration):

    cinema_layout_list = []

    for line in cinema_layout:
        cinema_layout_list.append(list(line))


    fri_con_layout = friends_configuration_layout(friends_configuration)

    for x in range(len(cinema_layout_list)):
        for y in range(len(cinema_layout_list[0])):


            all_friends_seat = True

            for name, position in fri_con_layout.items():
                fr_x, fr_y = position
                temp_x = x + fr_x
                temp_y = y + fr_y

                if not in_range(temp_x, temp_y, cinema_layout_list) or cinema_layout_list[temp_x][temp_y] == '*':
                    all_friends_seat = False
                    break
                else:
                    cinema_layout_list[temp_x][temp_y] = name

            if all_friends_seat:

                cinema_layout_temp = []
                for line in cinema_layout:
                    cinema_layout_temp.append(list(line))

                for name, position in fri_con_layout.items():
                    fr_x, fr_y = position
                    temp_x = x + fr_x
                    temp_y = y + fr_y
                    cinema_layout_temp[temp_x][temp_y] = name

                for line in cinema_layout_temp:
                    print(''.join(line))              
                print('----------')

cinema_layout = [
'..*...*.**',
'.....**...',
'*.*...*..*',
'.**....*.*',
'...*..*.*.',
'.***...*..',
'*......*.*',
'.....**..*',
'..*.*.*..*',
'***.*.**..'
]

friends_configuration = ["A", "BAA", "FRA", "CAB", "DRC", "EAD", "GLE"]

stranger_forms(cinema_layout, friends_configuration)