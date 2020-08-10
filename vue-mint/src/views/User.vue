<template>
  <div>
    <van-button type="primary" @click="onGetconfig()">获取服务器列表</van-button>
    <van-button type="primary" @click="onGetdepth()">获取尝试</van-button>
  </div>
</template>

<script>
import { Button } from "vant";
export default {
  name: "home",
  components: {
    [Button.name]: Button,
  },
  data() {
    return {
      title: "user",
      phone: "18602736776",
      password: "53358861",
      address:'jNC1n9WeniAErRAatYwarRUPCybozPqioW'
    };
  },
  mounted() {},
  methods: {
    onGetconfig() {
        const that = this
        this.$api.swtcAPI
        .getconfig()
        .then(function(respone) {
         console.log(respone)
          
        }).catch(function(e){
          console.log(e.message)
        });
    },
    onGetdepth(){
      this.$api.swtcAPI
        .getDepth({p:'0',s:'10',t:'Receive,Send',w:this.address})
        .then(function(respone) {
         console.log(respone)
          
        }).catch(function(e){
          console.log(e.message)
        });
    }
  },
};
</script>

<style lang="less">
</style>