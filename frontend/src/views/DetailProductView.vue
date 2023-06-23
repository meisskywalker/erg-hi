<script setup>
import LinkWithLabel from '../components/LinkWithLabel.vue';

import { onMounted, reactive, ref } from 'vue';

import { useProductStore } from '../stores/product';
import { useRoute } from 'vue-router';

const productStore = useProductStore();
const route = useRoute();
const product = reactive({});
const baseUrl = ref(import.meta.env.VITE_API_URL);

const { productId } = route.params;

onMounted(() => {
  productStore.getOneById({ id: productId });
});

productStore.$subscribe((mutation, state) => {
  Object.assign(product, state.product);
});
</script>

<template>
  <div
    class="mt-24 container w-full flex flex-col md:flex-row md:gap-4 md:px-4 lg:gap-0"
  >
    <div class="md:basis-1/2 flex justify-center">
      <img
        :src="`${baseUrl}/products/get-file/${
          product.filename ? product.filename : 'default.jpeg'
        }`"
        :alt="product.title"
        class="w-60 h-60 md:w-80 md:h-80 lg:w-96 lg:h-96 object-cover rounded-md"
        v-if="product.filename"
      />
      <div
        class="w-60 h-60 md:w-80 md:h-80 lg:w-96 lg:h-96 bg-grey-500 rounded-md"
        v-else
      ></div>
    </div>
    <div class="px-8 pt-8 md:p-0 md:basis-1/2 flex flex-col items-start">
      <h1 class="text-2xl text-ellipsis line-clamp-2 font-medium text-grey-900">
        {{ product.title }}
      </h1>
      <div class="mt-5 flex flex-col gap-2">
        <div class="text-grey-800">
          <span>Author</span>:
          <span class="font-medium">{{ product.author }}</span>
        </div>
        <link-with-label label="Demo" :link="product.demo_link">
          visit here
        </link-with-label>
        <link-with-label label="Journal" :link="product.journal_link">
          visit here
        </link-with-label>
        <link-with-label label="Video" :link="product.video_link">
          visit here
        </link-with-label>
        <div class="text-grey-800">
          <span>Description</span>:
          <p class="text-grey-900">
            {{ product.description }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
