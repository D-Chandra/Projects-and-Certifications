<?php
  session_start();
  if(isset($_POST['logout']))
    {
        session_unset();
        session_destroy();
        header("location: main.php");
        exit();
    }
  else
    {
          if(isset($_SESSION['whois']))
              {
                header("location: recordsfetch.php");
                exit();
              }
          else
              {
                header("location: main.php");
                exit();
              }   
    }
?>