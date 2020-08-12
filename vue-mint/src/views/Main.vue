<template>
  <div class="main">
    <div class="main-swipe">
      <van-swipe class="my-swipe" :autoplay="3000" indicator-color="white">
        <van-swipe-item>1</van-swipe-item>
        <van-swipe-item>2</van-swipe-item>
        <van-swipe-item>3</van-swipe-item>
        <van-swipe-item>4</van-swipe-item>
      </van-swipe>
    </div>
    <Textitem></Textitem>
    <van-divider />
    <Orderitem> </Orderitem>
  </div>
</template>

<script type="text/javascript">
import { Swipe, SwipeItem, Divider  } from "vant";
import Textitem from './components/Textitem.vue'
import Orderitem from './components/Orderitem.vue'

export default {
  name: "home",
  components: {
    [Swipe.name]: Swipe,
    [SwipeItem.name]: SwipeItem,
    [Divider.name]: Divider,
    Textitem,
    Orderitem,
  },
  data() {
    return {
      title: "home",
      address: "",
      noticehot: "在代码阅读过程中人们说脏话的频率是衡量",
    };
  },
  mounted() {},
  methods: {
    onCreateSWTC() {
      this.$router.push("login");

      // var w1 = Wallet.generate();
      // this.address = w1["address"];
      // console.log(w1["address"]);
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
.main {
  width: 100%;
  height: 100%;
  &-swiper {
    width: 100%;
  }
}

.my-swipe .van-swipe-item {
  color: #fff;
  font-size: 20px;
  line-height: 150px;
  text-align: center;
  background-color: #39a9ed;
}
</style>