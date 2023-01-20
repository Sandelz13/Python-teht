sukupuoli = input('Anna sukupuolesi (N/M) ')

if sukupuoli == 'N':
    hemoglobiini = int(input('Anna hemoglobiinisi arvo: '))
    if hemoglobiini >= 175:
        print('Hemoglobiiniarvosi on korkea')
    elif 117 <= hemoglobiini <= 175:
        print('Hemoglobiiniarvosi on normaalin rajoissa')
    elif hemoglobiini < 117:
        print('Hemoglobiiniarvosi on matala')

elif sukupuoli == 'M':
    hemoglobiini = int(input('Anna hemoglobiinisi arvo: '))
    if hemoglobiini >= 195:
        print('Hemoglobiiniarvosi on korkea')
    elif 134 <= hemoglobiini <= 195:
        print('Hemoglobiiniarvosi on normaalin rajoissa')
    elif hemoglobiini < 134:
        print('Hemoglobiiniarvosi on matala')

else:
        print('Sukupuoli ei kelpaa')

