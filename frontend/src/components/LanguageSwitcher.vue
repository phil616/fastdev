<template>
   <div class="text-center">
    <v-menu offset-y>
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="primary"
          dark
          v-bind="attrs"
          v-on="on"
        >
        <svg-icon type="mdi" :path="path"></svg-icon>
        
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="(item, index) in items"
          :key="index"
          @click="switchLanguage(item.lang)"
        >
          <v-list-item-title>{{ item.name }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </div>
  </template>
  
  <script>
import SvgIcon from '@jamescoyle/vue-icon';
import { mdiTranslate } from '@mdi/js';
  export default {
    components: {
      SvgIcon
    },
    name:"LanguageSwitcher",
    methods: {
      switchLanguage(lang) {
        this.$i18n.locale = lang;
      }
    },
    data: () => ({
      path: mdiTranslate,
      items: [
        { lang: 'zh',name:'切换为中文' },
        { lang: 'en',name:'switch to English' },
      ],
    }),
  }
  </script>
