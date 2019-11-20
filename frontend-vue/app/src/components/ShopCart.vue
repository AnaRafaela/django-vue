<template>
  <v-container class="grey lighten-5">
    <div>
      <h2>Meu Carrinho de Compras</h2>
      <v-simple-table>
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-center">Produto</th>
              <th class="text-center">Preço</th>
              <th class="text-center">Retirar do carrinho</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in desserts" :key="item.name">
              <td>{{ item.name }}</td>
              <td>{{ item.calories }}</td>
              <td>
                <v-icon color="red">mdi-cart-arrow-up</v-icon>
              </td>
            </tr>
          </tbody>
          <tfoot>
            <th class="text-center">Total</th>
            <td>valor</td>
            <td>
              <v-tooltip top>
                <template v-slot:activator="{ on }">
                  <v-btn v-on="on">
                    <v-icon color="red darken-4">mdi-cart-remove</v-icon>
                  </v-btn>
                </template>
                <span>Esvaziar carrinho</span>
              </v-tooltip>
            </td>
          </tfoot>
        </template>
      </v-simple-table>
    </div>
  </v-container>
</template>

<script>
export default {
  name: "ShopCart", //this is the name of the component
  data() {
    return {
      desserts: [
        {
          name: "Frozen Yogurt",
          calories: 159
        },
        {
          name: "Ice cream sandwich",
          calories: 237
        },
        {
          name: "Eclair",
          calories: 262
        },
        {
          name: "Cupcake",
          calories: 305
        },
        {
          name: "Gingerbread",
          calories: 356
        },
        {
          name: "Jelly bean",
          calories: 375
        },
        {
          name: "Lollipop",
          calories: 392
        },
        {
          name: "Honeycomb",
          calories: 408
        },
        {
          name: "Donut",
          calories: 452
        },
        {
          name: "KitKat",
          calories: 518
        }
      ]
    };
  }
};
</script>
<style>
</style>