<template>
  <div class="outer">
    <div class="landing">
      <!--iframe
        src="https://open.spotify.com/embed/track/11dFghVXANMlKmJXsNCbNl"
        width="250"
        height="80"
        frameborder="0"
        allowtransparency="true"
        allow="encrypted-media" /-->
      <h2 class="header padding-bottom ">
        ACHTUNG !
      </h2>
      <h4 class="padding-bottom ">
        The scientists are hard at work  using equations and theorems, equalizers and synthesizers, to perfect Conception Calculator 2000. Please be patient and check back later. The science is super complex.
      </h4>
      <img
        class="logo padding-bottom "
        :src="require('@/assets/logo.png')"
        img>
    </div>
  </div>
</template>

<script>
  import {mapActions,mapGetters} from 'vuex'
  import {router} from '../main'

  export default {
    name: 'Landing',
    components: {
    },
    data () {
      return {}
    },
    mounted () {

    },
    methods: {
      ...mapActions([]),
      goToSelection () {
        router.push('/')
      }
    },
    computed: {
      ...mapGetters([])
    }
  }
</script>

<style scoped>
.outer {
  height: 100vh;
  width: 100vw;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  background: #363636;
}

.landing {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  text-align: center;
  color: #ddedec;
  width: 550px;
}

.header {
  font-size: 30px;
  padding-bottom: 1.5rem;
}

.logo {
  width: 40%;
  padding-top: 2rem;
}
</style>
