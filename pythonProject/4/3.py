user_list = []

while True:
    user_input = input('Anna luku, tyhjä merkkijono lopettaa: ')

    if user_input == '':
        break

    try:
        user_list.append(int(user_input))
    except ValueError:
        print('Invalid number.')
        continue
user_list.sort()

print("Antamasi lukujen suurin oli", max(user_list))
print("Antamasi lukujen pienin oli", min(user_list))