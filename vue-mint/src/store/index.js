import Vue from 'vue'
import Vuex from 'vuex';

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        lists: [],
        acitve:0
    },
    mutations: {
        addItem(state, value) {
            state.lists.push(value);
        },
        addActive(state,value){
            state.acitve = value;
        }
    },
    actions:{
        //功能同mutations,不过可以做异步操作

    },
    modules:{
        
    },
    getters:{
        getActive(state){
            return state.acitve;
        }
    }

})