'''
Created on 30 Sep 2018

@author: seanv

TBH... De oplossing op de vraag kan tig keer makkelijker dan dat school het wil...


Het makkelijkste zou zijn: 
    return hex(decimal)[2:]
en dan ben je alweer klaar... Maar neeeheeee, school moet en zal t lastig doen.

maar ik ga t wel doen zoals school t wil ofzo =( 
'''
# convert an integer to a hex digit (a character)
def hex_char(value):
    if value <= 9 and value >= 0:
        return chr(value + ord('0'))
    else:
        return chr(value - 10 + ord('A'))

# convert a decimal to a hex as a string 
def to_hex(decimal):
    hex_decimal = [] #Array voor opslaan return waarden uit hex_char
    quotient = decimal #Quotient defineren
    remainder = decimal #Remainder defineren
    while quotient > 0: #Zolang de quotient niet 0 is...
        remainder = decimal%16 #Remainder berekenen met modulo
        hex_decimal.insert(0, hex_char(remainder)) #De waarde van hex_char(remainder) in hex_decimal inserten op positie 0
        quotient = decimal//16 #Quotient berekenen an decimal
        decimal = quotient #De nieuwe decimal is gelijk aan de quotient, want herhaaldelijk delen etc =)
        
    return ''.join(hex_decimal) #Returned de waarden uit hex_decimal gejoined op '', zodat ze gewoon een string worden =)
        

def main():
    assert to_hex(12345) == '3039' 
    #assert to_hex(0) == '0' 
main()





'''
    Hexadecimaal naar decimal conversie, want ja... U never know of dit op de toets komt xd
'''
def decNummer(digit):
    digits = ['0', '1', '2','3', '4', '5','6', '7', '8','9', 'A', 'B','C', 'D', 'E','F']
    for x in range(len(digits)):
        if digit == digits[x]:
            return x
        
def hexToDec(hexNum):
    decNum = 0
    power = 0
    for digit in range(len(hexNum), 0, -1):
        decNum = decNum + 16 ** power * decNummer(hexNum[digit-1])
        power += 1
    return decNum

print(hexToDec("FF"))
