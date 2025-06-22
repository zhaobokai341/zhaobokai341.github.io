function changeTheme(theme) {
    // 移除所有主题相关的样式表
    const themeStylesheets = document.querySelectorAll('link[rel="stylesheet"]');
    themeStylesheets.forEach(stylesheet => {
        // 检查是否是主题样式表（通过路径判断）
        if (stylesheet.href.includes('/style/') && 
            (stylesheet.href.includes('rainbow.css') || 
             stylesheet.href.includes('white.css') || 
             stylesheet.href.includes('dark.css') || 
             stylesheet.href.includes('zhaobokai.css'))) {
            stylesheet.parentNode.removeChild(stylesheet);
        }
    });
    
    // 创建并添加新的主题样式表
    let link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = theme;
    
    // 将新样式表添加到head的开头，确保它的优先级
    const head = document.head;
    head.insertBefore(link, head.firstChild);
}


let html = `<div id="theme-menu">
    <label for="theme">选择主题：</label>
    <select id="theme" onchange="changeTheme(this.value)">
        <option value="/style/rainbow.css">彩虹色</option>
        <option value="/style/white.css">亮色</option>
        <option value="/style/dark.css">暗色</option>
        <option value="/style/zhaobokai.css">赵博凯</option>
    </select>
</div>`


body = document.body;
body.insertAdjacentHTML('afterbegin', html);