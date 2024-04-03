var socket = io.connect('http://' + document.domain + ':' + location.port);


function addNewAutomation_api(data){
    $.ajax({
        url:`/addNewAutomationDb`,
        type:'POST',
        data:JSON.stringify({'elementName':data['elementName'],'elementType':data['elementType'],'data':data['data'],'plataforma':data['plataforma']}),
        contentType:'application/json',
        success: function(response){
            console.log("teste adicionado com sucesso")
            getTestStatus(setStatusElement)
            getAutomationTests(setTestList)
        },
        error:function(error){
            console.log("falha ao salvar teste")
        }
    });
   
}
function getAutomationTests(callback){
    elementName = document.getElementById("infos").getAttribute("elementName")
    elementType = document.getElementById("infos").getAttribute("elementType")
    $.ajax({
        url:`/getAutomatedTests?elementName=${elementName}&elementType=${elementType}`,
        type:'GET',
        contentType:'application/json',
        success: function(response){
            callback(response)
            
        },
        error:function(error){
            console.log("erro ao buscar testes do elemento")
        }
    });
}
function getTestStatus(callback){
    elementName = document.getElementById("infos").getAttribute("elementName")
    elementType = document.getElementById("infos").getAttribute("elementType")
    $.ajax({
        url:`/getAutomatedTests?elementName=${elementName}&elementType=${elementType}`,
        type:'GET',
        contentType:'application/json',
        success: function(response){
            data = []
            response.forEach(element => {
                data.push(element["status"])
            });
            callback(data)
        },
        error:function(error){
            console.log("erro ao buscar testes do elemento")
        }
    });
}
function deleteTest(test){
    console.log("here")
    elementName = document.getElementById("infos").getAttribute("elementName")
    elementType = document.getElementById("infos").getAttribute("elementType")
    $.ajax({
        url:`/deleteTest`,
        type:'POST',
        data:JSON.stringify({"elementName":elementName, "elementType":elementType, "test":test}),
        contentType:'application/json',
        success: function(response){
            console.log("teste deletado com sucesso")
            getTestStatus(setStatusElement)
            getAutomationTests(setTestList)
        },
        error:function(error){
            console.log("erro ao deletar o teste")
        }
    });
}
function checkTodoNewAutomation(index, status){
    elementName = document.getElementById("infos").getAttribute("elementName")
    elementType = document.getElementById("infos").getAttribute("elementType")
    $.ajax({
        url:`/checkTodo`,
        type:'POST',
        data:JSON.stringify({'elementName':elementName,'index':index,'status':status}),
        contentType:'application/json',
        success: function(response){
            console.log("todo atualizado com sucesso")
            getTestStatus(setStatusElement)
        },
        error:function(error){
            console.log("erro ao atualizar todo")
        }
    });

 }

 function addBug(){
    elementName = document.getElementById("infos").getAttribute("elementName")
    elementType = document.getElementById("infos").getAttribute("elementType")
    bugElement = document.getElementById('newBugInput').value

    $.ajax({
        url:'/addBug',
        type:'POST',
        data:JSON.stringify({'elementName':elementName, 'elementType':elementType, 'bug':bugElement}),
        contentType:'application/json',
        success:function(response){
            setBugList(response)
            console.log(response)
        },
        error:function(error){
            console.log(error)
        }
    })
 }
 function getBugs(callback){
    elementName = document.getElementById("infos").getAttribute("elementName")
    elementType = document.getElementById("infos").getAttribute("elementType")

    $.ajax({
        url:`/getBugs?name=${elementName}&type=${elementType}`,
        type:'GET',
        contentType:'application/json',
        success:function(response){
            callback(response)
        },
        error:function(error){
            console.log(error)
        }

    })
 }

 function deleteBug(name){
    elementName = document.getElementById("infos").getAttribute("elementName")
    elementType = document.getElementById("infos").getAttribute("elementType")

    $.ajax({
        url:`/deleteBug`,
        type:'POST',
        data:JSON.stringify({'name':elementName,'type':elementType,'bugName':name}),
        contentType:'application/json',
        success:function(response){
            setBugList(response)
            console.log('deletado')
        },
        error:function(error){
            console.log(error)
        }

    })
 }
 function executeTeste(testeName){
     console.log(testeName)
    elementName = document.getElementById("infos").getAttribute("elementName")
    elementType = document.getElementById("infos").getAttribute("elementType")

    $.ajax({
        url:`/executaTesteEsp`,
        type:'POST',
        data:JSON.stringify({'name':elementName,'type':elementType,'testName':testeName}),
        contentType:'application/json',
        success:function(response){
            console.log(response)
        },
        error:function(error){
            console.log(error)
        }

    })
 }
function getMobileTestArea(callback, plataforma){
    $.ajax({
        url:`/getMobileTestArea`,
        type:'GET',
        contentType:'application/json',
        success:function(response){
            callback({'areas':response,'plataforma':plataforma})
        },
        error:function(error){
            console.log(error)
        }
    })
}

function getMobileAreaTests(pai,callback, value, index){
    
    $.ajax({
        url:`/getMobileTestes?value=${value}`,
        type:'GET',
        contentType:'application/json',
        success:function(response){
    
            callback({'index':pai.getAttribute('index'),'testes':response})
        },
        error:function(error){
            console.log(error)
        }
    })
    
}

 
socket.on('atualizaTesteEsp', function(data) {
   
    element = document.querySelectorAll('.checkboxTest')[data['index']]
   
    if(data['status']=='realizado'){
        element.checked = true
    }else{
        element.checked = false
    }
    //checkTodoNewAutomation(data['index'], data['status'])

});