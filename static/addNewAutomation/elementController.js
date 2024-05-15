function adicionar(name,type){
    var plataforma = document.getElementById('isTestMobile').checked
    var newData = {}
    var nameAutomation = document.getElementById("automationName").value
    var status = "naoRealizado"
    var acoes = []

    if(plataforma == true){
        var area = ""
        document.querySelectorAll('.testMobileLine').forEach(element=>{
            area = element.querySelector('.areasSelect').value
            element.querySelectorAll('.mobileTestes').forEach((testes,index)=>{
                teste = document.querySelector(`option[value='${testes.value}']`).getAttribute('teste')
                
               acoes.push({'area':area,'teste':teste})
               
            })
            
        })
        
        newData['plataforma'] = 'mobile'
        //acoes.push(element.value)
    }else{
        document.querySelectorAll('.linhaCodigo').forEach(elemento=>{
            acoes.push(elemento.value)
        })
        newData['plataforma'] = 'web'
    }
    console.log(acoes, "acoes")
    newData['teste'] = nameAutomation
    newData['status'] = status
    newData['automacao'] = acoes
    
    addNewAutomation_api({'elementName':name,'elementType':type, 'data':newData})
}
function addLine(data){
    
    var listaAutomationCode = document.getElementById("codigoAutomacao")

    if(data['plataforma']=='web'){
        var numOfLines = document.querySelectorAll("input[class='linhaCodigo']").length

        var line = document.createElement("div")

        line.setAttribute("class","line")
        line.setAttribute("index",`${numOfLines}`)

        var newLine = document.createElement("input")
        var newButton = document.createElement("button")

        
        newLine.setAttribute("type","text")
        newLine.setAttribute("class","linhaCodigo")
        newLine.setAttribute("index",`${numOfLines}`)

        newButton.setAttribute("class","addLine")
        newButton.setAttribute("index",`${numOfLines}`)
        newButton.setAttribute("onclick","addLine({'plataforma':'web'})")
        newButton.textContent = "add"

        line.appendChild(newLine)
        line.appendChild(newButton)
        listaAutomationCode.appendChild(line)
    

    //var previousButton = document.querySelectorAll(`button[index="${numOfLines-1}"]`)[0]
    //previousButton.textContent = "remove"
    //previousButton.setAttribute("onclick",`removeLine(${numOfLines-1})`)
    setAddRemoveButton('.line')
    
}else{//AQUI DEVE ENTRAR CASO TENHA QUE ADICIONAR UMA LINHA PARA UM TESTE MOBILE
    
    numOfLines = document.querySelectorAll('.testMobileLine').length

    divPai = document.createElement('div')
    divPai.setAttribute('class','testMobileLine')
    divPai.setAttribute('index',numOfLines)

    selectArea = document.createElement('select')
    selectArea.setAttribute('class','areasSelect')
    console.log(data, "to aqui")
    data['areas'].forEach(element=>{
        nvar = newOption = document.createElement('option');
        newOption.value = element;
        newOption.textContent = element;
        selectArea.appendChild(newOption)
    })

    selectTestes = document.createElement('select')
    selectTestes.setAttribute('class','mobileTestes')

    buttonAdd = document.createElement('button')
    buttonAdd.textContent = 'add'
    buttonAdd.setAttribute('class','addLineMobile')
    buttonAdd.setAttribute('onclick','getMobileTestArea(addLine,"mobile")')


    
    divPai.appendChild(selectArea)
    divPai.appendChild(selectTestes)
    divPai.appendChild(buttonAdd)
    listaAutomationCode.appendChild(divPai)


    selectArea.addEventListener('change',function(){
        getMobileAreaTests(this.parentNode,setMobileTests,this.value,numOfLines)
    })
    setAddRemoveButton('.testMobileLine')
}
}
function setAddRemoveButton(plataforma){

    numOfLines = document.querySelectorAll(plataforma).length

   
    lines = document.querySelectorAll(plataforma)

    lines.forEach(element=>{
        if(element.getAttribute('index') < numOfLines-1){
            console.log(element.getAttribute('index'))
            element.querySelector('button').textContent = 'remove'
            element.querySelector('button').setAttribute('onclick',`removeLine(${element.getAttribute('index')},"${plataforma}")`)
        }else{
            element.querySelector('button').textContent = 'add'
        }
    })
}
function removeLine(index,plataforma){
    document.querySelectorAll(plataforma)[index].remove()
    refreshIndexes(plataforma)
}
function refreshIndexes(plataforma){
    var linhas = document.querySelectorAll("input[class='linhaCodigo']")
    var botoes = document.querySelectorAll("button[class='addLine']")

    document.querySelectorAll(plataforma).forEach((element,index)=>{
        element.setAttribute("index",`${index}`)
    })

    setAddRemoveButton(plataforma)
        
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
        //console.log(element["automacao"].map(item=>item.teste).join('\n'))
        if(element.plataforma == 'mobile'){
            codigo.textContent = element["automacao"].map(item=> item.teste).join('\n')
        }else{
            codigo.textContent = element["automacao"].join('\n')
        }
        
        

        itemStatus = document.createElement("input")
        itemStatus.setAttribute("type","checkBox")
        itemStatus.setAttribute("onclick",`checkTodoNewAutomation(${index},'none')`)
        itemStatus.setAttribute('class','checkboxTest')

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

function setAutomationCode(state){


    if(state == true){//TESTE MOBILE
        document.querySelectorAll('.line').forEach(element=>{
            element.remove()
        })
        getMobileTestArea(addLine,'mobile')
        //addLine('mobile',data)
    }else{
        document.querySelectorAll('.testMobileLine').forEach(element=>{
            element.remove()
        })
        addLine({'plataforma':'web'})
    }
}
function setMobileTests(data){
    
    listItem = document.querySelector(`div[index="${data['index']}"]`)
    select = document.querySelector(`div[index="${data['index']}"] .mobileTestes`)


    select.querySelectorAll('.testOption').forEach(elemento=>{
        elemento.remove()
    })
   
    data['testes'].forEach(element=>{
        newOption = document.createElement('option')
        newOption.setAttribute('class','testOption')
        newOption.value = element['nome']
        newOption.textContent = element['nome']
        newOption.setAttribute('teste',element['automacao'])
        select.appendChild(newOption)
    })
}