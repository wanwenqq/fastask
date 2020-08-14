<template>
  <div class="usercenter">
    <van-nav-bar
      title="标题"
      left-text="返回"
      right-text
      left-arrow
      @click-left="onClickLeft"
      @click-right="onClickRight"
    />
    <!-- <div class="icon">
      <span class="title">头像</span>
      <img src="../../assets/user-normal.png" alt />
    </div> -->
    <van-cell-group>
      <van-cell title="昵称" value="anders" is-link />
      <van-cell title="性别" value="男" is-link />
      <van-cell title="生日" :value="brithday" is-link @click="selectBrithday" />
      <van-cell title="手机号" value="186*******5" is-link label="不对外公开" />
    </van-cell-group>
    <van-button size="large" style="margin-top:1rem" @click="logOut">退出登录</van-button>
    <!-- 时间选择器 -->
    <van-popup v-model="show" position="bottom">
      <div id="popupdiv">作用</div>
    </van-popup>
  </div>
</template>
<script>
import { NavBar, Cell, CellGroup, Button, Popup, DatetimePicker } from "vant";

export default {
  name: "home",
  components: {
    [NavBar.name]: NavBar,
    [Cell.name]: Cell,
    [CellGroup.name]: CellGroup,
    [Button.name]: Button,
    [Popup.name]: Popup,
    [DatetimePicker.name]: DatetimePicker,
  },
  data() {
    return {
      show: false,
      currentDate: new Date(),
      // 最小时间
      minDate: new Date("1949/01/01"),
      maxDate: new Date("2019/12/31"),
      brithday: "2019/12/31",
    };
  },
  mounted() {},
  methods: {
    onClickLeft() {
      this.$router.back();
    },
    onClickRight() {},
    // 选择生日
    selectBrithday() {
      console.log('select---------')
      this.show = true;
    },
    
    logOut(){

    }
  },
};
</script>
<style lang="less">
.usercenter {
  position: fixed;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  background-color: #f5f5f5;
  z-index: 999;
  .icon {
    display: flex;
    width: 100%;
    margin-top: 20px;
    padding: 0 20px;
    background-color: #ffffff;
    align-items: center;
    .title {
      height: 3rem;
      line-height: 3rem;
      color: #323233;
      font-size: 14px;
    }
    img {
      position: absolute;
      right: 1.6rem;
      height: 2.5rem;
      width: 2.5rem;
    }
  }
}
#popupdiv{
  height: 300px;
}
</style>