function atualizaGrafico(opcao){
    console.log(opcao)
    $.ajax({
        url:`/atualizaGrafico`,
        type:'POST',
        data:JSON.stringify({"opcao":opcao}),
        contentType:'application/json',
        success: function(response){
            document.getElementById('imagem').setAttribute('src',`/static/${response}`)
            
        },
        error:function(error){
            console.log(error, "deu ruim")
        }
    })  
}