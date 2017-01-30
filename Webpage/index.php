<!DOCTYPE html>

<html>
<head>




    <style>

        h1{ text-align:center;}

        h2{ color :blue; text-align:center;}

        h4{ color :blue; text-align :right;}



        #logo {
		width: 200px;
height: 125px;	
            position: absolute;
            left: 20px;
            top: 10px;
            z-index: -1;
		opacity:0.5;
        }


p{text-align: center;padding-top:10px;font-size 1em;color :blue;font-weight:bold;}



    </style>

    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="css/font-awesome.min.css" />
    <link rel="stylesheet" href="css/bootstrap.min.css" />
    <link rel="stylesheet" href="css/style.css" />

</head>


<?php if(isset($_GET["a"])){




   $Time = $_GET["a"];
  // $Secs = $Time/ 1000;

   date_default_timezone_set('US/Eastern');

   $PicTime = date("d-m-Y H:i:s ", $Time);


   //echo date("d-m-Y H:i:s T", $seconds);


   // $b = date("d-m-Y H:i:s ", $a) ;

   $Time1 = $Time + 1.2;
   $Time2 = $Time1 + 1.2;
   $Time3 = $Time2 + 1.2;
   $Time4 = $Time3 + 1.2;

   //$Secs1 = $Time1/ 1000;
   $PicTime1 = date("d-m-Y H:i:s ", $Time1);

   //$Secs2 = $Time2/ 1000;
   $PicTime2 = date("d-m-Y H:i:s ", $Time2);

   //$Secs3 = $Time3/ 1000;
   $PicTime3 = date("d-m-Y H:i:s ", $Time3);

   //$Secs4 = $Time4/ 1000;
   $PicTime4 = date("d-m-Y H:i:s ", $Time4);



 }

   else{ $Time = "There is some problem"; }
   ?>

<body>
    <div class="container-fluid">
        <section id="header">

            <h1> Intrusion Detection System </h1>

            <h2>Welcome to your Vault</h2>

            <img id = "logo" src="Img/Uml.png" alt="Uml_Logo">

            <h3><u>Following Intrusion was detected & captured by the River Hawk </u></h3>
        </section>

    </div>

    <div class="container">
        <section id="photos">
            <div class="row">
                <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                    <section id="intruder">
                        <a href="IntruderImg1.php"><img src="https://s3.amazonaws.com/intrusion-data/101.jpg" alt="Image 1" style="width :100%;height:100 % ;"></a>
                        <p>Picture Captured on : <?php echo $PicTime; ?> </p>
                    </section>
                </div>

                <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                    <section id="intruder">
                        <a href="IntruderImg2.php"><img src="https://s3.amazonaws.com/intrusion-data/102.jpg" alt="Image 2" style="width :100%;height:100 %" ></a>
                        <p>Picture Captured on : <?php echo $PicTime1; ?> </p>
                    </section>
                </div>


                <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                    <section id="intruder">
                        <a href="IntruderImg3.php"><img src="https://s3.amazonaws.com/intrusion-data/103.jpg" alt="Image 3" style="width :100%;height:100 %"></a>
                        <p>Picture Captured on : <?php echo $PicTime2; ?> </p>
                    </section>
                </div>

                <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                    <section id="intruder">
                        <a href="IntruderImg4.php"><img src="https://s3.amazonaws.com/intrusion-data/104.jpg" alt="Image 4" style=" width :100%; height:100 %"></a>
                        <p>Picture Captured on : <?php echo $PicTime3; ?> </p>
                    </section>
                </div>

            </div>
        </section>
    </div>


    <h4><u> Call 911 for an emergency </u></h4>


</body>


</html>