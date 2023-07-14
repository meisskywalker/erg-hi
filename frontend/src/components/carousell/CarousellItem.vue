<script setup>
import { computed, ref, toRefs } from 'vue';

const props = defineProps({
  slide: String,
  currentSlide: Number,
  index: Number,
});

const { slide } = toRefs(props);
const baseUrl = ref(import.meta.env.VITE_API_URL);
</script>

<template>
  <transition name="slide-in">
    <div class="absolute inset w-full h-[35rem]" v-show="currentSlide === index">
      <img :src="`${baseUrl}/images/slides/${slide}`" class="w-full h-full object-cover" />
    </div>
  </transition>
</template>

<style scoped>
.slide-in-enter-active,
.slide-in-leave-active {
  transition: all 1s ease-in-out;
}

.slide-in-enter-from {
  transform: translateX(-100%);
  /* opacity: 0; */
}

.slide-in-leave-to {
  /* opacity: 1; */
  transform: translateX(100%);
}
</style>
