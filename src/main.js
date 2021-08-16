import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App'
import store from './store'
import Landing from './components/Landing'

Vue.use(VueRouter)

export const router = new VueRouter({
  mode: 'history',
  routes: [{
    path: '/',
    component: Landing
  }
  ]
})

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
