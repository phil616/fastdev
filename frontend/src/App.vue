<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">
        <v-app-bar-nav-icon @click="change_drawer_state" />
      </div>

      <v-spacer></v-spacer>

      <v-btn href="https://github.com/vuetifyjs/vuetify/releases/latest" target="_blank" text >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>
    <Navigator/>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import Navigator from './components/NavigatorPage.vue';
export default {
  name: 'App',

  components: {
    Navigator,
  },

  data: () => ({
    //
  }),
  methods: {
    change_drawer_state() {
      console.log('change_drawer_state')
      this.$store.dispatch('toggle_navigator_drawer');
    },
  },
};
</script>