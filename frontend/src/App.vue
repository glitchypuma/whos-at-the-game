<template>
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
      this.scraperParams = game;
      this.gameString = game.home_team + " game" ;
      this.viewingGame = true;
    },
    setGameString(gameString) {
      if(!this.viewingGame){
        this.gameString = gameString;
      }
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
  background-color: rgba(0, 128, 0, 0.267);
}
</style>
