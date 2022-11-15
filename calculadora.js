var primeirovalor = parseInt(prompt("digite o primeiro valor:"))
var segundovalor = parseInt(prompt("digite o segundo valor:"))


var operação = prompt("digite 1 para divisão, 2 para multiplicação, 3 para soma e 4 para subtração")

if (operação == 1) {
 var resultado = primeirovalor / segundovalor
 print( primeirovalor + " / " + segundovalor + " = " + resultado ) 
} else if (operação == 2) {
 var resultado = primeirovalor * segundovalor
 print(primeirovalor + " x " + segundovalor + " = " + resultado) 
} else if (operação == 3) {
  var resultado = primeirovalor + segundovalor
 print(primeirovalor + " + " + segundovalor + " = " + resultado)
} else if (operação == 4) {
   var resultado = primeirovalor - segundovalor
 print(primeirovalor + " - " + segundovalor + " = " + resultado)
} else {
  print("Opçaõ invalida" )
}
