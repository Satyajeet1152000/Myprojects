<?php

	session_start();
	session_destroy();

	include 'db_config.php';

		if (isset($_POST['submit'])){
			$username = mysqli_real_escape_string($conn, $_POST['fullname']);
			$email = mysqli_real_escape_string($conn, $_POST['email']);
			$password = mysqli_real_escape_string($conn, $_POST['password']);
			$cpassword = mysqli_real_escape_string($conn, $_POST['cpassword']);
			$phono = mysqli_real_escape_string($conn, $_POST['phono']);

			$emailqry = "select * from users_dtl where email='$email'";
			$qry = mysqli_query($conn, $emailqry);


			$emailcount = mysqli_num_rows($qry);

			if ($emailcount > 0)
			{
				echo "Email already exists";			
			}
			else
			{
				if($password==$cpassword)
				{
					$insertqry = "insert into users_dtl(fullname, email, password, phoneno) VALUES('$username', '$email', '$password', '$phono')";

					$iqry = mysqli_query($conn, $insertqry);

					if($iqry)
					{
						?>
							<script type="text/javascript">
								alert("Inserted Successful");
							</script>
						<?php
					}
					else
					{
						?>
							<script type="text/javascript">
								alert("Inserted Unsuccessful.");
							</script>
						<?php
					}
				}
				else
				{
					echo "password is not matching.";
				}
			}
		}
?>