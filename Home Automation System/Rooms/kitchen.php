<!DOCTYPE html>
<html>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1">

	<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">

	<!-- Latest compiled and minified JavaScript -->
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

	<script src='https://kit.fontawesome.com/a076d05399.js' crossorigin='anonymous'></script>

	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

	<link rel="stylesheet" type="text/css" href="css/room.css" media="screen"/>

	<script type="text/javascript">
		function btnupdate(id,dn,rm)
		{
			if(document.getElementById(id).checked == true)
			{
				$.ajax
				({
					url: "database/btn_update.php",
					type: "GET",
					data: {
						device_name: dn,
						status: '1',
						room: rm,
					}
				});
			}
			else if(document.getElementById(id).checked == false)
			{
				$.ajax
				({
					url: "database/btn_update.php",
					type: "GET",
					data: {
						device_name: dn,
						status: '0',
						room: rm,
					}
				});				
			}
		}
	</script>	
</head>
<body>	
	<div id="auto_refresh">		
		<div class="table_data">
			<h1>Kitchen</h1>
			<table align="center">
				<thead>
					<tr>
						<th>ID</th>
						<th>Device Name</th>
						<th colspan="2">Status</th>
					</tr>
				</thead>

				<tbody>
					<?php
					include 'database/db_config.php';

					$show = "select * from kitchen";
					$qry = mysqli_query($conn , $show);

					// $getdata =mysqli_fetch_assoc($qry);


					if($qry)
					{
						while ($getdata = mysqli_fetch_assoc($qry)) 
						{
							?>
							<tr>
								<td> <?php echo $getdata['id']; ?> </td>
								<td> <?php echo $getdata['device_name']; ?> </td>
								<!-- <td> <?php echo $getdata['status']; ?> </td> -->
								<td> 	 
									<input type="checkbox" id="<?php echo $getdata['device_name'].'-kitchen'; ?>" 
									class = "toggle_btn"
									onclick="btnupdate('<?php echo $getdata['device_name'].'-kitchen'; ?>','<?php echo $getdata['device_name']; ?>','kitchen')" <?php echo $getdata['status'] == '1' ? 'checked' : '' ;?>>
								</td>
						</tr>
						<?php
					}
				}											
				?>										
			</tbody>
		</table>
	</div>
</div>
</body>
</html>