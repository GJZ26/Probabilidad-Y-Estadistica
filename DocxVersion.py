import PyE_tools as pye
import math
import decimal
import docx
from docx.shared import Pt

data = []
dataToShow = []

# Lectura de datos
try:
    info = open("problem.txt", "r", -1, "utf-8").readlines()
except:
    print("No se ha podido abrir el archivo problem.txt :(")
    quit()


# Lecturas de documento problem.txt
for i in range(1, len(info)):
    try:
        data.append(decimal.Decimal(info[i].strip()))
        dataToShow.append(info[i].strip())
    except:
        print(f"No se pudo convertir el siguiente dato: {info[i].strip()}")

# Escribiendo el documento
document = docx.Document()

# Fuente
font = document.styles["Normal"].font
font.name = "Arial"

# Escritura del problema
paragraph = document.add_paragraph()
run = paragraph.add_run()
run.bold = True
run.add_text("Problema: ")
run = paragraph.add_run()
run.add_text(info[0].strip())

# Escritura de los primero datos
paragraph = document.add_paragraph()
run = paragraph.add_run()
run.bold = True
run.add_text("Datos: ")
run = paragraph.add_run()
run.add_text(", ".join(dataToShow) + ".")

# Escritura de los datos ordenados
dataSorted = pye.bubbleSort(data)
dataToShow = []
k = pye.klassesNumber(data)
r = pye.dataRange(dataSorted)
a = pye.dataAmplitudeByList(dataSorted, True)
uv = pye.variationUnit(dataSorted)
dataTable = pye.calculateFrecuencyByDataList(dataSorted, k, r, a, uv)

for i in dataSorted:
    dataToShow.append(str(i))

paragraph = document.add_paragraph()
run = paragraph.add_run()
run.bold = True
run.add_text("Datos Ordenados: ")
run = paragraph.add_run()
run.add_text(", ".join(dataToShow) + ".")

# Número de clases
paragraph = document.add_paragraph()
run = paragraph.add_run()
run.bold = True
run.add_text("Número de Clases: ")
run = paragraph.add_run()
run.add_text(
    f"1 + 3.322 x log({len(dataSorted)}) = {1 + 3.322 * math.log10(len(data))} ≈ {k}"
)

# Rango
paragraph = document.add_paragraph()
run = paragraph.add_run()
run.bold = True
run.add_text("Rango: ")
run = paragraph.add_run()
run.add_text(
    f"{str(dataSorted[len(dataSorted)-1])} - {str(dataSorted[0])} = {str(dataSorted[len(dataSorted)-1] - dataSorted[0])} ≈ {r}"
)

# Amplitud
paragraph = document.add_paragraph()
run = paragraph.add_run()
run.bold = True
run.add_text("Amplitud: ")
run = paragraph.add_run()
run.add_text(f"{r} ÷ {k} = {r/k} ≈ {a}")

# Unidad de variacion
paragraph = document.add_paragraph()
run = paragraph.add_run()
run.bold = True
run.add_text("Unidad de variación: ")
run = paragraph.add_run()
run.add_text(str(uv))


# Tabla
header = [
    "Clase",
    "Límite Inf.",
    "Límite Sup.",
    "Frec.",
    "Marca d Clases",
    "Lim Inf Exac",
    "Lim Sup Exac",
]
table = document.add_table(rows=k+1, cols=len(header))

for i in range(0,len(dataTable)):
    table.cell(0,i).text = header[i]
    for k in range(0, len(dataTable[i])):
        table.cell(i+1,k).text = str(dataTable[i][k])        

document.save("result.docx")