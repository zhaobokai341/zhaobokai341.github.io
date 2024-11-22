<html>
<head>
    <meta charset="utf-8">
    <title>GitHub</title>
    <style>
        body{
            margin: 60px;
            width: 100%;
            height: 100vh;
            background: linear-gradient(-45deg,yellow,blue,green,purple,black);
            background-size: 200% 200%;
            animation: gradient 8s ease infinite;
        }

        @keyframes gradient {
            0% {
                background-position: 0 12%;
            }

            50% {
                background-position: 100% 100%;
            }

            100% {
                background-position: 0 12%;
            }
        }
        h1{
              text-align:center;
              font-size: 40px;
              color:white;
              text-shadow:0px 1px 0px #c0c0c0,
                 0px 2px 0px #b0b0b0,
                 0px 3px 0px #a0a0a0,
                 0px 4px 0px #909090,
                 0px 5px 10px rgba(0, 0, 0, .9);
                    }
        a{color:pink;}
        p{color:yellow}
    </style>
</head>
<body>
<h1>No Python at ... 错误解决（赵博凯）（2024/11/10）</h1>
<p>本网站只是简单介绍</p>
<p>它主要出现在PyCharm，意思是解释器错误，并且错误代码为103</p>
<p>我曾经也遇到。以下是解决方案</p>
<p>第1.一般错误都会指向指定的路径，快去看看路径是否存在</p>
<p>第2.如果不行，大概率是重要文件丢失，新建一个项目试试。</p>
</body>
</html>
