<?php
function read_file($file) {
        $jsonContent = file_get_contents($file);
        $data = json_decode($jsonContent, true, 512, JSON_UNESCAPED_UNICODE);
        header('Content-Type: application/json');
        echo json_encode($data, JSON_UNESCAPED_UNICODE);
}
if ($_SERVER['REQUEST_METHOD'] == 'GET') {
    header('Access-Control-Allow-Origin: *');
    $type = $_GET['type'];
    $id = $_GET['id'];
    if ($type){
        switch ($type) {
            case 'github':
                $file = 'github.json';
                read_file($file);
                break;
            case 'htmlcssjs':
                $file = 'HTML&CSS&JS.json';
                read_file($file);
                break;
            case 'python':
                $file = 'python.json';
                read_file($file);
                break;
            case 'other':
                $file = 'other.json';
                read_file($file);
                break;
            default:
                header('Content-Type: application/json');
                echo json_encode(array('error' => 'Invalid type'));
        }
    } elseif ($id) {
        $file = 'content/' . $id . '.md';
        $content = file_get_contents($file);
        $json = Array('diary' => Array('content' => $content));
        header('Content-Type: application/json');
        $json = json_encode($json, JSON_UNESCAPED_UNICODE);
        echo $json;
    } else {
        header('Content-Type: application/json');
        echo json_encode(array('error' => 'Invalid type'));
    }
} else {
    header('Content-Type: application/json');
    echo json_encode(array('error' => sprintf('Invalid request method: %s', $_SERVER['REQUEST_METHOD'])));
}
?>