<template>
  <div class="website-header">
    <!-- <h1 class="title">Who's at the game?</h1> -->
    <h2 style="border-bottom: .1rem solid black;">Today's Games</h2>
    <div class="games">
      <div v-if="baseballGames.length">
        <h3>⚾ Baseball <button id="header-toggle" v-on:click="togglediv('baseball_list')">V</button></h3>
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
        <a role="button" @mouseover="sendHoveredGameString(game)" v-on:click="sendScraperParams(game)">
          {{ game.away_team }} @ {{ game.home_team }}
        </a>
      </li>
    </ul>

    <ul class="basketball_list">
        <li v-for="game in basketballGames" :key="game.id">
          <a role="button" @mouseover="sendHoveredGameString(game)"  v-on:click="sendScraperParams(game)">
            {{ game.away_team }} @ {{ game.home_team }}
          </a>
        </li>
      </ul>
          
    <ul class="nfl_football_list">
      <li v-for="game in NFLGames" :key="game.id">
        <a role="button" @mouseover="sendHoveredGameString(game)"  v-on:click="sendScraperParams(game)">
          {{ game.away_team }} @ {{ game.home_team }}
        </a>  
      </li>
    </ul>

    <ul class="ncaa_football_list">
      <li v-for="game in NCAAGames" :key="game.id">
        <a role="button" @mouseover="sendHoveredGameString(game)"  v-on:click="sendScraperParams(game)">
          {{ game.away_team }} @ {{ game.home_team }}
        </a>
      </li>
    </ul>
        
    <ul class="football_list">
      <li v-for="game in footballGames" :key="game.id">
        <a role="button" @mouseover="sendHoveredGameString(game)"  v-on:click="sendScraperParams(game)">
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
      footballGames: []
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
      this.$emit("scraper-params", selectedGame)
    },
    sendHoveredGameString(game) {
      this.$emit("game-string", game.home_team + " game" )
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
  padding: 10px 40px;
  background-color: green;
  /* border-bottom: .3em solid #ca9420; */
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
  height: 400%;
}

/* button {
  background-color: #005A9C;
  color: #000000;
} */
h1 {
  margin: 0;
  text-align: left;
}
h2 {
  color: white ;
  margin: .1rem;
  text-align: left;
}
h3 {
  color: white ;
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
  padding: .2rem;
  border-radius: 5px;
  /* border-style: dotted;
  border-color: black; */
  background-color: rgb(255, 255, 255);
}
li a {
  padding: .2rem;
  border-radius: 12px;
  position: relative;
  /* display: block; */
  color: black;
  text-decoration: none;
  z-index: 0;
}
li a:before
{
  position: absolute;
  content: "";
  width: 100%;
  height: 100%;
  bottom: 0;
  left: 0;
  background-color: rgba(0, 128, 0, 0.267);
  z-index: -1;
  transform: scale(0);
  transition: transform 0.5s ease-in-out
}
li a:hover:before,
li a:focus:before {
  transform: scale(1);
}
/* a {
  color: #000000;
} */

#header-toggle {
  background-color: #a5acaf9a;
  border-color: #A5ACAF;
  border-radius: 180px;
  vertical-align: center;
}
</style>
