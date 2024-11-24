<?php
    include 'secret.php';
    error_reporting(0);

    $admin_username = "administrateur"; 
    $hashed_password = "61244f6699baf5afc8f95fd50e8fb7f2";
    # One of my friend bypassed my securities, so I added an OTP and hide it in the secret.php file so no one can access it !

    $params = [
        "username" => $_GET['username'] ?? '',
        "password" => $_GET['password'] ?? '',
        "otp" => $_GET['otp'] ?? ''
    ];

    $checks = [
        function($params) {
            if (preg_match("/^.*administrateur.*$/", $params["username"])) {
                return "Accès refusé : Ce nom d'utilisateur est interdit.";
            }
            return true;
        },
        function($params) use ($admin_username) {
            $safe_username = filter_var($params["username"], FILTER_UNSAFE_RAW, FILTER_FLAG_STRIP_LOW|FILTER_FLAG_STRIP_HIGH);
            return $safe_username === $admin_username ? true : "Accès refusé : Vous devez être administrateur.";
        },
        function($params) use ($hashed_password) {
            $user_hash = md5($params["password"]);
            return intval($user_hash) === intval($hashed_password) ? true : "Mot de passe incorrect.";
        },
        function($params) use ($admin_otp) {
            return strcmp($params["otp"], $admin_otp) == 0 ? true : "OTP incorrect.";
        }
    ];

    foreach ($checks as $check) {
        $result = $check($params);
        if ($result !== true) {
            echo "<!-- Le développeur frontend est en vacance, désolé à tous :) -->";
            echo "<p style='color: red; font-weight: bold;'>$result</p>";
            highlight_file(__FILE__);
            exit;
        }
    }
    
    echo "<!-- Le développeur frontend est en vacance, désolé à tous :) -->";
    echo "<h2 style='font-size: 1.5em; color: green;'>Connexion réussie, voici votre flag : " . htmlspecialchars($flag) . "</h2><br><br>";

    highlight_file(__FILE__);
?>