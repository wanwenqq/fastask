<template>
  <div id="text-item">
    <van-grid :column-num="4" :border="false">
      <van-grid-item icon="home-o" text="路由跳转"  @click="gotoCategory(index)"/>
      <van-grid-item icon="home-o" text="路由跳转"  @click="gotoCategory(index)"/>
      <van-grid-item icon="home-o" text="路由跳转"  @click="gotoCategory(index)"/>
      <van-grid-item icon="search" text="URL 跳转" url="/vant/mobile.html" />
    </van-grid>
  </div>
</template>
<script>
import { Grid, GridItem } from "vant";
export default {
  props: {},
  data() {
    return {};
  },
  components: {
    [Grid.name]: Grid,
    [GridItem.name]: GridItem,
  },
  methods: {
    gotoCategory (index) {
      this.$router.push('/login')
    }
  },
};
</script>

<style lang="less">
</style>