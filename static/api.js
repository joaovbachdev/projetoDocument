function getElementos(callback)
{    
    $.ajax({
        url:'/getElementos',
        type:'GET',
        contentType:'application/json',
        success: function(response){
            callback(response)
        },
        error:function(error){
            console.log(error, "deu ruim")
        }
    }) 
 }
 function getInformations(callback, name){
    $.ajax({
        url:`/getInformations?name=${name}`,
        type:'GET',
        contentType:'application/json',
        success: function(response){
            callback(response)
        },
        error:function(error){
            console.log(error, "deu ruim")
        }
    }) 
 }
 function getLines(callback){
    $.ajax({
        url:`/getLines`,
        type:'GET',
        contentType:'application/json',
        success: function(response){
            callback(response)
        },
        error:function(error){
            console.log(error, "deu ruim")
        }
    }) 
 }
 function getLineInformations(callback, name){
    $.ajax({
        url:`/getLineInformation?name=${name}`,
        type:'GET',
        contentType:'application/json',
        success: function(response){
            callback(response)
        },
        error:function(error){
            console.log(error, "deu ruim")
        }
    }) 
 }

 function saveLine(){
     console.log("saveLine")
 }
 function executar(){
    $.ajax({
        url:`/executar`,
        type:'GET',
        contentType:'application/json',
        success: function(response){
            console.log("executando")
        },
        error:function(error){
            console.log(error, "deu ruim")
        }
    })  
 }

 function auxCriaElemento(pos, nome){
    $.ajax({
        url:`/auxCriaElemento`,
        type:'POST',
        data:JSON.stringify({'pos':pos,'name':nome}),
        contentType:'application/json',
        success: function(response){
            console.log("executando")
        },
        error:function(error){
            console.log(error, "deu ruim")
        }
    })
 }
 function deletaElementTag(name, father){
    document.getElementsByName(name)[0].remove()
    $.ajax({
        url:`/deletaTag`,
        type:'POST',
        data:JSON.stringify({'name':name,'father':father}),
        contentType:'application/json',
        success: function(response){
            console.log("deletando tag")
        },
        error:function(error){
            console.log(error, "deu ruim ao deletar tag")
        }
    })
 }
 function addNewTag(){
    tagName = document.getElementById("newTagName").value
    fatherName = document.getElementById("card").getAttribute("name")

    
    $.ajax({
        url:`/addNewTag`,
        type:'POST',
        data:JSON.stringify({'tagName':tagName,'fatherName':fatherName}),
        contentType:'application/json',
        success: function(response){
            console.log("adicionando tag")
        },
        error:function(error){
            console.log(error, "deu ruim ao adicionar tag")
        }
    })
    updateTag(tagName,fatherName)
 }  