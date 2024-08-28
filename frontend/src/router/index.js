import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

const router = new Router({
  mode: 'history',
  base: process.env.VUE_APP_BASE_URL,

  routes: [
    {
        path: "/",
        name: "Index",
        redirect: "/home",
    },
    {
        path: "/home",
        name: "Home",
        component: () => import('@/views/HomeView.vue'),
    },
    
  ]
});

function authorizationCheck(requiresAuth){
    requiresAuth;
    // check if user is authenticated
    return true;
}

router.beforeEach((to, from, next) => {
  from;
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth)
  // const isAuthenticated = checkAuthorizaion()

  if (authorizationCheck(requiresAuth)) {
    next()
  } else {
    next({ name: 'Login', query: { redirect: to.fullPath } });
  }
  
})
// 全局后置钩子

router.afterEach((to, from) => {
    to;
    from;
});
export default router;