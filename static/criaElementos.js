

function createLine(items){
    svgEle = document.getElementById("campo")
    

    for(let i=0;i<items['positions'].length;i++){
        var linha = document.createElementNS("http://www.w3.org/2000/svg", 'line');
        linha.setAttribute('x1', items['positions'][i][0]);
        linha.setAttribute('y1', items['positions'][i][1]);
        linha.setAttribute('x2', items['positions'][i][2]);
        linha.setAttribute('y2', items['positions'][i][3]);
        linha.setAttribute('stroke', '#3498db');
        linha.setAttribute('stroke-width', '10');
        linha.setAttribute('lineName',items['names'][i])
        linha.setAttribute('onclick',`clickLine("${items['names'][i]}")`)
        linha.setAttribute('filter', 'url(#shadow)');
        //linha.setAttribute('onclick','cliquei("linha1")')
        svgEle.appendChild(linha)
    }
    
}
function createElement(items){ //itens recebo um array de arrays, o primeiro é um array das posicoes e o segundo dos nomes
    console.log(items)
    svgEle = document.getElementById("campo")
    for(let i=0;i<items['positions'].length;i++){
            var ele = document.createElementNS("http://www.w3.org/2000/svg", 'circle');
            ele.setAttribute('cx',items['positions'][i][0])
            ele.setAttribute('cy',items['positions'][i][1])
            ele.setAttribute('r','25')
            ele.setAttribute('fill','#0bfc03')
            ele.setAttribute('onclick',`clickElement("${items['names'][i]}")`)
            ele.setAttribute('elementName',items['names'][i])
            ele.setAttribute('class','elemento')



            svgEle.appendChild(ele)
    
        }
    }

