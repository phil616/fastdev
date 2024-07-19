import Vue from 'vue';
import Router from 'vue-router';

import Home from '@/pages/HomeView.vue';
import Aboutus from '@/pages/AboutusView.vue';
import Notifications from '@/pages/NotificationsView.vue';
import Productions from '@/pages/ProductionsView.vue';
import Projects from '@/pages/ProjectsView.vue';
import NotFound from '@/pages/NotFoundView.vue';
import Doc from '@/pages/DocView.vue';
import SingleDoc from '@/pages/SingleDocView.vue'
import Redirect from '@/pages/RedirectView.vue'
Vue.use(Router);

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: "Root",
      redirect: '/home',
    },
    {
      path: '/home',
      name: 'Home',
      component: Home,
    },
    {
      path: '/notifications',
      name: 'Notifications',
      component: Notifications,
    },
    {
      path: '/productions',
      name: 'Productions',
      component: Productions,
    },
    {
      path: '/doc',
      name: 'Doc',
      component: Doc,
    },
    {
      path: '/singleDoc',
      name: 'SingleDoc',
      component: SingleDoc,
      props: true,
    },
    {
      path: '/projects',
      name: 'Projects',
      component: Projects,
    },
    {
      path: '/aboutus',
      name: 'Aboutus',
      component: Aboutus,
    },
    {
      path: '/redirect',
      name: 'Redirect',
      component: Redirect,
      props: true
    },
    {
      path: '*',
      name: 'NotFound',
      component: NotFound // 捕获所有未定义的路由
    },
    
  ]
});

// 全局前置守卫
router.beforeEach((to, from, next) => {
  console.log('router.beforeEach', to.path, from.path);
  console.log('router.beforeEach', to, from,next);
  // 防止重复点击路由
  next();
 

});

// 全局后置钩子
/**
router.afterEach((to, from) => {

});
*/

export default router;