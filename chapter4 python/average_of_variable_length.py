
def average(first_number, *args): 

    addition = sum(args) + first_number
    length = len(args) + 1
    return addition / length

print(average(5))
