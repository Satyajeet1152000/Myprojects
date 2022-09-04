
<!DOCTYPE html>
<html>
<head>
	<title>Sign Up</title>

	<meta charset="utf-8">
  	<meta name="viewport" content="width=device-width, initial-scale=1">

	<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">

	<!-- Latest compiled and minified JavaScript -->
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

	<script src='https://kit.fontawesome.com/a076d05399.js' crossorigin='anonymous'></script>

	<link rel="stylesheet" type="text/css" href="css/signup.css" media="screen"/>
</head>
<body>
	<?php
		include 'database/db_insert.php';
	?>

	<div class="container h-100 d-flex justify-content-center align-items-center">
		<div class="box">
			<form action="<?php echo htmlentities($_SERVER['PHP_SELF']); ?>" method="POST">
				<h1>Sign Up</h1>
				<input type="textbox" name="fullname" placeholder="Full Name" required><br><br>
				<input type="email" name="email" placeholder="Email Address" required><br><br>
				<input type="password" name="password" placeholder="Create Password" required><br><br>
				<input type="password" name="cpassword" placeholder="Confirm Password" required><br><br>
				<input type="textbox" title="Please enter 10-digit Phone No." pattern="[1-9]{1}[0-9]{9}" name="phono" placeholder="Phone Number" required><br><br>
				<button type="submit" name="submit">Create Account</button>
			</form>
			<div class="bottom">
				Already have an account? <a href="login.php">LogIn Here</a>
			</div>
		</div>		
	</div>
</body>
</html>