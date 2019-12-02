<template>
<v-container>
<h1 class="text-center">Loja Casa Bonita</h1>
      <v-row no-gutters justify="center">
        <div v-for="produto in produtos" v-bind:key="produto.categoria">
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
              <v-img
                height="150px"
                width="300px"
                :src="produto.foto"
              >
              </v-img>
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
</v-container>
</template>
<script>
import axios from "axios";
export default {
  name: "Index",
  data() {
    return {
      produtos: {},
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
          url: `/loja/produtos/get/${this.$route.params.id}/`
        })
        .then(response => {
          this.produtos = response.data;
          //console.log(response)
        });
    },
    }
};
</script>