<template>
  <div id="orderitem">
    <van-tabs v-model="active" animated>
      <van-tab v-for="tab in listtabs" 
      :key="tab"
      :title="'选项 ' +tab">
      内容 {{ tab }}
      </van-tab>
    </van-tabs>
  </div>
</template>

<script>
import { Tab, Tabs } from "vant";
export default {
  components: {
    [Tab.name]: Tab,
    [Tabs.name]: Tabs,
  },
  data() {
    return {
      active: 0,
      listtabs: [1, 2, 3, 4],
    };
  },
};
</script>
<style lang="less">
</style>