<template>
    <div>
      <v-container>
        <v-row>
          <v-col>
            <v-card class="pa-5">
              <v-card-title>
                <v-row>
                  <v-col class="text-left">
                    <h1 class="display-1">{{ $t('message.doc.' + name) }}</h1>
                  </v-col>
                </v-row>
              </v-card-title>
              <v-card-text>
                <div class="text-justify">
                  <component :is="currentComponent" v-if="currentComponent" />
                  <div v-else>No component specified.</div>
                </div>
                </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </template>
  
  <script>
  import TermsDoc from '@/docs/TermsDoc.vue';
  import PrivacyDoc from '@/docs/PrivacyDoc.vue';
  import ContactDoc from '@/docs/ContactDoc.vue';
  import SecurityDoc from '@/docs/SecurityDoc.vue';
  import StatusDoc from '@/docs/StatusDoc.vue';
  import ManageCookiesDoc from '@/docs/ManageCookiesDoc.vue';
  import ReportDoc from '@/docs/ReportDoc.vue';
  import IcpDoc from '@/docs/IcpDoc.vue';
  import FilingDoc from '@/docs/FilingDoc.vue';
  import AntiFraudDoc from '@/docs/AntiFraudDoc.vue';
  import DocsDoc from '@/docs/DocsDoc.vue';
  export default {
    components:{
      TermsDoc,
      PrivacyDoc,
      ContactDoc,
      SecurityDoc,
      StatusDoc,
      ManageCookiesDoc,
      IcpDoc,
      FilingDoc,
      AntiFraudDoc,
      DocsDoc,
      ReportDoc,
    },
    watch: {
    '$route.query.name': {
      immediate: true,
      handler() {
        this.name = this.$route.query.name;
       
      },
    },
  },
    data:() => ({
      content:'',
    }),
    methods:{
      
    },
    computed: {
    currentComponent() {
      const name = this.$route.query.name;
      return name ? this.$options.components[name] : null;
    },
  },
  }
  </script>