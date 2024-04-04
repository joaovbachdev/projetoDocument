const response = http.post('http://127.0.0.1:5000/tratamentoErrosMobile', {
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(
        {
            retorno: myParameter
        }
    )
})