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
<h1>炫酷CSS背景，让你的网站栩栩如生（赵博凯）（2024/11/10）</h1>
<p>多种CSS背景样式，复制粘贴即可</p>
<h2>一，动态彩虹背景</h2>
<p>
        body {<br>
            margin: 60px;<br>
            width: 32%;<br>
            height: 48vh;<br>
            background: linear-gradient(-45deg, #dae, #f66, #3c9, #09f, #66f);<br>
            background-size: 200% 200%;<br>
            animation: gradient 8s ease infinite;<br>
        }<br>
<br>
        @keyframes gradient {<br>
            0% {<br>
                background-position: 0 12%;<br>
            }<br>
<br>
            50% {<br>
                background-position: 100% 100%;<br>
            }<br>
<br>
            100% {<br>
                background-position: 0 12%;<br>
            }<br>
        }<br>
</p>
<h1>二，文字逐渐消失效果</h1>
<p>        /* 主要是text-shadow和transform搭配动画的巧妙运用 */<br>
        body {<br>
            width: 600px;<br>
            height: 480px;<br>
            box-sizing: border-box;<br>
            padding: 120px;<br>
            background-color: #000;<br>
            color: transparent;<br>
            display: flex;<br>
        }<br>
<br>
        h3 {<br>
            text-shadow: 0 0 0 #fff;<br>
            animation: smoky 6s infinite;<br>
        }<br>
<br>
        @keyframes smoky {<br>
            60% {<br>
                text-shadow: 0 0 40px #fff;<br>
            }<br>
<br>
            100% {<br>
                text-shadow: 0 0 20px #fff;<br>
                /* 这里是重点 */<br>
                transform: translate3d(15rem, -8rem, 0) rotate(-40deg) skew(70deg) scale(1.5);<br>
                opacity: 0;<br>
            }<br>
        }<br>
<br>
        h3:nth-child(1) {<br>
            animation-delay: 1s;<br>
        }<br>
<br>
        h3:nth-child(2) {<br>
            animation-delay: 1.4s;<br>
        }<br>
<br>
        h3:nth-child(3) {<br>
            animation-delay: 1.8s;<br>
        }<br>
<br>
        h3:nth-child(4) {<br>
            animation-delay: 2.2s;<br>
        }<br>
<br>
        h3:nth-child(5) {<br>
            animation-delay: 2.6s;<br>
        }</p>
<p>然后插上div窗口，然后在弄上h3就行了</p>
<p>三，文字横向伸展模糊淡入淡出效果</p>
<p>CSS</p>
<p>        .enter {<br>
            margin-top: 120px;<br>
            text-align: center;<br>
            /* 贝塞尔曲线动画 */<br>
            animation: enterenter 1.8s infinite cubic-bezier(0.250, 0.460, 0.450, 0.940) both;<br>
        }<br>
<br>
        @keyframes enterenter {<br>
            0% {<br>
                /* 加上文字间距 */<br>
                letter-spacing: 1em;<br>
                /* Z轴变换 */<br>
                transform: translateZ(300px);<br>
                /* filter: blur(); 像素模糊效果 */<br>
                filter: blur(12px);<br>
                /* 透明度也要改变 */<br>
                opacity: 0;<br>
            }<br>
<br>
            100% {<br>
                transform: translateZ(12px);<br>
                filter: blur(0);<br>
                opacity: 1;<br>
            }<br>
        }<br>
<br>
        .leave {<br>
            text-align: center;<br>
            animation: leaveleave 1.8s infinite cubic-bezier(0.250, 0.460, 0.450, 0.940) both;<br>
        }<br>
<br>
        @keyframes leaveleave {<br>
            0% {<br>
                transform: translateZ(0);<br>
                filter: blur(0.01);<br>
            }<br>
<br>
            100% {<br>
                letter-spacing: 1em;<br>
                transform: translateZ(300px);<br>
                filter: blur(12px) opacity(0%);<br>
            }<br>
        }</p>
<p>HTML</p>
<p><br>
<h2 class="enter">我是赵博凯</h2><br>
<br>
<h2 class="leave">你好呀</h2></p>
</body>
</html>
</body>
</html>
