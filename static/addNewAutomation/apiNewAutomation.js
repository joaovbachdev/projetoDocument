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