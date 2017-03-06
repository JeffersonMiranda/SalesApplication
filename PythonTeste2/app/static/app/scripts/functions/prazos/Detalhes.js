$(document).ready(function () {

    $("#inserirPrazoForm").submit(function (e) {

        var novoPrazo = $("#novoPrazo").val();
  
            e.preventDefault();
            var csrftoken = getCookie('csrftoken');


            $.ajax({
                url: "/prazos/inserir_prazo/",
                dataType: 'json',
                type: "POST",
                data: { "prazo": novoPrazo },
                success: function (data) {

                    $("#prazoListaSelect").empty();
                    for (c = 0; c < data.length ; c++) {
                        $("#prazoListaSelect").append('<option value="' + data[c].pk + '">' + data[c].fields.descricao + '</option>');
                    }  // .FIELDS É O LUGAR ONDE FICA OS CAMPOS DO DATABASE                           
                    $("#prazoListaSelect").append('<option value="" disabled selected hidden>Escolha um prazo...</option>');

                    $("#novoPrazo").val("")
                    $("#novoPrazo").focus()

                },
                error: function (e) {
                    console.log(e)
                }
            });


    });



    // CSRF code
    function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });



    $("#prazoListaSelect").change(function () {
        
        $("#prazoDetalhes").css("display","block")

        $("#prazoDetalhes #descricaoPrazoCampo").prop('disabled', true);

        var prazo_id = $(this).val();


        $.ajax({
            url: '/prazos/get_prazo_by_id/',
            data: {'idPrazo':prazo_id},
            dataType: 'json',
            type: "GET",
            success: function (data) {

                $("#prazoIdCampo").val(data[0].pk);
                $("#descricaoPrazoCampo").val(data[0].fields.descricao);

            },
            error: function (e) {
                console.log(e)
            }
        });


    });


    $("#btnEditarPrazo").click(function () {

        $("#prazoDetalhes #descricaoPrazoCampo").prop('disabled', false);
        
    });



    $("#btnExcluirPrazo").click(function () {

        var prazo_id = $("#prazoIdCampo").val();

        $.ajax({
            url: '/prazos/deletar_prazo/',
            data: { 'prazoIdCampo': prazo_id },
            dataType: 'json',
            async:false,
            type: "GET",
            success: function (data) {

                    alert("Prazo excluido com sucesso");
                    location.reload(true);
           
               
            },
            error: function (e) {
                console.log(e)
            }
        });

    });
    

    $("#btnSalvarPrazo").click(function () {

        var id = $("#prazoIdCampo").val();
        var descricao = $("#descricaoPrazoCampo").val();


        $.ajax({
            url: "/prazos/manutencao_editar/",
            dataType: 'json',
            type: "POST",
            data: { "id": id, "descricao": descricao },
            success: function (data) {
                
                alert("Editado com sucesso");
                location.reload(true);
            },
            error: function (e) {
                console.log(e)
            }
        });


    });


});