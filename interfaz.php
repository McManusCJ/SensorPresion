<?php
echo'
<!DOCTYPE html>
<html>
	<title>
	Presión
	</title>
	<meta charset="UTF-8">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
	integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"
	integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.12.2/css/bootstrap-select.min.css">
	<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.12.2/js/bootstrap-select.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.12.2/js/i18n/defaults-*.min.js"></script>

<head>
</head>

<body>
	<div class="container">
		<div class="row">
			<div class="col-md-3">
				<h1>
					Sistema de Monitoreo de Presión
				</h1>
			</div>
			<div class="col-md-9">
				<h3>
					Rango de Consulta
				</h3>
			</div>
		</div>




		<div class="row">
		<div class="col-md-3">
		</br><button type="button" class="btn btn-danger btn-lg" id="off">
				<span>Apagar condensador</span>
			</button></br>
		</br><button type="button" class="btn btn-success btn-lg" id="on">
				<span>Prender condensador</span>
			</button>






		</br></br>
		<h4 id="resultado" ></h4>
		</div>
			<div class="col-md-2">
				<input type="number" id="numb" class="form-control" name="quantity" min="1" max="60">
			</div>
			<div class="col-md-2">
				<select class="selectpicker" id="rango">
					<option value="min">Minutos</option>
					<option value="h">Horas</option>
					<option value="d">Días</option>
					<option value="w">Semanas</option>
					<option value="m">Meses</option>
				</select>
			</div>
			<div class="col-md-3  col-md-offset-1 btn-group btn-group-lg">
				<button type="button" class="btn btn-default" id="bot" role="button">Enviar</button>
			</div>
		</div>
	</div>

	<div class="container">
		<div class="row">
			<div class="col-lg-6 col-lg-offset-3">
				<ul class="nav nav-tabs">
					<li class="active"><a data-toggle="tab" href="#tem">Temperatura</a></li>
					<li><a data-toggle="tab" href="#hum">Humedad</a></li>
					<li><a data-toggle="tab" href="#pre">Presión</a></li>
				</ul>
				<div class="tab-content">
					<div id="tem" class="tab-pane fade in active text-justify">
						<div class="row">
							<div class="col-md-2 ">
								<span>
								<br/><br/> Celsius <br/><br/>
								<button type="button" class="btn btn-default">
								<a download="somedata.csv" href="http://172.16.2.15/render?target=sensor.temperatura&height=400&width=600&format=csv&from=-30min">
									Descargar </br> .csv
								</a>
							</button>
								</span>
							</div>
							<div class="col-md-8">
								<img id="temp" src="http://172.16.2.15/render?target=sensor.temperatura&height=400&width=600&format=png&from=-30min">
							</div>
						</div>
					</div>
					<div id="hum" class="tab-pane fade text-justify">
						<div class="row">
							<div class="col-md-2">
								<span>
								<br/><br/>% ppm <br/><br/>
									<button type="button" class="btn btn-default">
										<a download="somedata.csv" href="http://172.16.2.15/render?target=sensor.humedad&height=400&width=600&format=csv&from=-30min">
											Descargar </br> .csv
										</a></span>
									</button>
							</div>
							<div class="col-md-8">
								<img id="hume" src="http://172.16.2.15/render?target=sensor.humedad&height=400&width=600&format=png&from=-30min">
							</div>
						</div>
					</div>
					<div id="pre" class="tab-pane fade text-justify">
						<div class="row">
							<div class="col-md-2 ">
								<span>
								<br/><br/>Pascales <br/><br/>
								<button type="button" class="btn btn-default">
									<a download="somedata.csv" href="http://172.16.2.15/render?target=sensor.presion&height=400&width=600&format=csv&from=-30min">
										Descargar </br> .csv
									</a></span>
								</button>
								</span>
							</div>
							<div class="col-md-8">
								<img id="pres" src="http://172.16.2.15/render?target=sensor.presion&height=400&width=600&format=png&from=-30min">
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</body>
<script>
	$("#bot").click(function(){
		$("#temp").attr("src","http://172.16.2.15/render?target=sensor.temperatura&height=400&width=600&format=png&from=-"+$("#numb").val()+$("#rango").val());
		$("#hume").attr("src","http://172.16.2.15/render?target=sensor.humedad&height=400&width=600&format=png&from=-"+$("#numb").val()+$("#rango").val());
		$("#pres").attr("src","http://172.16.2.15/render?target=sensor.presion&height=400&width=600&format=png&from=-"+$("#numb").val()+$("#rango").val());
		console.log($("rango").val());
	});
	$("#off").click(function(){
		$.ajax({
			url:"control_condensador.php",
			data:{
				"accion":"apagar"
			},
			type:"post",
			dataType:"text",
			success:function(data){
				if(data=="DONE")
					$("#resultado").html("El condensador se ha apagado");
				else
					$("#resultado").html("El condensador NO se ha apagado");
			}
		});
	});
	$("#on").click(function(){
		$.ajax({
			url:"control_condensador.php",
			data:{
				"accion":"prender"
			},
			type:"post",
			dataType:"text",
			success:function(data){
				console.log(data);
				if(data=="DONE")
					$("#resultado").html("El condensador se ha prendido");
				else
					$("#resultado").html("El condensador NO se ha prendido");
			}
		});
	});
</script>
</html>';
?>
