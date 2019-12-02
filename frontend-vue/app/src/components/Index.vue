<template>
<v-container>
  <div>
      <div class="d-block pa-2 black">
      <v-carousel cycle :show-arrows="false">
        <v-carousel-item v-for="(item,i) in items" :key="i" :src="item.src"></v-carousel-item>
      </v-carousel>
      <h1 class="text-center">Loja Casa Bonita</h1>
</div>
      <v-row no-gutters justify="center">
        <div v-for="produto in produtos" v-bind:key="produto.id">
          <v-col>
            <v-card max-width="300" max-height="350" :elevation="n - 10">
               <v-row
               align="center" 
               justify="end">
                <v-tooltip top>
                  <template v-slot:activator="{ on }">
                    <v-btn class="mx-2" color="#00695C" dark v-on="on" fab small>
                      <v-icon dark>mdi-cart-arrow-down</v-icon>
                    </v-btn>
                  </template>
                  <span>
                    Adicionar ao carrinho e continuar comprando</span>
                </v-tooltip>
               </v-row>
               <a v-bind:href="'/Detail/'+produto.id">
              <v-img
                height="150px"
                width="300px"
                :src="produto.foto"
              >
              </v-img>
               </a>
              <v-card-title>{{produto.nome}}</v-card-title>
              <v-card-subtitle>
                <div class="text-justify">{{produto.descricao}}</div>
              </v-card-subtitle>

              <v-card-text class="text--primary">
                <div
                  class="text-justify font-weight-black"
                  style="font-size: 20px"
                >R$ {{produto.preco}}</div>
              </v-card-text>
              <v-tooltip top>
                <template v-slot:activator="{ on }">
                  <v-btn color="#00695C" dark v-on="on">
                    <v-card-actions>Comprar</v-card-actions>
                  </v-btn>
                </template>
                <span>Comprar e ir para carrinho de compras</span>
              </v-tooltip>
            </v-card>
          </v-col>
        </div>
      </v-row>
    </div>
</v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "Index",
  data() {
    return {
      produtos: [],
      items: [
        {
          src: require("@/assets/foto/logoCasa.jpg")
        },
        {
          src: require("@/assets/foto/cama.jpeg")
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
    this.all();
  },
  methods: {
    all() {
      axios
        .request({
          baseURL: "http://localhost:8000",
          method: "get",
          url: "/loja/produtos/"
        })
        .then(response => {
          this.produtos = response.data;
        });
    },
    }
};
</script>
<style>
</style>