import Vue from 'vue';
import App from '@/App.vue';
import router from '@/router';
import store from '@/store';
import { vuetify,i18n } from '@/plugins/vuetify';


new Vue({
  i18n,
  store,
  router,
  el: '#app',
  vuetify,
  render: h => h(App)
});
