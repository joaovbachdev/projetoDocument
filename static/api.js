var socket = io.connect('http://' + document.domain + ':' + location.port);


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
 function executar(name,type){
    console.log("executando automacao de ", name)
    if(!name.includes(("/"))){{
        document.querySelector(`i[elementName='${name}']`).style.display = 'block'
        socket.send('start')
    }}

    $.ajax({
        url:`/executar`,
        type:'POST',
        data:JSON.stringify({"name":name,"type":type,'plataforma':'mobile'}),
        contentType:'application/json',
        success: function(response){
            console.log("executando",response)
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
    elementType = document.getElementById("card").getAttribute("elementType")
    $.ajax({
        url:`/deletaTag`,
        type:'POST',
        data:JSON.stringify({'name':name,'father':father,'elementType':elementType}),
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
    elementType = document.getElementById("card").getAttribute("elementType")

    
    $.ajax({
        url:`/addNewTag`,
        type:'POST',
        data:JSON.stringify({'tagName':tagName,'fatherName':fatherName,'elementType':elementType}),
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
 function checkTagExists(callback){
     
    const tagName = document.getElementById("tagFilter").value
        $.ajax({
            url:`/checkTagExists?tagName=${tagName}`,
            type:'GET',
            contentType:'application/json',
            success: function(response){
                console.log("api dos filtros solicitada com sucesso")
                callback(response)
            },
            error:function(error){
                console.log("erro na api dos filtros")
            }
        });

 }
 function checkTagExistsLine(elementName,tagName){
    return new Promise(function(resolve, reject){
        console.log(elementName, tagName)
        $.ajax({
            url:`/checkTagExists?elementName=${elementName}&tagName=${tagName}&elementType=line`,
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

 function checkTodo(elementName, index, status){
    $.ajax({
        url:`/checkTodo`,
        type:'POST',
        data:JSON.stringify({'elementName':elementName,'index':index,'status':status}),
        contentType:'application/json',
        success: function(response){
            console.log("todo atualizado com sucesso")
        },
        error:function(error){
            console.log("erro ao atualizar todo")
        }
    });

 }
function setTesteAleatorio(){
    $.ajax({
        url:`/setExecuaoAleatoria`,
        type:'POST',
        data:JSON.stringify({}),
        contentType:'application/json',
        success: function(response){
            console.log("setei", response['nome'])
            if(!response['nome'].includes(("/"))){{
                document.querySelector(`i[elementName='${response['nome']}']`).style.display = 'block'
                socket.send('start')
            }}
            //console.log(response['nome'],response['index'],response['testes'])
            executaTesteAleatorio(response['nome'],response['index'],response['testes'])
        },
        error:function(error){
            console.log("erro ao atualizar todo")
        }
    });
   // setTimeout(setTesteAleatorio, 10000);
}

function executaTesteAleatorio(nome,index,testes){
    $.ajax({
        url:`/executaTesteAleatorio`,
        type:'POST',
        data:JSON.stringify({'nome':nome,'index':index,'testes':"",'plataforma':'mobile'}),
        contentType:'application/json',
        success: function(response){
                console.log("executado com sucesso o aleatorio")
        },
        error:function(error){
            console.log("erro ao atualizar todo")
        }
    });
}


function extraiRelatorio(){
    $.ajax({
        url:`/extraiRelatorio`,
        type:'GET',
        contentType:'application/json',
        success: function(response){
                console.log("ESTA AQUI O RELATOCIO", response)
        },
        error:function(error){
            console.log("erro ao atualizar todo")
        }
    });
}
function updatePagesSugestions(){
    
    suggestions = document.getElementById('pageResults')
    data = document.getElementById('searchPages').value
    newValues = notionPages.filter(function(item){
        return item.includes(data)
    })

    Array.from(document.getElementsByClassName('pageItem')).forEach(element=>{
        element.remove()
    })

    Array.from(newValues).forEach(val => {
        newItem = document.createElement('div')
        newItem.setAttribute('class','pageItem')

        newLabel = document.createElement('label')
        newLabel.textContent = val

        newCheckBox = document.createElement('input')
        newCheckBox.type = 'checkbox'
        newCheckBox.setAttribute('pagename',val)

        if(pagesSelected[val] == true){
            newCheckBox.checked = true
        }
        newCheckBox.addEventListener('click',function(){
            pagesSelected[this.getAttribute('pagename')] = this.checked
            elementName = document.getElementById('card').getAttribute('name')
            histName = this.getAttribute('pageName')
            checked = this.checked
            $.ajax({
                url:'/updatElementHistorys',
                type:'POST',
                data:JSON.stringify({'elementName':elementName,'histName':histName,'checked':checked}),
                contentType:'application/json',
                success: function(response){
                        console.log("historia atualizada")
                },
                error:function(error){
                    console.log("erro ao atualizar historia")
                }

            })           
        })

        newItem.appendChild(newLabel)
        newItem.appendChild(newCheckBox)
        suggestions.append(newItem)
    })
}
function getElementPages(name){
    data = []
    $.ajax({
        url:`/getElementPages`,
        type:'POST',
        data:JSON.stringify({'name':name}),
        contentType:'application/json',
        success: function(response){
                data = response
                make()
                console.log("paginas no elemento selecionado", response)
        },
        error:function(error){
            console.log("erro ao pegar paginas do elemneto")
        }
    });
    function make(){
        notionPages.forEach(element => {
            if(data.includes(element)){
                pagesSelected[element] = true
            }else{
                pagesSelected[element] = false
            }
           
        });
    }



}
 socket.on('atualizar', function(data) {
    console.log("to aqui")
    elementos = document.querySelectorAll("input[type='checkbox']")
    if(elementos.length >0){
     if(data['status'] == "realizado"){
        document.querySelectorAll("input[type='checkbox']")[data["index"]].checked = true
     }else{
        document.querySelectorAll("input[type='checkbox']")[data["index"]].checked = false
     }
    }
});

socket.on('atualizarStatus', function(data) {
    updateElementeTestsStatus(data)
});

socket.on('desativarSpiner', function(elementName) {
    if(!elementName.includes("/"))
    document.querySelector(`i[elementName='${elementName}']`).style.display = 'none'
});