import csv
import copy


#checks which employees have infracted over the limits and reports
def susEmployeeChecker(extremeLogged,mildLogged):
    # for row in range(len(extremeLogged)):
    #     for row2 in range(len(extremeLogged)):
    #         print(extremeLogged[row2][1].count(extremeLogged[row][1]))
    extremeDict={}
    listCount= [[0 for x in range(len(extremeLogged))] for y in range((len(extremeLogged)))]

    for row2 in range(len(extremeLogged)):
        for elem in range(len(extremeLogged)):
            count = 0

            listCount[row2][elem]= extremeLogged[elem][1].count(extremeLogged[row2][1])

            for elem in range(len(extremeLogged)):
                if listCount[row2][elem]==1:
                    count=count+1

            extremeDict.update({extremeLogged[row2][1]:count})

    with open('ProblematicEmployees.txt','w') as f:
        toReport=""
        for key,val in extremeDict.items():
            if val>4:
                toReport=key
                f.write(toReport+"\n")
        print("Extreme Infractors")
        print(extremeDict)

    mildDict = {}
    listCount2 = [[0 for x in range(len(mildLogged))] for y in range((len(mildLogged)))]

    for row2 in range(len(mildLogged)):
        for elem in range(len(mildLogged)):
            count = 0
            # print(extremeLogged[row2][1].count(extremeLogged[0][1]))
            listCount2[row2][elem] = mildLogged[elem][1].count(mildLogged[row2][1])

            for elem in range(len(mildLogged)):
                if listCount2[row2][elem] == 1:
                    count = count + 1

            mildDict.update({mildLogged[row2][1]: count})

    with open('ProblematicEmployees.txt', 'w') as f:
        toReport=""
        for key, val in mildDict.items():
            if val > 14:
                toReport = key
                f.write(toReport + "\n")
        print("Mild Infractors")
        print(mildDict)


#checks to see if a day should be reported
def logConditionChecker(extremeLogged,mildLogged):
    with open('AnomalyData.csv', 'w', encoding='UTF8',newline='') as f:
        writer=csv.writer(f)
        rowPass=0

        for row in range(len(extremeLogged)-1):
            extremeOccurences=0
            i=0

            next= extremeLogged[row+1][0]
            while(next==extremeLogged[row][0]):
                extremeOccurences=extremeOccurences+1
                i=i+1
                next= extremeLogged[row+i][0]

            if extremeOccurences>=2:
                print(extremeLogged[row][0])
                writer.writerow([extremeLogged[row][0]])
                row2=row
                for x in range(extremeOccurences):
                    print(extremeLogged[row2][1])
                    writer.writerow([extremeLogged[row2][1]])
                    row2=row2+1


        for row in range(len(mildLogged)-1):
            mildOccurences=0
            i=0
            rowPass=row
            next= mildLogged[row+1][0]
            while(next==mildLogged[row][0]):
                mildOccurences=mildOccurences+1
                i=i+1
                next= mildLogged[row+i][0]

            if mildOccurences>=6:
                print(mildLogged[row][0])
                writer.writerow([mildLogged[row][0]])
                row2=row
                for x in range(mildOccurences):
                    print(mildLogged[row2][1])
                    writer.writerow([mildLogged[row2][1]])
                    row2=row2+1

            if mildOccurences==5:
                for row in range(len(extremeLogged)):
                    if extremeLogged[row][0]:
                        extremeOccurences = 0
                        i = 0
                        next = mildLogged[row + 1][0]
                        while (next == extremeLogged[row][0]):
                            extremeOccurences = extremeOccurences + 1
                            i = i + 1
                            next = extremeLogged[row + i][0]

                        if extremeOccurences>2:
                            print(extremeLogged[row][0])
                            writer.writerow([extremeLogged[row][0]])
                            row2 = row
                            for x in range(extremeOccurences):
                                print(extremeLogged[row2][1])
                                writer.writerow([extremeLogged[row2][1]])
                                row2 = row2 + 1

                            print(mildLogged[rowPass][0])
                            writer.writerow([mildLogged[row][0]])
                            row2 = rowPass
                            for x in range(mildOccurences):
                                print(mildLogged[row2][1])
                                writer.writerow([mildLogged[row2][1]])
                                row2 = row2 + 1



