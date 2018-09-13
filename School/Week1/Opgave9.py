'''
Created on 12 Sep 2018

@author: seanv
'''

'''
    Opdracht 9.A
''' 

import time
seq = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"
s_array = []
triplet_count = []
#SLECHTE 
def searchTriplet(triplet):
    s_array.append(seq.index(triplet))
    triplet_count.append(seq.count(triplet))
    return s_array, triplet_count
#print(searchTriplet('ATG'))  

#Goede =)
seq1_array = []
def searchSequenceV1(search_term):
    for i in range(len(seq)):
        if seq[i:i+len(search_term)] == search_term:
            seq1_array.append(i)
    return seq1_array
print("Versie 1: ",searchSequenceV1('ATG'))


#BETERE =)
seq2_array = []
#Zoekt een term in Seq en voegt de index toe aan seq2_array
def searchSequenceV2(search_term): 
    
    #Versneld code, omdat 'Use of . slows down code'
    appendSeq = seq2_array.append 
    
    #Zolang t nummer i in de grootte van seq is ...
    for i in range(len(seq)): 
        
        #Als index tot (index + lengte van search_term) gelijk is aan search_term 
        if seq[i:i+len(search_term)] == search_term:
             
            #Voeg index nummer toe aan array
            appendSeq(i) 
            
    return seq2_array #Returned array
print("Versie 2: ", searchSequenceV2('ATG'))

