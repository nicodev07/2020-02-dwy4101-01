function suma(numero_1,numero_2){
    return numero_1+numero_2; 
}
function resta(numero_1,numero_2){
    return numero_1-numero_2;    
}
function multiplicar(numero_1,numero_2){
    return numero_1*numero_2; 
}

const SUMA = 'suma';
const RESTA = 'resta';
const MULTIPLICAR = 'multiplicar';
function calculadora(numero_1,numero_2,operador){

    if(operador === SUMA)
    return suma(numero_1+numero_2);

    if(operador === RESTA)
    return resta(numero_1-numero_2);

    if(operador === MULTIPLICAR)
    return multiplicar(numero_1*numero_2);
}

let valorResultado= calculadora(1,1,SUMA);
console.log(valorResultado);