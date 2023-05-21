<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <SportsGamesHeader @game-string="setGameString" @scraper-params="getScraperParams"/>
  <WebsiteTitle :selectedGameString="gameString"/>
  <LandingPage v-if="!viewingGame" />
  <GameAttendance v-if="viewingGame" :selectedGame="scraperParams"/>
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
      viewingGame: false,
      gameString: ''
    }
  },

  methods: {
    getScraperParams(game) {
      console.log(game)
      this.scraperParams = game;
      this.viewingGame = true;
    },
    setGameString(gameString) {
      this.gameString = gameString
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
  color: black;
  /* background-color: blanchedalmond; */
}

::selection {
  background-color: lightblue;
}
</style>
