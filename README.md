# PyE Tools
Las herramientas de Probabilidad Y Estadísitica (PyE Tools) son un conjunto de funciones que te ayudan a realizar tablas de distribución de frecuencia de forma fácil y bonita :).

Este proyecto consta de un módulo:
 * **PyE_tools**
  
Y de un aplicativo:
 * **DocxVersion**

En este archivo explicaremos cada uno de ellos:

# PyE_tools
Es un módulo que contiene una serie de funciones para calcular tablas de frecuencia a partir de una serie de datos dada.

No es necesario la instalación de ningún otro documento.

## Algoritmo de ordenamiento

Este módulo provee de algoritmo de ordamiento de datos de tipo numéricos, dentro de los cuales se halla

  * **Estables**
    * `bubbleSort()`
    * `gnomeSort()`
    * `insertionSort()`
  * **Inestables**
    * `selectionSort()`

Cada uno de estos métodos recibe un único parámetro de tipo `list`, el cual contiene los datos a organizar y retorna una nueva lista, por lo que es importante guardar el retorno de esta función de una nueva variable.

Ejemplo:
``` python
import PyE_tools as pye

data = [2, 5, 3, 1, 4, 6]

dataSorted = pye.bubbleSort(data)
         # o pye.gnomeSort(data)
         # o pye.insertionSort(data)
         # o pye.selectionSort(data)

print(data) # [2, 5, 3, 1, 4, 6]
print(dataSorted) # [1, 2, 3, 4, 5, 6]
```

## Normalización de tipo de variables

Este módulo cuenta con una función llamada `listToDecimal()`, que convierte todos los valores de una lista de datos a variables de tipo decimal, es recomendable hacer esto antes de realizar cualquier otro paso. 

Este método SÍ cambia la lista original

Aquí un ejemplo de uso:

```python
import PyE_tools as pye

data = [1,2.2,3]

print(data) # [1, 2.2, 3]
pye.listToDecimal(data)
print(data) # [Decimal(1.0), Decimal(2.2), Decimal(3.0)]

```

Cuando se trabaja con números punto flotante, algunos lenguajes pueden tener errores al realizar operaciones, esto se debe a su naturaleza numérica, ya que trabajan con sistemas con base 2, mientras que nosotros usamos sistemas base 10.

Para resolver estos inconvenientes, podemos usar tipo de datos como `Decimal` para solventar estos errores.

Estos son algunos de los errores:

Resta de 1.83 - 1.43 con variables de tipo float.
```python
a = 1.83
b = 1.43
print (a-b) # 0.40000000000000013
```

Resta de 1.83 - 1.43 con variables de tipo Decimal redondeado.
```python
import decimal

a = decimal.Decimal(1.83)
b = decimal.Decimal(1.43)
print (a-b) # Decimal (0.4000000000000001332267629550)
```

Resta de 1.83 - 1.43 con variables de Decimal, convertido desde un String.
```python
import decimal

a = decimal.Decimal(str(1.83))
b = decimal.Decimal(str(1.43))
print (a-b) # Decimal (0.40)
```

De esta forma, podemos realizar operaciones con datos con decimales de forma precisa.

## Calculo de Distribución
### `klassesNumber()`
Calcula el número de clases de debe tener una tabla de frecuencia según los datos dados
* Parámetros: 
  * Data [List]: Lista de datos
* Retorno [Int]: Número de las clases previstas

Ejemplo:
```python
import PyE_tools as pye

data = [1,2,3,4,5,6]
k = pye.klassesNumber(data)

print(k) # 4
```
### `dataRange()`
Calcula el rango de los datos de una lista dada, esta puede ser ordenada o no.

