function addNewAutomation_api(data){
   
    $.ajax({
        url:`/addNewAutomationDb`,
        type:'POST',
        data:JSON.stringify({'elementName':data['elementName'],'elementType':data['elementType'],'data':data['data']}),
        contentType:'application/json',
        success: function(response){
            console.log("teste adicionado com sucesso")
        },
        error:function(error){
            console.log("falha ao salvar teste")
        }
    });
}
function getAutomationTests(elementName,elementType){
    $.ajax({
        url:`/getAutomatedTests?elementName=${elementName}&elementType=${elementType}`,
        type:'GET',
        contentType:'application/json',
        success: function(response){
            console.log("aqui estao os testes do elemento", response)
        },
        error:function(error){
            console.log("erro ao buscar testes do elemento")
        }
    });
}