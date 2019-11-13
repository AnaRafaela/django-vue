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
      <h3>gerérica</h3>

      <v-row no-gutters>
        <v-col>
          <v-card class="mx-auto" max-width="400">
            <v-img
              height="200px"
              src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
            ></v-img>

            <v-card-title>Number 10</v-card-title>

            <v-card-text class="text--primary">
              <div>Whitehaven Beach</div>

              <div>Whitsunday Island, Whitsunday Islands</div>
            </v-card-text>

            <v-card-actions>
              <v-btn color="orange" text>Share</v-btn>

              <v-btn color="orange" text>Explore</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "Index",
  data() {
    return {
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
  }
};
</script>
<style>
</style>