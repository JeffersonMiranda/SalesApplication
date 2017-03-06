function getRepresentacoes(represList) {

    $.ajax({
        url: "/produtos/get_representacoes_json/",
        dataType: 'json',
        beforeSend: function () {
             
            $(represList).prop('disabled', true);
            $(represList).empty();
            $(represList).append('<option value="" disabled selected hidden>Carregando...</option>');

        },
        success: function (data) {
            $(represList).prop('disabled', false);

            for (i = 0; i < data.length; i++) {
                $(represList).append('<option value="' + data[i].pk + '">' + data[i].fields.nome_fantasia + '</option>');
            }  // .FIELDS É O LUGAR ONDE FICA OS CAMPOS DO DATABASE                 
            $(represList).append('<option value="" disabled selected hidden>Escolha uma representação...</option>');
        }
    });

}