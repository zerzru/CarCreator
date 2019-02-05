<?php
    session_start();
    date_default_timezone_get('America/New_York');

    $suffix = $_GET['lang'];
    $username = $_GET['user'];
    if(empty($suffix) or $suffix!='en' && $suffix!='ru' && $suffix!='jp') {
        $suffix = 'en';
    }

    $settings = parse_ini_file('config.ini');
    $texts = parse_ini_file("config_$suffix.ini");
    $MainPageTitle = $texts['MainPageTitle'];
    $LoginPageTitle = $texts['LoginPageTitle'];
    $EditPageTitle = $texts['EditPageTitle'];
    $ProfilePageTitle = $texts['ProfilePageTitle'];
    $RegistrationPageTitle = $texts['RegistrationPageTitle'];

    $MainPageLinkName = $texts['MainPageLinkName'];
    $DownloadPageNameLink = $texts['DownloadPageNameLink'];
    $UpdatesPageNameLink = $texts['UpdatesPageNameLink'];
    $LoginPageNameLink = $texts['LoginPageNameLink'];
    $RegistrationPageNameLink = $texts['RegistrationPageNameLink'];
    $LogoutPageLinkName = $texts['LogoutPageLinkName'];

    $login_placeholder = $texts['login_placeholder'];
    $email_placeholder = $texts['email_placeholder'];
    $cquestion_placeholder = $texts['cquestion_placeholder'];
    $password_placeholder = $texts['password_placeholder'];
    $r_password_placeholder = $texts['r_password_placeholder'];

    $DefaultRank = $texts['DefaultRank'];
    $DefaultStatus = $texts['DefaultStatus'];

    $EditButtonText = $texts['EditButtonText'];
    $SaveButtonText = $texts['SaveButtonText'];

    $achievement_title_get100 = $texts['achievement_title_get100'];

    $achievesfolder = $settings['achievesfolder'];

    $link = mysqli_connect($settings['host'], $settings['user'], $settings['password'], $settings['database']) or die("".mysqli_error($link));
    mysql_connect($settings['host'], $settings['user'], $settings['password']) or die('Something went wrong');
    mysql_select_db($settings['database']) or die('Something went wrong');

    function check_os() {
        $uagent=$_SERVER['HTTP_USER_AGENT'];
        if(preg_match('/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i', $uagent)||preg_match('/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i',substr($uagent, 0, 4))) {
            echo '<link rel="stylesheet" type="text/css" href="lib/scripts/mstyle.css">';
        } else {
            echo '<link rel="stylesheet" type="text/css" href="lib/scripts/style.css">';
        }
    };

    function show_menu() {
        global $MainPageTitle, $MainPageLinkName, $DownloadPageNameLink, $UpdatesPageNameLink, $LoginPageNameLink, $RegistrationPageNameLink, $LogoutPageLinkName, $suffix;
        echo "<li><a href='index?lang=$suffix'>$MainPageLinkName</a></li>
        <li><a href='download?lang=$suffix'>$DownloadPageNameLink</a></li>
        <li><a href='updates?lang=$suffix'>$UpdatesPageNameLink</a></li>
        <li><a href='https://github.com/ZerZru/CarCreator/'>GitHub</a></li>";

        if(empty($_SESSION['login'])) {
            echo '<li><a href="login?lang='.$suffix.'">'.$LoginPageNameLink.'</a></li>';
            echo '<li><a href="registration?lang='.$suffix.'">'.$RegistrationPageNameLink.'</a></li>';
        } else {
            echo '<li><a href="profile?user='.$_SESSION["login"].'&lang='.$suffix.'">'.$_SESSION["login"].'</a></li>';
            echo '<li><a href="logout?lang='.$suffix.'">'.$LogoutPageLinkName.'</a></li>';
        }

        if($suffix=='en') {
            echo '<a href="?lang=jp"><img class="language-changer" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/1280px-Flag_of_Japan.svg.png"></a>';
            echo '<a href="?lang=ru"><img class="language-changer" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Russia.svg/1280px-Flag_of_Russia.svg.png"></a>';
        } else if($suffix=='ru') {
            echo '<a href="?lang=jp"><img class="language-changer" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/1280px-Flag_of_Japan.svg.png"></a>';
            echo '<a href="?lang=en"><img class="language-changer" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Flag_of_the_United_States_%28Pantone%29.svg/1920px-Flag_of_the_United_States_%28Pantone%29.svg.png"></a>';
        } else if($suffix=='jp') {
            echo '<a href="?lang=ru"><img class="language-changer" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Russia.svg/1280px-Flag_of_Russia.svg.png"></a>';
            echo '<a href="?lang=en"><img class="language-changer" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Flag_of_the_United_States_%28Pantone%29.svg/1920px-Flag_of_the_United_States_%28Pantone%29.svg.png"></a>';
        }
    };

    if(isset($_POST['l_submit'])) {
        global $suffix;
        $login = $_POST['login'];
        $password = $_POST['password'];

        $result = mysql_query("SELECT * FROM users WHERE login='$login'");
        $myrow = mysql_fetch_array($result);
        if(empty($myrow['password'])) {
            exit ("Извините, введённый вами логин или пароль неверный.");
        } else {
            if($myrow['password']==$password) {
                $_SESSION['login']=$myrow['login']; 
                $_SESSION['id']=$myrow['id'];
                header("Location: index?lang=$suffix");
            } else {
                header("Location: login?lang=$suffix");
            }
        }
    };

    if(isset($_POST['r_submit'])) {
        global $suffix;
        $login = $_POST['login'];
        $password = $_POST['password'];
        $r_password = $_POST['r_password'];
        $email = $_POST['email'];
        $cquestion = $_POST['cquestion'];
        $ip = getUserIP();
        $date = date('d.m.Y H:i:s');

        $result = mysql_query("SELECT * FROM users WHERE login='$login'");
        $myrow = mysql_fetch_assoc($result);
        if(!empty($myrow['login'])) {
            echo 'Такой пользователь уже существует';
        } else {
            if($r_password != $password) {
                echo 'Пароли не совпадают';
            } else {
                $result = mysql_query("INSERT INTO users(login, password, email, avatar, rank, status, cquestion, ip, date) VALUES('$login', '$password', '$email', 'avatar-default.jpg', '$DefaultRank', '$DefaultStatus', '$cquestion', '$ip', '$date')");
                $result2 = mysql_query("SELECT * FROM users WHERE login='$login'");
                $myrow2 = mysql_fetch_assoc($result2);
                $_SESSION['login']=$myrow2['login']; 
                $_SESSION['id']=$myrow2['id'];
                header("Location: index?lang=$suffix");
            }
        }
    };

    if(isset($_POST['e_submit'])) {
        global $suffix;
        $uploaddir = 'lib/images/avatars/';
        $apend=date('YmdHis').rand(100,1000).'.jpg';  
        $uploadfile = "$uploaddir$apend";
        if(empty($_FILES['userfile']['type'])) {
            echo '';
        } else {
            echo 'фвфдылвдж';
            if(($_FILES['userfile']['type'] == 'image/gif' || $_FILES['userfile']['type'] == 'image/jpeg' || $_FILES['userfile']['type'] == 'image/png') && ($_FILES['userfile']['size'] != 0 and $_FILES['userfile']['size']<=512000)) {
                if(move_uploaded_file($_FILES['userfile']['tmp_name'], $uploadfile)) {
                    $size = getimagesize($uploadfile); 
                    if ($size[0] < 501 && $size[1]<501) {
                        $request = mysql_query("UPDATE users SET `avatar`='$apend' WHERE login='{$_SESSION['login']}'");
                        header("Location: profile?user={$_SESSION['login']}&lang=$suffix");
                    } else {
                        exit("Загружаемое изображение превышает допустимые нормы (ширина не более - 500; высота не более 500)");
                        unlink($uploadfile);
                    } 
                } else {
                    exit("Файл не загружен, вернитеcь и попробуйте ещё раз");
                }
            } else {
                exit("Размер файла не должен превышать 512Кб или вы загрузили не картинку");
            }
        }
        if(!empty($_POST['status'])) {
            $request = mysql_query("UPDATE users SET status='{$_POST['status']}' WHERE login='{$_SESSION['login']}'");
        }
    };

    function get_user_info($user, $show='true') {
        global $suffix, $EditButtonText;
        $result = mysql_query("SELECT * FROM users WHERE login='$user'");
        $myrow = mysql_fetch_assoc($result);
        $userrank = $myrow['rank'];
        $userstatus = $myrow['status'];
        $avatar = $myrow['avatar'];

        if($show=='true') {
            echo "<img class='avatar_image' src='lib/images/avatars/$avatar'>
                  <p><span class='username'>$user - $userrank</span> <br>
                  <span class='status'>$userstatus</span></p>";
            if($user==$_SESSION['login']) {
                echo "<br><br><br><br><br><br><br><a class='edit_button' href='edit?lang=$suffix'><button>$EditButtonText</button></a>";
            } else {
                echo '';
            }
        }

        function edit_status($user) {
            $result = mysql_query("SELECT * FROM users WHERE login='$user'");
            $myrow=mysql_fetch_assoc($result);
            echo "<input name='status' type='text' style='width:200px' placeholder='{$myrow['status']}'>";
        };

        function get_achievements($user) {
            global $achievesfolder;
            $result = mysql_query("SELECT * FROM users WHERE login='$user'");
            $myrow=mysql_fetch_assoc($result);
            if($myrow['get100']=='yes') {
                echo "<img class='achievement' src='$achievesfolder/get100.png' title='$achievement_title_get100'>";
            } else {
                echo "<img class='achievement' src='$achievesfolder/get100-empty.png'>";
            }
            if($myrow['get1000']=='yes') {
                echo "<img src='lib/images/achievements/get1000.png'>";
            } else {
                echo '';
            }
            if($myrow['get10000']=='yes') {
                echo "<img src='lib/images/achievements/get10000.png'>";
            } else {
                echo '';
            }
            if($myrow['get100000']=='yes') {
                echo "<img src='lib/images/achievements/get100000.png'>";
            } else {
                echo '';
            }
            if($myrow['get1000000']=='yes') {
                echo "<img src='lib/images/achievements/get1000000.png'>";
            } else {
                echo '';
            }
        };
    };

    function getUserIP() {
        $client = @$_SERVER['HTTP_CLIENT_IP'];
        $forward = @$_SERVER['HTTP_X_FORWARDED_FOR'];
        $remote = $_SERVER['REMOTE_ADDR'];

        if(filter_var($client, FILTER_VALIDATE_IP)) {
            $ip = $client;
        } else if(filter_var($forward, FILTER_VALIDATE_IP)) {
            $ip = $forward;
        } else {
            $ip = $remote;
        }
        return $ip;
    };
?>