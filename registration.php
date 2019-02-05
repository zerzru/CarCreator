<?php
	require_once('engine.php');
?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
        <title>CarCreator | <?php echo $RegistrationPageTitle; ?></title>
        <?php
            check_os();
        ?>
        <link rel="icon" type="image/x-icon" href="lib/images/icon.jpg">
	</head>
	<body>
		<header class="menu">
            <?php
                show_menu();
            ?>
        </header>
        <center>
            <div class="registration">
                <form action="engine.php" method="post">
                    <input name="login" type="text" placeholder="<?php echo $login_placeholder; ?>" required>
                    <input name="email" type="email" placeholder="<?php echo $email_placeholder; ?>" required>
                    <input name="cquestion" type="text" placeholder="<?php echo $cquestion_placeholder; ?>" required>
                    <input name="password" type="password" placeholder="<?php echo $password_placeholder; ?>" required>
                    <input name="r_password" type="password" placeholder="<?php echo $r_password_placeholder; ?>" required>
                    <input name="r_submit" type="submit">
                </form>
            </div>
        </center>
        <footer>
        </footer>
        <script src="lib/scripts/main.js"></script>
	</body>
</html>