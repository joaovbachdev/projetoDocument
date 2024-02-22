function addNewAutomation_api(data){
   
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
            console.log("aqui estao os testes do elemento", response)
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
            console.log("aqui estao os testes do elemento", response)
        },
        error:function(error){
            console.log("erro ao buscar testes do elemento")
        }
    });
}
