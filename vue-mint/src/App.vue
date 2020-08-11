<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
import { Button } from "vant";
export default {
  name: "app",
  components: {
    [Button.name]: Button,
  },

  methods: {
    goHome() {
      this.$router.push("/login");
    },
  },
};
</script>

<style lang="less">
</style>