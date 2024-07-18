<template>
    <v-app>
      <v-app-bar app color="primary" dark    clipped-left >
        <v-btn icon @click="changeDrawerStatus"><svg-icon type="mdi" @click="changeDrawerStatus" :path="path"></svg-icon></v-btn>
        <div class="d-flex align-center">
          <v-app-bar-title class="text-h6">
             {{ $t('message.application') }}
          </v-app-bar-title>
        </div>
  
        <v-spacer></v-spacer>

          <LanguageSwitcher />
            <div style="width: 2%;"></div>
          <ThemeSwithcer />
      </v-app-bar>

      
    <v-navigation-drawer 
        v-model="isGlobalDrawerSwitchOn"
        app
        temporary
        clipped
        height="100rm"
      >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            {{ $t('message.application') }}
          </v-list-item-title>
          <v-list-item-subtitle>
            {{ $t('message.startup') }}
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>
      <v-list-item-content>
          <v-list-item-title>

            <v-btn @click="drawerback">
              <v-icon>mdi-arrow-left</v-icon>
              {{ $t('message.drawback') }}
            </v-btn>
            
          </v-list-item-title>
        </v-list-item-content>
      <v-divider></v-divider>

      <v-list
        dense
        nav
      >
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title @click="linkto(item.link)">{{ $t('message.routers.' + item.title) }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    
  
      <v-main>
        <Header/>
        <router-view></router-view>
      </v-main>
      <Footer />
    </v-app>
  </template>
<script>
import SvgIcon from '@jamescoyle/vue-icon';
import { mdiMenuClose } from '@mdi/js';

import Header from '@/components/HeaderPage.vue';
import LanguageSwitcher from '@/components/LanguageSwitcher.vue';
import ThemeSwithcer from '@/components/ThemeSwithcer.vue';
import Footer from '@/components/FooterPage.vue';
import { isNavigationFailure,NavigationFailureType } from 'vue-router';

export default {
  name: 'IndexView',

  components: {
    Header,
    Footer,
    ThemeSwithcer,
    SvgIcon,
    LanguageSwitcher,
  },

  methods: {
    linkto(link){
    this.$router.push({ path: link }).catch(err => {
      if (!isNavigationFailure(err, NavigationFailureType.duplicated)) {
        throw err;
      }
    });
    this.changeDrawerStatus()
    },
    computeRouter(){
      var routeMap = {}
      this.$router.getRoutes().forEach(route => {

        let routekey = String(route.path).replace("/","")
        //exclude [*, "", VuePrototype, Chlildren]
        if(!(routekey == "" || routekey == "*" || routekey == "singleDoc")&&route.parent == undefined){
          routeMap[route.name] = routekey;
        }
      })
      return routeMap;
    },
    changeDrawerStatus(){
      this.$store.dispatch('toggleglobalDrawerSwitch');
    },
    switchTheme(){
      this.$attrs.theme = !this.$attrs.theme
    },
    drawerback(){
      this.$store.dispatch('toggleglobalDrawerSwitch');
    }
  },
  computed: {
    // 使用计算属性来获取全局开关状态
    isGlobalDrawerSwitchOn:{
      get(){
        return this.$store.state.globalDrawerSwitch;
      },
      set(val){
        //
        val;
      }
    }
  },

  data: () => ({
    //
    path: mdiMenuClose,
    items: [],
  }),

  created(){

    let map = this.computeRouter()
    Object.keys(map).forEach(key => {
      this.items.push({"title":key,
        icon: "mdi-home",
        link: "/" + String(map[key])
      })
    })

  }
};
</script>