#creates logs of extreme and mild anomaly events
def anomalyCounter(extremeOutliersLo, mildOutliersLo, extremeOutliersHi,mildOutliersHi,cleanedData,data,numData):
    extremeCountLo=0
    extremeCountHi= 0
    mildCountLo=0
    mildCountHi = 0

    mildLoggedInc=0
    extremeLoggedInc = 0



    for row in range(1, len(mildOutliersLo) - 1):
        for elem in range(1, len(mildOutliersLo[0])):
            if(mildOutliersLo[row][elem]!=0):
                mildCountLo=mildCount+1

    for row in range(1, len(extremeOutliersLo) - 1):
        for elem in range(1, len(extremeOutliersLo[0])):
            if(extremeOutliersLo[row][elem]!=0):
                extremeCountLo=extremeCountLo+1

    for row in range(1, len(mildOutliersHi) - 1):
        for elem in range(1, len(mildOutliersHi[0])):
            if(mildOutliersHi[row][elem]!=0):
                mildCountHi=mildCountHi+1

    for row in range(1, len(extremeOutliersHi) - 1):
        for elem in range(1, len(extremeOutliersHi[0])):
            if(extremeOutliersHi[row][elem]!=0):
                extremeCountHi=extremeCountHi+1



    mildCount=mildCountLo+mildCountHi
    extremeCount=extremeCountLo+extremeCountHi

    mildLogged = [[0 for x in range(2)] for y in range(mildCount)]
    extremeLogged = [[0 for x in range(2)] for y in range(extremeCount)]

    if mildCount>6 or (mildCount==5 and extremeCount==2) or extremeCount>3:
        print("Need to report")
        if(mildCountLo>0):
            for row in range(1, len(mildOutliersLo) - 1):
                for elem in range(1, len(mildOutliersLo[0])):
                    if (mildOutliersLo[row][elem] != 0):
                        report=mildOutliersLo[row][elem]
                        date=data[row][0]
                        positionPreOrdered= cleanedData[row][report]
                        employee= numData[row].index(positionPreOrdered) #find original position of element that had been sorted
                        employee= data[0][employee]
                        mildLogged[mildLoggedInc][0] = date
                        mildLogged[mildLoggedInc][1] = employee
                        mildLoggedInc = mildLoggedInc + 1


        if(extremeCountLo>0):
            for row in range(1, len(extremeOutliersLo) - 1):
                for elem in range(1, len(extremeOutliersLo[0])):
                    if (extremeOutliersLo[row][elem] != 0):
                        report=extremeOutliersLo[row][elem]
                        date=data[row][0]
                        positionPreOrdered= cleanedData[row][report]
                        employee= numData[row].index(positionPreOrdered) #find original position of element that had been sorted
                        employee= data[0][employee]
                        extremeLogged[extremeLoggedInc][0] = date
                        extremeLogged[extremeLoggedInc][1] = employee
                        extremeLoggedInc = extremeLoggedInc + 1

        if (mildCountHi > 0):
            for row in range(1, len(mildOutliersHi) - 1):
                for elem in range(1, len(mildOutliersHi[0])):
                    if (mildOutliersHi[row][elem] != 0):
                        report = mildOutliersHi[row][elem]
                        date = data[row][0]
                        positionPreOrdered = cleanedData[row][report]
                        employee = numData[row].index(positionPreOrdered)  # find original position of element that had been sorted

                        employee = data[0][employee]
                        mildLogged[mildLoggedInc][0] = date
                        mildLogged[mildLoggedInc][1]= employee
                        mildLoggedInc= mildLoggedInc + 1

        if (extremeCountHi > 0):
            for row in range(1, len(extremeOutliersHi) - 1):
                for elem in range(1, len(extremeOutliersHi[0])):
                    if (extremeOutliersHi[row][elem] != 0):
                        report = extremeOutliersHi[row][elem]
                        date = data[row][0]
                        positionPreOrdered = cleanedData[row][report]
                        employee = numData[row].index(positionPreOrdered)  # find original position of element that had been sorted
                        employee = data[0][employee]
                        extremeLogged[extremeLoggedInc][0] = date
                        extremeLogged[extremeLoggedInc][1] = employee
                        extremeLoggedInc = extremeLoggedInc + 1

        return extremeLogged,mildLogged



