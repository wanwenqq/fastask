<template>
  <div class="data">
    <van-cell-group title="cny">
      <div class="data-info">
        <ul>
          <li v-for="(value,key,index) in pri_list" :key="index">{{key}}:{{value}}</li>
        </ul>
      </div>
    </van-cell-group>

    <div id="main" style="width: 100%;height:200px;"></div>
    <Orderitem> </Orderitem>
  </div>
</template>

<script>
import { Grid, GridItem, CellGroup } from "vant";
import Orderitem from './components/Orderitem.vue'
var echarts = require("echarts");

export default {
  components: {
    [Grid.name]: Grid,
    [GridItem.name]: GridItem,
    [CellGroup.name]: CellGroup,
    Orderitem,
  },
  data() {
    return {
      pri_list: {},
    };
  },
  mounted() {
    this.getInfos();
    this.initEcharts();
  },
  methods: {
    async getInfos() {
      let result = await this.$api.swtcAPI.getInfos();
      this.pri_list = result.data;
    },
    initEcharts() {
      // 基于准备好的dom，初始化echarts实例
      var myChart = echarts.init(document.getElementById("main"));
      // 绘制图表
      myChart.setOption({
        title: {
          show:false,
          text: "线图",
        },
        tooltip: {},
        xAxis: {
          data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
        },
        yAxis: {},
        series: [
          {
            name: "销量",
            type: "bar",
            data: [5, 20, 36, 10, 10, 20],
          },
        ],
      });
    },
  },
};
</script>

<style lang="less">
.data {
  margin-bottom: 0px;
}
.data-info {
  margin: 0 auto;
  ul {
    margin: 0 10px;
    padding: 0px;
    list-style: none;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
  }
  li {
    margin: 0px;
    padding: 0px;
    list-style: none;
    width: 30%; /*每个元素的初始化宽度*/
    text-align: left;
    margin-top: 10px;
    margin-bottom: 10px;
    flex: auto; //重要
    font-size: 12px;
  }
}
</style>