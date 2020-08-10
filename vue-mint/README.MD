# 创建流程和步骤 #

1. **初始化工作**

   mkdir webpack-demo && cd webpack-demo   
   npm init -y    
   npm install webpack webpack-cli --save-dev   

2. **创建webpack.config.js和.gitignore文件**

3. 在webpack.config.js中定义entry和output,并根据entry中的app创建js入口文件,如'./src/index.js'

4. 在package.json中添加 "build": "webpack --config webpack.config.js --mode production"

5. 管理输出

   npm install --save-dev html-webpack-plugin   
   npm install clean-webpack-plugin --save-dev   
   新增 html-webpack-plugin 和 clean-webpack-plugin 的plugin说明 并注意clean-webpack-plugin声明需要{}   
   在当前目录创建index.html
   创建dist目录

6. 构建开发环境

   npm install --save-dev webpack-dev-server   
   在webpack.config.js中新增devServer,在webpack.json中新增 start 脚本

7. 处理资源类(css,图片，字体，数据文件等),配置webpack.config.js中的module

   npm i style-loader css-loader less less-loader postcss-loader autoprefixer --save-dev

   npm i mini-css-extract-plugin optimize-css-assets-webpack-plugin  --save-dev

   npm install --save-dev file-loader url-loader

   npm install --save-dev sass-loader node-sass  //可以不需要

8. 处理js,配置webpack.config.js中的module

   npm i @babel/core @babel/preset-env @babel/plugin-proposal-decorators @babel/plugin-proposal-class-properties @babel/plugin-transform-runtime --save-dev

   npm i babel-core babel-loader babel-preset-env babel-preset-stage-3 --save-dev

9. 处理vue

   npm i vue vue-router vuex //生产环境 

   npm i vue-template-compiler vue-loader vue-style-loader --save-dev //开发依赖

   在webpack.confi.gj中新增VueLoaderPlugin plugin和module

10. css,js代码分离,压缩 TODO 

   npm i mini-css-extract-plugin --save-dev
   npm i optimize-css-assets-webpack-plugin --save-dev
   配置webpack.config.js中的plugins，module
   新增postcss.config.js文件

11. 安装 mint-ui

   npm i vant -S

12. 安装axio

   npm install axios  -S

13. es2015环境

   npm i @babel/polyfill --save-dev 

14. **开始vue+vant开发**

    1. 安装babel插件

         npm i babel-plugin-import --save-dev

    2. 新增babel.config.js,参考[vant引入组件](https://youzan.github.io/vant/?source=vuejsorg#/zh-CN/quickstart)
    3. npm install --save @swtc/lib 
    4. webpack.config.js中的devServer中配置proxy,解决跨域问题
