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
        title: "举报条款",
        content: {}
      },
      defaultTermsOfService: {
          title: "举报条款",
          content: {
            "1. 用户义务": "用户有义务向平台举报各类违法违规信息和行为,包括但不限于传播违法信息、侵犯他人权益、危害网络安全等行为。",
            "2. 举报范围": "用户应当举报平台内发现的各类不良信息,包括色情、暴力、谣言、诈骗、侵权、违禁品交易信息等。",
            "3. 举报方式": "用户可以通过平台的举报入口提交举报,需提供被举报内容的链接地址、截图等证据材料。",
            "4. 平台处理": "我们会对收到的举报信息进行核实,对确认属实的违法违规信息予以删除处置,并视情节轻重对相关账号进行警告、限制、冻结或永久封禁。",  
            "5. 举报奖励": "为鼓励用户参与平台治理,我们将根据举报成功次数、违规严重程度等,给予用户一定的现金奖励或会员积分等激励措施。",
            "6. 恶意举报": "对于恶意举报、骚扰举报等违反诚信原则的行为,我们将视情节对相关账号予以警告、限制、冻结直至永久封禁。",
            "7. 免责声明": "用户在举报时应当提供客观真实的材料,对于用户举报内容的真实性、准确性、合法性等,平台不承担审核义务和连带责任。"
          }
        }
      }
  },
  created() {
    this.fetchTermsOfService();
  },
  methods: {
    fetchTermsOfService() {
      http.get('/doc/report').then(res => {
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