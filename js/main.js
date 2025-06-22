// 注意：样式表现在直接在HTML文件中引入，不再动态加载
// 这样可以确保主题切换功能正常工作

let js_link_list = [
    '/js/css_select.js'
]

// 只动态加载JavaScript文件
for (let i = 0; i < js_link_list.length; i++) {
    let script = document.createElement('script');
    script.src = js_link_list[i];
    document.head.appendChild(script);
}