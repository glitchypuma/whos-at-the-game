<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <!-- for SportsGamesHeader, make the "current game" the prop to highlight it -->
  <SportsGamesHeader msg="Welcome to Your Vue.js App"/> 
  <!-- GAME COMPONENT HERE , pass through specifi sporting event prop -->
  <!-- FOOTER COMPONENT HERE -->
</template>

<script>
import SportsGamesHeader from './components/SportsGamesHeader.vue'

export default {
  name: 'App',
  components: {
    SportsGamesHeader
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  margin-top: 20px;
}
</style>
