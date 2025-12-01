def solution():
    reached_zero_amount = 0
    stored_elements = []
    starting_point = 50
    with open("input1.txt", "r") as lines:
        for line in lines:
            stored_elements.append(line.strip())
    for element in stored_elements:
        movement_amount = int(element[1:])
        direction = element[0]
        if direction == 'L':
            for i in range(movement_amount):
                starting_point -= 1
                if starting_point < 0:
                    starting_point = 99
        elif direction == 'R':
            for i in range(movement_amount):
                starting_point += 1
                if starting_point > 99:
                    starting_point = 0
        
        if starting_point == 0:
            reached_zero_amount += 1
    print(reached_zero_amount)


solution() # 1081