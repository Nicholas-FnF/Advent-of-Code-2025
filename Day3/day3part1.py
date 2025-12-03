def solution():
    total_output = []
    stored_lines = []
    batteries = []
    output = 0
    with open("input3.txt", "r") as lines:
        for line in lines:
            stored_lines.append(line.strip())
    # i've could've just used a stack like in part 2 after reading some hints, oh well
    for line in stored_lines:
        store = []
        prev = 0
        for i in range(len(line)):
            first_character = line[i]
            for j in range(i + 1, len(line)):
                second_character = line[j]
                combined = int(first_character + second_character)
                if combined > prev:
                    store.append(combined)
                    batteries.append(store)
                prev = combined
    batteries = [list(t) for t in {tuple(x) for x in batteries}]            
    for batteries_list in batteries:
        if len(batteries_list) == 1:
            total_output.append(batteries_list[0])
            continue
        total_output.append(max(batteries_list))
    for total_value in total_output:
        output += total_value
    print(output)


solution() # 17346