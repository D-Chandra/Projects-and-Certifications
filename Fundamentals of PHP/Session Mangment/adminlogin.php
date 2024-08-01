<?php
  session_start();
          
        if(isset($_SESSION['whois']))
          {
                  header("location: recordsfetch.php");
                  exit();
          }
                      
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Administrative Login</title>
    <link rel="Stylesheet" href="Styleandeffects/basedesign.scss">
</head>
<body>
    <h1>LOGGING AS ADMINISTRATOR</h1>
<div class="container">
    <form action="adminsession.php" method="POST">

      <div class="field tnb">
        <label for="email">Email address</label>
        <input type="email" name="E_mail"/>
      </div>

      <div class="field tnb">
        <label for="msg">Password</label>
        <input type="password" name="passwd"/>
      </div>
      <input class="btn btn--stripe btn--large" type="submit" name="Login" value="LOG IN">

    </form>
    <?php
        if(isset($_GET['error']))
          {
            if($_GET['error'] == 'emptyfields')
              {
                echo "<h3>Fill in all fields Properly</h3>";
              }

            if($_GET['error'] == 'internalservererror')
              { 
                echo "<h3>Error Occured::Internal server error</h3>";
              }

            if($_GET['error'] == 'internaldatabaseError')
              {
                echo "<h3>Error occured::Database Statment Error";
              }

              if($_GET['error'] == 'Usernotregistered')
              {
                echo "<h3>You are not Registered. Please contact Administrator on::Email(diwanshu.chandra.in@gmail.com) get Yourself registered</h3>";
              }

              if($_GET['error'] == 'wrongpasswd')
              {
                echo "<h3>Wrong Password entered</h3>";
              }

              if($_GET['error']=='entercredentials')
              {
                echo "<h3>First Enter Your credentials Here</h3>";
              }
          }   
    ?>
</body>
</html>