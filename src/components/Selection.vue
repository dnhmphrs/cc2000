<template>
  <div class="outer">
    <div class="selection">
      <input type="checkbox" id="date" value="date" v-model="data">
      <label for="date">date</label>
      <hr>
      <input type="checkbox" id="hair" value="hair" v-model="data">
      <label for="hair">hair</label>
      <hr>
      <button class="getResults" @click="getResults()"
      :class="{disabled:disableCalculate}">calculate</button>
    </div>
  </div>
</template>

<script>
import {mapActions,mapGetters} from 'vuex';
import {router} from '../main';

export default {
  name: 'Selection',
  components: {
  },
  data() {
    return {
      data: []
    }
  },
  methods: {
    ...mapActions([]),
    getResults() {
      router.push('results')
    }
  },
  computed: {
    ...mapGetters([]),
    disableCalculate() {
      if (this.data.length < 2) {
        return true
      } else {
        return false
      }
    }
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
}

.selection {
  height: 300px;
  width: 300px;
  background: #f0f0f0;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-flow: wrap;
  transform: translate(-10%, -40%);
}

hr {
  width: 100%;
}

.getResults {
  padding: .5rem;
  background: #e1bac8;
  cursor: pointer;
}

.getResults.disabled {
  pointer-events: none;
  background: #f0f0f0;
  opacity: .3;
}
</style>
