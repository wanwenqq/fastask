<template>
  <div class="user">
    <van-cell-group>
      <van-cell style="background-color: #3bba63;color:#FFF;" is-link center>
        <div class="user-msg">
          <div class="user-logined"  v-if="istoken" @click="goPage('usercenter')">
            <img src="../../assets/home-normal.png" alt />
            <div>
              <span>姓名</span>
              <span>性别</span>
            </div>
          </div>
          <div class="user-login"  v-if="!istoken" @click="goPage('login')">
            <img src="../../assets/user-normal.png" alt />
            <div>
              <span>姓名</span>
              <span>性别</span>
            </div>
          </div>
        </div>
      </van-cell>
    </van-cell-group>
  <!--路由的出口-->
  </div>
</template>

<script>
import { Cell, CellGroup  } from "vant";
export default {
  name: "home",
  components: {
    [Cell.name]: Cell,
    [CellGroup.name]: CellGroup,
  },
  data() {
    return {
      istoken: true,
    };
  },
  mounted() {},
  methods: {
    goPage(name){
      this.$router.push({name})
    }
  },
};
</script>

<style lang="less">
.user {
  width: 100%;
  height: 100%;
  .user-msg {
    .user-logined{
      display: flex;
      align-items: center;
      img{
        width: 100px;
        height: 100px;
      }
    }
    .user-login{
      display: flex;
      align-items: center;
      img{
        width: 100px;
        height: 100px;
      }
    }
  }
  /*转场动画*/
  .router-slider-enter-active,
  .router-slider-leave-active {
    transition: all 0.3s;
  }
  .router-slider-enter,
  .router-slider-leave-active {
    transform: translate3d(2rem, 0, 0);
    opacity: 0;
  }
}
</style>