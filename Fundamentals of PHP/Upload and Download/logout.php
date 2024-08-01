<?php
  session_start();
  if(isset($_POST['logout']))
    {
        session_unset();
        session_destroy();
        header("location: Firstpage.php");
        exit();
    }
  else
    {
        if(isset($_SESSION['whois']))
          {
              if($_SESSION['whois'] == "Teacher")
                {
                  header("location: Upload.php");
                  exit();
                }
              if($_SESSION['whois'] == "Student")
                {
                  header("location: download.php");
                  exit();
                }
            }
          else
            {
              header("location: Firstpage.php");
              exit();
            }   
    }
?>