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
    var line = document.createElement("div")

    line.setAttribute("class","line")

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

    line.appendChild(newLine)
    line.appendChild(newButton)
    divPai.appendChild(line)
    

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

        itemPai = document.createElement("div")//CRIO E ESTILIZO A DIV PAI DE UM ITEM DA LISTA DE TESTES AUTOMATIZADOS
        itemPai.setAttribute("class","itemPai")

        


       


        item = document.createElement("div")
        item.setAttribute("class","testItem")


        infoItemDiv = document.createElement("div")
        infoItemDiv.setAttribute("class","infoItemDiv")
        titulo = document.createElement("h3")
        titulo.textContent = element["teste"]

        codigo = document.createElement("label")
        codigo.textContent = element["automacao"].join("\n")
        

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
        deleteButton.setAttribute("class","deleteTest")

        executarButton = document.createElement("button")
        executarButton.textContent = "executar" 
        executarButton.setAttribute("onclick",`executeTeste("${element["teste"]}")`)
        executarButton.setAttribute("class","executar")


     
    


        infoItemDiv.appendChild(executarButton)
        infoItemDiv.appendChild(titulo)
        infoItemDiv.appendChild(codigo)
        infoItemDiv.appendChild(itemStatus)
        infoItemDiv.appendChild(deleteButton)

        item.appendChild(infoItemDiv)


        lista.appendChild(item)
    })
}

function setBugList(data){
    console.log(data)
    lista = document.getElementById('bugList')
    Array.from(document.getElementsByClassName('bugItem')).forEach(element=>{
        element.remove()
    })
    data.forEach(bug=>{
        divNewItem = document.createElement('div')
        divNewItem.setAttribute('class','bugItem')

        newItem = document.createElement('p')
        newItem.textContent = bug

        bugButton = document.createElement('button')
        bugButton.textContent = 'deletar'
        bugButton.setAttribute('onclick',`deleteBug("${bug}")`)

        
        divNewItem.append(newItem)
        divNewItem.append(bugButton)
        lista.appendChild(divNewItem)
    })

}