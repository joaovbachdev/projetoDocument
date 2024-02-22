function adicionar(name,type){
    var newData = {}
    var nameAutomation = document.getElementById("automationName").value
    var status = "naoRealizado"
    var acoes = []

    document.querySelectorAll("input[class='linhaCodigo']").forEach(element=>{
        acoes.push(element.value)
    })
    newData['teste'] = nameAutomation
    newData['status'] = status
    newData['automacao'] = acoes

    
    addNewAutomation_api({'elementName':name,'elementType':type, 'data':newData})
}
function addLine(){
    var newLine = document.createElement("input")
    var newButton = document.createElement("button")

    var numOfLines = document.querySelectorAll("input[class='linhaCodigo']").length
    var divPai = document.getElementById("codigoAutomacao")

    if(document.querySelectorAll("input[class='linhaCodigo']")[numOfLines-1].value != ""){
    newLine.setAttribute("type","text")
    newLine.setAttribute("class","linhaCodigo")
    newLine.setAttribute("index",`${numOfLines}`)

    newButton.setAttribute("class","addLine")
    newButton.setAttribute("index",`${numOfLines}`)
    newButton.setAttribute("onclick","addLine()")
    newButton.textContent = "add"

    divPai.appendChild(newLine)
    divPai.appendChild(newButton)

    var previousButton = document.querySelectorAll(`button[index="${numOfLines-1}"]`)[0]
    previousButton.textContent = "remove"
    previousButton.setAttribute("onclick",`removeLine(${numOfLines-1})`)
    }else{
        console.log("linha vazia")
    }

 
}
function removeLine(index){
    var linhas = document.querySelectorAll("input[class='linhaCodigo']")
    var botoes = document.querySelectorAll("button[class='addLine']")

    linhas[index].remove()
    botoes[index].remove()
    refreshIndexes()
}
function refreshIndexes(){
    var linhas = document.querySelectorAll("input[class='linhaCodigo']")
    var botoes = document.querySelectorAll("button[class='addLine']")

    linhas.forEach((element,index)=>{
        element.setAttribute("index",`${index}`)
    })

    botoes.forEach((element,index)=>{
        element.setAttribute("index",`${index}`)
        if(index == botoes.length-1){
        element.setAttribute("onclick",`addLine()`)
        }else{
            element.setAttribute("onclick",`removeLine(${index})`)
        }
    })
}
function setStatusElement(data){
    if(data.includes('naoRealizado')){
        document.getElementById("status").style.backgroundColor = "red";
    }else if(data.includes('realizado')){
        document.getElementById("status").style.backgroundColor = "green";
    }else{
        document.getElementById("status").style.backgroundColor = "orange";
    }
}
function setTestList(data){

    document.querySelectorAll("div[class='testItem']").forEach(element=>{
        element.remove()
    })

    lista = document.getElementById("listaDeTestes")
    data.forEach((element, index)=>{
        item = document.createElement("div")
        item.setAttribute("class","testItem")
        titulo = document.createElement("h3")
        titulo.textContent = element["teste"]

        codigo = document.createElement("label")
        codigo.textContent = element["automacao"]

        itemStatus = document.createElement("input")
        itemStatus.setAttribute("type","checkBox")
        itemStatus.setAttribute("onclick",`checkTodoNewAutomation(${index},'none')`)

        if(element["status"] == "realizado"){
            itemStatus.checked = true
        }else{
            itemStatus.checked = false
    }
        deleteButton = document.createElement("button")
        deleteButton.textContent = "delete"
        deleteButton.setAttribute("onclick",`deleteTest(${index})`)

        
        item.appendChild(titulo)
        item.appendChild(codigo)
        item.appendChild(itemStatus)
        item.appendChild(deleteButton)
        lista.appendChild(item)
    })
}
