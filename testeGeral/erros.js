console.log(inp_cpf)
console.log(inp_senha)
console.log(bt_entrar)

if(cpf_limit.lenght > 11){
    console.log("limite maior que 11")
}else{
    console.log("limite menor que 11")
}

console.log("contem apenas numeros: " + /^\d+$/.test(cpf_caracteres))