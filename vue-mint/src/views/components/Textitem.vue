<template>
  <div id="text-item">
    <van-cell-group title="cny">
      <van-grid>
        <van-grid-item
          v-for="(tick,index) in ticker_list"
          :key="tick.id"
          :text="tick.name"
          @click="goTicker(index)"
        >
          <van-cell :title="tick.name" :label="tick.des" />
        </van-grid-item>
      </van-grid>
    </van-cell-group>
    <van-cell-group title="swtc">
      <van-grid>
        <van-grid-item
          v-for="(tick,index) in ticker_list"
          :key="tick.id"
          :text="tick.name"
          @click="goTicker(index)"
        >
          <van-cell :title="tick.name" :label="tick.des" />
        </van-grid-item>
      </van-grid>
    </van-cell-group>
  </div>
</template>
<script>
import { Grid, GridItem, Image as VanImage, Cell, CellGroup } from "vant";
export default {
  props: {
    ticker_list: Array,
  },
  data() {
    return {};
  },
  components: {
    [Grid.name]: Grid,
    [GridItem.name]: GridItem,
    [VanImage.name]: VanImage,
    [Cell.name]: Cell,
    [CellGroup.name]: CellGroup,
  },
  mounted() {},
  methods: {
    goTicker(index) {
      console.log(index);
      this.$router.push("/user");
    },
  },
};
</script>

<style lang="less">
</style>