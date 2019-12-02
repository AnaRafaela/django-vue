<template>
<v-app-bar app :clipped-left="$vuetify.breakpoint.lgAndUp" color="black" dark>
    <v-app-bar-nav-icon 
      @click.stop="$emit('toggle-drawer')"
    > </v-app-bar-nav-icon>
    <v-toolbar-title >
      <v-btn text large href="/">
      Casa Bonita
      </v-btn>
      </v-toolbar-title>
    <v-spacer></v-spacer>
 <div>
      <v-toolbar-items>
      <v-btn text v-for="routes in links" 
      v-bind:key="routes.id"
      :to="`${routes.page}`">
      <v-btn text>
      {{routes.text}}
      <v-icon>{{ routes.icon }}</v-icon>
      </v-btn> 
      </v-btn>
      </v-toolbar-items>
   
  </div>
  </v-app-bar>
</template>

<script>
import eventBus from "../main"
export default {
  name: 'Navigation',
  props: ['drawer'],
  methods: {
    updateAppDrawer() {
      eventBus.$emit('updateAppDrawer')
    }
  },
  data() {
    return {
      links: [
        {
          id: 0,
          icon:'mdi-account-outline',
          text: 'Minha Conta',
          page:'/Login',
        },
        {
          id: 1,
          icon:'mdi-cart-outline',
          text: 'Carrinho',
          page:'/ShopCart'
        }
      ],
    }
  }

}
</script>
<style>
.spacing {
  margin-right: 10px;
}
</style>
