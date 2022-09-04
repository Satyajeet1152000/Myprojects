<?php

    $servername = "localhost";
	$dbname = "id16911337_home_auto";
	$username = "id16911337_satyajeet";
	$password = "t>K3kQq>IaXZM74h";
    
    
  if ($_SERVER["REQUEST_METHOD"] == "POST") 
  {
    $room = test_input($_POST['room']);
    $device = test_input($_POST['device']);
    
    $conn = mysqli_connect($servername, $username, $password, $dbname);

    if (!$conn) 
    {
     die("Connection failed: " . mysqli_connect_error());
    }
  
    $sql = "SELECT device, status FROM $room WHERE device='$device'";
    $result = mysqli_query($conn, $sql);
  
    // if (mysqli_num_rows($result) > 0) 
    // {
    //   while($row = mysqli_fetch_assoc($result)) 
    //   {
    $row = mysqli_fetch_assoc($result);
        echo $row["status"];
    //   }
    // } 
    mysqli_close($conn);
  }
  function test_input($data) 
  {
      $data = trim($data);
      $data = stripslashes($data);
      $data = htmlspecialchars($data);
      return $data;
  }
?>  