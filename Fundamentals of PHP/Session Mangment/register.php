<?php
    session_start();
    if(!isset($_SESSION['whois']))
        {
            header("location: adminlogin.php?error=entercredentials");
            exit();
        }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LOG A VISTORS's DETAIL</title>
    <link rel="Stylesheet" href="Styleandeffects/basedesign.scss">
</head>
<body>
<h1>FILL IN THE DETAILS OF VISITOR</h1>
<div class="container">
    <form action="registeringprocess.php" method="POST">
        <div class="field tnb">
            <label for="date">SELECT DATE</label>
            <input type="date" name="date" value="2020-06-20" min="2020-05-01" max="2020-07-30">
        </div>
        <div class="field tnb">
            <label for="name">NAME</label>
            <input type="text" name="Name"/>
        </div>
        <div class="field tnb">
            <label for="email">EMAIL</label>
            <input type="email" name="E_mail"/>
        </div>
        <div class="field tnb">
            <label for="phone">PHONE</label>
            <input type="text" name="Phone"/>
        </div>
      <input class="btn btn--stripe btn--large" type="submit" name="LogVisitor" value="SAVE">
    </form>
<form  action="logout.php" method="POST">
<input class="btn btn--stripe" type="submit" name="logout" value="LOG ME OUT">
</form>
<?php
        if(isset($_GET['error']))
            {
                if($_GET['error']=='emptyfields')
                    {
                        echo "<h3>Fill in all fields Properly</h3>";
                    }
                if($_GET['error'] == 'checkemail')
                    { 
                      echo "<h3>Error Occured::Invaid email entered</h3>";
                    }
                if($_GET['error'] == 'InternalPreperror')
                    { 
                      echo "<h3>Error Occured::DBPE</h3>";
                    }
                if($_GET['error'] == 'noerror')
                    { 
                      echo "<h3>LAST VISITOR's DETAILS WHERE SUCCESSFULLY RECORDED</h3>";
                    }
            }
    ?>
<br><br>
<a href="recordsfetch.php" class="btn btn--stripe">FETCH FROM AVAILABLE RECORDS</a>
    

</body>
</html>