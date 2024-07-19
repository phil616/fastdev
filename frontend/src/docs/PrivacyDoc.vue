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
          "title": "隐私协议",
          "content": {
            "1. 我们收集的信息": "我们收集您提供的注册信息、浏览记录、位置信息、设备信息等,以便为您提供更好的服务。",
            "2. 信息的使用方式": "我们使用收集的信息为您提供个性化推荐、发送服务通知、开展内部数据分析等,以改进我们的产品和服务。",
            "3. 信息共享": "未经您同意,我们不会与第三方共享您的个人信息,但法律法规要求或为保护我方权益而必须共享的除外。",
            "4. 信息的保护": "我们会采取各种安全技术和措施来保护您的个人信息,防止信息的丢失、不当使用、未经授权访问或披露。",
            "5. 您的权利": "您有权访问、更正、删除您的个人信息,也可以撤回此前同意我们收集和使用个人信息的授权。",
            "6. 未成年人保护": "我们非常重视对未成年人个人信息的保护。如您是未满14周岁的儿童,需要在监护人指导下使用我们的服务。",
            "7. 隐私政策的修订": "我们可能会不时修订隐私政策,所有修订将在页面公布。如有重大变更,我们还会通过推送通知等方式告知您。",
            "8. 联系我们": "如您对隐私政策有任何疑问、意见或建议,请通过页面列出的联系方式与我们联系。"
          }
        }
      };
    },
    created() {
      this.fetchTermsOfService();
    },
    methods: {
      fetchTermsOfService() {
        http.get('/doc/privacy').then(res => {
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