$(document).on("ready", inicio);
function inicio ()
{
	taps();
	cargo_tareas();
	cargo_tareassoli();
	$("#tab2").on("click", tab2);
	$("#tab1").on("click", tab1);
	$("#pag").on("click", cargo_tareasp);	
	
	//$('#preguntas button').on('click', enviar_pregunta);
}



function taps()
{
	$( "#tabs" ).tabs();
}
function tab1(data) 
{
	document.getElementById("TituloTab").innerHTML = "Lista de Tareas Pendientes";
	cargo_tareas();

}
function tab2(data) 
{
	document.getElementById("TituloTab").innerHTML = "Lista de Tareas Solicitadas";
	cargo_tareassoli();
}
function cargo_tareas(datos) 
{
	$('#tabs-1').html('&nbsp;').load('/cargo-mistareas/');
}

function cargo_tareassoli(datos) 
{
	$('#tabs-2').html('&nbsp;').load('/cargo-tareassoli/');
}


function cargo_tareasp(datos) 
{
	console.log(document.getElementById("pag"));
}

//esto es para usar con json
function cargo_tarea()
{
	$('#mis-tareas').empty();
	$.ajax(
	{
		type:"GET",
		contentType:"paplication/json; charset=utf-8",
		dataType:"json",
		url:"/cargo-tareas/",
		success:function(response)
		{
			
			$.each(response, function(i, elemento)
			{
				console.log(elemento);
				var dato = "<td>" + elemento.fecha + "</td>"
				dato += "<td><a href=tarea/" + elemento.slug + ">" + elemento.nombre + "</a></td>"
				dato += "<td>" + elemento.detalle + "</td>"
				dato += "<td>" + elemento.dquien + "</td>"
				$('#mis-tareas').append("<tr>" + dato + "</tr>");
				console.log(elemento.dquien);				
			});
		}
	});	
}


function buscarArticulos (datos) 
{

	var col = $('#text-art').val();
	col = col.replace(" ","-");
	
	$('#articulos').html('&nbsp;').load($get('articulos/search/?q=' + col));	
	alert(col);
}