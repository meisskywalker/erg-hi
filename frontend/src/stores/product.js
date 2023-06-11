import axios from 'axios';
import { defineStore } from 'pinia';
import router from '../router';

export const useProductStore = defineStore('products', {
  state: () => ({
    products: [],
    product: {},
    tdidf: {},
  }),
  actions: {
    async getAll() {
      try {
        const response = await axios.get('/products');
        const data = await response.data;
        if (response.status === 200) {
          this.products = [...data];
        }
      } catch (err) {
        console.error('[ERROR]: ' + err);
      }
    },
    async getOneById(payload) {
      try {
        const response = await axios.get(`/products/${payload.id}`);
        const data = await response.data;
        if (response.status === 200) {
          this.product = data;
        }
      } catch (err) {
        console.error('[ERROR]: ' + err);
      }
    },
    async getTfIdf(payload) {
      try {
        const response = await axios.get('/products/tfidf', {
          params: {
            query: payload.query,
          },
        });
        const data = await response.data;
        if (response.status === 200) {
          this.tdidf = { ...data };
        }
      } catch (err) {
        console.error('[ERROR]: ' + err);
      }
    },
    async create(payload) {
      try {
        const response = await axios.post('/products', payload, {
          headers: {
            Authorization: `Bearer ${$cookies.get('token')}`,
          },
        });
        if (response.status === 201) {
          router.push({ name: 'AdminProductList' });
        }
      } catch (err) {
        console.error('[ERROR]: ' + err);
      }
    },
    async update(id, payload) {
      try {
        const response = await axios.put(`/products/${id}`, payload, {
          headers: {
            Authorization: `Bearer ${$cookies.get('token')}`,
          },
        });
        if (response.status === 202) {
          router.push({ name: 'AdminProductEdit', params: { productId: id } });
        }
      } catch (err) {
        console.error('[ERROR]: ' + err);
      }
    },
  },
});
