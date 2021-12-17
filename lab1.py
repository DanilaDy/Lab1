import json

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
pokemon_name = '' # Имя покемона с самым длинным описанием
ability_list = list() # Список умений покемонов с наибольшим названием
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
