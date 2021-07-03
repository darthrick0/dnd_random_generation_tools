import random




def roll_xd4(x):
    total = 0
    for i in range(x):
        dice_roll = random.randint(1,4)
        print("roll in xd4 = " + str(dice_roll))
        total += dice_roll
    return total

def roll_xd6(x):
    total = 0
    for i in range(x):
        dice_roll = random.randint(1,6)
        total += dice_roll
    return total

def roll_xd8(x):
    total = 0
    for i in range(x):
        dice_roll = random.randint(1,8)
        total += dice_roll
    return total

def roll_xd10(x):
    total = 0
    for i in range(x):
        dice_roll = random.randint(1,10)
        total += dice_roll
    return total

def roll_xd12(x):
    total = 0
    for i in range(x):
        dice_roll = random.randint(1,12)
        total += dice_roll
    return total

def roll_xd20(x):
    total = 0
    for i in range(x):
        dice_roll = random.randint(1,20)
        total += dice_roll
    return total

def roll_xd100(x):
    total = 0
    for i in range(x):
        dice_roll = random.randint(1,100)
        total += dice_roll
    return total







for x in range(10):
    val = roll_xd4(3)
    print("total roll = " + str(val))
print("----------------")
# for x in range(10):    
#     val = roll_1d6()
#     print("1d6: " + str(val))
# print("----------------")
# for x in range(10):
#     val = roll_1d8()
#     print("1d8: " + str(val))
# print("----------------")
# for x in range(10):
#     val = roll_1d10()
#     print("1d10: " + str(val))
# print("----------------")
# for x in range(10):
#     val = roll_1d12()
#     print("1d12: " + str(val))
# print("----------------")
# for x in range(10):
#     val = roll_1d20()
#     print("1d20: " + str(val))
# print("----------------")
# for x in range(10):
#     val = roll_1d100()
#     print("1d100: " + str(val))
# print("----------------")