import random

def generate_tuple():
    number_one = random.randint(1,9)
    number_two = random.randint(1,9)
    result = number_one * number_two
    user_result = int(input(f"How much is {number_one} times {number_two}? "))

    while user_result != result:
            
        print("No. Please try again")
        user_result = int(input(f"How much is {number_one} times {number_two}? "))
    print("Very good!")
    generate_tuple()
   
generate_tuple()
