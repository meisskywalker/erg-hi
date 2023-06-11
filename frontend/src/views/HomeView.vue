<script setup>
import SearchIcon from '../components/icons/SearchIcon.vue';
import Hero from '../components/Hero.vue';
import BasicInput from '../components/inputs/BasicInput.vue';
import ProductItem from '../components/ProductItem.vue';

import { ref, onMounted, reactive } from 'vue';
import { useProductStore } from '../stores/product';

const productStore = useProductStore();

const searchQuery = ref('');
const products = reactive([]);
const tfIdf = reactive({});

onMounted(() => {
  productStore.getAll();
});

productStore.$subscribe((mutation, state) => {
  Object.assign(products, state.products);
  Object.assign(tfIdf, state.tdidf);

  products.sort((a, b) => {
    const productA = tfIdf[a.id];
    const productB = tfIdf[b.id];

    return productB - productA;
  });
});

const update = (payload) => {
  searchQuery.value = payload;
};

const search = () => {
  const query = searchQuery.value.trim();
  productStore.getAll();
  productStore.getTfIdf({ query });
};
</script>

<template>
  <div>
    <hero image="/img/hero.png">
      <h1 class="text-grey-100 text-4xl md:text-5xl font-medium leading-[3.5rem] md:leading-[4rem]">
        Lorem ipsum dolor sit amet consectetur
        <span class="text-brand-accent-300">adipiscing elit.</span>
        Pellentesque ac lorem tellus.
      </h1>
      <span class="text-grey-50 font-light">
        Lorem ipsum dolor sit amet consectetur adipiscing elit. Pellentesque ac
        lorem tellus.
      </span>
    </hero>
    <main class="mx-auto flex flex-col gap-8">
      <div id="products" class="container mx-auto w-full">
        <div class="w-full justify-center items-center flex flex-col p-8">
          <h1 class="text-3xl text-brand-900 font-semibold">Our Products</h1>
          <span class="text-brand-800">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ut
            suscipit dolor.</span>
        </div>
        <div id="products" class="flex flex-col gap-8 justify-center items-center px-4 md:p-0">
          <div class="w-full flex justify-end items-center gap-2">
            <form @submit.prevent="search" class="flex justify-end items-center gap-2">
              <basic-input className="w-52" :value="searchQuery" @update="update" />
              <button type="submit" class="bg-brand-400 p-2 rounded-md">
                <search-icon color="text-grey-200" size="20" />
              </button>
            </form>
          </div>
          <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
            <product-item v-for="product in products" :key="product.id" :product-id="product.id">
              {{ product.title }}
            </product-item>
          </div>
          <button class="bg-brand-200 rounded-md py-1 px-3 text-lg text-grey-900">
            See More
          </button>
        </div>
      </div>
      <div id="about" class="w-full justify-center items-center flex flex-col p-8 bg-grey-50 gap-8">
        <h1 class="text-3xl text-brand-900 font-semibold">About Us</h1>
        <div class="flex flex-col gap-4 items-center md:items-stretch md:gap-0 md:flex-row justify-between">
          <div class="basis-1 md:basis-1/2 flex justify-center">
            <img src="/img/about.png" alt="about" width="80%" />
          </div>
          <div class="basis-1 w-[80%] md:w-full md:basis-1/2 flex flex-col">
            <div class="flex gap-4 flex-col md:grow">
              <h2 class="text-brand-800 text-2xl font-medium">
                Lorem ipsum dolor sit amet.
              </h2>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Suspendisse in magna venenatis, mollis turpis eget, tempor
                nulla. Etiam sit amet nisl nec augue imperdiet egestas.
                Curabitur quis vestibulum lectus.
              </p>
            </div>
            <div class="flex gap-2 items-center">
              <span>Contact us by: </span>
              <img src="/img/ig-logo.png" alt="ig" width="35" />
              <img src="/img/wa-logo.png" alt="ig" width="35" />
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>
