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
              <p> ERROR :"{{ content }}", </p>
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
          title: "服务条款",
          content: {
            "1. 接受条款": "在使用我们的服务之前,请务必仔细阅读这些条款。一旦您访问或使用我们的服务,即表示您同意受这些条款的约束。如果您不同意这些条款的任何部分,请勿使用我们的服务。",
            "2. 服务描述": "我们的服务包括但不限于通过我们的网站和移动应用程序提供的各种在线资源、工具和功能。我们保留随时修改、暂停或终止任何服务的权利,恕不另行通知。",
            "3. 用户账户": "为了访问某些服务,您可能需要创建一个用户账户。您有责任维护账户信息的机密性,并对通过您的账户进行的所有活动负责。如果您发现任何未经授权使用您账户的情况,请立即通知我们。",
            "4. 知识产权": "我们的服务和相关的所有内容、功能以及用户界面均归我们所有或由我们许可。这些材料受版权、商标和其他知识产权法的保护。未经我们明确书面许可,不得复制、修改、分发或以其他方式使用这些材料。"
          }
        }
      };
    },
    created() {
      this.fetchTermsOfService();
    },
    methods: {
      fetchTermsOfService() {
        http.get('/doc/terms-of-service').then(res => {
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