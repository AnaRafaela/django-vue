import Vue from 'vue'
import Router from 'vue-router'
 
import Index from '@/components/Index'
import Contact from '@/components/Register'
import About from '@/components/ShopCart'
import Categoria from '@/components/Categoria'
import Login from '@/views/Login'
import Logout from '@/views/Logout'
import Pay from '@/components/Pay'
import ProductCategory from '@/components/ProductCategory'

 
Vue.use(Router)
 
export default new Router({
  mode:'history',
  hash: false,
 routes: [
   {
     path: '/',
     name: 'Index',
     component: Index
   },
   {
       path: '/Register',
       name: 'Register',
       component: Contact
   },
   {
       path: '/ShopCart',
       name: 'ShopCart',
       component: About
   },
   {
    path: '/Categoria',
    name: 'Categoria',
    component: Categoria
  },
  {
    path: '/Pay',
    name: 'Pay',
    component: Pay
  },
  {
    path: '/Login',
    name: 'Login',
    component: Login
  },
  {
    path: '/Logout',
    name: 'Logout',
    component: Logout
  },
  {
    path: '/ProductCategory/:id',
    name: 'ProductCategory',
    component: ProductCategory
  },
  ]
})