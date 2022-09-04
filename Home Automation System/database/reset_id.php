<?php
	include_once 'db_config.php';


	$upd = "set @autoid :=0";
	$qry = mysqli_query($conn, $upd);

	$upd = "update users_dtl set id = @autoid := (@autoid+1)";
			$qry = mysqli_query($conn, $upd);
	$upd = "alter table users_dtl Auto_Increment = 1";
	$qry = mysqli_query($conn, $upd);	

// header("Location: admin_panel.php");
?>
        <script>
          window.location.href = '/admin_panel.php';
     </script>
     <?php
     
?>