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
 function executar(name){
    console.log("executando automacao de ", name)
    $.ajax({
        url:`/executar`,
        type:'POST',
        data:JSON.stringify({"name":name}),
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
 function checkTagExists(elementName,tagName){
    return new Promise(function(resolve, reject){
        console.log(elementName, tagName)
        $.ajax({
            url:`/checkTagExists?elementName=${elementName}&tagName=${tagName}`,
            type:'GET',
            contentType:'application/json',
            success: function(response){
                resolve(response)
            },
            error:function(error){
                reject(response)
            }
        });
    });

 }

 function checkTodo(elementName, index){
    $.ajax({
        url:`/checkTodo`,
        type:'POST',
        data:JSON.stringify({'elementName':elementName,'index':index}),
        contentType:'application/json',
        success: function(response){
            console.log("todo atualizado com sucesso")
        },
        error:function(error){
            console.log("erro ao atualizar todo")
        }
    });

 }