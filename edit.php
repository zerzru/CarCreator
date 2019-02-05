<?php
    require_once('engine.php');
    if(empty($_SESSION['login'])) {
        header("Location: index?lang=$suffix");
    }
?>

<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>CarCreator | <?php echo $EditPageTitle; ?></title>
        <?php
            check_os();
        ?>
        <link rel="icon" type="image/x-icon" href="lib/images/icon.jpg">
    </head>
    <body>
        <header class="menu">
            <?php
                show_menu();
                get_user_info($_SESSION['login'], 'false');
            ?>
        </header>
        <div class="edit">
            <form action="engine.php" method="post" enctype="multipart/form-data">
                <input name="userfile" type="file">
                <?php get_user_info.edit_status($_SESSION['login']); ?>
                <input name="e_submit" type="submit" value="<?php echo $SaveButtonText; ?>">
            </form>
        </div>
        <footer>
        </footer>
        <script src="lib/scripts/main.js"></script>
    </body>
</html>