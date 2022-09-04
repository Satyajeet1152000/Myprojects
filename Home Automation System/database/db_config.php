<?php 
	$server = "localhost";
	$database = "id16911337_home_auto";
	$user = "id16911337_satyajeet";
	$password = "t>K3kQq>IaXZM74h";

	$conn = mysqli_connect($server, $user, $password, $database);

	if($conn)
	{
		?>
	 		<!-- <script type="text/javascript">
			 	alert("Connection Successful");
			 </script> -->
		 <?php
	}
	else
	{
		?>
			<script type="text/javascript">
				alert("Connection Unsuccessful");
			</script>
		<?php
	}

	//for admin_panel login page
	$admin_name = 'admin';
	$admin_email='admin@gmail.com';
	$admin_pass='@dmin';
?>