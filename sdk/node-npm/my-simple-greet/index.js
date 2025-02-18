// 作为SDK 定义简单的对外方法
function greet(name) {
  return `Hello, ${name}!`;
}

// 引入 express 模块
const express = require('express');

// 创建 express 应用
const app = express();

// 定义服务器端口
const PORT = 3000;

// 设置根路由的响应
app.get('/', (req, res) => {
  res.send('Hello, World!');
});

// 服务器监听指定端口
app.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}/`);
});
