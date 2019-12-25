import random
text = """
Welcome to lottery machine
"""
print(text)

column = int(input("Type the number of column "))
big_list = []
for i in range(0,column):
    small_list = []
    for i in range(0,6):
        rnd = random.randint(1,49)
        while rnd in small_list:
            rnd = random.randint(1,49)
        small_list.append(rnd)
    small_list.sort()
    big_list.append(small_list)
    big_list.sort()
print(*big_list,sep="\n")
print("Good luck!")

