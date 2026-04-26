<?php
session_start();

function require_login(string $redirect = '/login.php'): void {
    if (empty($_SESSION['user_id'])) {
        header("Location: $redirect");
        exit;
    }
}

function is_logged_in(): bool {
    return !empty($_SESSION['user_id']);
}

function logout(): void {
    session_destroy();
    header('Location: /login.php');
    exit;
}
