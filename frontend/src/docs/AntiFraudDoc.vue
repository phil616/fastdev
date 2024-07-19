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
          "1. 简介": "反诈骗策略是我们为打击网络诈骗犯罪,保护用户权益而制定的一套方针和措施。我们致力于为用户提供安全可靠的网络环境,防范各类诈骗行为。",
          "2. 服务方义务": "作为互联网服务提供商,我们有义务采取必要的技术和管理手段,防范和打击利用我们平台实施的各类诈骗犯罪行为。这包括:\
          - 建立健全的用户实名认证机制,加强用户身份核验\
          - 完善异常交易监测和风险预警机制,及时发现和处置可疑交易\
          - 配合相关部门开展反诈骗调查取证工作,协助警方打击犯罪\
          - 开展反诈骗宣传教育,提高用户防骗意识和能力",
          "3. 用户责任": "用户在使用我们的服务时,应当遵守国家法律法规和平台规则,不得利用平台实施任何诈骗犯罪。这包括但不限于:\
          - 不得冒充他人身份注册账号,从事虚假交易\
          - 不得发布虚假信息,传播诈骗内容\
          - 不得通过平台向他人索要财物,实施网络诈骗\
          - 如发现他人利用平台实施诈骗,应及时向平台和警方举报\
      用户应当妥善保管自己的账号密码,不轻易泄露给他人。因账号密码泄露而造成的损失,平台不承担责任。",
          "4. 反诈骗形势": "当前,新型网络诈骗手法层出不穷,给广大用户造成了严重的财产损失,也严重影响了互联网行业的健康发展。常见的诈骗类型包括:\
          - 虚假投资理财、借贷等;\
          - 冒充公检法实施诈骗;\
          - 网络刷单、兼职等;\
          - 虚假购物、抽奖中奖;\
          - 网络交友、婚恋诈骗等。\
      防范网络诈骗,需要全社会共同努力。我们也呼吁广大用户提高警惕,谨慎交友,理性消费,不轻信来历不明的信息,保护好自己的财产安全。"
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