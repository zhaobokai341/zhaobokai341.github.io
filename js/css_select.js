function changeTheme(theme) {
    var link = document.querySelector('link[rel="stylesheet"]');
    link.href = theme;
}

let html = `<div id="theme-menu">
    <label for="theme">选择主题：</label>
    <select id="theme" onchange="changeTheme(this.value)">
        <option value="https://zhaobokai341.github.io/style/rainbow.css">彩虹色</option>
        <option value="https://zhaobokai341.github.io/style/white.css">亮色</option>
        <option value="https://zhaobokai341.github.io/style/dark.css">暗色</option>
    </select>
</div>`

body = document.body;
body.insertAdjacentHTML('afterbegin', html);
