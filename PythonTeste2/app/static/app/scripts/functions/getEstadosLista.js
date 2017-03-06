function getEstadosLista(estadosList){  // INPUT DOS ESTADOS COMO PARAMETRO
      
        $.ajax({
            url: "/clientes/get_estados_json/",
            dataType: 'json',
            beforeSend: function () {

                $(estadosList).prop('disabled', true);
                $(estadosList).empty();
                $(estadosList).append('<option value="" disabled selected hidden>Carregando...</option>');

            },
            success: function (data) {
                $(estadosList).prop('disabled', false);

                for (i = 0; i < data.length; i++) {
                    $(estadosList).append('<option value="' + data[i].pk + '">' + data[i].fields.nome + '</option>');
                }  // .FIELDS É O LUGAR ONDE FICA OS CAMPOS DO DATABASE                 
                $(estadosList).append('<option value="" disabled selected hidden>Escolha um estado...</option>');
            }
        });
}