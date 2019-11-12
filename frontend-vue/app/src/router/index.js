import Vue from 'vue'
import Router from 'vue-router'
 
import Index from '@/components/Index'
import Contact from '@/components/Contact'
import About from '@/components/ShopCart'
 
Vue.use(Router)
 
export default new Router({
 routes: [
   {
     path: '/',
     name: 'Index',
     component: Index
   },
   {
       path: '/Contact',
       name: 'Contact',
       component: Contact
   },
   {
       path: '/ShopCart',
       name: 'ShopCart',
       component: About
   }
 ]
})