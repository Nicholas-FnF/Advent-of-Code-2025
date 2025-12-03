def solution():
    stored_elements = []
    invalid_ids = []
    output = 0
    with open("input2.txt", "r") as lines:
        for line in lines:
            stored_elements.append(line.strip())
    stored_split = []
    for stored in stored_elements:
        split = stored.split(",")
        for s in split:
            if len(s) == 0:
                continue
            stored_split.append(s)
    for range_stored in stored_split:
        components = range_stored.split("-")
        first_id = int(components[0])
        last_id = int(components[1])
        string_format = str(f"{first_id}-{last_id}").split("-")
        for i in range(len(string_format)):
            if i < len(string_format) - 1:
                for j in range(first_id, last_id + 1):
                    current = str(j)
                    if len(current) % 2 != 0:
                        continue
                    half = len(current) // 2
                    left = current[:half]
                    right = current[half:]
                    if left == right:
                        invalid_ids.append(int(current))
    for invalid_id in invalid_ids:
        output += invalid_id
    print(output)


solution() # 28844599675