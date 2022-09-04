<?php
session_start();

if(!isset($_SESSION['username']))
{
	header('location:login.php');
}
$usr=$_SESSION['username'];
?>
<!DOCTYPE html>
<html>
<head>
	<title>Home</title>

	<meta charset="utf-8">
  	<meta name="viewport" content="width=device-width, initial-scale=1">

	<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">

	<!-- Latest compiled and minified JavaScript -->
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

	<script src='https://kit.fontawesome.com/a076d05399.js' crossorigin='anonymous'></script>

	<link rel="stylesheet" type="text/css" href="css/index.css" media="screen"/>



	<script>
   	    setInterval(function() {
    	        $("#auto_refresh").load(location.href+" #auto_refresh>*","");
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
<?php
	if(isset($_POST['logout']))
	{
		?>
        <script>
            window.location.href = 'logout.php';
        </script>
        <?php
	}

	if(isset($_POST['admin_panel']))
	{
		if($_SESSION['username']=='admin')
		{
			?>
            <script>
                window.location.href = 'admin_panel.php';
            </script>
            <?php
		}
		else
		{
			echo '<script>alert("You\'re not admin.")</script>';
		}			
	}
?>
<!-- ---------------------------------------content start from here-----------------------------------  -->

<nav class="navbar navbar-expand">

  	<a class="sitename" href="index.php">One<br> Touch<br> Solutions</a>

  	<form action="<?php echo htmlentities($_SERVER['PHP_SELF']); ?>" method="post">
		<button type="submit" id="admin" name="admin_panel">Admin Panel</button>
		<button type="submit" id="logout" name="logout">LogOut</button>			
	</form>
</nav>

<div class="welcome">
	<div class="message container h-100 d-flex justify-content-center align-items-center"> 
		<h1>Welcome</h1>
		<h2>
			<?php echo $_SESSION['username'] ?>			
		</h2>
	</div>	
</div>


</div>
	
<div id="auto_refresh">
	<?php   
 		include_once 'Rooms/room1.php';	
 		include_once 'Rooms/room2.php'; 
 		include_once 'Rooms/kitchen.php';
 		include_once 'Rooms/other_switches.php';
	 ?>
</div>
</body>
</html>