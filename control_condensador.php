<?php
  ini_set('display_errors',1);
  error_reporting(E_ALL);
  $conexion=ssh2_connect("172.16.2.11");

  if(ssh2_auth_password($conexion,"p6","coyote"))
  {
    if($_POST["accion"]=="apagar")
    {
      if(ssh2_exec($conexion,"python sensor_servidor/condensador.py T"))
        echo 'DONE';
      else
        echo 'ERROR';
    }
    elseif ($_POST["accion"]=="prender")
    {
      if(ssh2_exec($conexion,"python sensor_servidor/condensador.py F"))
        echo 'DONE';
      else
        echo 'ERROR';
    }
  }else
    echo 'ERROR2';
?>
