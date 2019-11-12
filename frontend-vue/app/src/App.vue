<template>
  <div id="app">
    <Navigation @toggle-drawer="$refs.drawer.drawer = !$refs.drawer.drawer"></Navigation>
    <SideMenu ref="drawer"></SideMenu>
    <router-view/>
  </div>
</template>

<script>
import Navigation from './components/Navigation'
import SideMenu from "@/components/SideMenu"
export default {
  name: 'app',
  components: {
    'Navigation': Navigation,
    'SideMenu': SideMenu
  }
}
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