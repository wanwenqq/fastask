<template>
  <div class="user">
    <van-button type="primary" @click="onGetconfig()">获取服务器列表</van-button>
    <van-button type="primary" @click="onGetdepth()">获取尝试</van-button>
    <van-button type="primary" @click="getUser()">mock获取用户</van-button>
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
    onGetconfig() {
      const that = this;
      this.$api.swtcAPI
        .getconfig()
        .then(function (respone) {
          console.log(this.title);
          console.log(respone);
        })
        .catch(function (e) {
          console.log(e.message);
        });
    },
    async onGetdepth() {
      
      let result =  await this.$api.swtcAPI
        .getDepth({ p: "0", s: "10", t: "Receive,Send", w: this.address });
        console.log(result.data);
    },
    getUser() {
      // this.$api.userAPI
      //   .getUser()
      //   .then(function (respone) {
      //     console.log(respone);
      //   })
      //   .catch(function (e) {
      //     console.log(e.message);
      //   });
    },
  },
};
</script>

<style lang="less">
</style>