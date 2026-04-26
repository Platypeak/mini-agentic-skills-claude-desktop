<?php
// Load .env manually (no composer needed)
$envFile = __DIR__ . '/../../.env';
if (file_exists($envFile)) {
    foreach (file($envFile, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES) as $line) {
        if (str_starts_with(trim($line), '#')) continue;
        [$key, $val] = array_map('trim', explode('=', $line, 2));
        $_ENV[$key] = $val;
    }
}

$host   = $_ENV['DB_HOST']     ?? 'localhost';
$user   = $_ENV['DB_USER']     ?? 'root';
$pass   = $_ENV['DB_PASS']     ?? '';
$dbname = $_ENV['DB_NAME']     ?? '{{DB_NAME}}';

$conn = new mysqli($host, $user, $pass, $dbname);

if ($conn->connect_error) {
    http_response_code(500);
    die(json_encode(['error' => 'Database connection failed']));
}

$conn->set_charset('utf8mb4');
