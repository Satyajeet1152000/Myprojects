<?php

	include 'db_config.php';

	$id = $_GET['id'];

	$delqry = "delete from users_dtl where id=$id";
	
	$qry = mysqli_query($conn, $delqry);	
	
	if($qry)
	{
	    ?>
        <script>
            window.location.href = "/admin_panel.php";
        </script>
        <?php
	}
	else
	{
	    ?>
        <script>
            alert("error");
        </script>
        <?php
	}
?>