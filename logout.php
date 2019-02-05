<?php
	require_once('engine.php');
	global $suffix;
	session_destroy();
	header("Location: index?lang=$suffix");
?>