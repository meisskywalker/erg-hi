<script setup>
import { toRefs } from 'vue';

const props = defineProps({
  image: String,
});

const { image } = toRefs(props);
</script>

<template>
  <div id="hero" class="w-full relative flex flex-col h-[35rem]">
    <img
      :src="image"
      alt="hero image"
      class="w-full h-full absolute object-cover"
    />
    <div
      class="w-full p-4 md:w-3/4 md:p-12 lg:p-18 z-10 flex justify-center items-start flex grow flex-col"
    >
      <slot/>
    </div>
  </div>
</template>
