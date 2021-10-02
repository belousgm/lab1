file = open('pokemon_full.json')
all_symbols = file.read()
file.close()
print('Общее количество символов:', len(all_symbols))
print('Общее количество символов без пробелов и знаков препинания:',
      len(all_symbols) - all_symbols.count(' ') - all_symbols.count(',') - all_symbols.count(':'))
