<?php

// database
$servername = "localhost";
$username = "*********";
$password = "*********";
$dbname = "***************";
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    echo 'error';
  die("Connection failed: " . $conn->connect_error);
}

$chatid = "";
if(isset($_POST['chatid'])){
	$chatid=$_POST['chatid'];
}

$sql = "UPDATE player SET activate = 1 WHERE chatid = \"{$chatid}\"";
if ($conn->query($sql) === TRUE) {
echo "activate player update successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

?>