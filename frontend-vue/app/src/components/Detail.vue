<template>
  <v-container>
    <h1>Detail</h1>
    <div v-show="produto">
      <v-card>
        <v-row>
          <v-col>
            <v-img height="400px" width="500px" :src="produto.foto"></v-img>
          </v-col>
          <v-col>
            <v-card class="mx-auto" max-width="400" height="400px">
              <v-card-text>
                <p class="display-1 text--primary">{{produto.nome}}</p>

                <div class="text--primary">{{produto.descricao}}</div>
                
                  <p class="display-1 text--primary">
                    R$ {{produto.preco}}
                  </p>
                <div class="text--primary">Consultar valor do frete</div>
                <v-text-field
            v-model="CEP"
            label="Digite aqui seu CEP"
            required
          ></v-text-field>
              </v-card-text>
              <v-btn color="#00695C" dark v-on="on">
                <v-card-actions>Comprar</v-card-actions>
              </v-btn>
            </v-card>
          </v-col>
        </v-row>
      </v-card>
    </div>
  </v-container>
</template>
<script>
import axios from "axios";
export default {
  name: "Index",
  data() {
    return {
      produto: {}
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
          url: `/loja/produto/get/${this.$route.params.id}/`
        })
        .then(response => {
          this.produto = response.data;
          //console.log(response)
        });
    }
  }
};
</script>