# task 2 for program for shopping list


data_base = {"supermarket": ['mike', 'chocolate', 'egg', 'cigarette'], "shopping_from_india": [],
             "shopping_for_india": [], "shopping_from_poland": []}


def add_items(items):
    return data_base.update({new_list: [items]})


def call_f():
    print('The total number of shopping list:- ', len(data_base))
    for key in data_base.keys():
        print(key)
    else:
        show_list = input("Type list name to display the items:")
        for it in data_base[show_list]:
            print(it)


option_1: str = input('To create a list type list, to call the saved list type call. :- ')

if option_1 == 'list':
    new_list = input("give a name of list:-")
    data_base[new_list] = []

    for x in range(3):

        items1 = input("enter i")
        add_items(items1)
    else:
        for x in data_base[new_list]:
            print('you items is added:-', x)
        else:
            end = input('To save Enter stop:-')
            if end == 'stop':
                print('thanks you added all items')
                call_f()


elif option_1 == 'call':
    call_f()
