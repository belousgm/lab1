import json
import statistics

file = open('pokemon_full.json')
pokemon_list = file.read()
file.close()

print('Общее количество символов:', len(pokemon_list))

count_symb = 0
for symbols in pokemon_list:
    if symbols.isalnum():
        count_symb += 1
print('Общее количество символов без пробелов и знаков препинания:', count_symb)

pokemon_list = json.loads(pokemon_list)
max_description = 0
name_pokemon = ''
for characteristic in pokemon_list:
    if len(characteristic["description"]) > max_description:
        max_description = len(characteristic["description"])
        name_pokemon = characteristic["name"]
print('Самое длинное описание у покемона по имени', name_pokemon)

max_words = 0
max_abilities = []
for skills in pokemon_list:
    for skill in skills["abilities"]:
        if len(skill.split()) > max_words:
            max_words = len(skill.split())
for max_skills in pokemon_list:
    for max_skill in max_skills["abilities"]:
        if len(max_skill.split()) == max_words:
            max_abilities.append(max_skill)
print('Умения, содержащие больше всего слов: ', end='')
for ability in max_abilities:
    print(ability, end='; ')

min_dispersion = 100000
balance_pokemon = ''
for pokemon in pokemon_list:
    stats_for_dispersion = []
    for stat in pokemon["stats"]:
        stats_for_dispersion.append(pokemon["stats"][stat])
    stats_for_dispersion.pop()
    if statistics.pvariance(stats_for_dispersion) < min_dispersion:
        min_dispersion = statistics.pvariance(stats_for_dispersion)
        balance_pokemon = pokemon["name"]
print('\nСамый сбалансированный покемон:', balance_pokemon)
