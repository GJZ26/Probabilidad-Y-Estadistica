import math
from decimal import Decimal

# Versión pre-alpha :), se puede usar, pero es suuuuper inestable...

# Créditos por iluminarme durante la elaboración de esta vaina:
#   * https://github.com/Leonardo-Toledo-V
#   * https://github.com/ShonSagoro



# Funciones de ordamiento de datos (Sólo numéricos) - Estables
# Crédito: https://github.com/LWH-21

def bubbleSort(data: list):
    result = data.copy()
    permutation = True
    iteration = 0
    while permutation == True:
        permutation = False
        iteration = iteration + 1
        for actual in range(0, len(result) - iteration):
            if result[actual] > result[actual + 1]:
                permutation = True
                result[actual], result[actual + 1] = result[actual + 1], result[actual]
    return result


def gnomeSort(data: list):
    result = data.copy()
    i_b, i_i, dataLength = 1, 2, len(result)
    while i_b < dataLength:
        if result[i_b - 1] <= result[i_b]:
            i_b, i_i = i_i, i_i + 1
        else:
            result[i_b - 1], result[i_b] = result[i_b], result[i_b - 1]
            i_b -= 1
            if i_b == 0:
                i_b, i_i = i_i, i_i + 1
    return result


def insertionSort(data: list):
    result = data.copy()
    for i in range(1, len(result)):
        actual = result[i]
        j = i
        while j > 0 and result[j - 1] > actual:
            result[j] = result[j - 1]
            j = j - 1
        result[j] = actual
    return result


# Funciones de ordenamiento (Sólo numérico) - Inestable
# Crédito: https://github.com/LWH-21


def selectionSort(data: list):
    result = data.copy()
    nb = len(result)
    for actual in range(0, nb):
        mas_pequeno = actual
        for j in range(actual + 1, nb):
            if result[j] < result[mas_pequeno]:
                mas_pequeno = j
        if min is not actual:
            temp = result[actual]
            result[actual] = result[mas_pequeno]
            result[mas_pequeno] = temp
    return result


# Funciones de normalización de tipo de variables


def listToDecimal(data: list):
    for i in range(0, len(data)):
        data[i] = Decimal(str(data[i]))
    return data


# Funciones para cálculo de Distribuciones de Frecuencias :)

letterForNames = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def klassesNumber(data: list):
    return round(1 + 3.322 * math.log10(len(data)))


def dataRange(sortedData: list, isSorted: bool = True):
    if isSorted:
        return sortedData[len(sortedData) - 1] - sortedData[0]
    else:
        tempList = bubbleSort(sortedData)
        return tempList[len(tempList) - 1] - tempList[0]


def dataAmplitudeByList(data: list, isSorted: bool = True):
    range = (dataRange(data, isSorted))
    classesNumber = (klassesNumber(data))
    uv = variationUnit(data)
    if(variationUnit(data) == 1):
        if "." in str(range/classesNumber):
            return Decimal(str(math.ceil(Decimal(str(range/classesNumber)))))
        else:
            return Decimal(str(math.ceil(Decimal(str(range/classesNumber)))))+1
    
    return Decimal(str((math.ceil(Decimal(str(range / classesNumber))/uv)*uv)))


def dataAmplitudeByVariables(range: int, classesNumber: int):
    if(math.ceil(range / classesNumber)) is int:
        return math.ceil(range / classesNumber) + 1
    else:
        return math.ceil(range / classesNumber)


def variationUnit(data: list):
    maxDecimalNumber = 0
    for i in data:
        if "." in str(i):
            maxDecimalNumber = (
                len(str(i).split(".")[1])
                if len(str(i).split(".")[1]) > maxDecimalNumber
                else maxDecimalNumber
            )

    return Decimal(str(math.pow(10, -(maxDecimalNumber))))


def calculateFrecuencyByDataList(
    sortedData: list,
    classesNumber: int,
    amplitude: Decimal,
    variationUnit: Decimal,
):
    result = []
    limInf = sortedData[0]

    for i in range(0, classesNumber):
        limSup = limInf + amplitude - variationUnit
        result.append(
            [
                letterForNames[i],  # Clase
                limInf,  # Límite Inferior
                limSup,  # Límite Superior
                frecuencyInRange(sortedData, limInf, limSup),  # Frecuencia
                (limSup + limInf) / 2,  # Marca de la clase
                limInf - (variationUnit / 2),  # Limite Inferior Exacto
                limSup + (variationUnit / 2),  # Límite Superior Exacto
            ]
        )
        limInf = limSup + variationUnit

    return result


def frecuencyInRange(data: list, limInf: Decimal, limSup: Decimal):
    frecuency = 0
    for i in data:
        if i <= limSup and i >= limInf:
            frecuency += 1
    return frecuency


def drawTable(data: list):
    print(
        "{:<8}{:<15}{:<15}{:<10}{:<20}{:<18}{:<10}".format(
            "Clase",
            "Límite Inf.",
            "Límite Sup.",
            "Frec.",
            "Marca d Clases",
            "Lim Inf Exac",
            "Lim Sup Exac",
        )
    )
    print(
        "{:<8}{:<15}{:<15}{:<10}{:<20}{:<18}{:<10}".format(
            "---", "---", "---", "---", "---", "---", "---"
        )
    )
    for i in data:
        print(
            "{:<8}{:<15}{:<15}{:<10}{:<20}{:<18}{:<10}".format(
                i[0], i[1], i[2], i[3], i[4], i[5], i[6]
            )
        )
