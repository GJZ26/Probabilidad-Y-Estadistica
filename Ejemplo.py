import PyE_tools as pye

# Este es un script de cómo usar el módulo de PyE_tools...

# Los datos admitidos son de tipo lista, si lo almacenan Vectores, favor de convertirlo
# datos = [782,1333,515,1475,696,832,1052,700,987,542,1296,704,
#          814,1482,1023,739,643,956,1023,784]

# Aquí hay otros datos de ejemplos para que puedas probar el algoritmo,
# recuerda volver a comentar o eliminar la lista anterior, de tal modo que solo
# tengas una lista activa durante la ejecución.

datos = [1.82,1.43,1.51,1.47,1.69,1.88,1.52,1.72,1.78,1.54,1.61,1.66,
         1.70,1.81,1.58,1.48,1.53,1.73,1.61,1.56,1.57,1.78]

# datos = [87,66,73,68,48,37,76,85,74,65,93,77,66,83,78,49,57,38,69,78,89,
#          96,78,97,74,76,68,63,70,81,64,83,67,61,90,77,88,74,85,80,71,73,
#          61,57,72,80,77,85,80,89]

# datos = [128,146,136,136,150,140,124,134,142,138,136,120,130,136,132,136,
#          134,142,132,144]

print(pye.bubbleSort(datos))

# Es importante tratar la lista antes de empezar a usar la librería
# Usa la función listToDecimal para tratar las variables numéricas de las
# listas y evitar errores de redondeo por decimales...
pye.listToDecimal(datos)

# Puedes ordenar los datos de forma manual, o con las funciones
# de ordenamiento del módulo, estos métodos son:
#   * bubbleSort (Recomendado)
#   * gnomeSort
#   * insertionSort
#   * selectionSort
# 
# Estas funciones NO modifican la lista original, por lo que es necesario
# guardar la lista ordenada en una nueva variable.
datosOrdenados = pye.bubbleSort(datos)

# klassesNumber cuenta las clases que tendrá la tabla de distribución de frecuencia
# No es necesario tener los datos ordenados, retorna un número entero.
k = pye.klassesNumber(datos)

# dataRange calcula el rango de datos de datos de una lista, recibe dos parámetros
# list: La lista de datos
# isSorted: Un boleano para saber si la lista está ordenada, por defecto es True.
# Retorna un Int o Float
r = pye.dataRange(datosOrdenados)

# dataAmplitudeByList es una función que calcula la amplitud de las clases de la
# tabla de frecuencia, al igual que la función anterior, recibe dos parámetros
# list: La lista de datos
# isSorted: Un boleano para saber si la lista está ordenada, por defecto es True.
# Retorna un Decimal
# Puedes usar
a = pye.dataAmplitudeByList(datosOrdenados,True)

# Esta función identifica la unidad de variación de los datos, solo recibe un parámetro
#   * data: Lista con los datos, puede o no estar tratada u ordenada.
# Retorna un Decimal
uv = pye.variationUnit(datosOrdenados)

# Genera una lista bidimensional con los datos necesarios para generar una tabla,
# Recibe 5 parámetros:
#   * sortedData: lista con los datos ordenados,
#   * classesNumber: entero con el número de clases para la tabla,
#   * dataRange: Rango de los datos por clase de la tabla,
#   * amplitude: Amplitud de la tabla de datos,
#   * variationUnit: Unidad de variación de los datos,
# Retorna un lista bidiomensional
# Lista primer nivel: [[...],[...],[...],...]
# Lista segundo nivel: [LetraDeLaClase, LímiteInferior, LimiteSuperior, Frecuencia, Marca de la Clase, Limite Inferior Exacto, Limite Superior Exacto]
dataTable = pye.calculateFrecuencyByDataList(datosOrdenados,k,a,uv)


print(f'Número de Clases: {k}')
print(f'Rango: {r}')
print(f'Amplitud: {a}')
print(f'Unidad de Variación: {uv}')

# drawTable imprime la información formateada del retorno de la función calculateFrecuencyByDataList
# NO usar con ningún otro tipo de lista    
pye.drawTable(dataTable)