#checks to find lower anomalies
def anomalyChecker1(boxplotVals,cleanedData,data):
    extremeOutlier1 = [[0 for x in range(len(cleanedData[1]))] for y in range(len(cleanedData))]
    mildOutlier1 = [[0 for x in range(len(cleanedData[1]))] for y in range(len(cleanedData))]


    extremeOutlier2 = [[0 for x in range(len(cleanedData[1]))] for y in range(len(cleanedData))]
    mildOutlier2 = [[0 for x in range(len(cleanedData[1]))] for y in range(len(cleanedData))]


    for row in range(1, len(cleanedData) - 1):
        inc1=0
        inc2=0
        for elem in range(1, len(cleanedData[0])):
            if cleanedData[row][elem]<boxplotVals[row][5]: #lowerInner
                if cleanedData[row][elem] < boxplotVals[row][7]: #lowerOuter
                    extremeOutlier1[row][inc1] =elem
                    inc1= inc1+1

                else:
                    mildOutlier1[row][inc2] =elem
                    inc2= inc2+1

    return extremeOutlier1,mildOutlier1


#checks to find the higher anonamalies
def anomalyChecker2(boxplotVals,cleanedData,data):
    extremeOutlier1 = [[0 for x in range(len(cleanedData[1]))] for y in range(len(cleanedData))]
    mildOutlier1 = [[0 for x in range(len(cleanedData[1]))] for y in range(len(cleanedData))]
    extremeInc1=0
    mildInc1=0
    inc1=0
    inc2=0

    extremeOutlier2 = [[0 for x in range(len(cleanedData[1]))] for y in range(len(cleanedData))]
    mildOutlier2 = [[0 for x in range(len(cleanedData[1]))] for y in range(len(cleanedData))]
    extremeInc2 = 0
    mildInc2 = 0

    for row in range(1, len(cleanedData) - 1):
        inc1 = 0
        inc2=0
        for elem in range(1, len(cleanedData[0])):
            if cleanedData[row][elem] > boxplotVals[row][6]:  # higherInner
                if cleanedData[row][elem] > boxplotVals[row][8]:  # higherOuter
                    extremeOutlier1[row][inc1] = elem
                    inc1 = inc1 + 1


                else:
                    mildOutlier1[row][inc2] = elem
                    inc2 = inc2 + 1



    return extremeOutlier1,mildOutlier1




def median(numbersLists):
   # cleanerNumbersLists= numbersLists[1:len(numbersLists)-2]

    #cleanerNumbersLists=[]


    cleanerNumbersLists = copy.deepcopy(numbersLists)

    for row in range(1, len(numbersLists)):
        for elem in range(1, len(numbersLists[0])):
            #cleanerNumbersLists.append(numbersLists[row][elem])
            cleanerNumbersLists[row][elem]=numbersLists[row][elem]

    #for row in range(1, len(numbersLists)):
            #cleanerNumbersLists.append(numbersLists[row][elem])
        #cleanerNumbersLists[row]=cleanerNumbersLists[row].sort()

    #print(type(cleanerNumbersLists[1][0]))
    #print(cleanerNumbersLists[1].sort())
    cleanedData=[]
    #cleanedData.append(cleanerNumbersLists[0])
    cleanedData= cleanerNumbersLists.copy()

    for row in range(1, len(cleanerNumbersLists)):
        cleanedData[row]= sorted(cleanerNumbersLists[row])
        #print(cleanedData)
#cleanedData[0] = sorted(cleanerNumbersLists[1])
    # test=[1,2,3,4,5,6,7,8,9,10]
    # mid= (len(test)-1)/2
    # print(mid)
    #
    # test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
    # mid = (len(test) - 1) / 2
    # print(mid)
    return cleanedData

def boxplot(cleanedDataLists):
#     #[0]position of row,#[1]median,#[2]lower quartile,#[3]upper quartile
#     #[4]interquartile #[5]lower inner fence, #[6]upper inner fence,
#     #[7]lower outer fence, #[8]upper outer fence
    #lenList=len(cleanedDataLists)-1
    boxplotVals = [[0 for x in range(10)] for y in range(len(cleanedDataLists))]


#position
    cnt=0
    for row in range(0, len(cleanedDataLists[1])):
        boxplotVals[row][0] = cnt
        cnt= cnt +1

#median
    for row in range(1, len(cleanedDataLists[1])-1):


        if (len(cleanedDataLists[1])-1)%2==0:
            mid = (len(cleanedDataLists[1])-1) / 2
            #mid = round(mid)
            #mid= mid-1 #correct midpoint
            mid= int(mid)
            median= cleanedDataLists[row][mid+1] #factoring in 0 in 1st col
            #print(median)
