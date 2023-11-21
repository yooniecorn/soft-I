import random

while True: 
    with open("microservice.txt", "r") as file:
        file = file.read().strip()

        if file == 'go' :
        
            stat = random.randint(1, 30)
            modifier = float('-inf')

            print("stat: ", stat)

            if stat == 1: 
                modifier = -5
            if stat == 2 or stat == 3:
                modifier = -4
            if stat == 4 or stat == 5:
                modifier = -3
            if stat == 6 or stat == 7:
                modifier = -2
            if stat == 8 or stat == 9:
                modifier = -1
            if stat == 10 or stat == 11:
                modifier = 0
            if stat == 12 or stat == 13:
                modifier = 1
            if stat == 14 or stat == 15:
                modifier = 2
            if stat == 16 or stat == 17:
                modifier = 3
            if stat == 18 or stat == 19:
                modifier = 4
            if stat == 20 or stat == 21:
                modifier = 5
            if stat == 22 or stat == 23:
                modifier = 6
            if stat == 24 or stat == 25:
                modifier = 7
            if stat == 26 or stat == 27:
                modifier = 8
            if stat == 28 or stat == 29:
                modifier = 9
            if stat == 30:
                modifier = 10

            print("modifier: ", modifier)

            with open("microservice.txt", "w") as file: 
                file.write("stat: ")
                file.write(str(stat))

                file.write("\nmodifier: ")
                file.write(str(modifier))

                file.close()

