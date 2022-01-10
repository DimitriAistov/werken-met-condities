geel = input('Is de kaas geel? ')
if geel == 'ja':
    gaten = input('Zitten er gaten in? ')
    if gaten == 'ja':
        duur = input('Is de kaas belachelijk duur? ')
        if duur == 'ja':
            print('Emmenthaler')
        elif duur == 'nee':
            print('Leerdammer')
    elif gaten == 'nee':
        hard = input('Is de kaas hard als steen? ')
        if hard == 'ja':
            print('Parmigiano Reggiano')
        elif hard == 'nee':
            print('Goudse kaas')
elif geel == 'nee':
    blauw = input('Heeft de kaas blauwe schimmel? ')
    if blauw == 'ja':
        korst = input('Heeft de kaas een korst? ')
        if korst == 'ja':
            print('Bleu de Rochbaron')
        elif korst == 'nee':
            print("Foume d'Ambert")
    elif blauw == 'nee':
        blauweKorst = input('Heeft de kaas een korst? ')
        if blauweKorst == 'ja':
            print('Camembert')
        elif blauweKorst == 'nee':
            print('Mozarella')



