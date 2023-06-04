<template>
  <SportsGamesHeader @game-string="setGameString" @scraper-params="getGame"/>
  <WebsiteTitle :selectedGameString="gameString"/>
  <LandingPage v-if="!viewingGame" />
  <GameAttendance v-if="viewingGame" :bestGuess="bestGuess" :selectedGame="selectedGame"/>
  <WebsiteFooter />
</template>

<script>
import api from './api/api.js'
import SportsGamesHeader from './components/SportsGamesHeader.vue'
import WebsiteTitle from './components/WebsiteTitle.vue'
import GameAttendance from './components/GameAttendance.vue'
import LandingPage from './components/LandingPage.vue'
import WebsiteFooter from './components/WebsiteFooter.vue'

export default {
  name: 'App',
  components: {
    SportsGamesHeader,
    WebsiteTitle,
    LandingPage,
    GameAttendance,
    WebsiteFooter
  },

  data () {
    return {
      selectedGame: {},
      viewingGame: false,
      gameString: '',
      bestGuess: []
    }
  },

  methods: {
    getGame(game) {
      this.getBestGuess()
      this.selectedGame = game
      this.gameString = game.home_team + " game" 
      this.viewingGame = true
      //this.getBestGuess(this.selectedGame);
    },
    setGameString(gameString) {
      if(!this.viewingGame){
        this.gameString = gameString
      }
    },
    async getBestGuess() {
      try {
          const response = await api.get('scraper')
          console.log(response)
          this.bestGuess = response.data
      } catch (error) {
          console.log(error)
      }
    }
    // async getBestGuess(selectedGame) {
    //   var query = selectedGame.home_team
    //   // TODO: use selectedGame to construct query 
    //   try {
    //       const response = await api.get('scraper', query);
    //       console.log(response)
    //       this.bestGuess = response.data;
    //   } catch (error) {
    //       console.log(error);
    //   }
    // }
  }
};

</script>

<style>
@import './assets/base.css';

#app {
  display: flex;
  flex-flow: column wrap;
  justify-content: flex-start;
  align-content: stretch;
  font-family: var(--base-font);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: var(--oxford-blue);
}

::selection {
  background-color: var(--light-accent);
  /* color: var(--light-text); */
}
</style>
