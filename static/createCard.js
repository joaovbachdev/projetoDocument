function createCard(informations){
    ele = document.getElementById("card")
    but = ele.querySelector("button")
    //title = document.createElement("h1")
    ele.classList.toggle('hidden')
    ele.querySelector("h1").textContent = informations['name']
    ele.querySelector("p").textContent = informations['description']

    but.setAttribute("acao",informations['name'])
    but.setAttribute("onclick","executa()")
    //title.textContent = informations['name']

    //desciption = document.createElement('p')
    //desciption.textContent = informations['description']
    
    //ele.style.display = 'block'
    //ele.appendChild(title)
    //ele.appendChild(desciption)
}