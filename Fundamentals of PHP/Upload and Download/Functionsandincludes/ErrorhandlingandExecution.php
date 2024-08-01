<?php
  session_start();
   
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
?>

<?php
    function emptyfields($email,$pwd)
        {
            $result;
            if(empty($email) or empty($pwd))
                {
                    $result = false;
                }
            else
                {
                    $result = true;
                }
            return $result;
        }

    function Tlogin($email,$pwd)
        {
            $conn = mysqli_connect('localhost','root','root','php assignment');
            if(isset($conn))
                {
                    $sqlquery = "Select * from teach_ids where Email=?;";
                    $PrepareStmt = mysqli_stmt_init($conn);
                    if(!mysqli_stmt_prepare($PrepareStmt,$sqlquery))
                        {
                            header("Location: ../Teacher.php?error=internalservererror");
                            exit();
                        }
                    else
                        {
                            mysqli_stmt_bind_param($PrepareStmt,"s",$email);
                            if(mysqli_stmt_execute($PrepareStmt))
                                {
                                    $resultdata = mysqli_stmt_get_result($PrepareStmt);
                                    if($maindata = mysqli_fetch_assoc($resultdata))
                                        {
                                            $passwdhash = $maindata["password"];
                                            $checkingpasswd = password_verify($pwd,$passwdhash);
                                            if($checkingpasswd === true)
                                                {
                                                    session_start();
                                                    $_SESSION['username'] = $maindata["Name"];
                                                    $_SESSION['userid'] = $maindata["UID"];
                                                    $_SESSION['whois'] = "Teacher";
                                                    header("location: ../Upload.php");
                                                    exit();
                                                }
                                            else
                                                {
                                                    header("location: ../Teacher.php?error=wrongpasswd");
                                                    exit();
                                                }
                                        }
                                    else
                                        {
                                            header("location: ../Teacher.php?error=Usernotregistered");
                                            exit();
                                        }
                                    mysqli_stmt_close($PrepareStmt);
                                }
                            else
                                {
                                    header("location: ../Teacher.php?error=internaldatabaseError");
                                    exit();
                                }
                            
                        }
                }
            else
                {
                    header("Location: ../Teacher.php?error=internalservererror");
                    exit();
                }
        }



        function Slogin($email,$pwd)
        {
            $conn = mysqli_connect('localhost','root','root','php assignment');
            if(isset($conn))
                {
                    $sqlquery = "Select * from stud_ids where Email=?;";
                    $PrepareStmt = mysqli_stmt_init($conn);
                    if(!mysqli_stmt_prepare($PrepareStmt,$sqlquery))
                        {
                            header("Location: ../Student.php?error=internalservererror");
                            exit();
                        }
                    else
                        {
                            mysqli_stmt_bind_param($PrepareStmt,"s",$email);
                            if(mysqli_stmt_execute($PrepareStmt))
                                {
                                    $resultdata = mysqli_stmt_get_result($PrepareStmt);
                                    if($maindata = mysqli_fetch_assoc($resultdata))
                                        {
                                            $passwdhash = $maindata["password"];
                                            $checkingpasswd = password_verify($pwd,$passwdhash);
                                            if($checkingpasswd === true)
                                                {
                                                    session_start();
                                                    $_SESSION['username'] = $maindata["Name"];
                                                    $_SESSION['userid'] = $maindata["UID"];
                                                    $_SESSION['whois'] = "Student";
                                                    header("location: ../download.php");
                                                    exit();
                                                }
                                            else
                                                {
                                                    header("location: ../Student.php?error=wrongpasswd");
                                                    exit();
                                                }
                                        }
                                    else
                                        {
                                            header("location: ../Student.php?error=Usernotregistered");
                                            exit();
                                        }
                                    mysqli_stmt_close($PrepareStmt);
                                }
                            else
                                {
                                    header("location: ../Student.php?error=internaldatabaseError");
                                    exit();
                                }
                            
                        }
                }
            else
                {
                    header("Location: ../Student.php?error=internalservererror");
                    exit();
                }
        }
?>