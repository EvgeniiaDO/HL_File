from pprint import pprint

import os


file_path = os.path.join(os.getcwd(), "recipes.txt" )


with open(file_path, 'rt') as file:
    cook_book = {}
    for line in file:
        cook_name = line.strip()
        ingredient_count = int(file.readline())
        ingredient = []
        for i in range(ingredient_count):
            cook = file.readline()
            ingredient_name, quantity, measure = cook.strip().split(' | ')
            ingredient.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[cook_name] = ingredient
        file.readline()

pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    list_by_dishes1 = {}
    for i in dishes:
        if i in cook_book.keys():
            for n in cook_book[i]:
                if n['ingredient_name'] not in list_by_dishes1:
                    list_by_dishes1.setdefault(n['ingredient_name'], {'measure': n['measure'], 'quantity': int(n['quantity']) * person_count})
                else:
                    add_ = list_by_dishes1.pop(n['ingredient_name'])
                    list_by_dishes1.setdefault(n['ingredient_name'], {'measure': n['measure'], 'quantity': int(n['quantity'])* person_count + int(add_['quantity']) })

        else:
            print(f'Блюда {i} нет в кулинарной книге')
    return pprint((dict(sorted(list_by_dishes1.items()))))


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Каша'], 2)