<template>
  <div>
    <h1>Contato:</h1>
  <p>
    <ul>
      <li>Email: {{email}}</li>
      <li>Website: {{web}}</li>
    </ul>
  </p>
  </div>
</template>

<script>
export default {
  name: 'Contact',
  data(){
    return {
      email: "lojabonita@email.com",
      web: "lojabonita.com.br"
    }
  }
}
</script>