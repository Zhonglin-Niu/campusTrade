<script setup lang="ts">
// import Aside from "./components/Aside.vue";
import Footer from "./components/Footer.vue";
import Header from "./components/Header.vue";
</script>

<template>
  <div class="common-layout">
    <el-container>
      <!-- <el-aside width="200px"><Aside></Aside></el-aside> -->
      <el-container>
        <el-header><Header></Header></el-header>
        <el-main><router-view></router-view></el-main>
        <el-footer><Footer></Footer></el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped lang="scss">
@import "./variables";
.common-layout {
  width: 100vw;
  height: 100vh;

  .el-container {
    height: 100%;
  }

  .el-aside {
    background-color: $aside_bg;
    color: $aside_text;
    padding: 10px;
  }

  .el-header {
    background-color: $header_bg;
    color: $header_text;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .el-main {
    background-color: $main_bg;
    color: $main_text;
    overflow: hidden;
  }

  .el-footer {
    background-color: $footer_bg;
    color: $footer_text;
    display: flex;
    justify-content: center;
    align-items: center;
  }
}
</style>
