<template>
  <div>
    <v-container>
      <!-- 图片居中盒子 -->
       <div style="" class="d-flex justify-center">
        <v-img src="../assets/header2.png" height="100%"></v-img>
       </div>
      </v-container>

    <v-container>
      <v-row>
        <v-col cols="12" class="text-center">
          <h1 class="display-2 mb-3">{{$t('message.main.title')}}</h1>
          <p class="subtitle-1">绿荫三期项目个人合作者</p>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="12" md="4">
          <v-card>
            <v-img src="../assets/header1.png" height="100%"></v-img>
            <v-card-title>Green Shade Services</v-card-title>
            <v-card-text>
              Sed euismod, nulla sit amet aliquam lacinia, nisl nisl aliquam nisl, nec aliquam nisl nisl sit amet nisl. Sed euismod, nulla sit amet aliquam lacinia.
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      slides: [
        {
          image: 'header1.png',
        },
        {
          image: 'header2.png',
        }
      ],
      defaultImage: require('@/assets/default.jpg')
    };
  },
  methods: {
    getImageUrl(image) {
      try {
        return require(`@/assets/${image}`);
      } catch (error) {
        return this.defaultImage;
      }
    }
  }
};
</script>