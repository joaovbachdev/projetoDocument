function setFilter(values){

    const tagName = document.getElementById("tagFilter").value


    

    values["circles"].forEach(val => {
        if(val[1] === "True"){
            document.querySelector(`circle[elementName='${val[0]}']`).style.display = "block"
        }else{
            document.querySelector(`circle[elementName='${val[0]}']`).style.display = "none"
        }
        
    });
    values["lines"].forEach(val => {
        if(val[1] === "True"){
            document.querySelector(`line[elementName='${val[0]}']`).style.display = "block"
        }else{
            document.querySelector(`line[elementName='${val[0]}']`).style.display = "none"
        }
        
    });
}
function updateElementeTestsStatus(data){ //deve receber um dicionario da seguinte forma {"nome do elemento":"status"}
    Object.keys(data).forEach(val=>{
        if(data[val] == "none"){
            document.querySelectorAll(`circle[elementName='${val}'], line[elementName='${val}']`)[0].setAttribute("fill","#f5b470")
        }else if(data[val] == "naoRealizado"){
            document.querySelectorAll(`circle[elementName='${val}'], line[elementName='${val}']`)[0].setAttribute("fill","#e60000")
        }else{
            document.querySelectorAll(`circle[elementName='${val}'], line[elementName='${val}']`)[0].setAttribute("fill","#0bfc03")
        }
    })
}

function addNewAutomation(elementName,type){
        window.location.href = `/addNewAutomation?name=${elementName}&type=${type}`; 
}