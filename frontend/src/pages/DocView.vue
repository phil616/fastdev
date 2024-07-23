<template>
    <div>
        <v-container>
            <v-row>
              <v-col>
                <v-card class="pa-5">
                  <v-card-title>
                    <v-row>
                      <v-col class="text-left">
                        <h1 class="display-1"> {{ title }}</h1>
                      </v-col>
                    </v-row>
                </v-card-title>
    <v-list dense>
      <v-list-item-group
        color="primary"
      >
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
        >
          <v-list-item-icon>
            <svg-icon type="mdi" :path="path"></svg-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title v-text="item.text" @click="goHref(item.href)"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
            </v-card>
        </v-col>
        </v-row>
    </v-container>
    <router-view></router-view>
        
    </div>

</template>

<script>
import SvgIcon from '@jamescoyle/vue-icon';
import { mdiTextAccount } from '@mdi/js';
import defaultText from '@/utils/docs.js'
import { isNavigationFailure,NavigationFailureType } from 'vue-router';

export default {
    // doc?name=xxx
    name: 'DocView',
    data:() => ({
        title:"Doc Center",
        path: mdiTextAccount,
        items: [],

    }),
    components: { SvgIcon },
    created() {
        //render all key
        let prefix = "/singleDoc?name="
        let keys = Object.keys(defaultText)
        keys.forEach(key => {
            if(this.$te("message.footers."+key)){
                this.items.push({text: this.$t("message.footers."+key),href:prefix+key})
            }else if(this.$te("message.footerLabels."+key)){
                this.items.push({text:this.$t("message.footerLabels."+key),href:prefix+key})
            }else{
                this.items.push({text:key})
            }
        })
    },
    methods: {
        goHref(link){
        this.$router.push({path: link}).catch(err => {
        if (!isNavigationFailure(err, NavigationFailureType.duplicated)) {
            throw err;
        }
        });
    },
    }
}


</script>