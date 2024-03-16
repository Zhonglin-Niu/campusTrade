<script setup lang="ts">
import { ref } from "vue";

const value1 = ref("");
const value2 = ref("");
const value3 = ref("");
const value4 = ref("");

const options = [
  {
    value: "Option1",
    label: "Option1",
  },
  {
    value: "Option2",
    label: "Option2",
  },
  {
    value: "Option3",
    label: "Option3",
  },
  {
    value: "Option4",
    label: "Option4",
  },
  {
    value: "Option5",
    label: "Option5",
  },
];
</script>

<template>
  <h1>Campus Trader</h1>
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
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value"
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
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value"
      />
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
</style>
