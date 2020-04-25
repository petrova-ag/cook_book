from pprint import pprint


def cookbook():
    cook_book = {}
    with open('cookbook.txt', encoding='utf-8') as f:
        while True:
            list_for_cookbook = []
            dish = f.readline().strip()
            if not dish:
                break
            # print(dish)
            try:
                number_of_ingridients = int(f.readline().strip())
            except ValueError:
                pass
            except IndexError:
                pass
            # print(number_of_ingridients)
            for lines in range(0, number_of_ingridients):
                current_dish = dish
                ingridients = f.readline().strip().split(' |')
                # print(ingridients)
                ingridients_dict = {}
                try:
                    ingridients_dict['ingridient_name'] = ingridients[0]
                    ingridients_dict['quantity'] = int(ingridients[1])
                    ingridients_dict['measure'] = ingridients[2]
                except IndexError:
                    pass
                list_for_cookbook.append(ingridients_dict)
                cook_book[current_dish] = list_for_cookbook
            f.readline()
    return cook_book


def get_shop_list_by_dishes(dish, person_count):
    list_of_ingridients = {}
    cook_book = cookbook()
    for elements in dish:
        if elements in cook_book.keys():
            for points in cook_book[elements]:
                quantities_and_measures = {}
                quantities_and_measures['quantity'] = points['quantity'] * person_count
                quantities_and_measures['measure'] = points['measure']
                if points['ingridient_name'] in list_of_ingridients:
                    quantities_and_measures['quantity'] += quantities_and_measures['quantity']
                list_of_ingridients[points['ingridient_name']] = quantities_and_measures
        else:
            print('Такого блюда нет в списке')
    pprint(list_of_ingridients)


get_shop_list_by_dishes(['Омлет','Фахитос'], 4)












