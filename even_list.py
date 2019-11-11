def find_pairs(values, target):
    for i in range(len(values)):
        for v in values:
            if values[i] + v == target:
                return values[i], v

print(find_pairs([7, 1, 1, 18, 1, 1, 4, 2], 11))
