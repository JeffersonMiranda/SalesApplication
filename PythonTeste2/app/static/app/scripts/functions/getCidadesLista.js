function getCidadesLista(estadoLista,cidadeLista) {
    idEstado = $(estadoLista).val();

    $.ajax({
        url: "/clientes/get_cidades_json/",
        data: { 'id_estado': idEstado },
        dataType: 'json',
        beforeSend: function(){
            $(cidadeLista).prop('disabled', true);
            $(cidadeLista).empty();
            $(cidadeLista).append('<option value="" disabled selected hidden>Carregando...</option>');
        },
        success: function (data) {
            $(cidadeLista).prop('disabled', false);

            for (i = 0; i < data.length; i++) {
                $(cidadeLista).append('<option value="' + data[i].pk + '">' + data[i].fields.nome + '</option>');
            }  // .FIELDS É O LUGAR ONDE FICA OS CAMPOS DO DATABASE                 
            $(cidadeLista).append('<option value="" disabled selected hidden>Escolha uma cidade...</option>');
        }
    });
}
