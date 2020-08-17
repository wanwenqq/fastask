<template>
  <div>
    <van-form @submit="onSubmit">
      <van-field
        v-model="phone"
        name="phone"
        label="用户名"
        placeholder="用户名"
        :rules="[{ required: true, message: '请填写用户名' }]"
      />
      <van-field
        v-model="password"
        type="password"
        name="password"
        label="密码"
        placeholder="密码"
        :rules="[{ required: true, message: '请填写密码' }]"
      />
      <div style="margin: 16px;">
        <van-button round block type="info" native-type="submit">提交</van-button>
      </div>
    </van-form>
  </div>
</template>
<script>
import { Form, Field, Button } from "vant";
import {PUTUSERINFO} from '../store/types.js'
export default {
  components: {
    [Form.name]: Form,
    [Field.name]: Field,
    [Button.name]: Button,
  },
  data() {
    return {
      phone: "18602736775",
      password: "53358861",
    };
  },
  mounted() {
    // console.log(this.$store.state.userinfo.token)
  },
  methods: {
    
    onSubmit(values){
      this.onLogin(values)
    },
   
    Userinfo(){
      console.log(this.$store.state.userinfo)
    },
    async onLogin(values) {
      // console.log("submit", values);
      let result = await this.$api.userAPI.login(values);
      if(result.status ===200){
          // userinfo['id'] = result.data['id']
          // userinfo['phone'] = result.data['phone']
          // userinfo['token'] = result.data['token']
          this.$store.commit(PUTUSERINFO,result.data.data)
          this.$router.back()

      }else{
          console.log('用户名或密码错误')
      }
    },
  },
};
</script>

<style lang="less">
</style>