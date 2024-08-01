<?php
  session_start();
   
        if(isset($_SESSION['whois']))
            {
              if($_SESSION['whois'] == "Teacher")
                {
                  header("location: Upload.php");
                  exit();
                }
              
            }
        else
            {
                header("location: Firstpage.php");
                exit();
            } 
              
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Downlaod page</title>
    <link rel="Stylesheet" href="Designandeffects/Studdesign.scss">
    <script type = "text/javascript" src = "Designandeffects/Studeffects.js" ></script>
</head>
<body>
<?php
        echo "<h1> Welcome " . $_SESSION['username'] . "</h1>" ;
?>
    <h2>CHOOSE ANY OPTION THEN CLICK ON FETCH</h2>
<ul class="rolldown-list" id="myList">
<form action="fetchanddownload.php" method="POST">
  <li><label> CAP 189(Database Administration)&nbsp &nbsp</label>
                <input type="radio" value="CAP 189" name="Coursedownload" /></li>
  <li><label> CAP 525(PHP Practicle)</label>&nbsp &nbsp
                <input type="radio" value="CAP 525" name="Coursedownload" /></li>
  <li><label> CAP 906(Pyhton Programming)&nbsp &nbsp</label>
                <input type="radio" value="CAP 906" name="Coursedownload" /></li>
  <li><label> CAP 602(Wireless Networking)&nbsp &nbsp</label>
                <input type="radio" value="CAP 602" name="Coursedownload" /></li>
   <li ><input class="btn btn--stripe btn--large" type="submit" name="fetch" value="FETCH ASSIGNMENTS"></li>
   <?php 
        if(isset($_GET['error']))
            {
                if($_GET['error'] == 'selectcourse')
                    {
                        echo "<h2 style='color:red;'' > PLEASE SELECT THE COURSE FIRST !! </h2>";
                    }
                if($_GET['error'] == 'Internalservererror')
                    {
                        echo "<h2 style='color:red;'' > AN INTERNAL SERVER ERROR HAS BEEN OCCURED !! PLz Try Again </h2>";
                    }
                if($_GET['error'] == 'nofiles')
                    {
                        echo "<h2 style='color:red;'' > YOU HAVE NO ASSIGNMENTS UNDER THAT COURSE CODE </h2>";
                    }
            }
    ?>
</form>
</ul> 

<button id="btnReload"><form  action="logout.php" method="POST">
    <input class="btn btn--stripe" type="submit" name="logout" value="LOG ME OUT">
    </form></button>
    <br><br>
    
</body>
</html>