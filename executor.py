file = open('pokemon_full.json')
pokemon_list = file.read()
file.close()
print('Общее количество символов:', len(pokemon_list))
print('Общее количество символов без пробелов и знаков препинания:',
      len(pokemon_list) - pokemon_list.count(' ') - pokemon_list.count(',') - pokemon_list.count(':'))
