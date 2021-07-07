def in_range(x, y, matrix):
    min_x = 0
    max_x = len(matrix)
    min_y = 0
    max_y = len(matrix[0])

    if_range = x >= min_x and x < max_x and y >= min_y and y < max_y

    return if_range

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


"""
The function should return a list of all possible placements, that satisfy the given form. 
This is basically a list of possible cinema layouts (structure the layouts the same way as the input)

Possible placement is a configuration where:

Our friends can book seats in the way they want.
They are not going outside of the cinema.
They are not taking any already reserved seats.

Lets break it down:

A - that's the first letter of the name of someone, who is going to be "central" for the configuration.
BAA - means - person with name B will be Above the person with name A.
FRA - means - person with name F will be Right of the person with name A.
CAB - means - person with name C will be Above the person with name B.
DRC - means - person with name D will be Right of person with name C.
EAD - means - person with name E will be Above the person with name D.
GLE means - person with name G will be Left of the person with name E.
Few things to consider:

The input will be correct - there won't be 2 people occupying the same place.
All names are going to be unique.
There won't be a configuration for someone not being previously introduced.

..*GE.*.**
...CD**...
*.*B..*..*
.**AF..*.*
...*..*.*.
.***...*..
*......*.*
.....**..*
..*.*.*..*
***.*.**..

..*...*.**
.....**...
*.*.GE*..*
.**.CD.*.*
...*B.*.*.
.***AF.*..
*......*.*
.....**..*
..*.*.*..*
***.*.**..

..*...*.**
.....**...
*.*...*..*
.**.GE.*.*
...*CD*.*.
.***B..*..
*...AF.*.*
.....**..*
..*.*.*..*
***.*.**..
"""