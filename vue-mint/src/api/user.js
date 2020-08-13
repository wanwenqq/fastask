import httpserver from './https'
import baseurl from './baseurl';
import qs from 'qs';

const userAPI = {
    login(params) {
        console.log(params)
        return httpserver.post(`${baseurl.dev}/login`, params);
    },
    getUser(){
        return httpserver.get(`${baseurl.mock}/api/user`);
    }
}

export default userAPI;
