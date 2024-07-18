import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import VueI18n from 'vue-i18n';
import messages from '@/i18n';

Vue.use(Vuetify);
Vue.use(VueI18n);


const i18n = new VueI18n({
    locale: 'zh', // 设置默认语言为中文
    messages, // 使用上面加载的语言文件
  });
  
const vuetify =  new Vuetify({
    lang: {
      t: (key, ...params) => i18n.t(key, params), // 使用 VueI18n 的 t 方法
    },
  });


export {vuetify, i18n};