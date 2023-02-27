from functions import *

#create a list of list of shrooms, divided into cathegories
shroom_cathegories = []
for urls in DICT:
    shroom_cathegories.append(Soup_like.list_of_cat_shrooms(DICT[urls]) )

for el in shroom_cathegories:
    for elem in el:
        print(str(elem))

Soup_like.html_table_browser(shroom_cathegories[1][0])
