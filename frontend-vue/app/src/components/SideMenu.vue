<template>
  <v-navigation-drawer app fixed
    class="app---drawer" 
    v-model="drawer"
    :mini-variant.sync="mini"
    :clipped="$vuetify.breakpoint.lgAndUp"
  >
    <v-divider></v-divider>

    <v-list dense>
      <v-list-item :to="item.endpoint" v-for="item in items" :key="item.title" link>
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title >{{ item.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <template v-if="logged">
        <hr>
        <v-list-item :to="item.endpoint" v-for="item in items_logged" :key="item.title" link>
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title >{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </template>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: "SideMenu",
  data() {
    return {
      drawer: true,
      mini: false,
      user: {},
      items: [        
        { title: "Home", icon: "mdi-store", endpoint: '/' },
        { title: "Área externa", icon: "mdi-grill-outline", endpoint: '/experiments'},
        { title: "Banheiro", icon: "mdi-shower", endpoint: '/user' },
        { title: "Cozinha", icon: "mdi-table-chair", endpoint: '/users' },
        { title: "Quarto", icon: "mdi-hotel", endpoint: '/books'},
        { title: "Sala", icon: "mdi-sofa", endpoint: '/experiments'},
      ],
      items_logged: [
        { title: "Logout", icon: "mdi-logout", endpoint: '/logout'}
      ]
    };
  },
  created () {
    this.getUserDetails()
  },
  methods: {
    getUserDetails() {
      if (this.$session.has('token')){
        this.user.name = null
      }
      else {
        this.user.name = 'None2'
      }
    },
  },
  computed: {
    logged() {
      return this.$session.has('token')
    }
  }
};
</script>
