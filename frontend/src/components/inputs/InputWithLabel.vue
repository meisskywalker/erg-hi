<script setup>
import { toRefs } from 'vue';

const props = defineProps({
  value: String,
  type: String,
  className: String,
  label: String,
  placeholder: String,
});
const emit = defineEmits(['update']);

const { value, type, className, label } = toRefs(props);

const lowerCaseLabel = label.value.toLowerCase();

const changeHandler = (e) => {
  emit('update', {
    [label.value.toLowerCase()]: {
      value: e ? e.target.value : value,
    },
  });
};
</script>

<template>
  <div class="flex flex-col">
    <label :for="lowerCaseLabel" class="font-medium text-base">{{
      label
    }}</label>
    <input v-if="type !== 'textarea'" :type="type" :id="lowerCaseLabel"
      class="bg-transparent border-2 border-grey-400 rounded-md py-1 px-2 outline-none" :class="className" :value="value"
      @keyup="changeHandler" :placeholder="placeholder" />

    <textarea v-else :id="lowerCaseLabel"
      class="bg-transparent border-2 border-grey-400 rounded-md py-1 px-2 outline-none" :class="className"
      @keyup="changeHandler" :value="value" :placeholder="placeholder" cols="25" rows="3"></textarea>
  </div>
</template>
