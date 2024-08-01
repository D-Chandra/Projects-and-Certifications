<?php
    if(!isset($_POST["LogVisitor"]))
    {
        header("location: register.php");
        exit();
    }
?>
<?php
    include_once 'FunctionsandErrorhandling/Credentialschecking.php';
?>
<?php
    $date= $_POST['date'];
    $name= $_POST['Name'];
    $email = $_POST['E_mail'];
    $phone= $_POST['Phone'];

    if(emptyfieldsreg($date,$name,$email,$phone) === false)
        {
            header ("location: register.php?error=emptyfields");
            exit(); //exit() used to exit the current running script
        }
    if(emailcheck($email) === false)
        {
            header ("location: register.php?error=checkemail");
            exit();
        }

    startregistering($date,$name,$email,$phone);
    
?>