$(document).ready(function () {


    $("#form_consultar_cliente :input").prop('disabled', true);
    $("#form_consultar_cliente button").prop('disabled', false);

    $("#estadosList").click(function () {
        $("#estadosList").unbind('click');  // DESATIVANDO O EVENTO CLICK PARA NÃO CARREGAR A LISTA DE NOVO
        
            getEstadosLista('#estadosList');
    
    });

    $("#estadosList").change(function () {   // SELECIONAR CIDADE AO MUDAR O ESTADO
        getCidadesLista('#estadosList', '#cidadesList');
     
    });

    $("#cidadesList").click(function () {  // SELECIONAR CIDADE AO MUDAR O ESTADO
        $("#cidadesList").unbind('click');    // DESATIVANDO O EVENTO CLICK PARA NÃO CARREGAR A LISTA DE NOVO
 
            getCidadesLista('#estadosList', '#cidadesList');

    });

    $("#btnDetalhesClienteEditar").click(function () {

        $("#form_consultar_cliente :input").prop('disabled', false);

    });

});
       