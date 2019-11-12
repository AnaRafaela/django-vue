import Vue from 'vue'
import Router from 'vue-router'
 
import Index from '@/components/Index'
import Contact from '@/components/Contact'
import About from '@/components/About'
 
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
       path: '/About',
       name: 'About',
       component: About
   }
 ]
})