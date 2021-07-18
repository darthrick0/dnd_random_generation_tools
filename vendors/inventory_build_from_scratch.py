import pandas


# set up spreadsheet sheets for each vendor on the island
# check each sheet for type of vendors

# buy function
    # if gold value is high, try to buy item (buy rare/expensive items first)
    # if max number of items is reached, do not buy
        # need only 2 sets of plate armor
        # only need 5 lamps
        # how to balance max number of items
            # >=500: 2
            # >= 25: 3
            # >=2: 5
            # else 10

# if sheet_name.contains('Blacksmith')
# elif sheet_name.contains('General Store')
# elif sheet_name.contains('Leatherworker')
# elif sheet_name.contains('Fletcher')
# elif sheet_name.contains('Adventuring Store')
# elif sheet_name.contains('Dock')
# elif sheet_name.contains('Magic Shop')
# elif sheet_name.contains('Temple')
# elif sheet_name.contains('Bank')
# elif sheet_name.contains('Arts and Games')
# elif sheet_name.contains('Tailor')
# elif sheet_name.contains('Jeweler')
# elif sheet_name.contains('Alchemist')


# for each vendors
    # open relevent vendor inventory spreadsheet
    # allocate gold value for vendor of type
        # get gold values for all items
        # generate probability for aquiring items (higher gold value = less chance of appearing)
        # roll for inventory based on adjusted priority
        # append each item rolled
        # open island vendors spreadsheet
        # write list to inventory



# for file in current_dir.rglob('*.xlsx'):
#     current_excel = pandas.ExcelFile(file)
#     for x in current_excel.sheet_names:
#         print(x)
#         current_dataframe = pandas.read_excel(file, sheet_name=x)
#         print(current_dataframe)
#         current_json = current_dataframe.to_json(str(file_index)+'.json',indent=4)
#
#         print(current_json)
#         file_index = file_index + 1
