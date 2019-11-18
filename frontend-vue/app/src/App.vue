<template>
  <v-app id="app">
    <Navigation @toggle-drawer="$refs.drawer.drawer = !$refs.drawer.drawer"></Navigation>
    <SideMenu ref="drawer"></SideMenu>
    <v-content>
      <router-view></router-view>
    </v-content>
    <Footer @toggle-drawer="$refs.drawer.drawer = !$refs.drawer.drawer"></Footer>
  </v-app>
</template>

<script>
import Navigation from './components/Navigation'
import SideMenu from "@/components/SideMenu"
import Footer from "@/components/Footer"
export default {

  name: 'app',
  components: {
    'Navigation': Navigation,
    'SideMenu': SideMenu,
    'Footer': Footer,
  }
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>