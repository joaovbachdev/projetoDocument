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