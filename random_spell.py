import random
import pandas
import argparse
import sys

parser = argparse.ArgumentParser(description='Enter spell level (0-9) or provide no arguments to roll random spell')
parser.add_argument('-level', '--level', help='Enter spell level as an integer between 0 - 9, if left blank spell, a random spell of any level will be returned', type=int)
args = parser.parse_args()

def roll_XdY_timesZ(x, y, z):
    total = 0
    for i in range(int(x)):
        dice_roll = random.randint(1,int(y))
        # print("roll in xdy*z = " + str(dice_roll))
        total += dice_roll
    total = total * int(z)

    return total

if not args.level and args.level != 0:
    print('no arg given')
    # get all spells apend and roll
    # spell_dataframe = pandas.DataFrame()
    spell_excel = pandas.ExcelFile('spells.xlsx')
    spell_list =[]
    for x in spell_excel.sheet_names:
        print(x)
        spell_list.append(pandas.read_excel('spells.xlsx', sheet_name=x, index_col='Roll'))
        # individual_df =
    spell_dataframe = pandas.concat(spell_list, ignore_index=True)

elif 0 <= args.level <= 9:
    if args.level == 0:
        level_string = 'Cantrip'
        print('we got a cantrip')
    else:
        level_string = 'Level ' + str(args.level)
        print('0-9 selected')

    spell_dataframe = pandas.read_excel('spells.xlsx', sheet_name=level_string, index_col='Roll')
else:
    print("Enter valid spell level between 0 (Cantrip) - 9")
# print('These be the spells!!!!!')
# print(spell_dataframe)

roll = roll_XdY_timesZ(1, len(spell_dataframe.index), 1)
item = spell_dataframe.iloc[roll-1, 0]
print('random roll is: ' + str(roll))
print('item is: ' + item)
