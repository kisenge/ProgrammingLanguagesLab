import csv


def anomalyCounter(extremeOutliers, mildOutliers):
    extremeCount = 0
    mildCount = 0

    for row in range(1, len(extremeOutliers) - 1):
        if extremeOutliers[row][0] != 0:
            extremeCount = extremeCount + 1
        else:
            break

    for row in range(1, len(mildOutliers) - 1):
        if mildOutliers[row][0] != 0:
            mildCount = mildCount + 1
        else:
            break

    print(mildCount)
    if mildCount > 6 or (mildCount == 5 and extremeCount == 2) or extremeCount > 3:
        print("Need to report")


def anomalyChecker1(boxplotVals, cleanedData, data):
    extremeOutlier1 = [[0 for x in range(3)] for y in range(len(cleanedData))]
    mildOutlier1 = [[0 for x in range(3)] for y in range(len(cleanedData))]

    extremeInc1 = 0
    mildInc1 = 0

    extremeOutlier2 = [[0 for x in range(len(cleanedData[1]))] for y in range(len(cleanedData))]
    mildOutlier2 = [[0 for x in range(len(cleanedData[1]))] for y in range(len(cleanedData))]
    extremeInc2 = 0
    mildInc2 = 0

    for row in range(1, len(cleanedData) - 1):
        for elem in range(1, len(cleanedData[0])):
            if cleanedData[row][elem] < boxplotVals[row][5]:  # lowerInner
                if cleanedData[row][elem] < boxplotVals[row][7]:  # lowerOuter
                    extremeOutlier1[extremeInc1][0] = extremeInc1
                    extremeOutlier1[extremeInc1][1] = data[row][0]  # date
                    extremeOutlier1[extremeInc1][2] = data[0][elem]  # employee
                    extremeInc1 = extremeInc1 + 1

                else:
                    mildOutlier1[mildInc1][0] = mildInc1
                    mildOutlier1[mildInc1][1] = data[row][0]  # date
                    mildOutlier1[mildInc1][2] = data[0][elem]  # employee
                    mildInc1 = mildInc1 + 1

    # for row in range(1, len(cleanedData) - 1):
    #     for elem in range(1, len(cleanedData[0])):
    #         if cleanedData[row][elem] > boxplotVals[row][6]:  # upperInner
    #             if cleanedData[row][elem] > boxplotVals[row][8]:  # upperOuter
    #                 extremeOutlier2[extremeInc2][0] = extremeInc2
    #                 extremeOutlier2[extremeInc2][1] = data[row][0]  # date
    #                 extremeOutlier2[extremeInc2][2] = data[0][elem]  # employee
    #                 extremeInc2 = extremeInc2 + 1
    #
    #             else:
    #                 mildOutlier2[mildInc2][0] = mildInc2
    #                 mildOutlier2[mildInc2][1] = data[row][0]  # date
    #                 mildOutlier2[mildInc2][2] = data[0][elem]  # employee
    #                 mildInc2 = mildInc2 + 1

    return extremeOutlier1, mildOutlier1


def anomalyChecker2(boxplotVals, cleanedData, data):
    extremeOutlier1 = [[0 for x in range(3)] for y in range(len(cleanedData))]
    mildOutlier1 = [[0 for x in range(len(cleanedData[1]))] for y in range(len(cleanedData))]
    extremeInc1 = 0
    mildInc1 = 0
    inc = 0

    extremeOutlier2 = [[0 for x in range(len(cleanedData[1]))] for y in range(len(cleanedData))]
    mildOutlier2 = [[0 for x in range(len(cleanedData[1]))] for y in range(len(cleanedData))]
    extremeInc2 = 0
    mildInc2 = 0

    for row in range(1, len(cleanedData) - 1):
        for elem in range(1, len(cleanedData[0])):
            if cleanedData[row][elem] > boxplotVals[row][6]:  # lowerInner

                if cleanedData[row][elem] > boxplotVals[row][8]:  # lowerOuter
                    extremeOutlier1[extremeInc1][0] = extremeInc1
                    extremeOutlier1[extremeInc1][1] = data[row][0]  # date
                    extremeOutlier1[extremeInc1][2] = data[0][elem]  # employee
                    extremeInc1 = extremeInc1 + 1

                # else:
                #     mildOutlier1[mildInc1][0] = mildInc1
                #     mildOutlier1[mildInc1][1] = data[row][0]  # date
                #     mildOutlier1[mildInc1][2] = data[0][elem]  # employee
                #     mildInc1 = mildInc1 + 1

    # for row in range(1, len(cleanedData) - 1):
    #     for elem in range(1, len(cleanedData[0])):
    #         if cleanedData[row][elem] > boxplotVals[row][6]:  # upperInner
    #             if cleanedData[row][elem] > boxplotVals[row][8]:  # upperOuter
    #                 extremeOutlier2[extremeInc2][0] = extremeInc2
    #                 extremeOutlier2[extremeInc2][1] = data[row][0]  # date
    #                 extremeOutlier2[extremeInc2][2] = data[0][elem]  # employee
    #                 extremeInc2 = extremeInc2 + 1
    #
    #             else:
    #                 mildOutlier2[mildInc2][0] = mildInc2
    #                 mildOutlier2[mildInc2][1] = data[row][0]  # date
    #                 mildOutlier2[mildInc2][2] = data[0][elem]  # employee
    #                 mildInc2 = mildInc2 + 1

    return extremeOutlier1


