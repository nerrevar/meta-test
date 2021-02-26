import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import PsychotherapistInfoView from '@/views/PsychotherapistInfoView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView,
  },
  {
    path: '/psychotherapist_info/:id',
    name: 'PsychotherapistInfoView',
    component: PsychotherapistInfoView,
    props: true,
  },
  {
    path: '*',
    redirect: '/',
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

router.beforeEach((to, from, next) => {
  let title
  switch (to.name) {
    case 'HomeView': {
      title = 'Список психотерапевтов'
      break
    }
    case 'PsychotherapistInfoView': {
      title = 'Информация о психотерапевте'
      break
    }
  }
  document.title = title
  next()
})

export default router
