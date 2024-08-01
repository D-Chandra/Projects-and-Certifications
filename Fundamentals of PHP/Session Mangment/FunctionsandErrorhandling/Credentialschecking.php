
<?php  
    function emptyfields($email,$pwd)
        {
            $result=0;
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

    function admlogin($email,$pwd)
        {
            $conn = mysqli_connect('localhost','root','root','php assignment');
            if(isset($conn))
                {
                    $sqlquery = "Select * from admin_ids where Email=?;";
                    $PrepareStmt = mysqli_stmt_init($conn);
                    if(!mysqli_stmt_prepare($PrepareStmt,$sqlquery))
                        {
                            header("Location: ../QUES 2/adminlogin.php?error=internalservererror");
                            mysqli_stmt_close($PrepareStmt);
                            mysqli_close($conn);
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
                                                    // $_SESSION['userid'] = $maindata["UID"];
                                                    $_SESSION['whois'] = "Administrative";
                                                    header("location: ../QUES 2/recordsfetch.php");
                                                    mysqli_stmt_close($PrepareStmt);
                                                    mysqli_close($conn);
                                                    exit();
                                                }
                                            else
                                                {
                                                    header("location: ../QUES 2/adminlogin.php?error=wrongpasswd");
                                                    mysqli_stmt_close($PrepareStmt);
                                                    mysqli_close($conn);
                                                    exit();
                                                }
                                        }
                                    else
                                        {
                                            header("location: ../QUES 2/adminlogin.php?error=Usernotregistered");
                                            mysqli_stmt_close($PrepareStmt);
                                            mysqli_close($conn);
                                            exit();
                                        }
                                    mysqli_stmt_close($PrepareStmt);
                                }
                            else
                                {
                                    header("location: ../QUES 2/adminlogin.php?error=internaldatabaseError");
                                    mysqli_stmt_close($PrepareStmt);
                                    mysqli_close($conn);
                                    exit();
                                }
                            
                        }
                }
            else
                {
                    header("location: ../QUES 2/adminlogin.php?error=internalservererror");
                    exit();
                }
        }

    function emptyfieldsreg($date,$name,$email,$phone)
        {
            $result=0;
            if(empty($date) or empty($name) or empty($email) or empty($phone) )
                {
                    $result = false;
                }
            else
                {
                    $result = true;
                }
            return $result;
        }
    function emailcheck($email)
        {
            $result=0;
            if(!filter_var($email,FILTER_VALIDATE_EMAIL))
                {
                    $result= false;
                }
            else
                {
                    $result = true;
                }
            return $result;
        }
    function emailexists($email)
        {   
            $result=0;
            $connection = mysqli_connect('localhost','root','root','php assignment');
            if(isset($connection))
                {
                    $sqlquery = "Select * from customer_visits where email=?;";
                    $PrepareStmt = mysqli_stmt_init($connection);
                    if(mysqli_stmt_prepare($PrepareStmt,$sqlquery))
                        {
                            $fetchrows = mysqli_stmt_get_result($PrepareStmt);
                            if($fetchrows)
                                {
                                    $result = false;
                                    mysqli_stmt_close($PrepareStmt);
                                    mysqli_close($connection);
                                    return $result;
                                }
                        }
                    else
                        {
                            header("Location: ../QUES 2/register.php?error=internalservererror");
                            mysqli_stmt_close($PrepareStmt);
                            mysqli_close($connection);
                            exit();
                        }
                }
            else
                {
                    header("location: /PHP Programs/EVALUATION 2/QUES 2/register.php?error=internalservererror");
                    mysqli_close($connection);
                    exit();
                }
        }

    function startregistering($date,$name,$email,$phone)
        {
            $conn = mysqli_connect('localhost','root','root','php assignment');
            if(isset($conn))
                {
                    $Insertionquery = "Insert into customer_visits (date, name, email, phone_no) values (?, ?, ?, ?);";
                    $InsertionStmt = mysqli_stmt_init($conn);
                    if(mysqli_stmt_prepare($InsertionStmt,$Insertionquery))
                        {
                            mysqli_stmt_bind_param($InsertionStmt,"ssss",$date,$name,$email,$phone);
                            if(mysqli_stmt_execute($InsertionStmt))
                                {
                                    header("location: /PHP Programs/EVALUATION 2/QUES 2/register.php?error=noerror");
                                    exit();           
                                }
                        }
                    else
                        {
                            header("location: /PHP Programs/EVALUATION 2/QUES 2/register.php?error=InternalPreperror");
                            exit();  
                        }
                }           
            else
                {
                    header("location: /PHP Programs/EVALUATION 2/QUES 2/register.php?error=internaldatabaseerror");
                    exit();
                }
            
            
        }
?>