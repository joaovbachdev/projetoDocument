function createCard(informations){
    ele = document.getElementById("card")
    ele.setAttribute("name",informations["name"])
    but = ele.querySelector("button")
    tags = document.getElementById("tags")
    //title = document.createElement("h1")
    ele.classList.toggle('hidden')
    ele.querySelector("h1").textContent = informations['name']
    ele.querySelector("p").textContent = informations['description']

    but.setAttribute("acao",informations['name'])
    but.setAttribute("onclick","executa()")


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
    
    //title.textContent = informations['name']

    //desciption = document.createElement('p')
    //desciption.textContent = informations['description']
    
    //ele.style.display = 'block'
    //ele.appendChild(title)
    //ele.appendChild(desciption)
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