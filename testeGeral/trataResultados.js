//input_cpf    variavel que diz que o input de cpf existe -> bool    NAO PRECISA DE TRATATIVA
//input_senha    variavel que diz se o input se senha existe -> bool   NAO PRECISA DE TRATATIVA
//botao_entrar   variavel que diz se o botao entrar existe -> bool    NAO PRECISA DE TRATATIVA
//botao_recuperar_senha  variavel que diz se o botao de recuperar senha existe -> bool   NAO PRECISA DE TRATATIVA
//limite_cpf  variavel que valida se o cpf tem mais de 11 caracteres -> string   VALIDAR O TAMANHO DA STRING
//cpf_only_numbers  variavel que valida se o cpf tem caracteres diferentes de numeros -> string   VALIDAR A STRING
//login_sucess  variavel que diz se o login foi realizado com sucesso -> bool   NAO PRECISA DE TRATATIVA


//VALIDACAO DO TAMANHO DO CPF
if(limite_cpf.length > 11){
    console.log("cpf maior que 11 caracteres")
}else{
    console.log("cpf respeitando o limite")
}


//VALIDACAO DOS CARACTERES DA STRING
if(/^\d+$/.test(cpf_only_numbers) == false){
    console.log("cpf aceitando caracteres diferente de numeros")
}else{
    console.log("cpf aceitando apenas numeros")
}
