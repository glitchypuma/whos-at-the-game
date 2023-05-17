<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <!-- for SportsGamesHeader, make the "current game" the prop to highlight it -->
  <SportsGamesHeader/>
  <!-- <SportsGamesHeader v-bind:baseballGames="baseballGames"/>  -->
  <!-- GAME COMPONENT HERE , pass through specific sporting event prop -->
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
  display: flex;
  flex-flow: column wrap;
  justify-content: flex-start;
  align-content: stretch;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
