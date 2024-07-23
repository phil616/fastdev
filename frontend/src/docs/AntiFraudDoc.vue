<template>
    <v-card-text>
      <v-container>
          <v-alert
          v-show="error"
          border="bottom"
          colored-border
          type="warning"
          elevation="5"
          >
          {{ errorMsg }}.<br> {{$t('message.errorMsg.contentError')}}
          </v-alert>
        <v-row v-for="(content, title) in termsOfService.content" :key="title">
          <v-col>
            <h3>{{ title }}</h3>
            <p> {{ content }} </p>
          </v-col>
        </v-row>
      </v-container>
    </v-card-text>
</template>

<script>
import http from '@/http';
export default {
  data() {
    return {
      error:false,
      errorMsg:"",
      termsOfService: {
        title: "",
        content: {}
      },
      defaultTermsOfService: 
        {
        "title": "反诈骗",
        "content": {
          "1. 简介": "用户未更新反欺诈协议",
        }
      }
            
    };
  },
  created() {
    this.fetchTermsOfService();
  },
  methods: {
    fetchTermsOfService() {
      http.get('/doc/anti-fraud').then(res => {
          this.termsOfService = res.data;
      }).catch(err => {
          console.log(err)
          this.errorMsg = err.message;
          this.error = true;
          this.termsOfService = this.defaultTermsOfService;
      })
    }
  }
};
</script>