<script setup>
import ProductIcon from '../../components/icons/ProductIcon.vue';
import PencilIcon from '../../components/icons/PencilIcon.vue';
import ArrowLeftIcon from '../../components/icons/ArrowLeftIcon.vue';
import SectionTitle from '../../components/admin/SectionTitle.vue';
import LinkWithLabel from '../../components/LinkWithLabel.vue';
import BasicButton from '../../components/inputs/BasicButton.vue';

import { onMounted, reactive, ref } from 'vue';

import { useProductStore } from '../../stores/product';
import { useRoute, useRouter } from 'vue-router';

const productStore = useProductStore();
const route = useRoute();
const router = useRouter();
const product = reactive({});
const baseUrl = ref(import.meta.env.VITE_API_URL)

const { productId } = route.params;

onMounted(() => {
  productStore.getOneById({ id: productId });
});

productStore.$subscribe((mutation, state) => {
  Object.assign(product, state.product);
});

const back = () => {
  router.go(-1);
};
</script>

<template>
  <section-title with-button>
    <template #icon>
      <product-icon size="28" />
    </template>
    Detail Products
    <template #buttons>
      <basic-button class-name="bg-red-500 text-grey-200" @click="back">
        <arrow-left-icon size="24" />
        Back
      </basic-button>
      <basic-button
        class-name="bg-yellow-900 text-grey-200"
        is-link
        :link="`/admin/products/${product.id}/edit`"
      >
        <pencil-icon size="24" />
        Edit
      </basic-button>
    </template>
  </section-title>
  <div
    class="bg-grey-50 rounded-md my-8 flex flex-col gap-6 py-6 px-6 md:flex-row lg:py-12"
  >
    <div class="basis-1/2 flex justify-center">
      <img
        v-if="product"
        :src="`${baseUrl}/products/get-file/${
          product.filename ? product.filename : 'default.jpeg'
        }`"
        :alt="product.title"
        class="w-96 rounded-md "
      />
      <div v-else class="w-96 h-96 bg-grey-500 rounded-md"></div>
    </div>
    <div class="basis-1/2 flex flex-col items-start">
      <h1 class="text-2xl text-ellipsis line-clamp-2 font-medium text-grey-900">
        {{ product.title }}
      </h1>
      <div class="mt-5 flex flex-col gap-2">
        <div class="text-grey-800">
          <span>Author</span>:
          <span class="font-medium">{{ product.author }}</span>
        </div>
        <link-with-label label="Demo" :link="product.demo_link">
          {{ product.demo_link }}
        </link-with-label>
        <link-with-label label="Journal" :link="product.journal_link">
          {{ product.journal_link }}
        </link-with-label>
        <link-with-label label="Video" :link="product.video_link">
          {{ product.video_link }}
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
