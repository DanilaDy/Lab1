import json
import random


def pokemon_stats(text):
    id = random.randint(1,801)
    id_str = f'{id:03d}'
    similar_total_stats_id = 0
    stats_total_difference = 10000
    pokemon = text[id-1]
    print('Сгенерированный id покемона -', id_str)
    print('Имя покемона:', pokemon['name'], 'Вид покемона -', pokemon['species'])
    print('Статистики ', pokemon['name'],':', pokemon['stats'])
    for pokemon_info in text:
        if (pokemon_info['species'] == pokemon['species']) and (pokemon_info['id'] != id_str):
            # print(pokemon_info, id)  # вывод других покемонов того же вида для проверки
            diff = abs(int(pokemon_info['stats']['total'])-int(pokemon['stats']['total']))
            if diff < stats_total_difference:
                stats_total_difference = diff
                similar_total_stats_id = int(pokemon_info['id'])
    if stats_total_difference != 10000:
        print('Покемон, с наиболее близкой суммой статов -', text[similar_total_stats_id-1]['name'])
        # print(text[similar_total_stats_id-1])  # полный вывод инфы о покемоне из списка тоже для проверки
    else:
        print('Нет других покемонов этого вида')


with open('pokemon_full.json') as file:
    text = json.load(file)
file.close()

string_of_text = str(text)
text_length_full = len(string_of_text)
print('Общее количество символов в файле -', text_length_full)

text_length_except_punctuation = 0
for symbol in string_of_text:
    if symbol.isalnum():
        text_length_except_punctuation += 1
print('Общее количесто символов без пробелов и знаков препинания -', text_length_except_punctuation)

max_description = 0
max_ability = 0
word_count = 0
pokemon_name = ''  # Имя покемона с самым длинным описанием
ability_list = list()  # Список умений покемонов с наибольшим названием
for pokemon_info in text:
    description = pokemon_info['description']
    if len(description) > max_description:
        max_description = len(description)
        pokemon_name = pokemon_info['name']
    for ability in pokemon_info['abilities']:
        word_count = len(ability.split())
        if word_count > max_ability:
            max_ability = word_count
            ability_list.clear()
            ability_list.append(ability)
        if word_count == max_ability:
            if ability not in ability_list:
                ability_list.append(ability)

print('Имя покемона с самым длинным описанием -', pokemon_name)
print('Названия умений с наибольшим количеством слов:')
for ability in ability_list:
    print(ability)

print('----------------------')

pokemon_stats(text)
