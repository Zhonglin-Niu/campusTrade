<script setup lang="ts">
import { ref } from "vue";
const genProducts = (count: number) => {
  const products = [];
  for (let i = 0; i < count; i++) {
    const width = Math.floor(Math.random() * 300) + 200;
    const height = Math.floor(Math.random() * 200) + 200;
    products.push({
      id: i,
      name: `Product ${i}`,
      price: Math.floor(Math.random() * 1000),
      image: `https://picsum.photos/${width}/${height}?random=${i}`,
    });
  }
  return products;
};

const products = ref(genProducts(80));
const search = ref("");
</script>

<template>
  <div class="filters">
    <el-input placeholder="Search" prefix-icon="el-icon-search" v-model:model-value="search" />
  </div>
  <el-scrollbar class="scroll">
    <div class="products">
      <div class="product" v-for="product in products" :key="product.id">
        <div class="img-wrapper">
          <el-image :src="product.image" fit="fill" />
        </div>
        <p class="name">{{ product.name }}</p>
        <p class="price">${{ product.price }}</p>
      </div>
    </div>
  </el-scrollbar>
</template>

<style scoped lang="scss">
@import "../variables";
.filters {
  padding: 20px;
  .el-input {
    width: 100%;
  }
}

.products {
  display: flex;
  flex-wrap: wrap;
  padding-bottom: 80px;
}

.product {
  width: 200px;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  margin: 20px;
  border: 1px solid #ebeef5;
  border-radius: 5px;
  text-align: center;
  transition: all 0.15s;
  box-shadow: 4px 4px 10px 0px $main_bg_shadow;

  .img-wrapper {
    width: 150px;
    height: 200px;
    border-radius: 5px;
    overflow: hidden;
  }

  .el-image {
    position: relative;
    margin-bottom: 10px;
    width: 150px;
    height: 200px;
    cursor: pointer;
    transition: all 0.3s;
    overflow: hidden;
  }

  .name {
    font-size: 18px;
    margin: 10px 0;
  }

  .price {
    font-size: 18px;
    color: $main_primary;
    font-weight: bold;
  }

  &:hover {
    box-shadow: 12px 12px 14px 0px rgba(0, 0, 0, 0.1);

    .el-image {
      transform: scale(1.1);
    }
  }
}
</style>
