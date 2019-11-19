<template>
  <div>
    <v-container class="grey lighten-5">
      <v-carousel cycle :show-arrows="false">
        <v-carousel-item
          v-for="(item,i) in items"
          :key="i"
          :src="item.src"
        ></v-carousel-item>
      </v-carousel>

      <h1 class="text-center">Loja Casa Bonita</h1>

      <v-row no-gutters justify="center">
        <div v-for="produto in produtos" v-bind:key="produto.id">
          
        <v-col>   
          <v-card max-width="300" max-height="350" :elevation="n - 10">
            <v-img
              height="150px"
              width="300px"
              src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
            ></v-img>
            <v-item>
              {{produto.foto}}
            </v-item>
            <v-card-title>
              {{produto.nome}}
              </v-card-title>
              <v-card-subtitle>
                <div class="text-justify">{{produto.descricao}}</div>
              </v-card-subtitle>

            <v-card-text class="text--primary">

              <div class="text-justify font-weight-black" style="font-size: 20px">
                R$ {{produto.preco}}
                </div>
            </v-card-text>

            <v-card-actions>
              
    <v-btn block color="#00695C" dark>Comprar</v-btn>
  
            </v-card-actions>
          </v-card>
        </v-col>
        </div>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "Index",
  data() {
    return {
      produtos: [],
      items: [
        {
          src: "https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg"
        },
        {
          src: "https://cdn.vuetifyjs.com/images/carousel/sky.jpg"
        },
        {
          src: "https://cdn.vuetifyjs.com/images/carousel/bird.jpg"
        },
        {
          src: "https://cdn.vuetifyjs.com/images/carousel/planet.jpg"
        }
      ]
    };
  },
  created() {
    this.getCategorias(),
        this.all();
        },
  methods: {
  all () {
   axios.request({
    baseURL: 'http://localhost:8000',
    method: 'get',
    url: '/loja/produtos/'
   }).then( response => {
     this.produtos = response.data
   });
  },
  getCategorias() {
        axios
        .request({
          baseURL: "http://localhost:8000",
          method: "get",
          url: "/loja/categorias/"
        })
      },
}
}
</script>
<style>
</style>