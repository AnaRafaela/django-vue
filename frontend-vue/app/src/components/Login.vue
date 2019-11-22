<template>
    <div class='login'>
        <h1>
            login
        </h1>
        <input type="text" placeholder="Email">
        <br>
        <input type="password" placeholder="Senha">
        <br>
        <div class="btn-login">
            <button>Login</button>
        </div>
        <p>
            Você não possui uma conta?
            <a href="">Crie uma conta</a>
        </p>
    </div>
</template>
<script>
export default {
    name: "Login",
    data() {
        return {};
    },
    methods: {}
};
</script>