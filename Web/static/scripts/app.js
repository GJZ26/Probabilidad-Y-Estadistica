const wiwtk = document.getElementById("wiwtk")
const singleDataGiven = document.getElementById("singleDataGiven")
const groupedDataGiven = document.getElementById("groupedDataGiven")


const ig = document.getElementById("infoGiven")

const optionsSelections = document.getElementsByClassName("userInformation")

let availableOptions = []
let allowedOperations = []
let allowedOperationsForGroupedData = []

const possibleOperations = {
    "classesNumber": [["dataLen"], ["dataList"]],
    "dataRange": [["minData", "maxData"], ["dataList"]],
    "dataAmplitude": [["dataRange", "classesNumber", "variationUnit"], ["dataList"]],
    "variationUnit": ["dataList"],
    "frec": ["dataList", "limInf", "limSup"]
}

const individualData = ["minData", "maxData", "dataLen", "classesNumber", "dataRange", "dataAmplitude", "variationUnit"]
const groupedData = ["frec", "limSup", "limInf", "marcaClasses", "limInfEx", "limSupEx"]

const possibleOperationsWithGroupedData = {
    "limSup": ["limInf", "dataAmplitude", "variationUnit"],
    "limInf": ["limSup", "variationUnit"],
    "marcaClasses": ["limSup", "limInf"],
    "limInfEx": ["limSup", "limInf"],
    "limSupEx": ["limSup", "limInf"]
}

const namesOperation = {
    "limSup": "Límite Superior",
    "limInf": "Límite Inferior",
    "marcaClasses": "Marca de Clases",
    "limInfEx": "Límite Inferior Exacto",
    "limSupEx": "Límite Superior Exacto",
    "classesNumber": "Número de clases",
    "dataRange": "Rango",
    "dataAmplitude": "Amplitud",
    "variationUnit": "Unidad de Variación",
    "frec": "Frecuencia",
    "minData": "Valor mínimo",
    "maxData": "Valor máximo",
    "dataLen": "Longitud de los datos"
}

for (let i = 0; i < optionsSelections.length; i++) {
    optionsSelections[i].addEventListener('click', () => {
        validatePossibleOperations()
        addOptions()
        askData()
    })
}

function validatePossibleOperations() {
    // Verifica cuales casillas de "Qué Sé están seleccionadas"
    availableOptions = []
    allowedOperations = []
    allowedOperationsForGroupedData = []

    for (let i = 0; i < optionsSelections.length; i++) {
        if (optionsSelections[i].checked) availableOptions.push(optionsSelections[i].name)
    }

    // Recorremos cada posible operación
    for (i in possibleOperations) {
        // Recorremos cada posible recepción de datos de las operaciones
        if (typeof (possibleOperations[i][0]) === 'string') {
            if (possibleOperations[i].every((val) => {
                return availableOptions.includes(val)
            })) {
                allowedOperations.push(i)
            }
        } else {
            for (let j = 0; j < possibleOperations[i].length; j++) {
                if (possibleOperations[i][j].every((val) => {
                    return availableOptions.includes(val)
                })) {
                    allowedOperations.push(i)
                }
            }
        }
    }

    // Data Grouped Dara
    for (i in possibleOperationsWithGroupedData) {
        // Recorremos cada posible recepción de datos de las operaciones
        if (typeof (possibleOperationsWithGroupedData[i][0]) === 'string') {
            if (possibleOperationsWithGroupedData[i].every((val) => {
                return availableOptions.includes(val)
            })) {
                allowedOperationsForGroupedData.push(i)
            }
        } else {
            for (let j = 0; j < possibleOperationsWithGroupedData[i].length; j++) {
                if (possibleOperationsWithGroupedData[i][j].every((val) => {
                    return availableOptions.includes(val)
                })) {
                    allowedOperationsForGroupedData.push(i)
                }
            }
        }
    }
}

function addOptions() {
    let htmlFormat = '<h1 class="segmentTitle">¿Qué quieres saber?</h1>'

    for (let i = 0; i < allowedOperations.length; i++) {
        htmlFormat += `
        <div class="results">
            <input type="checkbox" class="resultInformation" name="${allowedOperations[i]}-result" id="${allowedOperations[i]}-result">
            <label for="${allowedOperations[i]}-result">${namesOperation[allowedOperations[i]]}</label>
        </div>
        `
    }

    for (let i = 0; i < allowedOperationsForGroupedData.length; i++) {
        htmlFormat += `
        <div class="results">
            <input type="checkbox" class="resultInformation" name="${allowedOperationsForGroupedData[i]}-result" id="${allowedOperationsForGroupedData[i]}-result">
            <label for="${allowedOperationsForGroupedData[i]}-result">${namesOperation[allowedOperationsForGroupedData[i]]}</label>
        </div>
        `
    }

    wiwtk.innerHTML = htmlFormat
}

function askData() {

    let HTMLSingleData = ""

    const table = document.createElement('table')
    const row = document.createElement('tr')
    const row2 = document.createElement('tr')

    for (let i = 0; i < availableOptions.length; i++) {

        if (individualData.includes(availableOptions[i])) {
            HTMLSingleData += `
            <label>${namesOperation[availableOptions[i]]}</label>
            <input type="number" name="${availableOptions[i]}">
            `
        }

        if (groupedData.includes(availableOptions[i])) {
            const header = document.createElement('th')

            const cell = document.createElement('td')
            const input = document.createElement('input')

            header.textContent = namesOperation[availableOptions[i]]
            row.appendChild(header)

            cell.appendChild(input)
            row2.appendChild(cell)
        }

    }

    table.appendChild(row)
    table.appendChild(row2)

    groupedDataGiven.innerHTML = ""
    groupedDataGiven.appendChild(table)
    singleDataGiven.innerHTML = HTMLSingleData
}