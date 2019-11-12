import Vue from 'vue';
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router/index'
import 'vuetify/dist/vuetify.min.css'
import VueSession from 'vue-session'
import Vuelidate from 'vuelidate'

 
Vue.config.performance = true;
Vue.config.productionTip = false;
Vue.use(VueSession)
Vue.use(Vuelidate)

 
new Vue({
  el: "#app",
  router,
  vuetify,
  components: { App },
  render: h => h(App)
})

export const EvenBus = new Vue();
