'''
statistics.minutes delayed.weather: number of minutes delayed (per month) caused by significant meteorological
conditions that, in the judgment of the carrier, delays or prevents the operation of a flight.
'''


'''
    In de opdracht willen ze dat we list_of_airports twee keer gaan gebruiken...
    Dit kan natuurlijk niet....
    
    Maar de 'tweede' list_of_airports is nu vliegveld_code =)
'''
import json
from pprint import pprint

list_of_airports = []

with open('airports.json', 'r') as infile:
    list_of_airports = json.load(infile) #Laadt alle data uit airports.json in list_of_airports
    infile.close() #Sluit de file, want wij hebben m niet meer nodig
    #pprint(list_of_airports)
    
vliegveld_code = [] #Nieuwe lijst, omdat de opdracht is slecht gemaakt en anders moeten we list_of_airports overschrijven :3
for vliegveld in list_of_airports:
    airport_code = vliegveld['airport']['code']  #JSON.airport.code
    min_delayed_weather = vliegveld['statistics']['minutes delayed']['weather'] #JSON.statistics.minutes delayed.weather
    vliegveld_code.append((airport_code, min_delayed_weather)) #Voegt code en minuten vertraging als gevolg van Weather toe als TUPLE aan vliegveld
    
pprint(vliegveld_code)
    

# ssort airports by min_delayed_weather

#print(sorted(vliegveld_code)) #sorteerd op key, maar moet op value =(
vliegveld_code_sorted = sorted(vliegveld_code, key=lambda vliegveld_code: vliegveld_code[1], reverse=True) #Sorted op 2e plaats in tuple(Weather delay) =) en omgekeerd, want standaard is klein ---> groot :(
pprint(vliegveld_code_sorted)