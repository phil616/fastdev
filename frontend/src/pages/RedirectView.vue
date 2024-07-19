<template>
    <v-container>
      <v-row justify="center">
        <v-col cols="12" sm="8" md="6">
          <v-card>
            <v-card-title class="headline">
              {{ $t('message.redirect.header') }}
            </v-card-title>
            <v-card-text>
               {{$t('message.redirect.content')}} {{ name }}
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary" @click="redirect">确定</v-btn>
              <v-btn color="secondary" @click="goBack">取消</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        name: '',
      };
    },
    created() {
      const urlParams = new URLSearchParams(window.location.search);
      this.name = urlParams.get('gs') || '';
    },
    methods: {
      redirect() {
        if (this.name) {
          window.location.href = `${this.$store.state.globalTextDict.referer}/link?name=${this.name}`;
        }
      },
      goBack() {
        window.history.back();
      },
    },
  };
  </script>