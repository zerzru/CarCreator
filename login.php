<?php
    require_once('engine.php');
?>
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>CarCreator | <?php echo $LoginPageTitle; ?></title>
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
            <div class="login">
                <form action="engine?lang=<?php global $suffix; echo $suffix; ?>" method="post">
                    <input name="login" type="text" placeholder="<?php echo $login_placeholder; ?>" required>
                    <input name="password" type="password" placeholder="<?php echo $password_placeholder;?>" required>
                    <input name="l_submit" type="submit" value="<?php echo $LoginPageNameLink; ?>">
                </form>
            </div>
        </center>
        <footer>
        </footer>
        <script src="lib/scripts/main.js"></script>
    </body>
</html>