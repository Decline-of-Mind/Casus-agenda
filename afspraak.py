import sys
from kalender import agenda

# Normaal presenteer je de keuzes in HTML waarin we verkeerde antwoorden al kunnen uitsluiten.

print("Welkom User, u wilt een afspraak inplannen met Dhr.Randomnaam.")
print("type 1 voor Maandag,")
print("type 2 voor Dinsdag")
print("type 3 voor Woensdag")
print("type 4 voor Donderdag")
print("type 5 voor Vrijdag")
dagkeuze = input('Kies welke dag u uw afspraak wilt deze week: ')


def geef_eerste_vrije_slot(getal):

    dag = agenda[getal]
    # print(dag['tijdslot'])
    for nummer in dag['tijdslot'].values():
        if nummer['bezet'] == False:
            print(f"Dhr Randomnaam kan van {nummer['tijd']} op {dag['naam']}")
            bevestiging = input("Is dit the afspraak die u wilt maken? ja of nee? ")
            if bevestiging == 'ja':
                print('Uw afspraak is gemaakt! Dankuwel en tot dan.')
                nummer['bezet'] = True
                print(nummer)
                print(nummer)
                # Kan niet bij het voorgaande nummer van het daadwerkelijk tijdslot
                # agenda = [dag]['tijdslot'][nummer]
                return nummer
        else:
            print('We hebben helaas deze dag geen plek voor u, probeer een andere dag')
            return plan_afspraak(dagkeuze)
        return

def plan_afspraak(dagkeuze):
    dagpreferentie = int(dagkeuze)
    if dagpreferentie == 1:
       geef_eerste_vrije_slot(1)
    #    return (timeslot)
    elif dagpreferentie == 2:
        geef_eerste_vrije_slot(2)
        # return (timeslot)
    elif dagpreferentie == 3:
        geef_eerste_vrije_slot(3)
        # return (timeslot)
    elif dagpreferentie == 4:
        geef_eerste_vrije_slot(4)
        # return (timeslot)
    elif dagpreferentie == 5:
        geef_eerste_vrije_slot(5)
        # return (timeslot)
    else:
        return print("Sorry, dat is geen juist antwoord")
    return dagpreferentie

plan_afspraak(dagkeuze)


