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
    <van-search v-model="value" show-action label="地址" placeholder="请输入地址" @search="onSearch">
      <template #action>
        <div @click="onSearch">搜索</div>
      </template>
    </van-search>

    <div class="title">
      <div class="order">排行</div>
      <div class="address">地址</div>
    </div>
    <ul>
      <li class="title" v-for="item in lists" :key="item.id">
        <div class="order">{{item.id}}</div>
        <div class="address item" @click="goPage(item.address)">{{item.address}}</div>
      </li>
    </ul>
  </div>
</template>
<script>
import { NavBar, Divider, Search } from "vant";
export default {
  name: "orderlist",
  components: {
    [NavBar.name]: NavBar,
    [Divider.name]: Divider,
    [Search.name]: Search,
  },
  data() {
    return {
      lists: [],
      backlists:[],
      value:''
    };
  },
  mounted() {
    this.loadOrderlist();
  },
  methods: {
    onSearch(){
      const that = this;
      this.backlists = this.lists;
      let alist = this.lists.find(function(ele){
        return (ele.address === that.value)
        // if(ele.address === that.value){
        //   console.log('找到了')
        //   return
        // }else{
        //   console.log('没有找到')
        // }
      })
      this.lists = []
      if(alist != null){
        this.lists.push(alist)
      }else{
        this.lists = this.backlists
        console.log('没有搜索到')
      }
    },
    onClickLeft() {
      this.$router.back();
    },
    onClickRight() {},
    async loadOrderlist() {
      let result = await this.$api.swtcAPI.getSwtctop();
      // console.log("swtctop", result);
      this.lists = result.data.data.datas;
    },
    goPage(name) {
      // url = 'https://swtcscan.jccdex.cn/#/wallet/?wallet='+name
      // console.log('https://swtcscan.jccdex.cn/#/wallet/?wallet='+name)
      // this.$router.push({url})
      // window.open('https://swtcscan.jccdex.cn/#/wallet/?wallet='+name)
      window.location.href =
        "https://swtcscan.jccdex.cn/#/wallet/?wallet=" + name;
    },
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
      color:#1989fa;
    }
  }
}
</style>