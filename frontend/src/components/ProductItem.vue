<script setup>
import { ref, toRefs } from 'vue';

const props = defineProps({
  image: String,
  productId: String
});

const baseUrl = ref(import.meta.env.VITE_API_URL)

const { image, productId } = toRefs(props);
</script>

<template>
  <div class="basis-1/3 flex flex-col gap-2">
    <img :src="`${baseUrl}/images/${image ? image : 'default.jpeg'
      }`" :alt="image" class="w-full h-56 rounded-md object-cover " v-if="image" />
    <div class="w-full h-56 bg-grey-500 rounded-md" v-else></div>
    <router-link :to="`/${productId}`" class="text-xl text-ellipsis line-clamp-2 font-medium text-grey-900">
      <slot />
    </router-link>
  </div>
</template>
