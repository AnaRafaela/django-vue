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
import eventBus from "../main"
export default {
  name: 'ToolBar',
  props: ['drawer'],
  methods: {
    updateAppDrawer() {
      eventBus.$emit('updateAppDrawer')
    }
  }
}
<style>
.spacing {
  margin-right: 10px;
}
</style>
