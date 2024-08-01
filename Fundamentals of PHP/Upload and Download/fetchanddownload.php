<?php
    if(!isset($_POST['fetch']))
        {
            header("location: download.php?error=selectcourse");
            exit();
        }
    if(!isset($_POST['Coursedownload']))
        {
            header("location: download.php?error=selectcourse");
            exit();
        }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fetching From server</title>
    <link rel="Stylesheet" href="Designandeffects/Studdesign.scss">
    <script type = "text/javascript" src = "Designandeffects/Studeffects.js" ></script>
</head>
<body>
    <?php
        $destination = 'Assignments/'.$_POST['Coursedownload'] .'/';
        $fetchingfiles = scandir($destination);
        unset($fetchingfiles[0]);unset($fetchingfiles[1]);
        if($fetchingfiles)
            {
                foreach($fetchingfiles as $val)
                    {
                        echo "<ul class='rolldown-list' id='myList'>
                        <li><label>".$val."&nbsp &nbsp &nbsp &nbsp"."<a download='$val' href='$destination$val'>DOWNLOAD</a>". "</label></li></ul>";
                        echo "<br><br><br>";
                    }
            }
        else
            {
                header("location: download.php?error=nofiles");
                exit();
            }
    ?>
<button id="btnReload"><form  action="logout.php" method="POST">
    <input class="btn btn--stripe" type="submit" name="logout" value="LOG ME OUT">
    </form></button>  
</body>
</html>