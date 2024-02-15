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