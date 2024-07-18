<template>
  <div>
    <v-carousel cycle height="400" hide-delimiter-background show-arrows-on-hover>
      <v-carousel-item v-for="(slide, i) in slides" :key="i">
        <v-img :src="getImageUrl(slide.image)" height="100%">
          <v-container fill-height>
            <v-layout align-center>
              <v-flex>
                <h3 class="display-3 white--text mb-3">{{ slide.title }}</h3>
                <p class="headline white--text">{{ slide.text }}</p>
              </v-flex>
            </v-layout>
          </v-container>
        </v-img>
      </v-carousel-item>
    </v-carousel>


    <v-container>
      <v-row>
        <v-col cols="12" class="text-center">
          <h1 class="display-2 mb-3">Welcome to Our Company</h1>
          <p class="subtitle-1">We are a leading provider of innovative solutions.</p>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="12" md="4">
          <v-card>
            <v-img src="https://example.com/service1.jpg" height="200px" @error="onImageError"></v-img>
            <v-card-title>Service 1</v-card-title>
            <v-card-text>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam mauris neque, bibendum vitae magna at, rhoncus volutpat metus.
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" md="4">
          <v-card>
            <v-img src="https://example.com/service2.jpg" height="200px" @error="onImageError"></v-img>
            <v-card-title>Service 2</v-card-title>
            <v-card-text>
              Sed euismod, nulla sit amet aliquam lacinia, nisl nisl aliquam nisl, nec aliquam nisl nisl sit amet nisl. Sed euismod, nulla sit amet aliquam lacinia.
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" md="4">
          <v-card>
            <v-img src="https://example.com/service3.jpg" height="200px" @error="onImageError"></v-img>
            <v-card-title>Service 3</v-card-title>
            <v-card-text>
              Praesent vel lorem euismod, aliquam velit vel, placerat velit. Praesent vel lorem euismod, aliquam velit vel, placerat velit.
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
          image: 'slide1.jpg',
          title: 'Slide 1',
          text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
        },
        {
          image: 'slide2.jpg',
          title: 'Slide 2',
          text: 'Sed euismod, nulla sit amet aliquam lacinia, nisl nisl aliquam nisl.'
        },
        {
          image: 'slide3.jpg',
          title: 'Slide 3',
          text: 'Praesent vel lorem euismod, aliquam velit vel, placerat velit.'
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