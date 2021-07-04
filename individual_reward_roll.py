import random
import pandas



def roll_XdY_timesZ(x, y, z):
    total = 0
    for i in range(x):
        dice_roll = random.randint(1,y)
        print("roll in xd4 = " + str(dice_roll))
        total += dice_roll
    total = total * z
    #error check
    min_check = x * x * z
    max_check = x * y * z
    if min_check < total < max_check:
        total = -1

    return total
#---------------------------------------
def read_coin_table_entry(row):
    for cell in row:

    return -1

#---------------------------------------
def read_hoard_reward_entry(row):
    for cell in row:

    return -1

#---------------------------------------
def coin_entry_parser(cell):
    return -1

#---------------------------------------
def hoard_entry_parser(cell):
    return -1

#---------------------------------------
def read_item_entry():
    
    return -1





for x in range(10):
    val = roll_xd4(3)
    print("total roll = " + str(val))
print("----------------")
