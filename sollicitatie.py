print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('+     Sollicitatieformulier "Circusdirecteur voor Circus HotelDeBotel     +')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Er wordt u een aantal relevante vragen gesteld...')
print('Gelieve die naar eer en geweten in te vullen')
print('Als blijkt dat u aan de criteria voldoet dan komt u in')
print('aanmerking voor een serieus sollicitatiegesprek!')
print('Ontspan maar blijf wakker, hier komen de vragen')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

N = 'N' or 'n'
J = 'J' or 'j'

#algemene vragen
geslacht = input('U geslacht? M/V ')
lengte = input('Wat is uw lengte in cm? ')
gewicht = input('Wat is uw lichaamsgewicht in kg? ')

#gerichte vragen
certificaat = input('Heeft u het certificaat "Overleven met gevaarlijk personeel"? J/N ')
dieren = input('Hoeveel jaar praktijkervaring met dieren-dressuur heeft u? ')
jongleren = input('Hoeveel jaar ervaring heeft u met jongleren? ')
acrobatiek = input('Hoeveel jaar praktijkervaring heeft u met acrobatiek? ')
diploma = input('Bent u in het bezit van een MBO-4 ondernemen diploma? J/N ')
rijbewijs = input('Bent u in het bezit van een geldig vrachtwagen rijbewijs? J/N ')
hoed = input('Bent u in het bezit van een hoge hoed? J/N ')

#geslacht
if geslacht == 'M' or 'm':
    snor = input('Hoe breed is uw snor in cm? ')
elif geslacht == 'V' or 'v':
    haar = input('Hoe lang is uw krulhaar in cm? ')

#Rare vragen
auto = input('Bent u in het bezit van een oranje auto? J/N ')
frikandelbroodjes = input('Vind u frikandelbroodjes lekker? J/N ')
water = input('Is water nat? J/N ')
stofzuiger = input('Bent u de stofzuiger als u stof opzuigt met een stofzuiger? J/N ')

#grens
if lengte <=150 and gewicht <=90:
    uitslag = 'N'
if dieren <= 4 or jongleren <= 5 or acrobatiek <= 3:
    uitslag = 'N'
if certificaat or diploma or rijbewijs or hoed or auto or frikandelbroodjes or stofzuiger == N:
    uitslag = 'N'
if water == J: 
    uitslag = 'N'
if snor >= 10:
    uitslag = 'N'
if haar >= 20:
    uitslag = 'N'

#uitslag
if uitslag == 'N':
    print('U voldoet niet aan onze strenge eisen voor de functie Circusdirecteur, het spijt ons! ')
else:
    print('Proficiat! U komt in aanmerking voor een solliciatiegesprek, stuur snel uw CV. ' )
