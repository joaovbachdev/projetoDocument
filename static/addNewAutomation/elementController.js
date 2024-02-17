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