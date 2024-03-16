<script setup lang="ts">
import { onMounted, ref } from "vue";
import api from "../api";
import { Product } from "../interfaces";
import { Category, Tag } from "../interfaces";

const category = ref("");
const tag = ref<string[]>([]);

const categories = ref<Category[]>([]);
const tags = ref<Tag[]>([]);

onMounted(() => {
  api.get("categories").then(res => {
    categories.value = res;
  });
  api.get("tags").then(res => {
    tags.value = res;
  });
});

const genProducts = async (count: number) => {
  const products = [];

  const items: Product[] = await api.get("items");
  products.push(...items);

  for (let i = 0; i < count; i++) {
    const width = Math.floor(Math.random() * 300) + 200;
    const height = Math.floor(Math.random() * 200) + 200;
    products.push({
      id: i + 100000,
      title: `Product ${i}`,
      price: Math.floor(Math.random() * 1000),
      cover: `https://picsum.photos/${width}/${height}?random=${i}`,
      category: "Category",
      tags: ["Tag1", "Tag2", "Tag3"],
    });
  }
  return products as Product[];
};

let products = ref<Product[]>([]);
let products_copy: Product[] = [];

onMounted(async () => {
  products.value = await genProducts(80);
  products_copy = products.value;
});

const search = ref("");

// search onchange
const handleSearch = (value: string) => {
  if (!value) {
    products.value = products_copy;
    return;
  }
  // return filtered products
  products.value = products.value.filter(product => {
    return product.title.toLowerCase().includes(value.toLowerCase());
  });
};

const handleCategory = (value: string) => {
  category.value = value;
  if (value === undefined || value === "") {
    products.value = products_copy;
    return;
  }
  products.value = products_copy.filter(product => {
    return value.includes(product.category);
  });
};

const handleTag = (values: string[]) => {
  tag.value = values;
  if (values.length === 0) {
    products.value = products_copy;
    return;
  }
  products.value = products_copy.filter(product => {
    return values.every(tag => product.tags.includes(tag));
  });
};
</script>

<template>
  <div class="filters">
    <div class="type">
      <div class="filter">
        <p>Category</p>
        <el-select
          v-model="category"
          clearable
          collapse-tags
          collapse-tags-tooltip
          :max-collapse-tags="3"
          placeholder="Category"
          @change="handleCategory"
        >
          <el-option
            v-for="category in categories"
            :key="category.id"
            :label="category.name"
            :value="category.name"
          />
        </el-select>
      </div>
      <div class="filter">
        <p>Tag</p>
        <el-select
          v-model="tag"
          multiple
          clearable
          collapse-tags
          collapse-tags-tooltip
          :max-collapse-tags="3"
          placeholder="Tag"
          @change="handleTag"
        >
          <el-option v-for="tag in tags" :key="tag.id" :label="tag.name" :value="tag.name" />
        </el-select>
      </div>
    </div>
    <el-input
      placeholder="Search"
      prefix-icon="el-icon-search"
      v-model:model-value="search"
      @input="handleSearch"
    />
  </div>
  <el-scrollbar class="scroll">
    <div class="products">
      <div class="product" v-for="product in products" :key="product.id">
        <div class="img-wrapper">
          <el-image :src="product.cover" fit="cover" />
        </div>
        <router-link :to="{ name: 'detail', params: { id: product.id } }" class="name">{{
          product.title
        }}</router-link>
        <p class="price">${{ product.price }}</p>
        <div class="category">
          <el-tag type="info" round>{{ product.category }}</el-tag>
        </div>
        <!-- <div class="tags">
          <el-tag v-for="tag in product.tags" type="info" round>{{ tag }}</el-tag>
        </div> -->
        <div class="owner">{{ product.owner }}</div>
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

.type {
  display: flex;
  gap: 20px;

  .filter {
    width: 50%;
  }

  margin-bottom: 20px;
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

  .category {
    margin-top: 10px;
    cursor: pointer;
  }

  .tags {
    margin-top: 10px;
    display: flex;
    gap: 5px;
    width: 100%;
    justify-content: right;
    cursor: pointer;
  }

  .owner {
    margin-top: 10px;
    font-size: 12px;
    color: #666;
    width: 100%;
    text-align: right;
  }
}
</style>
