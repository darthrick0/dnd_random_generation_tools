# dnd_random_generation_tools
These utilities will use python and Excel tables to generate loot and perform other functions that are useful for Dungeon Masters. 

I’ve chosen to use Excel files over other data storage so that a user can easily edit the tables and add more content if they wish. In this same spirit, the coding involved will be constructed such a way that it is easily readable for novices.

It is my intent to expand this toolset to perform a variety of functions listed in the Dungeon Master’s guide. It will also be filled with utilities that I use in my own campaigns to simulate activities and events. 

If you download this, I hope it serves you well. Feel free to message me with questions or if you want contribute to the project. If you want to use the content here, I request you credit myself and provide a link to the repository.

--------------------------------------------
































Project Notes:

Required modules:
Pandas



Hoard Treasure tables:
The Gem and Art object tables are expanded such that a single roll can be used. 

Gem Table: Expanded to 120 rows instead of  4, 6, 8, 10, and 12 entries. The entries for the tables duplicated, preserving the original probability.

Art Object Table: Expanded to 40 rows instead of 10 and 8. The entries for the tables duplicated, preserving the original probability



Code Notes:

gem_entry_interpreter function in hoard_reward_roll.py: I tried to keep out of the strictly number based indexing of columns for readability's sake, but this one merited using index based searches. 





Notes on expanding tables:

the gem and art object tables are dependent on having the same number of entries in each column. It is fine if you change up entries in the tables or add rows, but if you are going to change the number of entries and add rows, ensure they match the current number of rows in the respective table. If necessary determine the least common denominator if you would like to use a different roll (d3 or d7...)
