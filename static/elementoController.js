function setFilter(){
    const tagName = document.getElementById("tagFilter").value
    document.querySelectorAll("circle").forEach(async element=>{
       
        let response = await checkTagExists(element.getAttribute("elementName"),tagName)
        if(response == "False"){
            element.style.display = "None"
        }else{
            element.style.display = "Block"
        }
    })
}