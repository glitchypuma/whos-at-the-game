<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <!-- for SportsGamesHeader, make the "current game" the prop to highlight it -->
  <SportsGamesHeader @scraper-params="getscraperParams"/>
  <WebsiteTitle />
  <LandingPage v-if="viewingGame" />
  <GameAttendance v-if="!viewingGame" :params="scraperParams"/>
  <!-- <SportsGamesHeader v-bind:baseballGames="baseballGames"/>  -->
  <!-- GAME COMPONENT HERE , pass through specific sporting event prop -->
  <!-- FOOTER COMPONENT HERE -->
</template>

<script>
import SportsGamesHeader from './components/SportsGamesHeader.vue'
import WebsiteTitle from './components/WebsiteTitle.vue'
import GameAttendance from './components/GameAttendance.vue'
import LandingPage from './components/LandingPage.vue'

export default {
  name: 'App',
  components: {
    SportsGamesHeader,
    WebsiteTitle,
    LandingPage,
    GameAttendance
  },

  data () {
    return {
      scraperParams: {},
      viewingGame: false
    }
  },

  methods: {
    getscraperParams(params) {
      console.log(params)
      this.scraperParams = params;
      this.viewingGame = true;
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
  color: #552583;
  /* background-color: blanchedalmond; */
}

::selection {
  background-color: lightblue;
}
</style>