* Parámetros:
  * sortedData [list]: Lista de los datos, debe ser una lista con las variables tratadas, véase: [Normalización de tipo de variables](#normalización-de-tipo-de-variables).
  * isSorted [bool] [defecto: True]: Define si la lista dada está o no ordenada, en caso de ser True, el método ordenará la lista y hará el cálculo.
* Retorno [int || float]: Rango de los datos

Ejemplo:
```python
import PyE_tools as pye

data = [5,2,1,4,6,3]

# Resultado con los datos desordenado: Erróneo
pye.dataRange(data) # -2

# Para ordenar y luego realizar el cálculo
pye.dataRange(data, False) # 5

```

### `dataAmplitudeByList()`
Calcula la amplitud de los datos dados, a través de una lista.

Nota: Los datos dados están redondeado al número entero mayor más cercano en caso de tener una unidad de variación igual a 1.

* Parámetros:
  * data [list]: Lista de los datos, debe ser una lista con las variables tratadas, véase: [Normalización de tipo de variables](#normalización-de-tipo-de-variables).
  * isSorted [bool] [defecto: True]: Define si la lista dada está o no ordenada, en caso de ser True, el método ordenará la lista y hará el cálculo.
* Retorno [Decimal]: Amplitud de los datos

Ejemplo:
```python
import PyE_tools as pye

data = [5,2,1,4,6,3]

# Resultado con los datos desordenado: Erróneo
pye.dataAmplitudeByList(data) # 0

# Para ordenar y luego realizar el cálculo
pye.dataAmplitudeByList(data, False) # 2

```

### `variationUnit()`
Identifica la unidad de variación de la lista tomando en cuenta el número con mayor decimales de la lista.

* Parámetro [list]: Lista con los datos.
* Retorno [Decimal]: Unidad de variación.

Ejemplo:
```python
import PyE_tools as pye

data1 = [1, 2, 3]

data2 = [1.1, 2.2, 3.4]

data3 = [1.1, 2.12, 3.123]

pye.variationUnit(data1) # 1.0
pye.variationUnit(data2) # 0.1
pye.variationUnit(data3) # 0.001
```

### `calculateFrecuencyByDataList()`
Esta función calcula la cada clase de la tabla de distribución de frecuencia.

* Parámetro:
  * sortedData [list]: Lista con los datos ordenados y con las variables tratadas, véase: [Normalización de tipo de variables](#normalización-de-tipo-de-variables) y [Algoritmo de ordenamiento](#algoritmo-de-ordenamiento).
  * classesNumber [int]: Número de clases de la tabla, véase [klassesNumber()](#klassesnumber).
  * amplitude [Decimal]: Amplitud de los datos, véase [dataAmplitudeByList()](#dataamplitudebylist).
  * variationUnit [Decimal]: Unidad de variación, véase [variationUnit()](#variationunit).
* Retorno: Un arreglo bidimensional con los datos de cada clase.

Ejemplo de uso.
```python
import PyE_tools as pye
from decimal import Decimal

data = [1, 2, 3, 4, 5, 6]
numero_de_clases = 4
amplitud = Decimal(2)
unidad_de_variacion = Decimal(1.0)

table_info = pye.calculateFrecuencyByDataList(data, numero_de_clases, amplitud, unidad_de_variacion)

print(table_info) # [[...][...][...]...] longitud = numero_de_clases
print(table_info[0]) # ['A', 1, Decimal('2.0'), 2, Decimal('1.5'), Decimal('0.5'), Decimal('2.5')]
```
Donde:
```python
table_info[n] # ['A', 1, Decimal('2.0'), 2, Decimal('1.5'), Decimal('0.5'), Decimal('2.5')] -> info de la clase n
table_info[n][0] # 'A' -> Letra de la clase
table_info[n][1] # '1' -> Limite Inferior
table_info[n][2] # '2.0' -> Límite Superior
table_info[n][3] # '2' -> Frecuencia
table_info[n][4] # '1.5' -> Marca de la clase
table_info[n][5] # '0.5' -> Limite Inferior Exacto
table_info[n][6] # '2.5' -> Límite Superior Exacto
```

### `drawTable()`
Presenta los resultados de la función [`calculateFrecuencyByDataList()`](#calculatefrecuencybydatalist).

Ejemplo de uso:
```python
import PyE_tools as pye
from decimal import Decimal

data = [1, 2, 3, 4, 5, 6]
numero_de_clases = 4
amplitud = Decimal(2)
unidad_de_variacion = Decimal(1.0)

table_info = pye.calculateFrecuencyByDataList(data, numero_de_clases, amplitud, unidad_de_variacion)

drawTable(table_info)
```

Salida:
```bash
Clase   Límite Inf.    Límite Sup.    Frec.     Marca d Clases      Lim Inf Exac      Lim Sup Exac
---     ---            ---            ---       ---                 ---               ---
A       1              2.0            2         1.5                 0.5               2.5
B       3.0            4.0            2         3.5                 2.5               4.5
C       5.0            6.0            2         5.5                 4.5               6.5
D       7.0            8.0            0         7.5                 6.5               8.5
```