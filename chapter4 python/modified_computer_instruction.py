
import random

def generate_tuple():
    number_one = random.randint(1,9)
    number_two = random.randint(1,9)
    
    pass1 = "Very good" 
    pass2 = "Nice work"
    pass3 = "Keep up the good work"

    fail1 ="No. Please try again"
    fail2 ="Wrong. Try once more"
    fail3 ="No. Keep trying"     
    

    while (True):
        user_result = int(input(f"How much is {number_one} times {number_two}? "))
        result = number_one * number_two
        #random.randint(1,3)
        if(result == user_result):
            if random.randint(1,3)==1:
                print(pass1)
            elif random.randint(1,3)==2:
                print(pass2)
            elif random.randint(1,3)==3:
                print(pass3)
            break
        elif (result != user_result):
            if random.randint(1,3) == 1:
                print(fail1)
            elif random.randint(1,3) == 2:
                print(fail2)
            elif random.randint(1,3) == 3:
                print(fail3)
               

generate_tuple()
