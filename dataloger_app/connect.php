<html>
    <body>
        <?php

        $dbname = 'Data';
        $dbuser = 'amirhoseinarya';
        $dbpass = 'amir_1382';
        $dbhost = 'localhost';

        $connect = @mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

        if(!connect){
            echo "Error: " . mysqli_connect_error();
            exit();
        }

        echo "connection success!<br><br>";

        $b1 = $_GET["temprature"];
        $b2 = $_GET["humidity"];

        $query = "INSERT INTO DATA ("