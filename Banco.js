//Observações:

//- buscar saldo deve retornar o valor atual do saldo;

//- para o depósito, você deverá passar um valor como parâmetro e adicioná-lo no saldo final do objeto;

//- para o saque, você deverá passar um valor como parâmetro e subtraí-lo no saldo final do objeto;

//- o número da conta deve retornar o número da conta.

var banco = {
    conta: 1050,
    saldo: 100,
    tipo: "Conta-corrente",
    agencia: 283,
    buscarsaldo: function() {
        console.log('Seu saldo é de:', banco.saldo, "reais.")
    },
    deposito: function(valor) {
        banco.saldo = banco.saldo + valor
    },
    saque: function(valor) {
        banco.saldo = banco.saldo - valor
    }, 
    numconta: function() {
        console.log('O número da sua conta é:', banco.conta, ".")
    },
 };
