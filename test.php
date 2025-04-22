<?php
// 检查是否有GET参数
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    // 获取GET参数
    header('Access-Control-Allow-Origin: *');
    $param1 = isset($_GET['param1']) ? $_GET['param1'] : 'default_value';
    $param2 = isset($_GET['param2']) ? $_GET['param2'] : 'default_value';

    // 处理参数
    // 这里只是一个示例，你可以根据需要处理参数
    $response = [
        'param1' => $param1,
        'param2' => $param2,
        'message' => 'GET request received successfully'
    ];

    // 设置响应头
    header('Content-Type: application/json');

    // 输出JSON响应
    echo json_encode($response);
} else {
    // 如果不是GET请求，返回错误信息
    header('HTTP/1.1 405 Method Not Allowed');
    echo json_encode(['error' => 'Only GET requests are allowed']);
}
?>
