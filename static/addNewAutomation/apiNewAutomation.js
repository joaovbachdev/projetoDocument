function addNewAutomation_api(data){
   console.log("to aqui")
    $.ajax({
        url:`/addNewAutomationDb`,
        type:'POST',
        data:JSON.stringify({'elementName':data['elementName'],'elementType':data['elementType'],'data':data['data']}),
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