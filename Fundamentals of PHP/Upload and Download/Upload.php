<?php
  session_start();
    
        if(!isset($_SESSION['whois']))
            {
                header("location: Firstpage.php");
                exit();
            }
        if($_SESSION['whois'] == "Student")
            {
                header("location: download.php");
                exit();
            }
                 
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Uploading Files</title>
    <link rel="Stylesheet" href="Designandeffects/design.scss">
</head>
<body>
    <?php
        echo "<h1> Welcome " . $_SESSION['username'] . "</h1>" ;
    ?>
    <h2>Select a Course From Given List then Upload</h2>
    <div class="Container">
        <form  action="Uploadassign.php" method="POST" enctype="multipart/form-data">
            <div class="field tnb">
                <label> CAP 189(Database Administration)</label>
                <input type="radio" value="CAP 189" name="Course" />
                <label> CAP 525(PHP Practicle)</label>
                <input type="radio" value="CAP 525" name="Course" />
                <label> CAP 906(Pyhton Programming)</label>
                <input type="radio" value="CAP 906" name="Course" />
                <label> CAP 602(Wireless Networking)</label>
                <input type="radio" value="CAP 602" name="Course" />
                <br>
                <label> Select File</label>
                <input type="file" name="assignment" >
                <input class="btn btn--stripe btn--large" type="submit" name="fileupload" value="UPLOAD">
              </div>
        </form>     
    </div>
    <form  action="logout.php" method="POST">
    <input class="btn btn--stripe" type="submit" name="logout" value="LOG ME OUT">
    </form>
    <?php
        if(isset($_POST['error']))
            {
                if($_POST['error']=='selectfilesandcourse')
                    {
                        echo "<h3>First Properly Enter Select the File and Course then click Upload</h3>";
                    }
            }
    ?>
      
    <label>Allowed extensions to be used are :: ('jpg','jpeg','png','doc','docx','pdf','txt')</label>
    <label>Allowd Size of file Maximum of 20 MB</label>
</body>
</html>