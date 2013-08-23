
$(document).on('ready', function() {
	$('#id_especialidad').on('change', function() { 
		var val = $('#id_especialidad option:selected').html();

		$.ajax({
			async:true,
			url:'ajaxespecialidad',
			data:'a='+val+'&valor&csrfmiddlewaretoken=' + getCookie('csrftoken'),
			type:'post',
			dataType: 'html',
			beforeSend: function () {
				$('#id_dentista').empty()
				
			},
			success: function(respuesta) {
				hora(respuesta);
			},
			timeout: 8000,
			error: function () {
				alert('Ha ocurrido un error, por favor inténtelo nuevamente.');
			}
		})
	});
});

function hora(jdata){
	$('#id_dentista').append('<option value ="0">elija...</option>');
	var coso = JSON.parse( jdata );
    for (var i = 0; i < coso.length; i++){
		$('#id_dentista').append('<option value ="'+i+'">'+coso[i]+'</option>');
	};
}

///**********************************************

