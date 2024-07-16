<template>
    <div>
    <v-footer
      dark
      bottom
      padless
    >
   


        <v-row
        v-for="item in footerLink"
        :key="item.name"
        justify="center"
        class="my-4 subheading mx-3"
        >
        <v-col class="subheading mx-3">
          <a class="white--text" @click="goHref(item.name)" target="_blank">
            {{ $t('message.footers.' + item.name) }}
          </a>
        </v-col>
        </v-row>

        <v-row
        v-for="item in footerLabel"
        :key="item.name"
        justify="center"
        class="my-4 subheading mx-3"
        >
        <v-col>
          <a class="white--text" @click="goHref(item.name)" target="_blank">
            {{ $t('message.footerLabels.'+item.name) }}
          </a>
        </v-col>
        </v-row>


        <v-container fluid>
        <v-card
    
    flat
    tile
    class="indigo lighten-1 white--text text-center"
  >
    <v-card-text>
      <v-btn
        v-for="icon in icons"
        :key="icon"
        class="mx-4 white--text"
        icon
      >
        <v-icon size="24px">
          {{ icon }}
        </v-icon>
      </v-btn>
    </v-card-text>
    <v-card-text class="white--text pt-0">
      {{$t('message.shareThisPage')}} | {{this.$store.state.globalTextDict.projectName}}{{ $t('message.footerLabels.allRightsReserved') }}
    </v-card-text>
    
    <v-divider></v-divider>
  </v-card>

    </v-container>

    </v-footer>
</div>
  </template>

<script>
import { isNavigationFailure,NavigationFailureType } from 'vue-router';

export default {
  data: () => ({
    projectName:"Vuetify.js",
    icons: [
      'mdi-facebook',
      'mdi-twitter',
      'mdi-linkedin',
      'mdi-instagram',
    ],
    items: [
        {
          text: 'Dashboard',
          disabled: false,
          href: 'breadcrumbs_dashboard',
        },
        {
          text: 'Link 1',
          disabled: false,
          href: 'breadcrumbs_link_1',
        },
        {
          text: 'Link 2',
          disabled: true,
          href: 'breadcrumbs_link_2',
        },],

        footerLink:[
          {name:"terms",href:"/"},
          {name:"privacy",href:"/"},
          {name:"contact",href:"/"},
          {name:"security",href:"/"},
          {name:"status",href:"/"},
          {name:"docs",href:"/"},
          {name:"manageCookies",href:"/"},
          {name:"report",href:""}
        ],
        footerLabel:[
          {name:"icp",href:"/"},
          {name:"copyRight",href:"/"},
          {name:"poweredBy",href:""},
          {name:"anti-fraud",href:"/"},
          {name:"filing",href:"/"},
        ],
  }),
  methods:{
    goHref(link){
      let prefix = "singleDoc?name="
    this.$router.push({ path: prefix+link }).catch(err => {
      if (!isNavigationFailure(err, NavigationFailureType.duplicated)) {
        throw err;
      }
    });
    }
  },
  computed:{
    links(){
      return Object.keys(this.$store.state.globalTextDict.routers);
    }
  }
}
</script>