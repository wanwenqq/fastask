<template>
  <div>
    <van-button type="primary" @click="onCreateSWTC()">创建</van-button>
    <van-button type="primary" @click="onrequestOrderBook()">挂单列表</van-button>
  </div>
</template>

<script>
//创建Wallet对象
var jlib = require("@swtc/lib");
var Wallet = jlib.Wallet;
var Remote = jlib.Remote;
//测试环境
// var remote = new Remote({
//   server: "ws://ts5.jingtum.com:5030",
//   issuer: "jBciDE8Q3uJjf111VeiUNM775AMKHEbBLS",
// });
// 生产环境
var remote = new Remote();
import { Button } from "vant";

export default {
  name: "home",
  components: {
    [Button.name]: Button,
  },
  data() {
    return {
      title: "home",
      address: "",
    };
  },
  mounted() {},
  methods: {
    onCreateSWTC() {
      var w1 = Wallet.generate();
      this.address = w1["address"];
      console.log(w1["address"]);
    },
    onrequestOrderBook() {
      remote
        .connectPromise()
        .then(async () => {
          let options = {
            limit: 10,
            pays: remote.makeCurrency(),
            gets: remote.makeCurrency("CNY"),
          };
          let req = remote.requestOrderBook(options);
          let response = await req.submitPromise();
          console.log(response);
          remote.disconnect();
        })
        .catch(console.error);
    },
  },
};
</script>

<style lang="less">
</style>