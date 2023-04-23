
from LongTermRenterFile import *
from ShortTermRenterFile import *

#from LongTermRenterFile import LongTermRenter as LongTermRenter
#from ShortTermRenterFile import ShortTermRenter as ShortTermRenter


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def checkOut(roomNum,availableRooms):
    flag=0
    for x in availableRooms:
        if x!=roomNum:
            flag=1

        else:
            return 0
    return 1


def main():

    availableRooms=[1,2,3,4,5,6,7,8]
    emptyList=[]
    incrementor=0
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/

    while(1):

        inputIn= input("Make a Selection:\nRent a Room (R), Check Out (C), Print Motel Details (P), Exit Program (X)\n")

        if inputIn== "R":
            name= input("Input name:")
            daysString= input("Number of days staying:")
            daysNum= int(daysString)




            if daysNum<15:
                breakfast = input("Would they like to purchase the breakfast plan? (Y/N)")

                while (1):
                    if (breakfast == "Y"):
                        break

                    elif (breakfast == "N"):
                        break

                else:
                    print("\nInvalid response. Try Again.")
                    continue

                if availableRooms!=emptyList:
                    roomNumber= availableRooms.pop(incrementor)
                    incrementor= incrementor+1
                    renter= ShortTermRenter(name,roomNumber,daysNum,breakfast)
                    cost=0
                    cost= 119.00*daysNum*1.15
                    if breakfast=="Y":
                        cost= cost + (daysNum*5.99)
                    cost2 = round(cost, 2)
                    print("\nYour room number is ",roomNumber)
                    print("\nThe cost is $",cost2)
                    continue

                else:
                    print("Rooms are full")
                    continue

            else:
                insuranceString= input("Would they like to purchase an insurance package?"
                                       +"\n\t0: No Package"
                                       +"\n\t1: Basic Package"
                                       "\n\t2: Premium Package\n")
                insurance= int(insuranceString)

                if availableRooms != emptyList:
                    roomNumber = availableRooms.pop(incrementor)
                    incrementor = incrementor + 1
                    renter = LongTermRenter(name,roomNumber, daysNum, insurance)


                    cost = 0
                    cost = 119.00 * daysNum * 1.15*.7
                    if insurance == 1:
                        cost=cost+25

                    if insurance==2:
                        cost = cost + 75

                    cost2= round(cost,2)
                    print("\nYour room number is ", roomNumber)
                    print("\nThe cost is $",cost2)
                    continue

                else:
                    print("Rooms are full")
                    continue


        if inputIn== "C":
            roomNumString= input("Input the room number checking out:")
            roomNum= int(roomNumString)

            if checkOut(roomNum,availableRooms)==1:
                availableRooms[incrementor]=roomNum
                incrementor= incrementor-1

                print("\nSuccessful checkout")
                continue

            else:
                print("\nThe room you are trying to checkout,has not been checked into ")
                continue



        if inputIn== "P":
                print("MotelDetails not able to be mplemented\n")
                continue

        if inputIn== "X":
                print("Thank you for using the program!")
                exit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


