<?php
  $prod_1=$_GET['per_kg1'] * $_GET['amount_1'];
  $prod_2=$_GET['per_kg2'] * $_GET['amount_2'];
  $prod_3=$_GET['per_kg3'] * $_GET['amount_3'];
  $prod_4=$_GET['per_kg4'] * $_GET['amount_4'];
  $prod_5=$_GET['per_kg5'] * $_GET['amount_5'];
//  echo "<style type='text/css'> table,th,td{border: 2px green;  border-spacing: 0px;} </style>";
  echo "<center>";
//  echo "<Font size ='12'>";
  echo "<table border=10 bordercolor='green' cellspacing='0' width='80%'>";
          echo "<thead>";

            echo "<tr align=center>";
              echo "<th bgcolor='Yellow'>FRUITS</th>";
              echo "<th bgcolor='Yellow'>VALUE/KG</th>";
              echo "<th bgcolor='Yellow'>AMOUNT in KG</th>";
              echo "<th bgcolor='Yellow'>TOTAL COST</th>";
            echo "</tr align=center>";

          echo "</thead>";
          echo "<tbody>";

            echo "<tr align=center>";
              echo "<td>" . $_GET['frst_fru'] . "</td>";
              echo "<td>" . $_GET['per_kg1'] . "</td>";
              echo "<td>" . $_GET['amount_1'] . "</td>";
              echo "<td>$prod_1</td>";
            echo "</tr align=center>";

            echo "<tr align=center>";
            echo "<td>" . $_GET['sec_fru'] . "</td>";
            echo "<td>" . $_GET['per_kg2'] . "</td>";
            echo "<td>" . $_GET['amount_2'] . "</td>";
              echo "<td>$prod_2</td>";
            echo "</tr align=center>";

            echo "<tr align=center>";
            echo "<td>" . $_GET['thrd_fru'] . "</td>";
            echo "<td>" . $_GET['per_kg3'] . "</td>";
            echo "<td>" . $_GET['amount_3'] . "</td>";
              echo "<td>$prod_3</td>";
            echo "</tr align=center>";

            echo "<tr align=center>";
            echo "<td>" . $_GET['frth_fru'] . "</td>";
            echo "<td>" . $_GET['per_kg4'] . "</td>";
            echo "<td>" . $_GET['amount_4'] . "</td>";
              echo "<td>$prod_4</td>";
            echo "</tr align=center>";

            echo "<tr align=center>";
            echo "<td>" . $_GET['fifth_fru'] . "</td>";
            echo "<td>" . $_GET['per_kg5'] . "</td>";
            echo "<td>" . $_GET['amount_5'] . "</td>";
              echo "<td>$prod_5</td>";
            echo "</tr align=center>";

          echo "</tbody>";

  echo "</table";
  echo "</Font>";
  echo "</center>";

 ?>
