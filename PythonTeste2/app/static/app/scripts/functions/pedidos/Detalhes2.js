$(document).ready(function () {

    var products = {};   
    var products2 = {}; // COPIA DOS PRODUTOS, SÓ PODE SER ALTERADA SE MUDAR REPRESENTAÇÃO
    var productRow = {};

    function setProductsLista(lista) {  // FUNÇÃO PARA SETAR A LISTA DE PRODUTOS
        $(lista).empty();
        
        var arraySize = products.length;

        for (c = 0; c < arraySize; c++) {
            $(lista).append("<option value=" + products[c].pk + ">" + products[c].fields.nome + "</option>");
        
        }

         $(lista).append('<option value="" disabled selected hidden>Escolha um produto...</option>');
    }

    function addHeaderTable() { // FUNÇÃO ADICIONAR HEADER

        var header = '<tr>' +
           ' <th> </th> ' + // COLUNA PARA O BOTÃO DELETAR
           ' <th>Produto</th> '+
           '<th>Quantidade</th>'+
           '<th>Preço padrão</th>'+
           '<th>Preço com desconto</th>'+
          '<th>Total</th>' +
          '</tr>';

        $("#tablePedido").append(header);


    } // 

    function addNovaLinha() {

        var novaRow = '<tr> ' +
           '<td>'+ 
           ' <button type="button" class="btn btn-default btnDeletarProduto" aria-label="Left Align">'+
            ' <span class="glyphicon glyphicon-trash" aria-hidden="true"></span>'+
            '</button> </td>' +
                '<td> ' +
                 '<select class="form-control productsLista">  ' +                 
                 '</select>' +
                 '</td> ' +
                '<td> <input class="form-control quantidade" type="text" name="quantidade" value="" /> </td>  <!-- QUANTIDADE --> ' +
               '<td> <input class="form-control precoPadrao" type="text" name="precoPadrao" value="" /> </td>  <!-- PREÇO PADRÃO --> ' +
              '<td> <input class="form-control precoDesconto" type="text" name="precoDesconto" value="" /> </td>  <!-- PREÇO COM DESCONTO --> ' +
              '<td> <p class="total lead">  </p>  </td>  ' +
           '</tr>';

        $("#tablePedido").append(novaRow);


    }
    
    function limparLista(produtoId) { // RETIRAR PRODUTOS DAs LISTAs QUE JÁ ESTÃO SELECIONADOS

        var firstRow = $("#tablePedido").find(".productsLista");

        $(".productsLista option[value='"+ produtoId +"']").each(function () {

            if (!$(this).is(':selected')) {  //SE NÃO ESTIVER SELECTED, ENTÃO DELETA,APENAS UM PODE ESTAR SELECIONADO NAS LISTAS
                $(this).remove();
            }

        });

    } 

    $("#represLista").change(function () { // TRAZER PRODUTOS DE ACORDO COM A REPRESENTAÇÃO       

    var idRepres = $("#represLista").val();

    products =  getProducts(idRepres); // PRODUTOS EM JSON    
    products2 = JSON.parse(JSON.stringify(products));

    $("#tablePedido").empty();
    
    addHeaderTable();// ADICIONAR HEADER

    addNovaLinha(); // ADICIONAR PRIMEIRA LINHA

    setProductsLista(".productsLista");

    }); // FIM DA FUNÇÃO 



    $('body').on('change','.productsLista', function () {  // LEVAR DADOS PARA A TABLE ROW DE ACORDO COM O PRODUTO SELECIONADO
        
        idPro = $(this).val(); 
        
        productRow = $.grep(products, function (e) { return e.pk == idPro });
               
        $(this).closest("tr").find("input[name='precoPadrao']").val(productRow[0].fields.preco1);
      
     
   
    });  // FIM DA FUNÇÃO 
  

    $('body').on('change','.quantidade , .precoPadrao', function () { // CALCULAR VALOR TOTAL QUANDO ALTERAR QUANTIDADE OU PRECO
        
        var quant = $(this).closest("tr").find(".quantidade").val();
        var preco = $(this).closest("tr").find(".precoPadrao").val();

        var total = parseFloat(quant * preco).toFixed(2);

        $(this).closest("tr").find(".total").html(total);
        

    }); // FIM DA FUNÇÃO


    $('body').on('keyup','.precoDesconto', function (e) {  // ADICIONAR NOVA LINHA NA TABLE QUANDO PRESSIONAR TAB KEY

        if (products.length >= 1 ) {
            rowId = $(this).closest("tr").find(".productsLista").val();
         

            var index = products.map(function (d) { return d['pk']; }).indexOf(parseInt(rowId));  // RECUPERANDO A POSIÇÃO DO PRODUTO NO ARRAY
          
            if(index >= 0){  // SE PRODUDO É DIFERENTE DE -1, OU SEJA, SE AINDA NÃO FOI TIRADO DA LISTA
                products.splice(index, 1); // DELETANDO O PRODUTO DO ARRAY DE PRODUTOS    
              
            }
           
        }
            
        limparLista(idPro); // TIRANDO DAS LISTAS OS PRODUTOS JÁ SELECIONADOS      

        
      if (e.which == 9 && $(this).closest("tr").next("tr")[0] == null && products.length > 0  && $.isNumeric($(this).closest("tr").find(".productsLista :selected").val())) {  // CHECANDO SE A TAG "TR" É A ULTIMA DA TABLE, SE FOR, ADD OUTRA ROW
    
            addNovaLinha(); // FUNÇÃO PARA ADD A NOVO LINHA
          
            var novosProdutos = $(this).closest("tr").next("tr").find(".productsLista");

            if (novosProdutos.empty()) {

                setProductsLista(novosProdutos); // SETANDO NOVO SELECT DE PRODUTOS 

            }   

         }// FIM DO IF
        
    });  // FIM DE FUNÇÃO


    $('body').on('click','.btnDeletarProduto', function () {  // FUNÇÃO PARA EXCLUIR LINHA         
        
        var id = $(this).closest("tr").find(".productsLista :selected").val();
      
        if ($.isNumeric(id)){ // SE VALUE É UM NÚMERO, OU SEJA, SE ALGUM PRODUTO ESTIVER SELECIONADO

        var index = products2.map(function (d) { return d['pk']; }).indexOf(parseInt(id));  

        var product =  $.grep(products2, function (e) { return e.pk == id });  // RECUPERAR PRODUTO DE ACORDO COM O ID PARA INSERIR NA LISTA NOVAMENTE   

        products.splice(index, 0, product[0]); // INSERINDO O PRODUTO NA LISTA DE VOLTA (POSIÇÃO 0 DO ARRAY)
          
     
        } // FIM IF

        $(this).closest("tr").remove();

        console.log(JSON.stringify(products));
        
    });

});