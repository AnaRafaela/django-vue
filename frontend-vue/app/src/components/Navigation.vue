<template>
<v-app-bar app :clipped-left="$vuetify.breakpoint.lgAndUp" color="black" dark>
    <v-app-bar-nav-icon 
      @click.stop="$emit('toggle-drawer')"
    > </v-app-bar-nav-icon>
    <v-toolbar-title>Casa Bonita</v-toolbar-title>
    <v-spacer></v-spacer>
 <div>
    <nav-item>
      
      <router-link class="spacing" v-for="routes in links" 
      v-bind:key="routes.id"
      :to="`${routes.page}`">
      {{routes.text}}
      <v-list-item-icon>
            <v-icon>{{ routes.icon }}</v-icon>
        </v-list-item-icon>
      </router-link>
    </nav-item>
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
          text: 'Categoria',
          page:'/Categoria'
        },
        {
          id: 1,
          text: 'Contact',
          page:'/Contact',
        },
        {
          id: 2,
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
