function changeTheme(theme) {
    // 通过id选择器找到主题样式表
    var link = document.getElementById('theme-style');
    if (link) {
        link.href = theme;
    } else {
        console.error('主题样式表元素未找到');
    }
}

// 检测当前页面是否在子目录中
function getThemePath() {
    // 检查当前URL是否包含子目录
    const isInSubdirectory = window.location.pathname.split('/').length > 2;
    // 如果在子目录中，返回相对路径前缀
    return isInSubdirectory ? '../style/' : './style/';
}

let themePath = getThemePath();
let html = `<div id="theme-menu">
    <label for="theme">选择主题：</label>
    <select id="theme" onchange="changeTheme(this.value)">
        <option value="${themePath}rainbow.css">彩虹色</option>
        <option value="${themePath}white.css">亮色</option>
        <option value="${themePath}dark.css">暗色</option>
        <option value="${themePath}zhaobokai.css">赵博凯</option>
    </select>
</div>`

body = document.body;
body.insertAdjacentHTML('afterbegin', html);