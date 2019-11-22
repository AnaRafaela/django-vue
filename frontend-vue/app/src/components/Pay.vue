<template>
  <section class="container">
    <h1>Método de pagamento</h1>
    <button v-if="authenticated">Logout</button>
  </section>
</template>

<script>
import router from "../router";

export default {
  name: "Pay",
  data() {
    return {
      authenticated: false
    };
  },
  mounted() {
    this.checkAuthenticated();
  },
  methods: {
    checkAuthenticated() {
      this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/Login");
      } else {
        this.authenticated = true;
      }
    }
  }
};
</script>
