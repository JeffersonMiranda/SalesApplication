$(document).ready(function () {

    $("#form_consultar_produtos :input").prop('disabled', true);
    $("#form_consultar_produtos button").prop('disabled', false);



    $("#btnDetalhesProdutosEditar").click(function () {
       
        $("#form_consultar_produtos :input").prop('disabled', false);

    });

    $("#represLista").click(function () {
        $("#represLista").unbind('click');
        getRepresentacoes(this);

    });





});