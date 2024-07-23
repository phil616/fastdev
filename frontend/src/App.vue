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
      "routers":{
        "Home":"home",
        "Projects":"projects",
        "Notifications": "notifications",
        "Productions": "productions",
        "About us": "aboutus",
      },
    })
  }
};
</script>
