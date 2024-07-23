<template>
    <v-container>
      <v-row align="center" justify="center">
        <v-col cols="12" md="8">
          <h1 class="text-center mb-4">系统状态</h1>
          <v-card>
            <v-card-text>
              <v-row
              v-for="(item, i) in items"
              :key="i">
                <v-col>
                  <v-card :color="getColor(item.serverStatus)" dark>
                    <v-card-title>{{item.serverName}}</v-card-title>
                    <v-card-text>
                      <v-icon size="64" class="mb-2">mdi-server</v-icon>
                      <p class="text-h5">{{ item.serverStatus }}</p>
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
        items: [
          {
            serverName: 'API',
            serverStatus: 'error',
            serverId: '1'
          },
          {
            serverName: 'OSS',
            serverStatus: 'error',
            serverId: '2'
          },
          {
            serverName: 'Blog Server',
            serverStatus: 'error',
            serverId: '3'
          },
          {
            serverName: 'Authorization Server',
            serverStatus: 'error',
            serverId: '4'
          },
          {
            serverName: 'Basic Resource Server',
            serverStatus: 'error',
            serverId: '5'
          },
          {
            serverName: 'VPN Server',
            serverStatus: 'error',
            serverId: '6'
          },
        ]
      };
    },
    methods: {
      getColor(status) {
        return status === 'Operational' ? 'green' : 'red';
      },
      fetchServerStatus() {
        // get server status
      }
    },
    mounted() {
      this.fetchServerStatus();
    }
  };
  </script>