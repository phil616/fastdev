<template>
  <footer class="footer">
    <div class="footer-bottom">
      <p>&copy; {{ new Date().getFullYear() }}
        <a v-for="(item, index) in footerLinks" :key="index" :href="item.link" class="a"><span class="footer-ref">{{ item.name }} </span></a>
      </p>
      <div class="social-icons">
        <a href="#">微博</a>
        <a href="#">知乎</a>
        <a href="#">LinkedIn</a>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  data(){
    return {
        footerLinks:[
            {
                name: "隐私政策",
                link: "https://www.cloudflare.com/zh-cn/privacypolicy/"
            },
            {
                name: "使用条款",
                link: "https://www.cloudflare.com/zh-cn/terms/"
            },
            {
                name: "隐私政策",
                link: "https://www.cloudflare.com/zh-cn/privacypolicy/"
            },
            {
                name: "使用条款",
                link: "https://www.cloudflare.com/zh-cn/terms/"
            }
        ]
    };
  }
}
</script>

<style scoped>
.footer {
  background-color: #282c34;
  color: white;
  padding: 20px;

}
.a {
    text-decoration: none;
}
.footer-ref{
  color: white;
}
p {
    font-size: 14px;
}
.social-icons {
  margin-top: 10px;
}

@media (min-width: 768px) {
  .footer-ref {
    flex-direction: row;
    justify-content: space-around;
  }

  .footer-section {
    border: none;
    padding: 0;
  }

  .footer-title {
    margin-bottom: 10px;
  }
}
</style>
