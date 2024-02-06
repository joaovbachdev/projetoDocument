const canvas = document.getElementById('campo');
const canvasContainer = document.getElementById('canvas-container');


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

  canvas.appendChild(newElement);
}



addNewImage(-330,120,1300,1300,'static/telaLogin.jpeg')
addNewImage(1000,120,1300,1300,'static/modalTopDrivers.jpeg')
addNewImage(2300,120,1300,1300,'static/telaInicial.jpeg')

addNewImage(3000,1800,1300,1300,'static/telaMenu.jpeg')
addNewImage(3700,1800,1300,1300,'static/telaMenu2.jpeg')
addNewImage(1300,1800,1300,1300,'static/telaAgenda.jpeg')
addNewImage(4500,120,1300,1300,'static/telaViagens.jpeg')
