<template>
  <div>
    <img class="background" src="@/assets/computer.jpg" >
    <Navbar></Navbar>
    <div>
      <router-view class="app"></router-view>
    </div>
  </div>
</template>

<script>
import Navbar from './components/Navbar';

export default {
  name: 'App',
  components: {
    Navbar
  }
};
</script>

<style>

*,
*::after,
*::before {
  margin: 0;
  padding: 0;
  box-sizing: inherit;
}

html {
  font-size: 110%;
}

body, button{
  font-family: "europa-regular", sans-serif;
  font-weight: 700;
  font-style: italic;
  /*font-size: 16px;*/
  line-height: initial;
  color: @textColour;
  opacity: 1;

  background-color: @bgColour;
  box-sizing: border-box;
}

@media only screen and (max-width: 1365px) {
  html {
    font-size: 110%;
  }
}

</style>

<style scoped>
.background {
  position: absolute;
  height: 100vh;
  width: 100vw;
  z-index: -10;
}

.app {
  z-index: 1000;
}
</style>
