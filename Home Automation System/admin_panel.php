<?php
	session_start();

	if(!isset($_SESSION['username']))
	{
		header('location:login.php');
	}
?>
<!DOCTYPE html>
<html>
<head>
	<title>Admin Panel</title>

	<meta name="viewport" content="width=device-width, initial-scale=1">

	<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">

	<!-- Latest compiled and minified JavaScript -->
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

	<script src='https://kit.fontawesome.com/a076d05399.js' crossorigin='anonymous'></script>

	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

	<link rel="stylesheet" type="text/css" href="css/admin_panel.css" media="screen"/>

	<script>
		function show_users_dtl() 
		{
  			var x = document.getElementById("show_userdtl");
  			if (x.style.display === "none") 
  			{
   		 		x.style.display = "block";
  			} 
  			else 
  			{
    			x.style.display = "none";
  			}
		}

		function show_home_stats() 
		{
  			var x = document.getElementById("home_stats");
  			if (x.style.display === "none") 
  			{
   		 		x.style.display = "block";
  			} 
  			else 
  			{
    			x.style.display = "none";
  			}
		}
		
		setInterval(function() {
    	        $("#home_stats").load(location.href+" #home_stats>*","");
        }, 1000);

        document.addEventListener("DOMContentLoaded", function(event) { 
            var scrollpos = localStorage.getItem('scrollpos');
            if (scrollpos) window.scrollTo(0, scrollpos);
        });

        window.onbeforeunload = function(e) {
            localStorage.setItem('scrollpos', window.scrollY);
        };
	</script>
</head>
<body>
	<!-- ---------------------------------------content start from here-----------------------------------  -->
	<?php
				if(isset($_POST['logout']))
				{
					?>
                     <script>
                         window.location.href = 'logout.php';
                     </script>
                    <?php
				}

				if(isset($_POST['home_page']))
				{
					?>
                    <script>
                        window.location.href = 'index.php';
                    </script>
                    <?php
				}
			?>
	<nav class="navbar navbar-expand">

  		<a class="sitename" href="index.php">One<br> Touch<br> Solutions</a>

  		<form action="<?php echo htmlentities($_SERVER['PHP_SELF']); ?>" method="post">  			
			<button type="submit" name="home_page">Home Page</button>
			<button type="submit" name="logout">LogOut</button>	
		</form>
	</nav>

	<div class="welcome">
		<div class="message container h-100 d-flex justify-content-center align-items-center"> 
		<h1>Admin Panel</h1>
	</div>

	<nav class="navbar navbar-expand">
		<div class="admin_control container">
			<button name="show_users_dtl" onclick="show_users_dtl()">Show Users Details</button> 
			<button name="show_home_stats" onclick="show_home_stats()">Show Home Stats</button>
		</div>		
	</nav>

	<!-- ------------------User Details----------------------------- -->
		
	<div id="show_userdtl" style="display: block;">
		<table id="user_details" align="center">
			<thead>
				<tr>
					<th>ID</th>
					<th>Username</th>
					<th>Email</th>
					<!--<th>Password</th>-->
					<th>Phone No.</th>
					<th colspan="2">Action</th>
				</tr>
			</thead>
			
			<tbody>
				<?php
					include 'database/db_config.php';

					$show = "select * from users_dtl";
					$qry = mysqli_query($conn , $show);

					// $getdata =mysqli_fetch_assoc($qry);

					
					if($qry)
					{
						while ($getdata = mysqli_fetch_assoc($qry)) 
						{
							?>
							<tr>
								<td> <?php echo $getdata['id']; ?> </td>
								<td> <?php echo $getdata['fullname']; ?> </td>
								<td> <?php echo $getdata['email']; ?> </td>
								<!--<td> <?php echo $getdata['password']; ?> </td>-->
								<td> <?php echo $getdata['phoneno']; ?> </td>
								<td><a name="update" href="database/db_update.php?id=<?php echo $getdata['id']; ?>" target=""><i class="fa fa-edit" style="font-size:30px"></i></a></td>
								<td><a name="delete" href="database/db_delete.php?id=<?php echo $getdata['id']; ?>"><i class="fa fa-trash-o" style="font-size:30px"></i></a></td>	
							</tr>
							<?php
						}
					}
					else
					{
						echo "not able to fetch";
					}			
				?>
			</tbody>
		</table>
		<center>
			<form action="database/reset_id.php">
				<button name="reset_id">Reset ID <i class="fa fa-refresh" style="font-size:25px"></i></button>
			</form> 
		</center>
	</div>
	<div id="home_stats" style="display: none;">		
	   		<?php
	   		    include_once 'Rooms/room1.php';	
 				include_once 'Rooms/room2.php'; 
 				include_once 'Rooms/kitchen.php';
 				include_once 'Rooms/other_switches.php';
	    	?>
	</div>	
</body>
</html>