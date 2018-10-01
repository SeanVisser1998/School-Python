'''
Created on 30 Sep 2018

@author: seanv
'''
with open('packets.txt', 'r') as f:
    packet_stream = f.read()

packet_list = []
packet_start = 0

def splitPacket(stream):
    #MAC = 0:12
    #Lengte = 12:15
    #Bericht = 15 : 15+waarde van 12-15
    while len(stream) > 0:
        MAC = stream[0:12] #MAC adres
        Lengte = stream[12:15] #Lengte indicator
        i = int(Lengte, 16) #Convert de HEX waarde van Lengte naar Decimal
        bericht = stream[15:15+i] #Bericht is gelijk aan index 15 tm index 15+i
    
        stream = stream[15+i::] #Haalt de eerste packet uit de stream
        packet_list.append(tuple((MAC, Lengte, bericht))) #Slaat de packet op als tuple in de lijst
    
splitPacket(packet_stream)
while packet_start < len(packet_stream):
    #print(packet_start)
    packet_start += 1
# print the tuples
for packet in packet_list:
    print(packet)
