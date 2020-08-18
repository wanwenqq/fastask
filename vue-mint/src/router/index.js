import Vue from 'vue'
import VueRouter from 'vue-router'

// 解决两次访问相同路由地址报错
const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
    return originalPush.call(this, location).catch(err => err)
}


import Home from '../views/Home.vue'
Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        redirect: '/main', 
    },
    {
        path: '/',
        name: 'home',
        component: Home, 
        children: [
            {
                path: 'main',
                name: 'main',
                component: () => import(/* webpackChunkName: "list" */ '../views/home/Main.vue')
            },
            {
                path: 'data',
                name: 'data',
                component: () => import(/* webpackChunkName: "list" */ '../views/data/Data.vue')
            },
            {
                path: 'discory',
                name: 'discory',
                component: () => import(/* webpackChunkName: "list" */ '../views/discory/Discory.vue'),
                // children:[
                //     {
                //         path: 'slist',
                //         name: 'slist',
                //         component: () => import(/* webpackChunkName: "list" */ '../views/discory/Slist.vue'),
                //     }
                // ]
            },
            {
                path: 'user',
                name: 'user',
                component: () => import(/* webpackChunkName: "list" */ '../views/user/User.vue'),
                children:[
                    // {
                    //     path: 'usercenter',
                    //     name: 'usercenter',
                    //     component: () => import(/* webpackChunkName: "list" */ '../views/user/Usercenter.vue'),
                    // }
                    
                ]
            },
            {
                path: 'usercenter',
                name: 'usercenter',
                component: () => import(/* webpackChunkName: "list" */ '../views/user/Usercenter.vue'),
            },
            
        ],
    },
    {
        path: '/login',
        name: 'login',
        component: () => import(/* webpackChunkName: "home" */ '../views/Login.vue')
    },
    {
        path: 'slist',
        name: 'slist',
        component: () => import(/* webpackChunkName: "list" */ '../views/discory/Slist.vue'),
    },
    {
        path: 'orderlist',
        name: 'orderlist',
        component: () => import(/* webpackChunkName: "list" */ '../views/discory/Orderlist.vue'),
    },
    {
        path: '*',
        redirect: '/404'
      }
    
    
]

const router = new VueRouter({
    mode: 'history',
    linkExactActiveClass: 'active', //
    routes
})

export default router