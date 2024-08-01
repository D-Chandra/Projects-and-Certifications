<?php
  $a=0;
  $b=1;
  echo "$a"," ","$b"," ";
  $num=10;
  for($i=0;$i<=$num;$i++)
    {
      $c=$a+$b;
      echo "$c"," ";
      $a=$b;
      $b=$c;
    }
?>
