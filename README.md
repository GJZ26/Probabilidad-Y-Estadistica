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

