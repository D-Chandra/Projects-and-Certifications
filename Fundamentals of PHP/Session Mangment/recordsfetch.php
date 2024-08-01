<?php
session_start();
if(!isset($_SESSION['whois']))
{
        header("location: adminlogin.php");
        exit();
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="Stylesheet" href="Styleandeffects/basedesign.scss">
</head>
<body>
<h2>SELECT THE DATE FROM WHICH AND TILL WHICH YOU WANT TO FETCH THE VISITED CUSTOMERS</h2>
<div class="Container">
        <form  action="FunctionsandErrorhandling/fetcheddata.php" method="POST">
            <div class="field tnb">
                <label>From</label>
                <input type="date" name="from-date" value="2020-06-20" min="2020-05-01" max="2020-07-30">
                <label>TO</label>
                <input type="date" name="to-date" value="2020-06-30" min="2020-05-01" max="2020-07-30">
                <input class="btn btn--stripe btn--large" type="submit" name="datedata" value="FETCH">   
              </div>
        </form>     
</div>

<form  action="logout.php" method="POST">
<input class="btn btn--stripe" type="submit" name="logout" value="LOG ME OUT">
</form>
<br><br><br>
<a href="register.php" class="btn btn--stripe">REGISTER A VISITOR's DETAILS</a>

<?php
        if(isset($_GET['error']))
            {
                if($_GET['error']=='selectdatedata')
                    {
                        echo "<h3>First Properly Select the Dates and then click FETCH Button</h3>";
                    }
                if($_GET['error']=='internalservererror')
                    {
                        echo "<h3>Internal Server Error have Occured::DBCE</h3>";
                    }
                if($_GET['error']=='internalservererror2')
                    {
                        echo "<h3>Internal Server Error have Occured::DBSPE</h3>";
                    }
                if($_GET['error']=='internaldatabaseerror')
                    {
                        echo "<h3>Internal Database Error have Occured::DBSEE</h3>";
                    }
                if($_GET['error']=='nodata')
                    {
                        echo "<h2>NO ONE VISITED BETWEEN THOSE DATES</h2>";
                    }
            }       
?>
</body>
</html>