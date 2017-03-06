function getProducts(idRepres) {     //GET PRODUCTS BY REPRESENTACAO
      
        $.ajax({
        async:false,
        url: "/pedidos/get_produtos_by_repres_json/",
        data: { 'idRepres': idRepres },
        dataType: 'json',
        success: function (data) {

  
            obj = data;
         
        }
     });
    

    return obj;

}