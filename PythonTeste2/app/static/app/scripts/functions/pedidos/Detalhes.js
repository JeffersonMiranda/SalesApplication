$(document).ready(function () {

    var products = {};
    var productRow = {};


    $("#represLista").change(function () { // TRAZER PRODUTOS DE ACORDO COM A REPRESENTAÇÃO       

        var idRepres = $("#represLista").val();

        products = getProducts(idRepres); // PRODUTOS EM JSON    
        products2 = JSON.parse(JSON.stringify(products));

        $("#tablePedido").empty();

        var arraySize = products.length;

        addHeaderTable();  // ADICIONAR O HEADER ANTES DAS LINHAS
        $("#tablePedido").append('<tbody>');  
        for (c = 0; c < arraySize; c++) {

            var novaRow = '<tr> ' +
                    '<td><span class="idProduto">'  + products[c].pk + '</spans></td>'+
                    '<td>' + products[c].fields.nome + '</td> ' +
                    '<td> <input class="form-control quantidade" type="text" name="quantidade" value="" /> </td>  <!-- QUANTIDADE --> ' +
                   '<td> <input class="form-control precoPadrao" type="text" name="precoPadrao" value="' + products[c].fields.preco1 + '"/> </td>  <!-- PREÇO PADRÃO --> ' +
                  '<td> <input class="form-control precoDesconto" type="text" name="precoDesconto" value="" /> </td>  <!-- PREÇO COM DESCONTO --> ' +
                  '<td> <span class="total"></span> </td>  ' +
               '</tr>';

            $("#tablePedido").append(novaRow);
        }

        $("#tablePedido").append('</tbody>');
    
    });


    function addHeaderTable() { // FUNÇÃO ADICIONAR HEADER

        var header = '<thead>'+
            '<tr>' +
           '<th>Código</th> ' +
           '<th>Produto</th> ' +
           '<th>Quantidade</th>' +
           '<th>Preço padrão</th>' +
           '<th>Preço com desconto</th>' +
          '<th>Total</th>' +
          '</tr>'+
        '</thead>';

        $("#tablePedido").append(header);
        
    } 


    $('body').on('change', '.quantidade , .precoPadrao', function () { // CALCULAR VALOR TOTAL QUANDO ALTERAR QUANTIDADE OU PRECO

        var quant = $(this).closest("tr").find(".quantidade").val();
        var preco = $(this).closest("tr").find(".precoPadrao").val();

        var total = parseFloat(quant * preco).toFixed(2);

        $(this).closest("tr").find(".total").html(total);


    }); // FIM DA FUNÇÃO


    $('body').on('change', '.quantidade , .precoPadrao, .precoDesconto', function () { // CALCULAR VALOR TOTAL QUANDO ALTERAR QUANTIDADE OU PRECO


        var campo = $(this).closest("tr").find(".precoDesconto"); // CALCULAR VALOR TO DESCONTO E ANULAR PREÇO PADRÃO

        if (!campo.val()) {
            var idPro = $(this).closest("tr").find(".idProduto").html();
            var p = getProductById(idPro); // RECEBE PREÇO DO PRODUTO
            $(this).closest("tr").find(".precoPadrao").val(p.fields.preco1);
        }
        else {
            $(this).closest("tr").find(".precoPadrao").val(""); // ESVAZIAR CAMPO PREÇO PADRÃO SE DESCONTO ESTIVER PREENCHIDO
        
        }


        console.log("entrou no evento");
        var quant = $(this).closest("tr").find(".quantidade").val();
        var preco = $(this).closest("tr").find(".precoPadrao").val();
        var precoDesconto = $(this).closest("tr").find(".precoDesconto").val();
        var p;

        if (preco) {  // VERIFICANDO SE PRECO PADRÃO OU PRECO DESCONTO TEM MUDANÇAS
            p = preco;
        }
        else {
            p = precoDesconto;
             }


        var total = parseFloat(quant * p).toFixed(2);

        $(this).closest("tr").find(".total").html(total);


        calcularValorPedido(); //CALCULANDO VALOR FINAL DO PEDIDO


    }); // FIM DA FUNÇÃO

    $('body').on('change', '.precoDesconto', function () { 
        
      

    }); // FIM DA FUNÇÃO

    function getProductById(idPro){ // RETORNAR OBJETO POR ID
    
        var arraySize = products.length;
         
        for(c = 0; c < arraySize; c++){
        
            if (products[c].pk == idPro) {
                return products[c];

            }
        
        }
        return -1; // RETORN -1 SE NÃO ENCONTRAR O ID 
    
    }

    function calcularValorPedido() {  // CALCULAR O VALOR FINAL DO PEDIDO

        var valorFinal = 0;

        $("#tablePedido .total").each(function () {  // PERCORRENDO TODAS AS LINHAS E COLETANDO O VALOR DE CADA PRODUTO
            valorFinal += Number($(this).html());

        });

        $("#valorTotalPedido span").empty();
        $("#valorTotalPedido span").html("R$ " + valorFinal);
    }

    //LANÇAR PEDIDO

    $("#lancarPedido").click(function () {

        var itemsPedido = [];
        var c = 0; //CONTADOR DO LAÇO

      //  itemsPedido.prazo

        $("#tablePedido tbody tr").each(function () {

            if ($(this).find(".quantidade").val() > 0) {   // SÓ REGISTRA NO BANCO SE TIVER QUANTIDADE > 0, OU SEJA, SE O PRODUTO ESTIVER NO PEDIDO

            item = {};
            item.quantidade = $(this).find(".quantidade").val();

            if ($(this).find(".precoPadrao").val()){
                item.preco = ($(this).find(".precoPadrao").val())
            }
            else if ($(this).find(".precoDesconto").val()) {
                item.preco = $(this).find(".precoDesconto").val();
            }       

            itemsPedido.push(item);

            }
        });


    });


});