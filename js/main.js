let css_link_list = [
    'https://zhaobokai341.github.io/style/rainbow.css',
    'https://zhaobokai341.github.io/style/beautify.css',
    'https://zhaobokai341.github.io/style/css_select_options.css',
]

let js_link_list = [
    'https://zhaobokai341.github.io/js/css_select.js'
]


for (let i = 0; i < css_link_list.length; i++) {
    let link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = css_link_list[i];
    document.head.appendChild(link);
}
for (let i = 0; i < js_link_list.length; i++) {
    let script = document.createElement('script');
    script.src = js_link_list[i];
    document.head.appendChild(script);
}
