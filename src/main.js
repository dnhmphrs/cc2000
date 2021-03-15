import Vue from 'vue';
import VueRouter from 'vue-router';
import App from './App';
import store from './store';
import Selection from './components/Selection';
import Results from './components/Results';

Vue.use(VueRouter);

export const router = new VueRouter({
  mode: 'history',
  routes: [{
      path: '/',
      component: Selection
    },
    {
        path: '/results',
        component: Results
      }
  ]
})

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app');
