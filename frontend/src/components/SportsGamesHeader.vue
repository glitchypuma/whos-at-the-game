<template>
  <div class="website-header">
    <!-- <h1 class="title">Who's at the game?</h1> -->
    <h2 style="border-bottom: .1rem solid black;">Today's Games</h2>
    <div class="games">
      <div v-if="baseballGames.length">
        <h3>⚾ Baseball <button id="header-toggle" v-on:click="togglediv('baseball_list');">V</button></h3>
      </div>
      <div v-if="basketballGames.length">
        <h3>🏀 Basketball <button id="header-toggle" v-on:click="togglediv('basketball_list')">V</button></h3>
      </div>
      <div v-if="NFLGames.length">
        <h3>🏈 NFL <button id="header-toggle" v-on:click="togglediv('nfl_football_list')">V</button></h3>
      </div>
      <div v-if="NCAAGames.length">
        <h3>🏈 NCAA <button id="header-toggle" v-on:click="togglediv('ncaa_football_list')">V</button></h3>
      </div>
      <div v-if="footballGames.length">
        <h3>⚽ Football <button id="header-toggle" v-on:click="togglediv('football_list')">V</button></h3>
      </div>
  </div>

    <ul class="baseball_list">
      <li v-for="game in baseballGames" :key="game.id">
        <a role="button" @mouseover="sendHoveredGameString(game)" v-on:click=" togglediv('baseball_list'); sendScraperParams(game);">
          {{ game.away_team }} @ {{ game.home_team }}
        </a>
      </li>
    </ul>

    <ul class="basketball_list">
        <li v-for="game in basketballGames" :key="game.id">
          <a role="button" @mouseover="sendHoveredGameString(game)"  v-on:click="togglediv('basketball_list'); sendScraperParams(game);">
            {{ game.away_team }} @ {{ game.home_team }}
          </a>
        </li>
      </ul>
          
    <ul class="nfl_football_list">
      <li v-for="game in NFLGames" :key="game.id">
        <a role="button" @mouseover="sendHoveredGameString(game)"  v-on:click="togglediv('nfl_football_list'); sendScraperParams(game);">
          {{ game.away_team }} @ {{ game.home_team }}
        </a>  
      </li>
    </ul>

    <ul class="ncaa_football_list">
      <li v-for="game in NCAAGames" :key="game.id">
        <a role="button" @mouseover="sendHoveredGameString(game)"  v-on:click="togglediv('ncaa_football_list'); sendScraperParams(game);">
          {{ game.away_team }} @ {{ game.home_team }}
        </a>
      </li>
    </ul>
        
    <ul class="football_list">
      <li v-for="game in footballGames" :key="game.id">
        <a role="button" @mouseover="sendHoveredGameString(game)"  v-on:click="togglediv('football_list'); sendScraperParams(game);">
          {{ game.away_team }} vs {{ game.home_team }}
        </a>
      </li>
    </ul>

  </div>
</template>

<script>
import api from '../api/api.js'

export default {
  name: 'SportsGamesHeader',

  data() {
    return {
      baseballGames: [],
      basketballGames: [],
      NFLGames: [],
      NCAAGames: [],
      footballGames: [],
      showGameList: false
    };
  },

  methods: {
    async getTodaysBaseballGames() {
      try {
        const response = await api.get('baseball');
        this.baseballGames = response.data;
      } catch (error) {
        console.log(error);
      }
    },
    async getTodaysBasketballGames() {
      try {
        const response = await api.get('basketball');
        this.basketballGames = response.data;
      } catch (error) {
        console.log(error);
      }
    },
    async getTodaysFootballGames() {
      try {
        const response = await api.get('football');
        this.footballGames = response.data;
      } catch (error) {
        console.log(error);
      }
    },
    async getTodaysNFLGames() {
      try {
        const response = await api.get('nfl');
        this.NFLGames = response.data;
      } catch (error) {
        console.log(error);
      }
    },
    async getTodaysNCAAGames() {
      try {
        const response = await api.get('ncaa');
        this.NCAAGames = response.data;
      } catch (error) {
        console.log(error);
      }
    },

    sendScraperParams(selectedGame) {
      this.toggleGameList()
      this.$emit("scraper-params", selectedGame)
    },
    sendHoveredGameString(game) {
      this.$emit("game-string", game.home_team + " game" )
    },

    toggleGameList() {
      this.showGameList = !this.showGameList
    },
    togglediv: function (name) {
      var div = document.getElementsByClassName(name)[0]

      if(div.style.display == "flex"){
        div.style.display = "none"
      } else {
        var gameLists = document.querySelectorAll("ul")

        gameLists.forEach((list) => {
          list.style.display = "none"
        });

        div.style.display = "flex"
      }
    }
  },

  created() {
    this.getTodaysBaseballGames();
    this.getTodaysBasketballGames();
    this.getTodaysFootballGames();
    this.getTodaysNFLGames();
    this.getTodaysNCAAGames();
  }
}
</script>

<style scoped>
.website-header{
  padding: .5rem 3rem;
  background-color: #6DA34D;
  border-radius: 0 0 12px 12px;
}
.baseball_list,
.basketball_list,
.nfl_football_list,
.ncaa_football_list,
.football_list
{
  margin: 0;
  display: none;
}

.games{
  display: flex;
  align-items: stretch;
  flex-flow: row wrap;
  justify-content: flex-start;
  column-gap: 1rem;
  text-align: center;
  padding: 0;
  margin: .2rem;
}

h1 {
  margin: 0;
  text-align: left;
}
h2 {
  color: #0B132B ;
  margin: .1rem;
  text-align: left;
}
h3 {
  color: #0B132B ;
  position: relative;
}
ul {
  display: flex;
  align-items: center;
  flex-flow: row wrap;
  gap: .5rem;
  list-style-type: none;
  padding: 0;
  column-gap: 1rem;
}
li {
  align-self: stretch;
  display: flex;
  align-items: center;
  background-color: #F2EFE9;
  border-radius: .5rem;
}
li a {
  color: #0B132B;
  text-decoration: none;
  border-radius: .5rem;
  border: 5px inset transparent;
}
li a:hover,
li a:focus {
  padding: 2px;
  border: 3px solid #D8D4F2;
}
#header-toggle {
  background-color: #a5acaf9a;
  border-color: #A5ACAF;
  border-radius: 180px;
  vertical-align: center;
}
</style>
<!-- 
A27E8E mountbatten pink
D8D4F2 lavender
EE4266 red (crayola) -->

<!-- mary hodge

mario lopez

spike lee -->