<script setup lang="ts">
import api from "./api";
import { useRoute } from "vue-router";
import { Product } from "./interfaces";
import { onMounted, ref } from "vue";
const route = useRoute();
const params = route.params;

const product = ref<Product>();

onMounted(() => {
  api.get(`item/${params.id}`).then(res => {
    product.value = res;
    console.log(res);
  });
});
</script>

<template>
  <h1>Product Detail</h1>
  <div class="product">
    <div class="left">
      <el-scrollbar>
        <el-image v-for="img in product?.images" :src="img" fit="cover" :key="img" />
      </el-scrollbar>
    </div>
    <div class="right">
      <div class="price">${{ product?.price }}</div>
      <div class="tags">
        <el-tag v-for="tag in product?.tags" type="info" round>{{ tag }}</el-tag>
      </div>
      <div class="category">{{ product?.category }}</div>
      <div class="description">{{ product?.description }}</div>
      <div class="owner">Owner: {{ product?.owner }}</div>
    </div>
  </div>
</template>

<style scoped lang="scss">
@import "./variables";

.el-scrollbar {
  width: 100%;
  // height: calc(100% - 200px);
  height: 300px;
  margin-bottom: 20px;
}

.el-image {
  width: 100%;
  height: 300px;
  margin-bottom: 20px;
  border: 3px solid white;
  border-radius: 7px;
}

.product {
  height: 100%;
  display: flex;

  .left {
    width: 40%;
  }
  .right {
    width: 60%;
    padding: 20px;
    .price {
      font-size: 24px;
      margin-bottom: 20px;
      color: $main_primary;
      font-weight: bold;
    }
    .tags {
      margin-bottom: 20px;
      .el-tag {
        margin-right: 10px;
      }
    }
    .category {
      margin-bottom: 20px;
    }
    .description {
      margin-bottom: 20px;
    }
    .owner {
      font-size: 12px;
      color: #666;
    }
  }
}
</style>
