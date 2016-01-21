$(document).ready(function() {

	//$("#contenido").css("margin","5%")

	//$.cookie('query', '1');


	//if($.cookie('tam_letra')) { 

		//$("body").css("font-size",$.cookie('tam_letra'))

	//}


$(".Megusta").click(function(){
	identificado = $(this).attr("id")
	value=$(this).attr("value")


	$.get("/rango/probando_ajax", {"id":$(this).attr("value"),"prueba":"Esto es un texto de prueba"}, function(votos) {
		$("span[id="+identificado+"]").html(votos)
		$("button[id="+identificado+"]").remove()
	});
	
});	

$("#letra_normal").click(function(){
	$("body").css("font-size","14px")
	//$.cookie("tam_letra", "14px");

	
});

$("#letra_grande").click(function(){
	$("body").css("font-size","20px")
	//$.cookie("tam_letra", "20px");
});


$("#letra_enorme").click(function(){
	$("body").css("font-size","30px")
	//$.cookie("tam_letra", "30px");
});



	if ( $("#container").length > 0 ) {
		//alert("grafica")
		$.ajax({
			url: "/rango/reclama_datos",
			type: 'get',                        
			success: function(datos) {
				Visualiza_datos(datos);  
			},
			failure: function(datos) { 
				alert('esto no vá');
			}
		});

		function Visualiza_datos (datos) {

			var bares = []
			var visitas = []
			for (i = 0; i < datos["length"]; i++) {
    			bares.push(datos[i])
    			visitas.push(datos[datos[i]])




			}



    $('#container').highcharts({
    	



	



        chart: {
            type: 'bar'
        },
        title: {
            text: 'Diagrama visita bares'
        },
        xAxis: {
            categories: bares
        },
        yAxis: {
            title: {
                text: 'Visitas'
            }
        },
        series: [{
            name: 'Visitas',
            data: visitas
        }],
    });




		};
	}	


});


