<template>
  <div>
    <router-view />
    <van-tabbar v-model="active" @change="onChange">
      <van-tabbar-item
        v-for="(item,index) in tabbars"
        :key="index"
        :to="(item.name)"
        :badge="(item.badge)"
      >
        <span>{{item.title}}</span>
        <img slot="icon" slot-scope="props" :src="props.active ? item.normal : item.active" />
      </van-tabbar-item>
    </van-tabbar>
  </div>
</template>

<script>
import { Tabbar, TabbarItem } from "vant";
import normal from "./assets/dis-normal.png";
import active from "./assets/dis-active.png";
export default {
  name: "app",
  components: {
    [Tabbar.name]: Tabbar,
    [TabbarItem.name]: TabbarItem,
  },
  data() {
    return {
      title: "app",
      active: 0,
      tabbars: [
        {
          name: "/home",
          title: "首页",
          badge: "",
          normal: require('./assets/dis-normal.png'),
          active: require('./assets/dis-active.png'),
        },
        {
          name: "/info",
          title: "新闻",
          badge: 9,
          normal: normal,
          active: active,
        },
        {
          name: "/discory",
          title: "发现",
          badge: 3,
          normal: normal,
          active: active,
        },
        {
          name: "/user",
          title: "我的",
          badge: 4,
          normal: normal,
          active: active,
        },
      ],
    };
  },
  methods: {
    onChange(index) {
      this.tabbars[index].badge = "";
      console.log("当前选中的是:" + index);
    },
  },
};
</script>

<style lang="less">
</style>