def parse_recipes(file_path):
    cook_book = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        current_dish = None
        ingredient_count = 0

        for line in lines:
            line = line.strip()

            if line:
                if current_dish is None:
                    current_dish = line
                elif ingredient_count == 0:
                    ingredient_count = int(line)
                else:
                    ingredient_parts = line.split('|')
                    if len(ingredient_parts) == 3:
                        ingredient_name = ingredient_parts[0].strip()
                        quantity = int(ingredient_parts[1].strip())
                        measure = ingredient_parts[2].strip()

                        ingredient = {
                            'ingredient_name': ingredient_name,
                            'quantity': quantity,
                            'measure': measure
                        }
                        if current_dish not in cook_book:
                            cook_book[current_dish] = []
                        cook_book[current_dish].append(ingredient)

                        ingredient_count -= 1
                    else:
                        print(f"Ошибка в формате строки: {line}")
            else:
                current_dish = None
                ingredient_count = 0

    return cook_book



cook_book = parse_recipes('recipes.txt')
print(cook_book)


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {
                        'measure': measure,
                        'quantity': quantity
                    }

    return shop_list



shop_list = get_shop_list_by_dishes(cook_book, ['Запеченный картофель', 'Омлет'], 2)
print(shop_list)

import os


def merge_files(file_list, output_file):
    file_data = []

    for file_name in file_list:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            file_data.append((file_name, len(lines), lines))


    file_data.sort(key=lambda x: x[1])

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for file_name, line_count, lines in file_data:
            out_file.write(f"{file_name}\n{line_count}\n")
            out_file.writelines(lines)



merge_files(['files/1.txt', 'files/2.txt'], 'files/merged.txt')