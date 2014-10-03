<?php
include_once "gramatica.php";
$palabra = "Alex Requeno";
$res_w = "";
$cleanword = ereg_replace( "([ ]+)", "", $palabra );
$tam = strlen( $cleanword );
for ( $i = 0; $i <= $tam-1; $i++ )
{
	$letra = substr( $cleanword, $i, 1 );
	$res_w .= grammar( $letra );
}

echo $res_w;
