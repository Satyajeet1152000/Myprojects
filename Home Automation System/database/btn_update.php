<?php
	include 'db_config.php';

	if (isset($_GET['device_name']) && isset($_GET['status']) && isset($_GET['room'])) 
	{
   		$device_name = $_GET['device_name'];
		$status = $_GET['status'];
		$room = $_GET['room'];

		// $status = '0';
		// $device = 'switch1';

		$updqry = "UPDATE $room SET status='$status' WHERE device_name='$device_name'";

			$qry = mysqli_query($conn, $updqry);

			
			if($qry)
			{
				// header('location:index.php');
			}
			// else
			// {
			// 	echo "update not";
			// }
	}	
?>