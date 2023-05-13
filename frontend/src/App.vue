<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <!-- for SportsGamesHeader, make the "current game" the prop to highlight it -->
  <SportsGamesHeader/> 
  <!-- <SportsGamesHeader v-bind:baseballGames="baseballGames"/>  -->
  <!-- GAME COMPONENT HERE , pass through specific sporting event prop -->
  <!-- FOOTER COMPONENT HERE -->
</template>

<script>
//import axios from 'axios';
import SportsGamesHeader from './components/SportsGamesHeader.vue'

export default {
  name: 'App',
  components: {
    SportsGamesHeader
  },

  data() {
    return {
      baseballGames: [],
    };
  },

  methods: {
    async getTodaysBaseballGames() {
      try {
        const baseballGamesResponse = await this.axios.get(
          'https://api-baseball.p.rapidapi.com/games/',
          {
            params: {
              timezone: 'America/Los_Angeles',
              date: '2023-05-12',
              season: '2023',
              league: '1',
            },
            headers: {
              'Content-Type': 'application/json',
              'x-rapidapi-key': 'e0a8f66d5dmsh53685da2f2425e3p138e6cjsnd3a33ec1fb3a',
              'x-rapidapi-host': 'api-baseball.p.rapidapi.com'
            }
          }
        );
        // JSON responses are automatically parsed.
        this.baseballGames = baseballGamesResponse.data;
      } catch (error) {
        console.log(error);
      }
    },
  },

  created() {
    this.getTodaysBaseballGames();
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
