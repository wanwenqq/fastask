<template>
  <div class="orderlist">
    <van-nav-bar
      title="排行榜"
      left-text="返回"
      right-text
      left-arrow
      @click-left="onClickLeft"
      @click-right="onClickRight"
    />
    <div class="title">
      <div class="order">排行</div>
      <div class="address">地址</div>
    </div>
    <hr style="margin:1px 0" />
    <ul>
      <li class="title" v-for="item in lists" :key="item.id">
        <div class="order">{{item.id}}</div>
        <div class="address item" @click="goPage(item.address)">{{item.address}}</div>
      </li>
    </ul>
  </div>
</template>
<script>
import { NavBar, Divider } from "vant";
export default {
  name: "orderlist",
  components: {
    [NavBar.name]: NavBar,
    [Divider.name]: Divider,
  },
  data() {
    return {
      lists: [],
    };
  },
  mounted() {
    this.loadOrderlist();
  },
  methods: {
    onClickLeft() {
      this.$router.back();
    },
    onClickRight() {},
    async loadOrderlist() {
      let result = await this.$api.swtcAPI.getSwtctop();
      console.log("swtctop", result);
      this.lists = result.data.data.datas;
    },
    goPage(name){
      // url = 'https://swtcscan.jccdex.cn/#/wallet/?wallet='+name
      console.log('https://swtcscan.jccdex.cn/#/wallet/?wallet='+name)
      // this.$router.push({url})
      window.open('https://swtcscan.jccdex.cn/#/wallet/?wallet='+name) 
    }
  },
};
</script>

<style lang="less">
.orderlist {
  width: 100%;
  height: 100%;
  .title {
    display: flex;
    flex-direction: row;
    text-align: center;
    line-height: 30px;
    margin: 0 30px;
    box-shadow: 0 1px 0 #d1d9e6;
    .order {
      width: 20%;
      height: 30px;
    }
    .address {
      width: 80%;
      height: 30px;
    }
    .item {
      font-size: 12px;
      text-align: left;
    }
  }
}
</style>