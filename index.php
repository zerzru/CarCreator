<?
    require_once('engine.php');
?>
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>CarCreator | <?php echo $MainPageTitle; ?></title>
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
            <div class="last_news">
                <script src="lib/scripts/main.js">
                    get_last_news();
                </script>
            </div>
        </center>
        <footer>
        </footer>
        <script src="lib/scripts/main.js"></script>
    </body>
</html>