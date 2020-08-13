<template>
  <div class="data">
    <van-grid :column-num="3" :border='false'>
      <van-grid-item v-for="value in 6" :key="value" text="最新价：1234567890" />
    </van-grid>
  </div>
</template>

<script>
import { Grid, GridItem } from "vant";
export default {
  components: {
    [Grid.name]: Grid,
    [GridItem.name]: GridItem,
  },
  data() {
    return {};
  },
  methods: {},
};
</script>

<style lang="less">
.data {
  margin-bottom: 0px;
}
</style>