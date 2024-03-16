<script setup lang="ts"></script>

<template>
  <div class="container">
    <div class="left"></div>
    <div class="middle">
      <h1><router-link to="/">Campus Trader</router-link></h1>
    </div>
    <div class="right">
      <el-button type="primary" round link>Sign Up</el-button>
      <el-button type="primary" round link>Log In</el-button>
    </div>
  </div>
</template>

<style scoped lang="scss">
a {
  text-decoration: none;
  color: inherit;
}

.container {
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: center;
  padding: 20px 0;
}

.left {
  width: 20%;
}

.middle {
  width: 60%;
  text-align: center;
}

.right {
  width: 20%;
  display: flex;
  justify-content: flex-end;
  .el-button {
    margin-left: 10px;
  }
}
</style>
