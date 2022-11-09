<!DOCTYPE html>
<html>
<body>

<?php
header("Refresh:1"); //rafraichi la page automatiquement toute les 1 seconde
//echo("<meta http-equiv='refresh' content='1'>");//rafraichi la page automatiquement toute les 1 seconde
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "data_pressure";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

//$sql = "SELECT data.data FROM data ORDER BY data.id DESC LIMIT 1";
$sql = "SELECT data FROM data ORDER BY id DESC LIMIT 1";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "<br> pressure: ". $row["data"]. "<br>";
    }
} else {
    echo "0 results";
}

$conn->close();
?>

</body>
</html>