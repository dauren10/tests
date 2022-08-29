from full_name import full_name

print('For the exit enter symbol Q')
while True:
    first=input('\nEnter your name: ')
    if first =="Q":
        break
    last=input('\nEnter your lastname: ')
    if last =="Q":
        break
    format_name=full_name(first,last)
    print("\tФорматирование имени: " + format_name)