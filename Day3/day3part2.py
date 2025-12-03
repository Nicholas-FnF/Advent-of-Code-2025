# i did read some hints online on how to tackle this problem lol
def solution():
    total_output = []
    stored_lines = []
    output = 0
    with open("input3.txt", "r") as lines:
        for line in lines:
            stored_lines.append(line.strip())
    for line in stored_lines:
        length = len(line)
        remove = length - 12
        stack = []
        for number in line:
            while stack and remove > 0 and stack[-1] < number:
                stack.pop()
                remove -= 1
            stack.append(number)
        result_digits = stack[:12]
        total_output.append(int("".join(result_digits)))        
    for total_value in total_output:
        output += total_value
    print(output)


solution() # 172981362045136