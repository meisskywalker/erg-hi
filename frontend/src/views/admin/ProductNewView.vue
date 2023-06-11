<script setup>
import PlusIcon from '../../components/icons/PlusIcon.vue';
import ArrowLeftIcon from '../../components/icons/ArrowLeftIcon.vue';
import InputWithLabel from '../../components/inputs/InputWithLabel.vue';
import SectionTitle from '../../components/admin/SectionTitle.vue';
import BasicButton from '../../components/inputs/BasicButton.vue';

import { useRoute, useRouter } from 'vue-router';
import { reactive } from 'vue';

import { useProductStore } from '../../stores/product';

const router = useRouter();
const route = useRoute();
const productStore = useProductStore();

const { productId } = route.params;

const data = reactive({
  title: { value: '' },
  author: { value: '' },
  'demo link': { value: '' },
  'journal link': { value: '' },
  'video link': { value: '' },
  description: { value: '' },
});

const submit = () => {
  if (productId) {
    productStore.update(productId, {
      title: data.title.value,
      author: data.author.value,
      demo_link: data['demo link'].value,
      journal_link: data['journal link'].value,
      video_link: data['video link'].value,
      description: data.description.value,
    });
  } else {
    productStore.create({
      title: data.title.value,
      author: data.author.value,
      demo_link: data['demo link'].value,
      journal_link: data['journal link'].value,
      video_link: data['video link'].value,
      description: data.description.value,
    });
  }
};

const reset = () => {
  data.title.value = '';
  data.author.value = '';
  data['demo link'].value = '';
  data['journal link'].value = '';
  data['video link'].value = '';
  data.description.value = '';
};

const update = (payload) => {
  Object.keys(payload).forEach((payloadKey) => {
    Object.keys(data).forEach((key) => {
      if (key == payloadKey) {
        data[key].value = payload[key].value;
      }
    });
  });
};

const back = () => {
  router.go(-1);
};
</script>

<template>
  <section-title with-button>
    <template #icon>
      <plus-icon size="28" />
    </template>
    Add Products
    <template #buttons>
      <basic-button class-name="bg-red-500 text-grey-200" @click="back">
        <arrow-left-icon size="24" />
        Back
      </basic-button>
    </template>
  </section-title>
  <div class="bg-grey-50 rounded-md my-8 flex flex-col p-4 gap-2">
    <input-with-label
      label="Title"
      type="text"
      @update="update"
      :value="data.title.value"
    />
    <input-with-label
      label="Author"
      type="text"
      @update="update"
      :value="data.author.value"
    />
    <input-with-label
      label="Demo Link"
      type="text"
      @update="update"
      :value="data['demo link'].value"
    />
    <input-with-label
      label="Journal Link"
      type="text"
      @update="update"
      :value="data['journal link'].value"
    />
    <input-with-label
      label="Video Link"
      type="text"
      @update="update"
      :value="data['video link'].value"
    />
    <input-with-label
      label="Description"
      type="textarea"
      @update="update"
      :value="data.description.value"
    />
    <div class="flex justify-start items-centeri gap-2">
      <basic-button class-name="bg-brand-500 text-grey-200" @click="submit">
        Submit
      </basic-button>
      <basic-button
        class-name="bg-transparent border border-brand-500 text-brand-500"
        @click="reset"
      >
        Reset
      </basic-button>
    </div>
  </div>
</template>
