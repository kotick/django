
$(document).on('ready', function() {
	$('#olitest').on('change', function() { 

		$.ajax({

			//var coso = $("#olitest:selected").text();
			//var valor= $("#olitest").val();
			async:true,
			url:'ajax/test',
			data:'a=1&b=2&valor&csrfmiddlewaretoken=' + getCookie('csrftoken'),
			type:'post',
			dataType: 'html',
			beforeSend: function () {
				//alert('enviando peticion ajax...');
			},
			success: function(respuesta) {
			
				//Lafuncion(respuesta);
				$('#respuesta').html(respuesta)


				
			},
			timeout: 8000,
			error: function () {
				alert('Ha ocurrido un error, por favor inténtelo nuevamente.');
			}
		})
	});
});


function Lafuncion(jdata)
{

//	$('#respuesta').append('<h2> me lleva el chanfe!</h2>');

		$('#combo2').append('<option value ="0">Select...</option>');
	    for (var i = 0; i < jdata.length; i++)
    {
    	$('#combo2').append('<option value ="'+i+'">'+jdata[i]+'</option>');

        //options += '<option value="' + jdata[i].Description + '">' + jdata[i].Description + ' (' + jdata[i].ProcedureCode + ')' + '</option>';
    
    };

    
}