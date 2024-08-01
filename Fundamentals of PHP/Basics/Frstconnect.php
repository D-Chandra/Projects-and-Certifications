<?php
    $dbserver = "localhost";
    $dbuser = "root";
    $dbpassword = "";

    $connect = mysqli_connect($dbserver, $dbuser , $dbpassword) or die("Unable to connect");

    echo"First connection Successful ";
 ?>
