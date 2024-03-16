<script setup lang="ts">
import Aside from "./components/Aside.vue";
import Footer from "./components/Footer.vue";
import Header from "./components/Header.vue";
import Main from "./components/Main.vue";
</script>

<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="200px"><Aside></Aside></el-aside>
      <el-container>
        <el-header><Header></Header></el-header>
        <el-main><Main></Main></el-main>
        <el-footer><Footer></Footer></el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped lang="scss">
.common-layout {
  width: 100vw;
  height: 100vh;

  .el-container {
    height: 100%;
  }

  .el-aside {
    background-color: #333;
    color: #fff;
    text-align: center;
  }

  .el-header {
    background-color: #20a0ff;
    color: #fff;
    line-height: 60px;
  }

  .el-main {
    background-color: #f5f5f5;
    color: #333;
  }

  .el-footer {
    background-color: #20a0ff;
    color: #fff;
    line-height: 60px;
  }
}
</style>
