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
      defaultTermsOfService: {
        title: "联系我们",
        content: {
          "1. 平台沟通": "在此平台反馈",
          "2. 工单反馈": "您可使用工单反馈功能来提交反馈。",
          "3. 邮箱": "我们的邮箱为：<EMAIL>",
        },
      }
  }},
  created() {
    this.fetchTermsOfService();
  },
  methods: {
    fetchTermsOfService() {
      http.get('/doc/contact').then(res => {
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