#
        else:
            mid = (len(cleanedDataLists[1]) - 1) / 2
            low= mid-0.5
            high= mid+0.5
            median= (cleanedDataLists[row][low+1]+cleanedDataLists[row][high+1])/2
            #print(median)
        boxplotVals[row][1]=median




#lowerquartile
    for row in range(1, len(cleanedDataLists)-1):
        rowLength= len(cleanedDataLists[1])
        lowerQ= .25*rowLength
        lowerQ= int(lowerQ)

        lowerQuartile= cleanedDataLists[row][lowerQ]
        boxplotVals[row][2]=lowerQuartile
        #print(boxplotVals[row][2])


#upperquartile

    for row in range(1, len(cleanedDataLists) - 1):
        rowLength = len(cleanedDataLists[1])
        upperQ = .75 * rowLength
        upperQ = int(upperQ)

        upperQuartile = cleanedDataLists[row][upperQ]
        boxplotVals[row][3] = upperQuartile
        #print(boxplotVals[row][2])

#interquartile
    for row in range(1, len(cleanedDataLists) - 1):
        interquartile1=boxplotVals[row][3]
        interquartile2 = boxplotVals[row][2]

        #for some inexplicable reason regular subtraction yielded
        #terribly wrong results.
        interquartile= interquartile1-interquartile2

        boxplotVals[row][4]=interquartile
        #print(boxplotVals[row][3])
        #print(boxplotVals[row][2])
        #print(boxplotVals[row][4])

#lower inner fence2
    for row in range(1, len(cleanedDataLists) - 1):
        #calculations for some reason still arent accurate
        lowerInnerFence=boxplotVals[row][2]-((boxplotVals[row][4])*1.5)
        boxplotVals[row][5] = lowerInnerFence

#upper inner fence2
    for row in range(1, len(cleanedDataLists) - 1):
        #calculations for some reason still arent accurate
        upperInnerFence=((boxplotVals[row][4])*1.5)+boxplotVals[row][3]
        boxplotVals[row][6] = upperInnerFence

#lower outer fence2
    for row in range(1, len(cleanedDataLists) - 1):
        #calculations for some reason still arent accurate
        lowerOuterFence=boxplotVals[row][2]-((boxplotVals[row][4])*3)
        boxplotVals[row][7] = lowerOuterFence
        #print(lowerOuterFence)

#upper outer fence2
    for row in range(1, len(cleanedDataLists) - 1):
        #calculations for some reason still arent accurate
        upperOuterFence=boxplotVals[row][3]+((boxplotVals[row][4])*3)
        boxplotVals[row][8] = upperOuterFence

    return boxplotVals
#9626
#     0 1 2 3 4 5 6 7 8 9 10 11-6
#     1 2 3 4 5 6 7 8 9 10 11 -5
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# 1 2 3 4 5 6 7 8 9 10


def main():
    data=[]
    rowInc=0
    initFlag=0

    with open('RawFinancialData2022.csv', newline='') as csvfile:
        infoReader = csv.reader(csvfile, delimiter=',')
        for row in infoReader:
            data.append(row)
            rowInc = rowInc+1


    #now move to a number array

    #numData = data.copy()
    #numData = data[:]
    numData= copy.deepcopy(data)

    #remove date
    for elem in range(0,len(numData)):
        numData[elem][0]=float(0)



    # turn first string row to float
    for row in range(0, 1):
        for elem in range(1, len(numData[0])):
            numData[row][elem] = float(0)



    # convert strings to lists of numbers
    for row in range(1,len(numData)):
        for elem in range(1,len(data[0])):
            x=numData[row][elem]
            numData[row][elem]=float(x)
    #print(type(numData[1][1]))
    #print(len(numData[1]))
    #print(numData[1])


    cleanedData=median(numData)



    boxplotVals=boxplot(cleanedData)

    extremeOutliersLo,mildOutliersLo=anomalyChecker1(boxplotVals,cleanedData,data)
    extremeOutliersHi,mildOutliersHi = anomalyChecker2(boxplotVals, cleanedData, data)

    extremeLogged,mildLogged= anomalyCounter(extremeOutliersLo, mildOutliersLo, extremeOutliersHi,mildOutliersHi,cleanedData,data,numData)

    logConditionChecker(extremeLogged,mildLogged)
    susEmployeeChecker(extremeLogged,mildLogged)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