def anomalyChecker3(boxplotVals, cleanedData, data):
    extremeOutlier1 = [[0 for x in range(len(cleanedData[1]))] for y in range(len(cleanedData))]
    mildOutlier1 = [[0 for x in range(len(cleanedData[1]))] for y in range(len(cleanedData))]
    extremeInc1 = 0
    mildInc1 = 0
    inc = 0

    extremeOutlier2 = [[0 for x in range(len(cleanedData[1]))] for y in range(len(cleanedData))]
    mildOutlier2 = [[0 for x in range(len(cleanedData[1]))] for y in range(len(cleanedData))]
    extremeInc2 = 0
    mildInc2 = 0

    for row in range(1, len(cleanedData) - 1):
        inc = 0
        for elem in range(1, len(cleanedData[0])):
            if cleanedData[row][elem] > boxplotVals[row][6]:  # lowerInner

                if cleanedData[row][elem] < boxplotVals[row][8]:  # lowerOuter

                    mildOutlier1[row][inc] = elem
                    inc = inc + 1

    # for row in range(1, len(cleanedData) - 1):
    #     for elem in range(1, len(cleanedData[0])):
    #         if cleanedData[row][elem] > boxplotVals[row][6]:  # upperInner
    #             if cleanedData[row][elem] > boxplotVals[row][8]:  # upperOuter
    #                 extremeOutlier2[extremeInc2][0] = extremeInc2
    #                 extremeOutlier2[extremeInc2][1] = data[row][0]  # date
    #                 extremeOutlier2[extremeInc2][2] = data[0][elem]  # employee
    #                 extremeInc2 = extremeInc2 + 1
    #
    #             else:
    #                 mildOutlier2[mildInc2][0] = mildInc2
    #                 mildOutlier2[mildInc2][1] = data[row][0]  # date
    #                 mildOutlier2[mildInc2][2] = data[0][elem]  # employee
    #                 mildInc2 = mildInc2 + 1

    return mildOutlier1


