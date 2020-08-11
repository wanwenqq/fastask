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
                path: '/main',
                name: 'main',
                component: () => import(/* webpackChunkName: "list" */ '../views/Main.vue')
            },
            {
                path: '/data',
                name: 'data',
                component: () => import(/* webpackChunkName: "list" */ '../views/Data.vue')
            },
            {
                path: '/discory',
                name: 'discory',
                component: () => import(/* webpackChunkName: "list" */ '../views/Discory.vue')
            },
            {
                path: '/user',
                name: 'user',
                component: () => import(/* webpackChunkName: "list" */ '../views/User.vue')
            },
        ],
    },
    {
        path: '/login',
        name: 'login',
        component: () => import(/* webpackChunkName: "home" */ '../views/Login.vue')
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