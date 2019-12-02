<template>
  <v-navigation-drawer app fixed
    class="app---drawer" 
    v-model="drawer"
    :mini-variant.sync="mini"
    :clipped="$vuetify.breakpoint.lgAndUp"
  >
    <v-divider></v-divider>

    <v-list dense>
      <v-list-item :to="item.endpoint" v-for="item in items" :key="item.id" link>
        <v-list-item-content>
          <a v-bind:href="'/ProductCategory/'+item.id">
            <v-list-item-title >{{ item.nome }}</v-list-item-title>
          </a>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import axios from "axios"
export default {
  name: "SideMenu",
  data() {
    return {
      drawer: true,
     mini: false,
      user: {},
      items: [        
      ],
    };
  },

  created () {
    this.getUserDetails(),
    this.getCategorias()
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
    getCategorias() {
        axios
        .request({
          baseURL: "http://localhost:8000",
          method: "get",
          url: "/loja/categorias/"
        })
        .then(response => {
          this.items = response.data
          //console.log(response)
        });
      },
  },
  computed: {
    logged() {
      return this.$session.has('token')
    }
  }
};
</script>
