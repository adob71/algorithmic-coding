#usage
#python3 parking-bill.py
#output
#You entered the car parking lot at time [10:00]
#You left the car parking lot at time [13:21]
#Parking time : 3 hours 21 minutes
#Parking bill : $ 17

#functions

def solution(E, L):

    EH = E[0:2]
    EM = E[3:5]
    LH = L[0:2]
    LM = L[3:5]

    H=int(LH)-int(EH)
    M=int(LM)-int(EM)

    print ("Parking time :",H,"hours",M,"minutes")

    entrance_fee=2
    the_first=0
    each_successive=0

    if H>0:
        the_first=3
        H=H-1

    while H > 0:
        each_successive=each_successive+4
        H=H-1

    if M>0:
        each_successive=each_successive+4

    parkingbill=entrance_fee+the_first+each_successive
    return parkingbill

#driver code

E = input("You entered the car parking lot at time [10:00]") or "10:00"
L = input("You left the car parking lot at time [13:21]") or "13:21"

print("Parking bill : $", solution(E, L))