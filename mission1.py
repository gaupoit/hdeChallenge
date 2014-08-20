def listSumSqrt(numList):
            if len(numList) == 1:
                    return numList[0] * numList[0]
            else:
                if (numList[0] > 0):
                    return (numList[0] * numList[0]) + listSumSqrt(numList[1:])
                else:
                     return listSumSqrt(numList[1:])

def mission1(numList):
        if len(numList) > 1:
            return listSumSqrt(numList)
        else:
            return ''
