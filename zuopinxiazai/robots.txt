<!--作者：赵博凯-->
<!--语言：HTML-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>robots.txt生成器</title>
  <style>
      input{background-color: lightblue}
      button{background-color: darksalmon}
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
  </style>
</head>
<body style="background-color: purple; font-family: Arial, sans-serif; text-align: center;">
<h1>欢迎来到robots.txt生成器，你可以生成属于你自己的robots</h1>
<p>开始</p>
<button onclick="add()">添加</button>
<button onclick="enter()">生成</button>
<br>
<label for="Sitemap">Sitemap（站点地图）（换行分隔）（要输入完整链接）<br>
  <textarea cols="60" rows="10" id="Sitemap"></textarea>
</label>
<div id="div" style="background-color: yellow;text-align: left;color: lightseagreen;font-size: 20px">
  <label>请求头（*为所有爬虫引擎）：<input id="User-Agent1" value="*"></label>
  <br>
  <label>允许爬取的内容（“/”代表允许爬取所有）：<input id="Allow1"></label>
  <br>
  <label>禁止爬取的内容（“/”代码禁止爬取所有）：<input id="Disallow1"></label>
  <br>
  <label>访问延迟（为整数）/秒：<input id="Crawl-delay1"></label>
</div>
<label for="robots">生成结果</label>
<br>
<textarea id="robots" style="background-color: cornflowerblue" rows="20" cols="80"></textarea>
<script>
  let i = 1;
  const div = document.getElementById("div");
  const text=['请求头（*为所有爬虫引擎）：', '允许爬取的内容（“/”代表允许爬取所有）：', '禁止爬取的内容（“/”代码禁止爬取所有）：', '访问延迟（为整数）/秒：：'];
  const id=['User-Agent', 'Allow', 'Disallow', 'Crawl-delay'];
  function add() {
    i+=1;
    let hr=document.createElement("hr");
    div.appendChild(hr);
    for(let j=0;j<text.length;j++)
    {
      let label = document.createElement("label");
      label.textContent = text[j];
      let input = document.createElement("input");
      input.id = id[j]+String(i);
      label.appendChild(input);
      div.appendChild(label);
      let br=document.createElement("br");
      div.appendChild(br);
    }
  }
  function enter() {
    let robots= "";
    robots+="#由“https://zhaonokai341.github.io/zuopin/robots”\n"
    for(let j=1;j<=i;j++){
      if(document.getElementById("User-Agent"+String(j)).value) {
        robots += "User-Agent: " + document.getElementById("User-Agent" + String(j)).value + "\n";
      }
      if(document.getElementById("Allow"+String(j)).value) {
        robots += "Allow: " + document.getElementById("Allow" + String(j)).value + "\n";
      }
      if(document.getElementById("Disallow"+String(j)).value) {
        robots += "Disallow: " + document.getElementById("Disallow" + String(j)).value + "\n";
      }
      if(document.getElementById("Crawl-delay"+String(j)).value) {
        robots += "Crawl-delay: " + document.getElementById("Crawl-delay" + String(j)).value + "\n";
      }
      robots+="\n"
    }
    let Sitemap=document.getElementById("Sitemap").value;
    if(Sitemap) {
      Sitemap = Sitemap.split("\n");
      for (let j = 0; j < Sitemap.length; j++) {
        robots += "Sitemap: " + Sitemap[j] + "\n";
      }
      document.getElementById("robots").value = robots;
      console.log(robots);
    }
  }
</script>
</body>
</html>
