<template>
    <div>
      <v-container>
        <v-row>
          <v-col>
            <v-card class="pa-5">
              <v-card-title>
                <v-row>
                  <v-col class="text-left">
                    <h1 class="display-1">{{ name }}</h1>
                  </v-col>
                </v-row>
              </v-card-title>
              <v-card-text>
                <div class="text-justify">
                  {{ content }}
                </div>
                </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </template>
  
  <script>
  import http from '@/http'
  import defaultText from '@/utils/docs'
  export default {
    watch: {
    '$route.query.name': {
      immediate: true,
      handler() {
        this.name = this.$route.query.name;
        this.fetchFromSource();
      },
    },
  },
    data:() => ({
      content:'',
    }),
    methods:{
      async fetchFromSource(){
        try{
          const resp = await http.get(`/api/docs/${this.$route.query.name}`)
          this.content = resp.data
        }catch(e){
          console.log(e)
          let name = this.$route.query.name;
          this.content = defaultText[name]
        }
      }
    },
    created(){
      this.name = this.$route.query.name;
      this.fetchFromSource();
    }
  }
  </script>