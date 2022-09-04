<?php

$servername = "localhost";
$dbname = "id16911337_home_auto";
$username = "id16911337_satyajeet";
$password = "t>K3kQq>IaXZM74h";

if ($_SERVER["REQUEST_METHOD"] == "POST") 
{
    $room = test_input($_POST['room']);
    $device = test_input($_POST['device']);
    $value = test_input($_POST['value']);
    
    $conn = mysqli_connect($servername, $username, $password, $dbname);

    if (!$conn) 
    {
        die("Connection failed: " . mysqli_connect_error());
    }

    $sql = "UPDATE $room SET status='$value' WHERE device='$device'"; 

    if (mysqli_query($conn, $sql)) 
    {
        echo "DB Updation Success.";
    }
    else
    {
        echo "DB Updation Failed.";
    }
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