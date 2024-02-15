function createCard(informations){
    ele = document.getElementById("card")
    ele.setAttribute("name",informations["name"])

    butExecutar = document.getElementById("executarCard")
    tags = document.getElementById("tags")
    todo = document.getElementById("todoTestes")

    let elementType = ""

    if(informations["name"].includes("/")){
        elementType = "lines"
        //ele.setAttribute("elementType","lines")
    }else{
        elementType = "elementos"
        //ele.setAttribute("elementType","elementos")
    }
    ele.setAttribute("elementType",elementType)

   
    if(ele.classList[1] == "hidden"){
        ele.classList.toggle('hidden')
        ele.classList.toggle('hidden')
    }else{
        ele.classList.toggle('hidden')
    }
       

    ele.querySelector("h1").textContent = informations['name']
    ele.querySelector("p").textContent = informations['description']

    butExecutar.setAttribute("acao",informations['name'])
    butExecutar.setAttribute("onclick",`executar("${informations['name']}","${elementType}")`)


    tags.querySelectorAll("label").forEach(element=>{
        element.remove();
    })
    informations["tags"].forEach(element => {
        newTag = document.createElement("label")
        newTag.setAttribute("class","tag")
        newTag.textContent = element
        newTag.setAttribute("name",element)

        deleteButton = document.createElement("button")
        deleteButton.setAttribute("class","deleteTag")
        deleteButton.setAttribute("name",element)
        deleteButton.setAttribute("element",informations["name"])
        deleteButton.setAttribute("onclick",`deletaElementTag('${element}','${informations["name"]}')`)
        deleteButton.textContent = "X"

        newTag.appendChild(deleteButton)
        tags.appendChild(newTag)
    });
    while (todo.firstChild) {
        todo.removeChild(todo.firstChild);
    }
    informations["testes"].forEach((teste,indice)=>{
        lab = document.createElement("label")
        inp = document.createElement("input")

        lab.textContent = teste["teste"]
        inp.setAttribute("type","checkbox")
        inp.setAttribute("onclick",`checkTodo("${informations["name"]}",${indice},"none")`)

        if(teste["status"]=="realizado"){
            inp.checked = true
        }

        todo.appendChild(lab)
        todo.appendChild(inp)
    })
    
}
function updateTag(tagName, elementName){
    tags = document.getElementById("tags")
    newTag = document.createElement("label")
    newTag.setAttribute("class","tag")
    newTag.textContent = tagName
    newTag.setAttribute("name",tagName)

    deleteButton = document.createElement("button")
    deleteButton.setAttribute("class","deleteTag")
    deleteButton.setAttribute("name",tagName)
    deleteButton.setAttribute("element",elementName)
    deleteButton.setAttribute("onclick",`deletaElementTag('${tagName}','${elementName}')`)
    deleteButton.textContent = "X"

    newTag.appendChild(deleteButton)
    tags.appendChild(newTag)
}

function closeCard(){
    ele = document.getElementById("card")
    ele.classList.toggle('hidden')
}
