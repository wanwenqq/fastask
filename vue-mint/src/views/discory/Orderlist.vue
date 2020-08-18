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
    <hr style="margin:1px 0"/>
    <ul>
      <li class="title" v-for="item in lists" :key="item.id">
        <div class="order">{{item.id}}</div>
        <div class="address">{{item.name}}</div>
      </li>
    </ul>
  </div>
</template>
<script>
import { NavBar,Divider } from "vant";
export default {
  name: "orderlist",
  components: {
    [NavBar.name]: NavBar,
    [Divider.name]: Divider,
  },
  data() {
    return {
      lists: [
        { id: 1, name: "de_modules/vue-loader/lib/inde" },
        { id: 2, name: "2x" },
      ],
    };
  },
  methods: {
    onClickLeft() {
      this.$router.back();
    },
    onClickRight() {},
    loadOrderlist() {
      this.lists.push({ id: 100, name: "100x" });
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
    padding: 0 0;
    .order{
        width: 20%;
        height: 30px;
    }
    .address{
        width: 80%;
        height: 30px;
    }
  }
}
</style>