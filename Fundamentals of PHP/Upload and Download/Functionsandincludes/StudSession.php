<?php
    include_once 'ErrorhandlingandExecution.php';
?>
<?php
if(!isset($_POST["Login"]))
    {
        header("location: ../Student.php");
        exit();
    }


$email = $_POST['E_mail'];
$pwd = $_POST['passwd'];
if(emptyfields($email,$pwd) === false)
    {
        header ("location: ../Student.php?error=emptyfields");
        exit(); //exit() used to exit the current running script
    }
else
    {
        Slogin($email,$pwd);
    }
?>
