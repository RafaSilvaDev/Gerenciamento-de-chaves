var stateA=1;
function btnAvaiable(clickedElement){
  if (stateA == 1){
    document.getElementById(clickedElement.id).innerHTML = "Fechar";
    console.log(clickedElement)
    console.log(stateA)
    stateA = 0
  }else{
    document.getElementById(clickedElement.id).innerHTML = "Reservar";
    stateA = 1
  }
}


var stateB=1;
function btnUnavaiable(clickedElement){
  if (stateB == 1){
    document.getElementById(clickedElement.id).innerHTML = "Fechar";
    stateB = 0
  }else{
    document.getElementById(clickedElement.id).innerHTML = "Devolver";
    stateB = 1
  }
}