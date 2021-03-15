<template>
  <div class="outer">
    <div class="results">
      <iframe src="https://open.spotify.com/embed/track/6epn3r7S14KUqlReYr77hA" width="250" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
      <div class="break" />
      <button class="return" @click="goToSelection()">try again</button>
    </div>
  </div>
</template>

<script>
import {mapActions,mapGetters} from 'vuex';
import {router} from '../main';

export default {
  name: 'Results',
  components: {
  },
  data() {
    return {}
  },
  mounted() {

  },
  methods: {
    ...mapActions([]),
    goToSelection() {
    router.push('/')
    }
  },
  computed: {
    ...mapGetters([]),
  }
};
</script>

<style scoped>
.outer {
  height: 100vh;
  width: 100vw;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.results {
  transform: translate(-10%, -85%);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.break {
  flex-basis: 10px;
  height: 0;
}

.return {
  padding: .5rem;
  cursor: pointer;
}
</style>
