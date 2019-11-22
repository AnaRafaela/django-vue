<template>
  <div class="Register">
    <h1>Crie uma conta:</h1>
  <input type="text" placeholder="Email">
  <br>
  <input type="password" placeholder="Senha">
  <br>
  <button>Salvar</button>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data(){
    return {
      email: "lojabonita@email.com",
      web: "lojabonita.com.br"
    }
  }
}
</script>