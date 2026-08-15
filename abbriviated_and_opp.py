names = input ('Enter the first and last name of your friends separated by a comma e.g:(George Mazroof, Malik Khoritch...): ').split(', ')
appriviated_words = []

for name in names :
  name_parts = name.split()
  print (name_parts)

  first = name_parts[0][0]
  second = name_parts[1][0]

  apprivia = first + '.' + second + '.'

  appriviated_words.append(apprivia)


print('\nAbbreviated Names:')
for x in appriviated_words :
  print (x)








sente = input('Enter a sentence: ').split()

opp_sente = sente[::-1]

print (" ".join(opp_sente))