<template>
  <IndexView />
</template>

<script>
import IndexView from '@/pages/IndexView.vue';

export default {
  name: 'App',

  components: {
    IndexView,
  },

  data: () => ({
    //
  }),
  
  created() {
    this.$store.dispatch('initGlobalTextDict',{
      "title":"Galaxy Solutions",
      "routers":{
        "Home":"home",
        "Projects":"projects",
        "Notifications": "notifications",
        "Productions": "productions",
        "About us": "aboutus",
      },
      "projectName":"Galaxy Solutions",
      "projectVersion":"0.0.1",
      "referer":"https://greenshadecapital.com"
    })
  }
};
</script>
