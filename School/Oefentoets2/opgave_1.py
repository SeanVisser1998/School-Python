blue='greenpark picadilly coventgarden holborn russellsquare kingscross'
yellow='towerhill bakerstreet holborn blackfriars temple'
red='bank holborn oxford bondstreet marblearch'
brown='bakerstreet oxford picadilly charingcross'
lines_london = [blue, yellow, red, brown] #Lijst strings

# (a)
set_of_stations = set()
list_lines = [] #lijst van lijsten
for line in lines_london: #Voor elke regel in lines_london
    list_lines.append(line.split()) #Converteerd de lijst van strings naar een lijst van Lijsten

for regio in list_lines: #Voor elke lijst in lines_list
    for stations in regio: #Voor elk station in de regio
        set_of_stations.add(stations) #Voegt elk station in de regio toe aan de set_of_stations
        
for stations in set_of_stations: #Voor elk station in set_of_stations
    print(stations) #Drukt alle stations in set_of_stations af
    

# (b)

'''
    Wat is een buur?
    
    regio[stations-1] & regio[stations+1] zijn de buren van regio[stations]
'''

dict_of_stations = {}
for s in set_of_stations: #Gebruikt set_of_stations, zodat elke waarde maar een keer voorkomt :3
    buur = []
    for line in lines_london: #Voor elke line in lines_londen
        stations = line.split() #Split de regio op in aparte stations
        if s in line: #Als station voorkomt in line
            i = stations.index(s) #I is gelijk aan de index van stations in de regio
            if i > 0: #Als i groter is dan 0 (0 is eerste, dus bijv 1 heeft ook 0 als buur)
                buur.append(stations[i-1]) #regio[stations-1]
            if i < len(stations) -1: #Als i kleiner is dan de max index van stations - 1
                buur.append(stations[i+1]) #Regio[stations+1]
            
    dict_of_stations[s] = buur #Station is key, waarde zijn de buren uit buur[]
          
for station,buur in dict_of_stations.items(): #Voor station,buur in de dictionary
    print(station,buur) #Print key(station) en value(buur)
        
        
    

# (c) #Holborn
meesteBuur = max(dict_of_stations, key=lambda k:len(dict_of_stations[k])) #Station met de meeste buren :)
hoogsteHoeveelheid = len(dict_of_stations[meesteBuur]) #Lengte van de lijst met buren waarbij de key gelijk is aan het station met de meeste buren

print("Station met meeste buren: ",  meesteBuur , ' met ',  hoogsteHoeveelheid, ' buren! =)')#De grootste waarde van dict_of_stations is het station met de meeste buren =)
    