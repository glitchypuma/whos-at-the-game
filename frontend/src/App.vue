<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <!-- for SportsGamesHeader, make the "current game" the prop to highlight it -->
  <SportsGamesHeader @crawler-params="getCrawlerParams"/>
  <GameAttendance  :crawlerParams="params"/>
  <!-- <SportsGamesHeader v-bind:baseballGames="baseballGames"/>  -->
  <!-- GAME COMPONENT HERE , pass through specific sporting event prop -->
  <!-- FOOTER COMPONENT HERE -->
</template>

<script>
import SportsGamesHeader from './components/SportsGamesHeader.vue'
import GameAttendance from './components/GameAttendance.vue'

export default {
  name: 'App',
  components: {
    SportsGamesHeader,
    GameAttendance
  },

  data () {
    return {
      params: {}
    }
  },

  methods: {
    getCrawlerParams(params) {
      console.log(params)
      this.crawlerParams = params;
    }
  }
};

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
