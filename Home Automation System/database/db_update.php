<?php
	include 'db_config.php';
	$id = $_GET['id'];
?>
<!DOCTYPE html>
<html>
<head>
	<title>Update</title>

	<meta charset="utf-8">
  	<meta name="viewport" content="width=device-width, initial-scale=1">
  	
	<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">

	<!-- Latest compiled and minified JavaScript -->
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

	<link rel="stylesheet" type="text/css" href="../css/update.css" media="screen"/>
</head>
<body>
	<?php
		if(isset($_POST['submit']))
		{
			$fullname = $_POST['fullname'];
			$email = $_POST['email'];
			$phoneno = $_POST['phono'];

			$updqry = "UPDATE users_dtl SET fullname='$fullname', email='$email', phoneno='$phoneno' WHERE id='$id'";

			$qry = mysqli_query($conn, $updqry);


			if($qry)
			{
				?>
                <script>
                    window.location.href = '/admin_panel.php';
                </script>
                <?php
			}
			else
			{
				?>
                <script>
                    alert("updation erro");
                </script>
                <?php
			}
		}
	?>

	<div class="container h-100 d-flex justify-content-center align-items-center">
		<div class="box">
			<h1>Update</h1>
		<?php
			$fill = "select * from users_dtl where id='$id'";

			$qry = mysqli_query($conn, $fill);

			$getdata =mysqli_fetch_assoc($qry);
		?>
		<div>
			<form method="POST">
				<label for="fullname">Fullname:</label>
				<input type="textbox" name="fullname" value="<?php echo $getdata['fullname'] ?>" required>

				<label for="email"> Email:</label>
				<input type="email" name="email"  value="<?php echo $getdata['email'] ?>" required>

				<label for="phono">Phone No.:</label>
				<input type="textbox" name="phono" value="<?php echo $getdata['phoneno'] ?>" required>
				<button type="submit" name="submit">Update</button>
			</form>
		</div>
		</div>
	</div>
</body>
</html>
