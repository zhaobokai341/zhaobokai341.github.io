/**
 * diary_api.js - 替代diary_api.php的JavaScript实现
 * 
 * 这个文件使用fetch API来获取JSON和Markdown文件，
 * 实现与原PHP文件相同的功能，但使用纯前端方式。
 */

class DiaryAPI {
    /**
     * 获取指定类型的日记列表
     * @param {string} type - 日记类型 (github, htmlcssjs, python, other)
     * @returns {Promise<Object>} - 返回包含日记列表的Promise，格式为 {diary: Array}
     */
    static async getDiaryList(type) {
        switch (type) {
            case 'github':
                type = 0;
                break;
            case 'HTML&CSS&JS':
                type = 1;
                break;
            case 'python':
                type = 2;
                break;
            case 'other':
                type = 3;
                break;
        }
        try {
            // 获取JSON文件
            const response = await fetch(`/json/diary_json.json`);
            if (!response.ok) {
                throw new Error(`HTTP错误! 状态: ${response.status}`);
            }
            
            // 解析JSON数据
            const data = await response.json();
            
            // 返回与原PHP文件相同格式的数据
            return {
                diary: data['diary'][type]
            };
        } catch (error) {
            console.error('获取日记列表时出错:', error);
            throw error;
        }
    }
    
    /**
     * 获取指定ID的日记内容
     * @param {string} id - 日记ID
     * @returns {Promise<Object>} - 返回包含日记内容的Promise，格式为 {diary: {content: string}}
     */
    static async getDiaryContent(id) {
        try {
            // 获取Markdown文件
            const response = await fetch(`../diary/content/${id}.md`);
            if (!response.ok) {
                throw new Error(`HTTP错误! 状态: ${response.status}`);
            }
            
            // 获取文本内容
            const content = await response.text();
            
            // 返回与原PHP文件相同格式的数据
            return {
                diary: {
                    content: content
                }
            };
        } catch (error) {
            console.error('获取日记内容时出错:', error);
            throw error;
        }
    }
    
    /**
     * 处理URL查询参数并返回相应的数据
     * 这个方法模拟PHP文件的行为，根据URL参数返回不同的数据
     */
    static async handleRequest() {
        // 获取URL查询参数
        const urlParams = new URLSearchParams(window.location.search);
        const type = urlParams.get('type');
        const id = urlParams.get('id');
        
        try {
            // 如果有type参数，返回日记列表
            if (type) {
                const data = await this.getDiaryList(type);
                return data;
            }
            // 如果有id参数，返回日记内容
            else if (id) {
                const content = await this.getDiaryContent(id);
                return content;
            }
            // 如果没有参数，返回错误信息
            else {
                return { error: '缺少必要的参数' };
            }
        } catch (error) {
            return { error: error.message };
        }
    }
    
    /**
     * 初始化API，自动处理当前页面的请求
     * 如果当前页面是通过AJAX加载的，则不会自动处理
     */
    static init() {
        // 检查当前页面是否是直接访问的API页面
        if (window.location.pathname.includes('diary_api')) {
            this.handleRequest().then(result => {
                // 如果结果是对象，转换为JSON字符串
                if (typeof result === 'object') {
                    document.body.innerHTML = `<pre>${JSON.stringify(result, null, 2)}</pre>`;
                } else {
                    // 否则直接显示内容（如Markdown文本）
                    document.body.innerHTML = `<pre>${result}</pre>`;
                }
            });
        }
    }
}

// 导出DiaryAPI类，以便其他文件可以导入使用
if (typeof module !== 'undefined' && module.exports) {
    module.exports = DiaryAPI;
}

// 当页面加载完成时，初始化API
document.addEventListener('DOMContentLoaded', () => {
    DiaryAPI.init();
});
