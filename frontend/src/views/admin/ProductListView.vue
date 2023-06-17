<script setup>
import ProductIcon from '../../components/icons/ProductIcon.vue';
import PlusIcon from '../../components/icons/PlusIcon.vue';
import SearchIcon from '../../components/icons/SearchIcon.vue';
import ChevronRightIcon from '../../components/icons/ChevronRightIcon.vue';
import ChevronLeftIcon from '../../components/icons/ChevronLeftIcon.vue';
import SectionTitle from '../../components/admin/SectionTitle.vue';
import BasicButton from '../../components/inputs/BasicButton.vue';
import BasicInput from '../../components/inputs/BasicInput.vue';

import { useProductStore } from '../../stores/product';
import { reactive, ref, onMounted } from 'vue';

const productStore = useProductStore();

const searchQuery = ref('');
const pageCount = ref(1);

const products = reactive([]);
const tfIdf = reactive({});

onMounted(() => {
  productStore.$reset();
  productStore.getSome(1);
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
  if (query == '') {
    products.length = 0;
    productStore.getSome(1, true);
  } else {
    productStore.getAll();
  }
  productStore.getTfIdf({ query });
};

const truncate = (string, n) => {
  return string?.length > n ? string.substring(0, n - 1) + '...' : string;
};

const next = () => {
  products.length = 0;
  pageCount.value = pageCount.value + 1;
  productStore.getSome(pageCount.value, true);
};

const previous = () => {
  products.length = 0;
  pageCount.value = pageCount.value - 1;
  productStore.getSome(pageCount.value, true);
};
</script>

<template>
  <section-title with-button>
    <template #icon>
      <product-icon size="28" />
    </template>
    Products
    <template #buttons>
      <basic-button class-name="bg-brand-400 text-grey-200" is-link link="/admin/products/new">
        <plus-icon size="24" />
        Add Product
      </basic-button>
    </template>
  </section-title>

  <div class="flex justify-end py-4">
    <form @submit.prevent="search" class="flex justify-end items-center gap-2">
      <basic-input className="w-52" :value="searchQuery" @update="update" />
      <button type="submit" class="bg-brand-400 p-2 rounded-md">
        <search-icon color="text-grey-200" size="20" />
      </button>
    </form>
  </div>
  <div class="relative overflow-x-auto shadow-md rounded-lg mb-4">
    <table class="w-full text-sm text-left text-grey-500">
      <thead class="text-xs text-grey-700 uppercase bg-grey-50">
        <tr>
          <th scope="col" class="px-6 py-3">Title</th>
          <th scope="col" class="px-6 py-3">Author</th>
          <th scope="col" class="px-6 py-3">Demo Link</th>
          <th scope="col" class="px-6 py-3">Journal Link</th>
          <th scope="col" class="px-6 py-3">Video Link</th>
          <th scope="col" class="px-6 py-3">Action</th>
        </tr>
      </thead>
      <tbody>
        <tr class="bg-white border-b" v-for="product in products" :key="product.id">
          <th scope="row" class="px-6 py-4 font-medium text-gray-900 w-60">
            {{ truncate(product.title, 20) }}
          </th>
          <td class="px-6 py-4">{{ product.author }}</td>
          <td class="px-6 py-4">
            {{ truncate(product.demo_link, 15) }}
          </td>
          <td class="px-6 py-4">
            {{ truncate(product.journal_link, 15) }}
          </td>
          <td class="px-6 py-4">
            {{ truncate(product.video_link, 15) }}
          </td>
          <td class="px-6 py-4">
            <router-link :to="`/admin/products/${product.id}`" class="font-medium text-blue-600 hover:underline">
              Detail
            </router-link>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  <nav class="flex items-center justify-between" aria-label="Table navigation">
    <ul class="inline-flex items-center -space-x-px">
      <li>
        <button @click="previous"
          class="block px-3 py-2 ml-0 leading-tight text-gray-500 bg-white border border-grey-300 rounded-l-lg hover:bg-grey-100 hover:text-grey-700">
          <chevron-left-icon size="20" color="text-grey-700" />
        </button>
      </li>
      <li>
        <button @click="next"
          class="block px-3 py-2 ml-0 leading-tight text-gray-500 bg-white border border-grey-300 rounded-r-lg hover:bg-grey-100 hover:text-grey-700">
          <chevron-right-icon size="20" color="text-grey-700" />
        </button>
      </li>
    </ul>
  </nav>
</template>
