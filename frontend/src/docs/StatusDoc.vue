<template>
    <v-container>
      <v-row align="center" justify="center">
        <v-col cols="12" md="8">
          <h1 class="text-center mb-4">系统状态</h1>
          <v-card>
            <v-card-text>
              <v-row>
                <v-col cols="12" md="4">
                  <v-card :color="getColor(apiServerStatus)" dark>
                    <v-card-title>API服务器</v-card-title>
                    <v-card-text>
                      <v-icon size="64" class="mb-2">mdi-server</v-icon>
                      <p class="text-h5">{{ apiServerStatus }}</p>
                    </v-card-text>
                  </v-card>
                </v-col>
                <v-col cols="12" md="4">
                  <v-card :color="getColor(contentServerStatus)" dark>
                    <v-card-title>内容服务器</v-card-title>
                    <v-card-text>
                      <v-icon size="64" class="mb-2">mdi-database</v-icon>
                      <p class="text-h5">{{ contentServerStatus }}</p>
                    </v-card-text>
                  </v-card>
                </v-col>
                <v-col cols="12" md="4">
                  <v-card :color="getColor(resourceServerStatus)" dark>
                    <v-card-title>资源服务器</v-card-title>
                    <v-card-text>
                      <v-icon size="64" class="mb-2">mdi-harddisk</v-icon>
                      <p class="text-h5">{{ resourceServerStatus }}</p>
                    </v-card-text>
                  </v-card>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        apiServerStatus: '',
        contentServerStatus: '',
        resourceServerStatus: ''
      };
    },
    methods: {
      getColor(status) {
        return status === 'Operational' ? 'green' : 'red';
      },
      fetchServerStatus() {
        // 模拟请求
        let response = {
            data: {
                apiServerStatus: 'Operational',
                contentServerStatus: 'Operational',
                resourceServerStatus: 'Operational'
            }
        }
        this.apiServerStatus = response.data.apiServerStatus;
        this.contentServerStatus = response.data.contentServerStatus;
        this.resourceServerStatus = response.data.resourceServerStatus;
      }
    },
    mounted() {
      this.fetchServerStatus();
    }
  };
  </script>