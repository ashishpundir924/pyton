# task 2 for program for shopping list


data_base = {"supermarket": ['mike', 'chocolate', 'egg', 'cigarette'], "shopping_from_india": [],
             "shopping_for_india": [], "shopping_from_poland": []}


def add_items() -> object:
    new_list = input("give a name of list:-")
    data_base[new_list] = [input("1:Enter the itme:-  "), input("2:Enter the itme:-  "), input("3:Enter the itme:- "),
                           input("4:Enter the itme:- ")]
    for x in data_base[new_list]:
        print(x)
    else:
        end = input('to save the list enter stop:- ')
        if end == 'stop':
            call_f()


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
    add_items()

elif option_1 == 'call':

    call_f()
