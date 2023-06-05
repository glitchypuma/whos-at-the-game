<template>
  <SportsGamesHeader @game-string="setGameString" @scraper-params="getGame"/>
  <WebsiteTitle :selectedGameString="gameString"/>
  <LandingPage v-if="!viewingGame" />
  <GameAttendance v-if="renderGuess" :bestGuess="bestGuess" :selectedGame="selectedGame"/>
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
      bestGuess: [],
      renderGuess: false
    }
  },

  methods: {
    getGame(game) {
      this.renderGuess = false
      this.selectedGame = game
      this.getBestGuess()
      this.viewingGame = true
      this.gameString = game.home_team + " game"
    },
    setGameString(gameString) {
      if(!this.viewingGame){
        this.gameString = gameString
      }
    },
    async getBestGuess() {
      const query = this.getScraperQuery(this.selectedGame);
      console.log(query)
      try {
          const response = await api.get('scraper', query);
          this.bestGuess = response.data;
          this.renderGuess = true
      } catch (error) {
          console.log(error);
      }
    },
      getScraperQuery(selectedGame) {
      var query = selectedGame.away_team + "/" + selectedGame.home_team + "/";
      return query;
    }
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
a {
  color: var(--dark-accent)
}
a:hover {
  opacity: 75%;
}

::selection {
  background-color: var(--light-accent);
  /* color: var(--light-text); */
}
</style>
