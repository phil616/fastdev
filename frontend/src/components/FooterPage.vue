<template>
  <v-footer dark height="auto">
    <v-container fluid>
      
      <v-layout row wrap justify-space-between class="py-4">
        <v-row>
          <v-col>
        <v-flex xs12 md3>
          
          <div class="footer-header mb-2">{{$t('message.footers.Product')}}</div>
          <ul class="footer-list">

            <li><a href="/redirect?gs=policy">{{$t('message.gs.policy')}}</a></li>
            <li><a href="/redirect?gs=education">{{$t('message.gs.education')}}</a></li>
            <li><a href="/redirect?gs=financial">{{$t('message.gs.financial')}}</a></li>
            <li><a href="/redirect?gs=general">{{$t('message.gs.general')}}</a></li>
          </ul>
        </v-flex>
      </v-col>
      <v-col>
        <v-flex xs12 md3>
          <div class="footer-header mb-2">{{ $t('message.footers.Platform') }}</div>  
          <ul class="footer-list">
            <li><a href="/redirect?gs=openapi">{{$t('message.gs.openapi')}}</a></li>
            <li><a href="/redirect?gs=cooperate">{{$t('message.gs.cooperate')}}</a></li>
            <li><a href="/redirect?gs=oa">{{$t('message.gs.oa')}}</a></li>
            <li><a href="/redirect?gs=system">{{$t('message.gs.system')}}</a></li>
          </ul>
        </v-flex>
      </v-col>
      <v-col>
        <v-flex xs12 md3>
          <div class="footer-header mb-2">{{ $t('message.footers.Support') }}</div>
          <ul class="footer-list">
            <li><a href="/redirect?gs=docs">{{$t('message.gs.docs')}}</a></li>
            <li><a href="/redirect?gs=github">{{$t('message.gs.github')}}</a></li>
            <li><a href="/redirect?gs=contact">{{$t('message.gs.contact')}}</a></li>
            <li><a href="/redirect?gs=report">{{$t('message.gs.report')}}</a></li>
          </ul>  
        </v-flex>
      </v-col>
      <v-col>
        <v-flex xs12 md3>
          <div class="footer-header mb-2">{{ $t('message.footers.Company') }}</div>
          <ul class="footer-list">
            <li><a href="/redirect?gs=fund">{{$t('message.gs.fund')}}</a></li>
            <li><a href="/redirect?gs=website">{{$t('message.gs.website')}}</a></li>
            <li><a href="/redirect?gs=dept">{{$t('message.gs.dept')}}</a></li>
            <li><a href="/redirect?gs=inspect">{{$t('message.gs.inspect')}}</a></li>
          </ul>
        </v-flex>
      </v-col>
      </v-row>
      </v-layout>
      
      <v-divider class="mt-4 mb-4"></v-divider>
      
      <v-layout row wrap>
        <v-flex xs12 md6 class="text-xs-center text-md-left">
          <div>
            © {{ new Date().getFullYear() }} {{$store.state.globalTextDict.projectName}} All Rights Reserved.
          </div>
          <ul class="footer-bottom-list mt-2">
            <li><a href="/singleDoc?name=TermsDoc">{{$t('message.footers.terms')}}</a></li>
            <li><a href="/singleDoc?name=PrivacyDoc">{{$t('message.footers.privacy')}}</a></li>
            <li><a href="/singleDoc?name=ContactDoc">{{$t('message.footers.contact')}}</a></li>
            <li><a href="/singleDoc?name=SecurityDoc">{{$t('message.footers.security')}}</a></li>
            <li><a href="/singleDoc?name=StatusDoc">{{$t('message.footers.status')}}</a></li>
            <li><a href="/singleDoc?name=ManageCookiesDoc">{{$t('message.footers.manageCookies')}}</a></li>
            <!--
                        <li><a href="/singleDoc?name=IcpDoc">{{$t('message.footers.icp')}}</a></li>
            -->
            <li><a href="/singleDoc?name=FilingDoc">{{$t('message.footers.filing')}}</a></li>
            <li><a href="/singleDoc?name=AntiFraudDoc">{{$t('message.footers.anti-fraud')}}</a></li>
            <li><a href="/singleDoc?name=DocsDoc">{{$t('message.footers.docs')}}</a></li>
            <li><a href="/singleDoc?name=ReportDoc">{{$t('message.footers.report')}}</a></li>
            
          </ul>
        </v-flex>
      </v-layout>
      
      <v-layout row wrap>
        <v-flex xs12 md6 class="text-xs-center text-md-left">
          <ul class="footer-bottom-list mt-2">
            <li><img :src="icpImage" style="width: 8%;"><a href="https://beian.mps.gov.cn/#/query/webSearch?code=22011302000114" rel="noreferrer" target="_blank">{{$store.state.globalTextDict.icpa}}</a></li>
            <li><a href="https://beian.miit.gov.cn/" rel="noreferrer" target="_blank">{{$store.state.globalTextDict.icp}}</a></li>
            
          </ul>
        </v-flex>
      </v-layout>
    </v-container>
  </v-footer>
</template>

<style scoped>
.footer-header {
  color: white;
  font-size: 16px;
  font-weight: bold;
}

.footer-list {
  padding: 0;
  list-style-type: none;
  font-size: 14px;  
}

.footer-list li {
  margin-bottom: 10px;
}

.footer-list a {
  color: #959da5;
  text-decoration: none;  
}
.footer-list a:hover {
  color: #2196f3;
}

.footer-bottom-list {
  padding: 0;
  list-style-type: none;
  font-size: 12px;
}

.footer-bottom-list li {
  margin: 0;
  display: inline-block;
  padding-right: 16px;
}

.footer-bottom-list a {
  color: #959da5;
  text-decoration: none;
}

.footer-bottom-list a:hover {
  color: #2196f3; 
}

a .v-icon {
  color: #959da5;
  font-size: 24px;
}

a:hover .v-icon {  
  color: #2196f3;
}
</style>

<script>

export default {
  data: () => ({
    icpImage: require('../assets/icp.png'),
  }),

}
</script>