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
            <p>{{ content }} </p>
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
        "title": "Cookie协议",
        "content": {
          "1. 什么是Cookie": "Cookie是服务器存储在用户设备上的小型文本文件,用于识别用户身份、保存用户偏好设置等用途。",
          "2. 我们使用Cookie的目的": "我们使用Cookie来为您提供个性化的服务体验,例如记住您的登录状态、语言偏好等,以及用于网站流量统计分析。",
          "3. Cookie的类型": "我们使用的Cookie分为会话Cookie和持久性Cookie。会话Cookie在您关闭浏览器后自动删除,持久性Cookie则会保留一段时间。",
          "4. 第三方Cookie": "我们的网站可能会嵌入第三方内容或服务,他们可能会设置自己的Cookie。这些Cookie不受我们控制,请您查看第三方的Cookie政策。",
          "5. 如何管理Cookie": "大部分浏览器默认允许Cookie。您可以在浏览器设置中查看、管理或删除Cookie。但请注意,禁用Cookie可能会影响网站的某些功能。",
          "6. 敏感个人信息": "我们不会将Cookie用于存储姓名、地址等敏感个人信息。涉及个人敏感信息的内容,我们会征得您的明示同意。",
          "7. 未成年人保护": "如果您是未满14周岁的未成年人,请在监护人指导下使用Cookie。我们不会主动收集未成年人的个人信息。",
          "8. 免责声明": "如果您选择禁用Cookie,可能导致某些功能无法正常使用。由此给您带来的不便,敬请谅解。"
        }
      }
    };
  },
  created() {
    this.fetchTermsOfService();
  },
  methods: {
    fetchTermsOfService() {
      http.get('/doc/manageCookie').then(res => {
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