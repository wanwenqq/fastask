const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin');
const {
    CleanWebpackPlugin
} = require('clean-webpack-plugin');
const VueLoaderPlugin = require('vue-loader/lib/plugin'); //VueLoaderPlugin,注意路径一定是('vue-loader/lib/plugin')，而不是('vue-loader')，不然会报错
const MiniCssExtractPlugin = require('mini-css-extract-plugin') //这个插件的主要作用是实现css分离
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin') // 这个插件作用是对单独抽离出来的css文件进行压缩。 
const devMode = process.env.NODE_ENV === 'production';



module.exports = {
    entry: {
        app: ['@babel/polyfill','./src/index.js']
    },
    output: {
        filename: '[name].[hash:8].js',
        path: path.resolve(__dirname, 'dist')
    },
    plugins:[
        new VueLoaderPlugin(),
        
        new MiniCssExtractPlugin({
            filename: devMode ? '[name].css' : '[name].[hash:8].css',
            chunkFilename: devMode ? '[id].css' : '[id].[hash:8].css',
        }),
        new OptimizeCSSAssetsPlugin({
            cssProcessor: require('cssnano'), //引入cssnano配置压缩选项
            cssProcessorOptions: {
                discardComments: {
                    removeAll: true
                }
            },
            canPrint: true //是否将插件信息打印到控制台
        }),
        new CleanWebpackPlugin(),
        new HtmlWebpackPlugin({
            title: 'vue-mint',
            template: path.resolve(__dirname, './src/index.html'),
            filename: 'index.html',
            inject: true
        }),
    ],
    devServer: {
        contentBase: './dist',
        port:8080,
        hot: true,
        proxy: {
            '/api': {
              target: 'https://jccdex.cn/',
              pathRewrite: {'^/api' : ''},
              changeOrigin: true,     // target是域名的话，需要这个参数，
              secure: false,          // 设置支持https协议的代理
            },
        }
    },
    module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            },
            {
                test: /\.css$/,
                use: [
                    devMode ? 'style-loader' : MiniCssExtractPlugin.loader, // 把样式都抽离成一个单独的css文件
                    // MiniCssExtractPlugin.loader,
                    "css-loader",
                    "postcss-loader" //给CSS3语法，比如transfrom加上前缀， 需要新建 postcss.config.js 配置文件，需要引用 autoprefixer 这个插件
                ]
            },
            {
                test: /\.less$/,
                use: [
                    // devMode ? 'style-loader' : MiniCssExtractPlugin.loader,
                    // MiniCssExtractPlugin.loader,
                    'style-loader',
                    'css-loader', // 解析 @import这种语法的
                    'postcss-loader',
                    'less-loader' // 把less转变为css
                ]
            },
            {
                test: /\.(png|svg|jpg|gif|JPG|jpeg)$/,
                use: [{
                    loader:'url-loader',
                    options:{
                        esModule: false, // 不加的话会有这种情况 img属性src="[object Module]"
                        limit: 1024 * 10, // 当大于10kb时候，将文件打包到publicPath中 
                        outputPath: 'images', // 将文件打包到哪里
                        publicPath: 'images/',
                        name: '[name].[hash:8].[ext]'
                    }
                }
                ]
            },
            {
                test: /\.js$/, // 找到所有的js文件
                use: {
                    loader: 'babel-loader', // 用babel-loader，需要把ES6转换成ES5语法
                    options: {
                        presets: [ // babel的集合
                            '@babel/preset-env' // @babel/preset-env 就是用来将ES6转化成ES5语法的
                        ],
                        plugins: [
                            ['@babel/plugin-proposal-decorators', {
                                'legacy': true
                            }], // 将ES7语法中的类装饰器转换成ES5语法， legacy 是宽松模式
                            ['@babel/plugin-proposal-class-properties', {
                                'loose': true
                            }], // 将ES7语法中的类转换成ES5语法
                            '@babel/plugin-transform-runtime' //避免编译出现重复
                        ]
                    }
                },
                include: path.resolve(__dirname, 'src'), // 只查找src目录下的js，不找node_modules里面的js
            }
        ]
    }
}