import httpserver from './https'
import baseurl from './baseurl';
import qs from 'qs';

const buurl = (process.env.NODE_ENV === 'production')? baseurl.mock : baseurl.dev

const swtcAPI = {

//     1 获取服务器列表
// HTTP请求
// GET https://jccdex.cn/static/config/jc_config.json
// 请求参数: 无
// 返回参数: 所有服务器配置信息，配置说明如下:
// exHosts：交易服务器列表，默认端口为80
// infoHosts：信息服务器列表，默认端口为80
    getconfig() {
        return httpserver.get(`jcc/static/config/jc_config.json`);
    },

    getDepth(params){
        // console.log(params)
        // return httpserver.get('https://explorer.jccdex.cn/wallet/trans/:uuid?p=0&s=10&t=Receive,Send&w=jNC1n9WeniAErRAatYwarRUPCybozPqioW');
        return httpserver.get('https://explorer.jccdex.cn/wallet/trans/:uuid?${p}/${s}/${t}/${w}',{params:params});
    },
    getAlltickers(){
        return httpserver.get(`${baseurl.mock}/api/swtc/getAlltickers`);
    },
    getInfos(){
        return httpserver.get(`${baseurl.mock}/api/swtc/getInfos`);
    }
 
}

export default swtcAPI;
