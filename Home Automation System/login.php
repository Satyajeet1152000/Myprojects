<?php
	session_start();
?>
<!DOCTYPE html>
<html>
<head>
	<title>Login</title>

	<meta charset="utf-8">
  	<meta name="viewport" content="width=device-width, initial-scale=1">
  	
	<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">

	<!-- Latest compiled and minified JavaScript -->
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

	<link rel="stylesheet" type="text/css" href="css/login.css" media="screen"/>

</head>
<body>
	<?php
	include 'database/db_config.php';

	if(isset($_POST['submit']))
	{
		$email = $_POST['email'];
		$password = $_POST['password'];

		$emailsearch = "select * from users_dtl where email='$email' AND password='$password'";


		$qry = mysqli_query($conn, $emailsearch);

		$usercount = mysqli_num_rows($qry);

		$getdata =mysqli_fetch_assoc($qry);

		if($usercount)
		{
				// echo "user found";
			if($getdata['email']==$admin_email && $getdata['password']==$admin_pass)
			{
				$_SESSION['username'] = $getdata['fullname'];
				?>
					<script>
						location.replace("admin_panel.php");
						// window.open("admin_panel.php");
					</script>
				<?php
			}
			else
			{
				$_SESSION['username'] = $getdata['fullname'];
				?>
					<script>
						location.replace("index.php");					
					</script>
				<?php
			}
		}			
		else
		{
			echo "not found";
		}
	}
	?>
	<div class="container h-100 d-flex justify-content-center align-items-center">
		<div class="box">					
			<form action="<?php echo htmlentities($_SERVER['PHP_SELF']); ?>" method="POST">
				<h1>Login</h1>
				<p class="text-muted"> Please enter your login and password!</p> 
				<div>
					<input type="email" name="email" placeholder="Email" required>
					<input type="password" name="password" placeholder="Password" required>
					<a class="forgot text-muted" href="#">Forgot Password</a>
					<!-- <button type="submit" name="submit">Login</button> -->
					<input type="submit" name="submit" value="Login">
				</div>					
			</form>	
			<div>
				<p class="text-muted">Don't have an account? <a class="forgot" href="signup.php">SignUp Here</a></p>
			</div>						
		</div>
	</div>
</body>