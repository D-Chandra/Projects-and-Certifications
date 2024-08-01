<?php
    include_once 'FunctionsandErrorhandling/Credentialschecking.php';
?>
<?php
if(!isset($_POST["Login"]))
    {
        header("location: adminlogin.php");
        exit();
    }


$email = $_POST['E_mail'];
$pwd = $_POST['passwd'];
if(emptyfields($email,$pwd) === false)
    {
        header ("location: adminlogin.php?error=emptyfields");
        exit(); //exit() used to exit the current running script
    }
else
    {
        admlogin($email,$pwd);
    }
?>
