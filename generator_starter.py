import random
import pandas
import os

#for now this will serve as a basic
#import relevent tables into pandas dataframes
# table_dataframe = pandas.read_excel('magic_item_tables.xlsx', sheet_name='Table A')
# num_rows_in_pandas = len(table_dataframe)
# print(str(num_rows_in_pandas))
# roll_for_row = roll_XdY_timesZ(1,num_rows_in_pandas,1)
# print(str(roll_for_row))
# print(table_dataframe.loc[roll_for_row+1])











def roll_XdY_timesZ(x, y, z):
    total = 0
    for i in range(x):
        dice_roll = random.randint(1,y)
        # print("roll in xdy*z = " + str(dice_roll))
        total += dice_roll
    total = total * z
    #error check
    # min_check = x * z
    # max_check = x * y * z
    # if min_check > total > max_check:
    #     total = -1

    return total

table_dataframe = pandas.read_excel('treasure_hoard_tables.xlsx', sheet_name='CR 17+', index_col='Roll')
num_rows_in_pandas = len(table_dataframe)
# table_dataframe.set_index('Roll', inplace=True, drop=True)

# print(table_dataframe)
# print(str(num_rows_in_pandas))
roll_for_row = roll_XdY_timesZ(1,num_rows_in_pandas,1)
print('random roll is: ' + str(roll_for_row))
# random_item = table_dataframe.loc[roll_for_row-1,'Item']



row = table_dataframe.loc[roll_for_row]

print(row)
print(row.size)
for x in range(row.size):
    print(row.get(x))
    print(type(row.get(x)))
    # print(type(str(row.get(entry))))
    output = str(row.get(x))

# print(output)

# row_as_list = row.Series.tolist()
# print(row_as_list)
# random_item = row_as_list[0, 1]
# random_item = table_dataframe.loc[row_index, 'Item']
# print(random_item)
# print('type of pandas output: ' + str(type(random_item)))

parser = argparse.ArgumentParser(description='Enter Challenge Rating and recieve rolled rewards')
parser.add_argument('CR', help='Enter and integer greater than or equal to 1', type=int)
args = parser.parse_args()
print(args.CR)


#---------------------------------------
def read_coin_table_entry(row):
    for cell in row:
        if cell != null:
            reward = coin_entry_parser(cell)
            print('reward') #incorporate header, based on column
    return -1

def coin_entry_parser(cell):
    string = str(cell)
    number_of_dice = string[0:string.find('d')]
    # dice_type = #d to x
    # multiplier = #x to cell.len()
    coin_total = roll_XdY_timesZ(number_of_dice, dice_type, multiplier)
    return coin_total

#---------------------------------------
def read_hoard_reward_entry(row):
    for cell in row:
        if cell != null:
            reward = hoard_entry_parser(cell)
            print('reward') #incorporate header, based on column
    return -1

def hoard_entry_parser(cell):
    # number_of_dice = #0 to d
    # dice_type = #d to x
    return -1

#---------------------------------------
def read_item_entry():
    return -1



# string = str('4d1x10')
# number_of_dice = string[0:string.find('d')]
# dice_type = string[string.find('d')+1:string.find('x')]
# multiplier = string[string.find('x')+1:len(string)]
# print('number of dice: ' + number_of_dice)
# print('type of dice: ' + dice_type)
# print('multiplier: ' + multiplier)
# total = roll_XdY_timesZ(int(number_of_dice), int(dice_type), int(multiplier))
# print(str(total))
