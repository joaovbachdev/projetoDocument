const canvas = document.getElementById('campo');
const canvasContainer = document.getElementById('canvas-container');
const grupoImagem = document.getElementById('grupo-img');


let isDragging = false;
let dragStart = { x: 0, y: 0 };
let viewBox = { x: 0, y: 0, width: 800, height: 600 };
let scale = 1;

function updateViewBox() {
  canvas.setAttribute('viewBox', `${viewBox.x} ${viewBox.y} ${viewBox.width} ${viewBox.height}`);
}

function handleMouseDown(event) {
  isDragging = true;
  dragStart = { x: event.clientX, y: event.clientY };
  canvas.style.cursor = 'grabbing';
}

function handleMouseMove(event) {
  if (!isDragging) return;

  const deltaX = (event.clientX - dragStart.x) / scale;
  const deltaY = (event.clientY - dragStart.y) / scale;

  viewBox.x -= deltaX;
  viewBox.y -= deltaY;

  updateViewBox();

  dragStart = { x: event.clientX, y: event.clientY };
}

function handleMouseUp() {
  isDragging = false;
  canvas.style.cursor = 'grab';
}

function handleWheel(event) {
  const scaleFactor = event.deltaY > 0 ? 0.9 : 1.1;
  scale *= scaleFactor;

  viewBox.width = canvasContainer.clientWidth / scale;
  viewBox.height = canvasContainer.clientHeight / scale;

  updateViewBox();
}

canvas.addEventListener('mousedown', handleMouseDown);
canvas.addEventListener('mousemove', handleMouseMove);
canvas.addEventListener('mouseup', handleMouseUp);
canvas.addEventListener('wheel', handleWheel);


function addNewElement(x, y, width, height, fill) {
  const newElement = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
  newElement.setAttribute('x', x);
  newElement.setAttribute('y', y);
  newElement.setAttribute('width', width);
  newElement.setAttribute('height', height);
  newElement.setAttribute('fill', fill);
  canvas.appendChild(newElement);
}
function addNewImage(x,y,width,height,img){
  const newElement = document.createElementNS('http://www.w3.org/2000/svg', 'image');
  newElement.setAttribute('x', x);
  newElement.setAttribute('y', y);
  newElement.setAttribute('width', width);
  newElement.setAttribute('height', height);
  newElement.setAttributeNS('http://www.w3.org/1999/xlink', 'href', img);

  grupoImagem.appendChild(newElement);
}



addNewImage(150,120,1300,1300,'static/telaLogin.jpeg')
addNewImage(150,1800,1300,1300,'static/modalTopDrivers.jpeg')
addNewImage(-500,3400,1300,1300,'static/telaInicial.jpeg')

addNewImage(800,3400,1300,1300,'static/telaMenu.jpeg')
addNewImage(1500,3400,1300,1300,'static/telaMenu2.jpeg')

addNewImage(150,5200,1300,1300,'static/telaAgenda.jpeg')
addNewImage(-800,5200,1300,1300,'static/telaAdicionarCompromisso.jpeg')
addNewImage(-1850,5200,1300,1300,'static/telaSelecionarEnderecoMapa.jpeg')

addNewImage(-2000,1200,1300,1300,'static/telaViagens.jpeg')

addNewImage(-4000,2000,1300,1300,'static/modalRanking.png')

addNewImage(-4000,4000,1300,1300,'static/telaCentralNotificacoes.png')

addNewImage(-6000,2000,1300,1300,'static/top5Ranking.png')

addNewImage(-6000,0,1300,1300,'static/modalHistoricoPontuacao.jpg')

addNewImage(3000,0,1300,1300,'static/telaControleDoSono.jpg')

addNewImage(3800,0,1300,1300,'static/telaViageComSeguranca.jpg')

addNewImage(5000,1500,1300,1300,'static/telaConversasAtivas.jpg')
addNewImage(5800,1500,1300,1300,'static/listaConversasAtivas.jpg')
addNewImage(6600,1500,1300,1300,'static/listaAssuntosPrincipais.jpg')
addNewImage(7400,1500,1300,1300,'static/listaSubAssuntos.jpg')
addNewImage(8200,1500,1300,1300,'static/assuntoSubAssuntoSelecionados.jpg')
addNewImage(9000,1500,1300,1300,'static/telaConversasFinalizadas.jpg')

addNewImage(6000,5500,1300,1300,'static/telaMeusVeiculos.jpeg')

addNewImage(6000,3500,1300,1300,'static/telaComissoes.jpeg')

addNewImage(5000,7000,1300,1300,'static/telaMeusComprovantes.jpeg')

addNewImage(4000,9000,1300,1300,'static/telaChecklist.jpeg')
addNewImage(4800,9000,1300,1300,'static/TelaCheklistEngateDesengate.jpg')
addNewImage(5600,9000,1300,1300,'static/checkListBotaoAvancarDesativado.jpg')
addNewImage(6400,9000,1300,1300,'static/conteudoItemChecklistVazio.jpg')
addNewImage(7200,9000,1300,1300,'static/conteudoItemChecklistPreenchido.jpg')
addNewImage(8000,9000,1300,1300,'static/itensChecklistFinalizados.jpg')
addNewImage(8800,9000,1300,1300,'static/listItensChecklistFinalizados.jpg')



addNewImage(-4000,-2800,1300,1300,'static/imgProcessoViagem/iniciarViagem.png')
addNewImage(-4800,-2800,1300,1300,'static/imgProcessoViagem/telaColetaInicio.png')
addNewImage(-4800,-4300,1300,1300,'static/imgProcessoViagem/3pontinhosColeta.png')
addNewImage(-5600,-4300,1300,1300,'static/imgProcessoViagem/modalColetaNaoRealizada.png')
addNewImage(-5600,-2800,1300,1300,'static/imgProcessoViagem/coletaIniciarCarregamento.jpeg')
addNewImage(-6400,-2800,1300,1300,'static/imgProcessoViagem/modalIniciarCarregamento.jpeg')
addNewImage(-7200,-2800,1300,1300,'static/imgProcessoViagem/etapaFinalizarCarregamento.jpeg')
addNewImage(-8000,-2800,1300,1300,'static/imgProcessoViagem/etapaIniciarLeitura.jpeg')
addNewImage(-8000,-4300,1300,1300,'static/imgProcessoViagem/botaoNaoInformarNf.jpeg')
addNewImage(-8800,-2800,1300,1300,'static/imgProcessoViagem/modalQuantidadeNf.jpeg')
addNewImage(-8000,-5800,1300,1300,'static/imgProcessoViagem/modalNaoInformarNf.jpeg')
addNewImage(-9600,-2800,1300,1300,'static/imgProcessoViagem/telaLeituraDeNf.jpeg')
addNewImage(-9600,-4300,1300,1300,'static/imgProcessoViagem/itemListaDeNfAnexada.jpeg')
addNewImage(-10400,-2800,1300,1300,'static/imgProcessoViagem/telaEscaneioOQRcode.jpeg')
addNewImage(-11200,-2800,1300,1300,'static/imgProcessoViagem/escaneieOQRcodeAvancar.jpeg')
addNewImage(-12000,-2800,1300,1300,'static/imgProcessoViagem/telaFotoDaNf.jpeg')
addNewImage(-12000,-4300,1300,1300,'static/imgProcessoViagem/pontoInterrogacaoCameraNf.jpeg')
addNewImage(-12800,-2800,1300,1300,'static/imgProcessoViagem/telaFotoNfTirada.jpeg')



