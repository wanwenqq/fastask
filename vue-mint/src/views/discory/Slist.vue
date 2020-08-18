<template>
  <div class="slist">
    <van-nav-bar
      title="排行榜"
      left-text="返回"
      right-text
      left-arrow
      @click-left="onClickLeft"
      @click-right="onClickRight"
    />
    <van-list v-model="loading" :finished="finished" finished-text="暂无更多数据" @load="load_more_items">
      <van-cell v-for="item in items" is-link :key="item.id" :title="item.id" :value="item.address" />
    </van-list>
  </div>
</template>
<script>
import { NavBar, Cell, CellGroup,List } from "vant";
export default {
  name: "slist",
  components: {
    [NavBar.name]: NavBar,
    [Cell.name]: Cell,
    [List.name]: List,
  },
  data() {
    return {
      items: [],
      finished: false,
      loading: false,
      offset: 0,
      page: 0,
      limit: 10,
    };
  },
  mounted() {
    // this.getSlist();
  },
  methods: {
    onClickLeft() {
      this.$router.back();
    },
    onClickRight() {},


    load_more_items: function () {
      this.page += 1;
      this.offset = this.limit * this.page;
      this.getSlist();
    },

    async getSlist() {
        this.loading = false;
        let result = await this.$api.swtcAPI.getSlist();
        this.items.push(...result.data);
        this.finished = true;
    },
    
  },
};
</script>
<style lang="less">
</style>