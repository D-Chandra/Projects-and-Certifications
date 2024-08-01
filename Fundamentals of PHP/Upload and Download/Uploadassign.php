<?php
    session_start();
    if(!isset($_POST['fileupload']))
        {
            header("location: Upload.php?error=selectfilesandcourse");
            exit();
        }
    if(!isset($_SESSION['whois']))
        {
            header("location: Teacher.php?error=entercredentials");
            exit();
        }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload</title>
    <link rel="Stylesheet" href="Designandeffects/design.scss">
</head>
<body>
    <?php
        if(isset($_POST['fileupload']))
            {
                $FileStruct = $_FILES['assignment'];
                $FileName = $_FILES['assignment']['name'];
                $FileSize = $_FILES['assignment']['size'];
                $FileTmpName = $_FILES['assignment']['tmp_name'];
                $FileError = $_FILES['assignment']['error'];
                $FileType = $_FILES['assignment']['type'];
                
                //Checking If any Error have Occured
                if( (!isset($_POST['Course'])) and ($FileError !== 0) )
                    {
                        echo "<a href='Upload.html' class='btn btn--stripe btn--large'>Course not selected and Error in File Please select a Proper File</a>" ;
                        die();
                    }
                elseif( (!isset($_POST['Course'])) or ($FileError !== 0))
                    {
                        if(!isset($_POST['Course']))
                            {
                                echo "<a href='Upload.php' class='btn btn--stripe btn--large'>Course Not Selected</a>" ;
                            }

                        if($FileError !== 0)
                            {
                                echo "<a href='Upload.php' class='btn btn--stripe btn--large'>Error in File Please select a Proper File</a>" ;
                            }
                            die();
                    }
                else
                    {
                        //Uploading data to server side starts here   
                        $FileExtFetch = explode('.',$FileName); //fetching extension value
                        $FileExt = strtolower(end($FileExtFetch)); //storing extension in $fileExt
                        $allowedExt = array('jpg','jpeg','png','doc','docx','pdf','txt');
                        if(in_array($FileExt,$allowedExt)) //checking file extension
                            {
                                if($FileSize <= 200000) //checking file size 
                                    {
                                        $FileNewName = $FileName . '_' .  uniqid(). "." .$FileExt;//Generating unique name for saving in Server Side
                                        $FileDestination = 'Assignments/' .$_POST['Course'].'/'. $FileNewName; //Destination on Server Side
                                        $connection = mysqli_connect("localhost","root","root","Php Assignment");
                                        if(!isset($connection))
                                            {
                                                echo "Error Connecting to Database";
                                            }
                                        else
                                            {
                                                $sqlquery = "INSERT INTO assignments (Course_code,File_addr) VALUES (?,?);";
                                                $InitiateStmt = mysqli_stmt_init($connection);//Using prepared statements for security
                                                if(!mysqli_stmt_prepare($InitiateStmt,$sqlquery))
                                                    {
                                                        echo "Server Side Error::Preparing Error";
                                                        die();
                                                    }
                                                else
                                                    {
                                                        mysqli_stmt_bind_param($InitiateStmt,"ss",$_POST['Course'],$FileDestination);
                                                        if(!mysqli_stmt_execute($InitiateStmt))
                                                            {
                                                                echo "Internal Server Error";
                                                                die();
                                                            }
                                                        else
                                                            {
                                                                if(move_uploaded_file($FileTmpName,$FileDestination))
                                                                    {
                                                                        echo "<h1>FILE UPLOADING SUCCESSFUL</h1><br>";
                                                                        echo "<a href='Upload.php' class='btn btn--stripe'>Want to Upload more files</a>";   
                                                                    }
                                                                else
                                                                    {
                                                                        echo '<h1>Server side error occured  ! Try again</h1>';
                                                                    }
                                                        }
                                                    }    
                                            }

                                        
                                       
                                    }
                                else
                                    {
                                        echo "<a href='Upload.php' class='btn btn--stripe btn--large'>Please Look for the Size of File allowed to Upload</a>" ; 
                                    }
                            }
                        else
                            {
                                echo "<a href='Upload.php' class='btn btn--stripe btn--large'>Please Look for the File Types allowed to Upload</a>" ;
                            }

                    }
        } 
    ?>
    
</body>
</html>