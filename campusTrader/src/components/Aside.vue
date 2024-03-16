<script setup lang="ts">
import { onMounted, ref } from "vue";
import api from "../api";
import { Category, Tag } from "../interfaces";

const value1 = ref("");
const value4 = ref("");

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
</script>

<template>
  <div class="filter">
    <p>Category</p>
    <el-select
      v-model="value1"
      multiple
      clearable
      collapse-tags
      collapse-tags-tooltip
      :max-collapse-tags="3"
      placeholder="Category"
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
      v-model="value4"
      multiple
      clearable
      collapse-tags
      collapse-tags-tooltip
      :max-collapse-tags="3"
      placeholder="Tag"
    >
      <el-option v-for="tag in tags" :key="tag.id" :label="tag.name" :value="tag.name" />
    </el-select>
  </div>
</template>

<style scoped lang="scss">
h1 {
  margin: 20px 0;
  text-align: center;
}

.filter {
  margin-bottom: 20px;
}

a {
  color: #000;
  text-decoration: none;
}
</style>
