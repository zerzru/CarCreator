<?php
    require_once('engine.php');
    if(empty($_SESSION['login'])) {
        header('Location: index');
    };
?>

<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>CarCreator | <?php echo $ProfilePageTitle.$username; ?></title>
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
        <div class="userpage">
                <?php
                    get_user_info($username);
                    get_user_info.get_achievements($username);
                ?>
        </div>
        <footer>
        </footer>
        <script src="lib/scripts/main.js"></script>
	</body>
</html>