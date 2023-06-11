<script setup>
import ProductIcon from '../../components/icons/ProductIcon.vue';
import PlusIcon from '../../components/icons/PlusIcon.vue';
import SectionTitle from '../../components/admin/SectionTitle.vue';
import BasicButton from '../../components/inputs/BasicButton.vue';

import { useProductStore } from '../../stores/product';
import { reactive, ref, onMounted } from 'vue';

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

const truncate = (string, n) => {
  return string?.length > n ? string.substring(0, n - 1) + '...' : string;
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

  <div class="relative overflow-x-auto shadow-md rounded-lg my-8">
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
        <tr
          class="bg-white border-b"
          v-for="product in products"
          :key="product.id"
        >
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
            <router-link
              :to="`/admin/products/${product.id}`"
              class="font-medium text-blue-600 hover:underline"
            >
              Detail
            </router-link>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
