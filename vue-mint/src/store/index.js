import Vue from 'vue'
import Vuex from 'vuex';

import {PUTUSERINFO} from './types.js'
Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        counter:100,
        student:[],
        userinfo:{}
    },
    mutations: {
        increase(state){
            state.counter++
          },
          decrease(state){
            state.counter--
          },
          increateCounter(state,count){
            state.counter += count
          },
          increateStu(state,stu){
            state.student.push(stu)
          },
          [PUTUSERINFO](state,value){
              state.userinfo = value
          }
    },
    actions:{
        //功能同mutations,不过可以做异步操作

    },
    modules:{
        
    },
    getters:{
        getUserinfo(state){
            return state.userinfo
        }
    }

})