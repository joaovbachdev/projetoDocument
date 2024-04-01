

function createLine(items){
    svgEle = document.getElementById("campo")
    icones = document.getElementById("icones")
    var grupoLinha = document.getElementById('grupo-circulos');
    
    
    for(let i=0;i<Object.keys(items).length;i++){
        var linha = document.createElementNS("http://www.w3.org/2000/svg", 'line');
        linha.setAttribute('x1', items[Object.keys(items)[i]]['positions'][0]);
        linha.setAttribute('y1', items[Object.keys(items)[i]]['positions'][1]);
        linha.setAttribute('x2', items[Object.keys(items)[i]]['positions'][2]);
        linha.setAttribute('y2', items[Object.keys(items)[i]]['positions'][3]);
        linha.setAttribute("elementName",items[Object.keys(items)[i]]['name'])
        linha.setAttribute('stroke', '#99ff33');
        linha.setAttribute('stroke-width', '10');
        linha.setAttribute('lineName',items[Object.keys(items)[i]]['name'])
        linha.setAttribute('onclick',`clickLine("${items[Object.keys(items)[i]]['name']}")`)
        linha.setAttribute('filter', 'url(#shadow)');
    
        grupoLinha.appendChild(linha)
    
    }

    
    
}
function createElement(items){ //itens recebo um array de arrays, o primeiro é um array das posicoes e o segundo dos nomes
    svgEle = document.getElementById("campo")
    var grupoCirculos = document.getElementById('grupo-circulos');
    var DivIcone = document.getElementById("icones")

    


    
    
   
    for(let i=0;i<Object.keys(items).length;i++){
        
        var ele = document.createElementNS("http://www.w3.org/2000/svg", 'circle');
        var icone = document.createElement("i")
        var foreing = document.createElementNS('http://www.w3.org/2000/svg',"foreignObject")
        var divI = document.createElement("div")

        foreing.setAttribute("width","30px")
        foreing.setAttribute("height","30px")
        foreing.setAttribute("x",`${items[Object.keys(items)[i]]['position'][0]}px`)
        foreing.setAttribute("y",`${items[Object.keys(items)[i]]['position'][1]-40}px`)

        divI.setAttribute("xmlns","http://www.w3.org/1999/xhtml")
        divI.setAttribute("id","icones")

        icone.setAttribute("class","fa-solid fa-spinner fa-spin fa-2x spinner")
        icone.setAttribute("elementName",items[Object.keys(items)[i]]['name'])
        icone.style.position = "absolute"
        icone.style.top=`30%`
        icone.style.left = `30%`
        icone.style.transform= 'translate(-60%, -60%)'
        icone.style.animation= "rotate 0.5s linear infinite";
        icone.style.display = 'none'
       
     
        
        divI.appendChild(icone)
        foreing.appendChild(divI)
        svgEle.appendChild(foreing)
        

        ele.setAttribute('cx',items[Object.keys(items)[i]]['position'][0])
        ele.setAttribute('cy',items[Object.keys(items)[i]]['position'][1])
        ele.setAttribute('r','25')


      
        
        if(items[Object.keys(items)[i]]["testes"].length == 0){
            ele.setAttribute('fill','#f5b470')
        }else{
            ele.setAttribute('fill','#0bfc03')
            for(let j=0;j<items[Object.keys(items)[i]]["testes"].length;j++){
                if(items[Object.keys(items)[i]]["testes"][j]["status"] == "naoRealizado"){
                    ele.setAttribute('fill','#e60000')
                    break;
                }
            }
            
        }
        
        ele.setAttribute('onclick',`clickElement("${items[Object.keys(items)[i]]['name']}")`)
        //ele.addEventListener("click",sinal)
        ele.setAttribute('elementName',items[Object.keys(items)[i]]['name'])
        ele.setAttribute('class','elemento')





        //DivIcone.appendChild(icone)
        grupoCirculos.appendChild(ele)
        
        
        
    }

    
    }

function sinal(){
    alert("ola mundo")
}