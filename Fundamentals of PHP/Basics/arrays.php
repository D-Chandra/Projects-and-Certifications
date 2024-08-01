<?php
//$arr = array('Hello'=>'i','am'=>'Diwanshu chandra','.','2'=>'My age' ,'is::' => 20 );
//$n=0;
//$m=0;
$size = (int)fgets(STDIN);
$arr1 = array($size);
//var_dump($arr);
/*for ($i=0; $i<=2 ; $i++) {
  echo "Enter $i key::"; $key=fgets(STDIN); //we can use (int) or (integer)
  echo "Enter $i value::"; $value=fgets(STDIN);
  $arr1[$n]=$key;
  $arr1[$m]=$value;
  //print_r($arr1[$i]);
  // code...
}*/
//echo $arr1."\n" ;
foreach ($arr1 as $key => $value) {
  echo "Enter $i key::"; $key=fgets(STDIN); 
  echo "Enter $i value::"; $value=fgets(STDIN);
  // code...
}

foreach ($arr1 as $key => $value) {
  echo $key . '=>' .  $value . " \t";
  // code...
}
//var_dump($arr1);
//print_r($arr1);
//echo $arr1;
 ?>
