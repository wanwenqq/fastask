<template>
  <div id="text-item">
    <van-grid :column-num="4" :border="true">
      <van-grid-item v-for="(tick,index) in ticker_list"
                     :key="tick.id"
                     :text="tick.name"
                     @click="gotoCategory(index)">
        <van-cell :title="tick.name"  :label="tick.des" />
      </van-grid-item>
    </van-grid>
  </div>
</template>
<script>
import { Grid, GridItem,Image as VanImage,Cell} from "vant";
export default {
  props: {
    ticker_list:Array
  },
  data() {
    return {
    };
  },
  components: {
    [Grid.name]: Grid,
    [GridItem.name]: GridItem,
    [VanImage.name]: VanImage,
    [Cell.name]: Cell,
  },
  mounted() {
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