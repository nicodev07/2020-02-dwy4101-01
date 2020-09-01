var nombre_variable = 'Soy una variable!';
let nombre_del_let = 'Soy un let!';
/*
NO PODEMOS modificar su valor.
*/
const NOMBRE_CONSTANTE = 'Soy una constante!';
let a = 'Hola mundo 2!';
//let a = 'Hola mundo 2!';

let nombreVariable = 'Valor de la variable';

if(true){
    let a ='Hola mundo!';
    console.log(a);
}

if(true){
let a = 'Hola mundo 3!';
console.log(a);
}
console.log(a);


function suma(numero_1, numero_2){
    return numero_1 + numero_2;
}

function resta(numero_1, numero_2){
    return numero_1 - numero_2;
}

function multiplicar(numero_1, numero_2){
    return numero_1 * numero_2;
}
const SUMA = 'suma';
const RESTA = 'resta';
const MULTIPLICAR = 'multiplicar';


function calculadora(numero_1,numero_2,operador){
    if(operador === SUMA)
    return suma(numero_1,numero_2);

    if(operador === RESTA)
    return resta(numero_1,numero_2);
    
    if(operador === MULTIPLICAR)
    return multiplicar(numero_1,numero_2);
}

let valorSuma = calculadora(1,1,SUMA);
console.log(valorSuma);