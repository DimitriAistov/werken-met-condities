start = input('Je bent op het strand aan het zwemmen en je zwemt te ver weg. Je spoelt ver weg aan op een eiland en moet nu zien te overleven en het begint nacht te worden. Maak je een [kampvuur] of ga je [slapen]. ')
if start == 'kampvuur' or 'Kampvuur':
    print('Je hebt een kampvuur gemaakt en gaat nu slapen.')
    kampvuur = input('Het is ochtend. Ga je [zwemmen] of een [hut] bouwen ')
    if kampvuur == 'Hut' or 'hut':
        print('Je hebt een hut gebouwd.')
        hut = input('Nu dat je een hut hebt ga je [verkennen] of [aandacht] trekken. ')
        if hut == 'Aandacht'or'aandacht':
            print('Je schrijft met stenen op het zand “SOS” en “Help”.')
            aandacht = input('Vliegtuigen kunnen nu zien dat je hulp nodig hebt. Je begint honger te krijgen en dus ga je het eiland bekijken. Ga je [oost] of ga je [west]? ')
            if aandacht == 'oost'or'Oost':
                print('Je ziet appels gevallen uit een appelboom liggen en eet ze.')
                oost = input('Je hebt het warm. Ga je [onder] de appelboom genieten van je appel of ga je na het eten de [zee] in. ')
                if oost == 'onder'or'Onder':
                    print('Je geniet van de schaduw en besluit je komende plan van aanpak.')
                    onder = input('Je pakt wat extra appels en gaat terug naar je hut. Als je thuis aankomt zie je een boot aankomen. [Eet] je op de boot de appels of [niet]. ')
                    if onder == 'Niet'or'niet':
                        print('Je komt aan op het strand en je gaat naar huis.')
                    elif onder == 'Eet'or'eet':
                        print('Er zit een worm in de appel en je gaat dood.')
                elif oost =='Zee'or'zee':
                    print('Je gaat na het eten zwemmen en verdrinkt aan kramp.')
            elif aandacht == 'West'or'west':
                print('Door de honger begin je te hallucineren.')
                west = input('Tijdens de hallucinatie zie je een burger. Ga je [eropaf] of ga je verder naar het [westen] ')
                if west == 'Westen'or'westen':
                    print('Je gaat verder richting het westen')
                    westen = input('Verder in het westen zie je en tijger. Ga je [aanvallen] of [ren] je weg? ')
                    if westen =='Aanvallen'or'aanvallen':
                        print('de tijger heeft je opgegeten.')              
                    elif westen =='Rennen'or'rennen':
                        print('de tijger heeft je ingehaald en eet je op.')
                elif west == 'Eropaf'or'eropaf':
                    print ('Het blijkt een giftige kever te zijn en je gaat dood.')
        elif hut == 'Verkennen'or'verkennen':
            print('Verkennen Je bent aangevallen door een giftige kikker.')
    elif kampvuur == 'Zwemmen'or'zwemmen':
        print('Je bent door een haai aangevallen en bent doodgegaan.')
elif start == 'slapen'or'Slapen':
    print('Je bent in je slaap doodgegaan aan de kou.')
