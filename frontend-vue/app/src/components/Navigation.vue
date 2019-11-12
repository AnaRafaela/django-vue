<template>
<v-app-bar app :clipped-left="$vuetify.breakpoint.lgAndUp" color="indigo" dark>
    <v-app-bar-nav-icon 
      @click.stop="$emit('toggle-drawer')"
    > </v-app-bar-nav-icon>
    <v-toolbar-title>Casa Bonita</v-toolbar-title>
    <v-spacer></v-spacer>
 <div>
    <nav-item>
      <router-link class="spacing" v-for="routes in links" 
      v-bind:key="routes.id"
      :to="`${routes.page}`">{{routes.text}}</router-link>
    </nav-item>
    <nav-iten>
     
      <v-icon>mdi-cart-outline</v-icon>
    
    </nav-iten>
  </div>
  </v-app-bar>
</template>

<script>
export default {
  name: 'Navigation',
  props: ['drawer'],
  data() {
    return {
      links: [
        {
          id: 0,
          text: 'Index',
          page:'/Index'
        },
        {
          id: 1,
          text: 'About',
          page:'/About'
        },
        {
          id: 2,
          text: 'Contact',
          page:'/Contact'
        }
      ]
    }
  }


}
</script>
<style>
.spacing {
  margin-right: 10px;
}
</style>
