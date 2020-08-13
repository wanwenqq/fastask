<template>
  <div>
    <router-view />
    <van-tabbar v-model="active" @change="onChange" route>
      <van-tabbar-item
        v-for="(item,index) in tabbars"
        :key="index"
        :to="(item.name)"
        :badge="(item.badge)"
      >
        <span>{{item.title}}</span>
        <img slot="icon" slot-scope="props" :src="props.active ? item.active : item.normal" />
      </van-tabbar-item>
    </van-tabbar>
  </div>
</template>

<script>
import { Tabbar, TabbarItem, Button } from "vant";
export default {
  name: "app",
  components: {
    [Tabbar.name]: Tabbar,
    [TabbarItem.name]: TabbarItem,
    [Button.name]: Button,
  },
  data() {
    return {
      title: "app",
      active: 0,
      tabbars: [
        {
          name: "/main",
          title: "首页",
          badge: "",
          normal: require("../assets/home-normal.png"),
          active: require("../assets/home-active.png"),
        },
        {
          name: "/data",
          title: "数据",
          badge: '',
          normal: require("../assets/data-normal.png"),
          active: require("../assets/data-active.png"),
        },
        {
          name: "/discory",
          title: "发现",
          badge: 3,
          normal: require("../assets/dis-normal.png"),
          active: require("../assets/dis-active.png"),
        },
        {
          name: "/user",
          title: "我的",
          badge: 4,
          normal: require("../assets/user-normal.png"),
          active: require("../assets/user-active.png"),
        },
      ],
    };
  },
  created() {},
  mounted() {},
  methods: {
    onChange(index) {
      this.tabbars[index].badge = "";
      console.log("当前选中的是:" + index);
      console.log("active:" + this.active);
    },
  },
};
</script>

<style lang="less">
</style>