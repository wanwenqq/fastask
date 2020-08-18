<template>
  <div>
     
    <van-row class="user-links">
      <van-col span="6" @click="goPage('slist')">
        <van-icon name="pending-payment" />SSS排行榜
      </van-col>
      <van-col span="6">
        <van-icon name="records" />AAA排行榜
      </van-col>
      <van-col span="6">
        <van-icon name="tosend" />BBB排行榜
      </van-col>
      <van-col span="6">
        <van-icon name="logistics" />CCC排行榜
      </van-col>
    </van-row>

    <van-cell-group class="user-group">
      <van-cell icon="records" title="全部订单" is-link @click="goPage('orderlist')"/>
    </van-cell-group>

    <van-cell-group>
      <van-cell icon="points" title="我的积分" is-link />
      <van-cell icon="gold-coin-o" title="我的优惠券" is-link />
      <van-cell icon="gift-o" title="我的转账" is-link />
    </van-cell-group>

   

  </div>
</template>

<script>
import { Row, Col, Icon, Cell, CellGroup, Image } from "vant";
export default {
  components: {
    [Row.name]: Row,
    [Col.name]: Col,
    [Icon.name]: Icon,
    [Cell.name]: Cell,
    [Image.name]: Image,
    [CellGroup.name]: CellGroup,
  },
  methods: {
    goPage(name) {
      this.$router.push({name})
    },
  },
};
</script>

<style lang="less">
.user {
  &-poster {
    width: 100%;
    height: 53vw;
    display: block;
  }
  &-group {
    margin-bottom: 15px;
  }
  &-links {
    padding: 15px 0;
    font-size: 12px;
    text-align: center;
    background-color: #fff;
    .van-icon {
      display: block;
      font-size: 24px;
    }
  }
}
</style>