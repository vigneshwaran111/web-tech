<?php
  
  // servername => localhost
  // username => root
  // password => empty
  // database name => rent_details
  $conn = mysqli_connect("localhost", "root", "", "rent_details");
    
  // Check connection
  if($conn === false){
      die("ERROR: Could not connect");
  }
    
  // Taking all 5 values from the form data
  $book_id =  $_REQUEST['book_id'];
  $name = $_REQUEST['name'];
  $m_number =  $_REQUEST['m_number'];
  $today = $_REQUEST['today'];
  $deadline = $_REQUEST['deadline'];
    

  $sql = "INSERT INTO books_rent  VALUES ('$book_id', 
      '$name','$m_number','$today','$deadline')";
    
  if(mysqli_query($conn, $sql)){
      echo "<h3>data stored in a database successfully."   . " Please browse your localhost php my admin"  . " to view the updated data</h3>"; 

      echo nl2br("\n$first_name\n $last_name\n "
          . "$gender\n $address\n $email");
  } else{
      echo "ERROR: Hush! Sorry $sql. " 
          . mysqli_error($conn);
  }
    
  // Close connection
  mysqli_close($conn);
  ?>