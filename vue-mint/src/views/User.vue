<template>
  <div class="user">
  </div>
</template>

<script>
import { Button } from "vant";
export default {
  name: "home",
  components: {
    [Button.name]: Button,
  },
  data() {
    return {
      title: "user",
      phone: "18602736776",
      password: "53358861",
      address: "jNC1n9WeniAErRAatYwarRUPCybozPqioW",
      ticker_list:[]
    };
  },
  mounted() {

  },
  methods: {
  },
};
</script>

<style lang="less">
</style>