<?php
// 定义JSON文件的路径
$jsonFile = 'diary/github.json';

// 读取JSON文件内容
$jsonContent = file_get_contents($jsonFile);

// 将JSON字符串转换为PHP数组
$data = json_decode($jsonContent, true, 512, JSON_UNESCAPED_UNICODE);
header('Content-Type: application/json');
// 输出数组内容
echo json_encode($data, JSON_UNESCAPED_UNICODE);

?>