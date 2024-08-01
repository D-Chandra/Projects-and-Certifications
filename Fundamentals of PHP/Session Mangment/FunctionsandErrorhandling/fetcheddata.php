<?php
    if(!isset($_POST['datedata']))
        {
            header("location: /PHP Programs/EVALUATION 2/QUES 2/recordsfetch.php?error=selectdatedata");
            exit();
        }
    
        
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="Stylesheet" href="/PHP Programs/EVALUATION 2/QUES 2/Styleandeffects/fetchdesign.scss">
    <script type = "text/javascript" src = "/PHP Programs/EVALUATION 2/QUES 2/Styleandeffects/fetcheffects.js" ></script>
</head>
<body>
    <h2>LIST OF VISITORS FOUND UNDER GIVEN DATES</h2>
    <?php
        $connection = mysqli_connect('localhost','root','root','php assignment');
        if(isset($connection))
            {
                $sqlquery = "Select * from customer_visits where date>=? and date<=?;";
                $PrepareStmt = mysqli_stmt_init($connection);
                if(!mysqli_stmt_prepare($PrepareStmt,$sqlquery))
                    {
                        header("location: /PHP Programs/EVALUATION 2/QUES 2/recordsfetch.php?error=internalservererror2");
                        exit();
                    }
                else
                    {   
                        mysqli_stmt_bind_param($PrepareStmt,"ss",$_POST['from-date'],$_POST['to-date']);
                        if(mysqli_stmt_execute($PrepareStmt))
                            {
                                $fetchrows = mysqli_stmt_get_result($PrepareStmt);
                                $countrows = mysqli_num_rows($fetchrows);
                                mysqli_stmt_close($PrepareStmt);
                                mysqli_close($connection);
                                if($countrows > 0)
                                    {   
                                        while($rowdata = mysqli_fetch_row($fetchrows))
                                            {
                                                echo "<ul class='rolldown-list' id='myList'>
                                                <li><label>".$rowdata['0']."&nbsp &nbsp &nbsp &nbsp".$rowdata['1']."&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp". $rowdata['2']."&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp".$rowdata['3']."</label></li></ul>";
                                                echo "<br><br><br>";;
                                            }
                                    }
                                else
                                    {
                                        echo"<h1>hello</h1>";
                                        header("location: /PHP Programs/EVALUATION 2/QUES 2/recordsfetch.php?error=nodata");
                                        exit();                                     
                                    }
                            }
                        else
                            {
                                header("location: /PHP Programs/EVALUATION 2/QUES 2/recordsfetch.php?error=internaldatabaseerror");
                                exit();        
                            }
                    }
            }
        else
            {
                header("location: /PHP Programs/EVALUATION 2/QUES 2/recordsfetch.php?error=internalservererror");
                exit();
            }
    ?>
  <button id="btnReload"><form  action="/PHP Programs/EVALUATION 2/QUES 2/logout.php" method="POST">
    <input class="btn btn--stripe" type="submit" name="logout" value="LOG ME OUT">
    </form></button>  
</body>
</html>
