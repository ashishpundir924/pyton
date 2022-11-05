# task 2 for program for shopping list
option_1: str = input('To create a list type list, to call the saved list type call.')

data_base = {"supermarket": ['mike', 'chocolate', 'egg', 'cigarette'], "shopping_from_india": [], "shopping_for_india": [], "shopping_from_poland": []}

if option_1 == 'list':
    new_list = input("give a name of list:-")
    data_base[new_list] = []
    nuber_of_element = int(input("enter the number of item you want to add :- "))
    i = 0
    for x in range(5):

        data_base[x].update({new_list: [input("enter the item ")]})
    else:
        print(data_base)


elif option_1 == 'call':
    print("in progress")
    print(len(data_base))
    print(data_base.keys())
    show_list = input("Type list name to display the list:")
    f_print = (show_list)
    s_1 = data_base.fromkeys(f_print)
    print(s_1)