def median(numbersLists):
    # cleanerNumbersLists= numbersLists[1:len(numbersLists)-2]

    # cleanerNumbersLists=[]

    cleanerNumbersLists = list(numbersLists)

    for row in range(1, len(numbersLists)):
        for elem in range(1, len(numbersLists[0])):
            # cleanerNumbersLists.append(numbersLists[row][elem])
            cleanerNumbersLists[row][elem] = numbersLists[row][elem]

    # for row in range(1, len(numbersLists)):
    # cleanerNumbersLists.append(numbersLists[row][elem])
    # cleanerNumbersLists[row]=cleanerNumbersLists[row].sort()

    # print(type(cleanerNumbersLists[1][0]))
    # print(cleanerNumbersLists[1].sort())
    cleanedData = []
    # cleanedData.append(cleanerNumbersLists[0])
    cleanedData = list(cleanerNumbersLists)

    for row in range(1, len(cleanerNumbersLists)):
        cleanedData[row] = sorted(cleanerNumbersLists[row])
        # print(cleanedData)
    # cleanedData[0] = sorted(cleanerNumbersLists[1])
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
    # lenList=len(cleanedDataLists)-1
    boxplotVals = [[0 for x in range(10)] for y in range(len(cleanedDataLists))]

    # position
    cnt = 0
    for row in range(0, len(cleanedDataLists[1])):
        boxplotVals[row][0] = cnt
        cnt = cnt + 1

    # median
    for row in range(1, len(cleanedDataLists[1]) - 1):

        if (len(cleanedDataLists[1]) - 1) % 2 == 0:
            mid = (len(cleanedDataLists[1]) - 1) / 2
            # mid = round(mid)
            # mid= mid-1 #correct midpoint
            mid = int(mid)
            median = cleanedDataLists[row][mid + 1]  # factoring in 0 in 1st col
            # print(median)
        #
        else:
            mid = (len(cleanedDataLists[1]) - 1) / 2
            low = mid - 0.5
            high = mid + 0.5
            median = (cleanedDataLists[row][low + 1] + cleanedDataLists[row][high + 1]) / 2
            # print(median)
        boxplotVals[row][1] = median

    # lowerquartile
    for row in range(1, len(cleanedDataLists) - 1):
        rowLength = len(cleanedDataLists[1])
        lowerQ = .25 * rowLength
        lowerQ = int(lowerQ)

        lowerQuartile = cleanedDataLists[row][lowerQ]
        boxplotVals[row][2] = lowerQuartile
        # print(boxplotVals[row][2])

    # upperquartile

    for row in range(1, len(cleanedDataLists) - 1):
        rowLength = len(cleanedDataLists[1])
        upperQ = .75 * rowLength
        upperQ = int(upperQ)

        upperQuartile = cleanedDataLists[row][upperQ]
        boxplotVals[row][3] = upperQuartile
        # print(boxplotVals[row][2])

    # interquartile
    for row in range(1, len(cleanedDataLists) - 1):
        interquartile1 = boxplotVals[row][3]
        interquartile2 = boxplotVals[row][2]

        # for some inexplicable reason regular subtraction yielded
        # terribly wrong results.
        interquartile = interquartile1 - interquartile2

        boxplotVals[row][4] = interquartile
        # print(boxplotVals[row][3])
        # print(boxplotVals[row][2])
        # print(boxplotVals[row][4])

    # lower inner fence2
    for row in range(1, len(cleanedDataLists) - 1):
        # calculations for some reason still arent accurate
        lowerInnerFence = boxplotVals[row][2] - ((boxplotVals[row][4]) * 1.5)
        boxplotVals[row][5] = lowerInnerFence

    # upper inner fence2
    for row in range(1, len(cleanedDataLists) - 1):
        # calculations for some reason still arent accurate
        upperInnerFence = ((boxplotVals[row][4]) * 1.5) + boxplotVals[row][3]
        boxplotVals[row][6] = upperInnerFence

    # lower outer fence2
    for row in range(1, len(cleanedDataLists) - 1):
        # calculations for some reason still arent accurate
        lowerOuterFence = boxplotVals[row][2] - ((boxplotVals[row][4]) * 3)
        boxplotVals[row][7] = lowerOuterFence
        # print(lowerOuterFence)

    # upper outer fence2
    for row in range(1, len(cleanedDataLists) - 1):
        # calculations for some reason still arent accurate
        upperOuterFence = boxplotVals[row][3] + ((boxplotVals[row][4]) * 3)
        boxplotVals[row][8] = upperOuterFence

    return boxplotVals


# 9626
#     0 1 2 3 4 5 6 7 8 9 10 11-6
#     1 2 3 4 5 6 7 8 9 10 11 -5
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# 1 2 3 4 5 6 7 8 9 10


def main():
    data = []
    rowInc = 0
    initFlag = 0

    with open('RawFinancialData2022.csv', newline='') as csvfile:
        infoReader = csv.reader(csvfile, delimiter=',')
        for row in infoReader:
            data.append(row)
            rowInc = rowInc + 1

    # now move to a number array

    numData = list(data)

    # remove date
    for elem in range(0, len(numData)):
        numData[elem][0] = float(0)

    # turn first string row to float
    for row in range(0, 1):
        for elem in range(1, len(numData[0])):
            numData[row][elem] = float(0)

    # convert strings to lists of numbers
    for row in range(1, len(numData)):
        for elem in range(1, len(data[0])):
            x = numData[row][elem]
            numData[row][elem] = float(x)
    # print(type(numData[1][1]))
    # print(len(numData[1]))
    # print(numData[1])

    cleanedData = median(numData)
    boxplotVals = boxplot(cleanedData)

    print(cleanedData[1])
    print(boxplotVals[1])
    extremeOutliers1, mildOutliers1 = anomalyChecker1(boxplotVals, cleanedData, data)
    extremeOutliers2 = anomalyChecker2(boxplotVals, cleanedData, data)
    mildOutliers2 = anomalyChecker3(boxplotVals, cleanedData, data)

    # print(extremeOutliers1)
    # print(mildOutliers1)
    # print(extremeOutliers2)
    # print(mildOutliers2)

    # anomalyCounter(extremeOutliers1,mildOutliers1)

    # print(', '.join(row))
    # print("\n"+row)

    # print(data[0][2])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
