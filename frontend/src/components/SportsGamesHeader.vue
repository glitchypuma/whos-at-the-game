<template>
  <div class="website-header">
    <!-- <h1 class="title">Who's at the game?</h1> -->
    <h2 style="border-bottom: .1rem solid black;">Today's Games</h2>
    <div class="games">
      <div v-if="baseballGames.length">
        <h3>⚾ Baseball <button id="header-toggle" v-on:click="togglediv('baseball_list')">∇</button></h3>
      </div>
      <div v-if="basketballGames.length">
        <h3>🏀 Basketball <button id="header-toggle" v-on:click="togglediv('basketball_list')">∇</button></h3>
      </div>
      <div v-if="NFLGames.length">
        <h3>🏈 NFL <button id="header-toggle" v-on:click="togglediv('nfl_football_list')">∇</button></h3>
      </div>
      <div v-if="NCAAGames.length">
        <h3>🏈 NCAA <button id="header-toggle" v-on:click="togglediv('ncaa_football_list')">∇</button></h3>
      </div>
      <div v-if="footballGames.length">
        <h3>⚽ Football <button id="header-toggle" v-on:click="togglediv('football_list')">∇</button></h3>
      </div>
  </div>

    <ul class="baseball_list">
      <li v-for="game in baseballGames" :key="game.id">
        <a href="">
          {{ game }}
          <!-- {{ game.teams.away.name }} @ {{ game.teams.home.name }} -->
        </a>
      </li>
    </ul>

    <ul class="basketball_list">
        <li v-for="game in basketballGames" :key="game.id">
          <a href="">
            {{ game }}
            <!-- {{ game.teams.away.name }} @ {{ game.teams.home.name }} -->
          </a>
        </li>
      </ul>
          
    <ul class="nfl_football_list">
      <li v-for="game in NFLGames" :key="game.id">
        <a>
          {{ game }}
          <!-- {{ game.teams.away.name }} @ {{ game.teams.home.name }} -->
        </a>  
      </li>
    </ul>

    <ul class="ncaa_football_list">
      <li v-for="game in NCAAGames" :key="game.id">
        <a>
          <!-- {{ game }} -->
          {{ game.teams.away.name }} @ {{ game.teams.home.name }}
        </a>
      </li>
    </ul>
        
    <ul class="football_list">
      <li v-for="game in footballGames" :key="game.id">
        <a>
          {{ game }}
          <!-- {{ game.teams.away.name }} vs {{ game.teams.home.name }} -->
        </a>
      </li>
    </ul>

  </div>
</template>

<script>
export default {
  name: 'SportsGamesHeader',

  data() {
    return {
      // baseballGames: [],
      // basketballGames: [],
      // NFLGames: [],
      // NCAAGames: [],
      // footballGames: []

      baseballGames: ['New York Yankees @ Toronto Blue Jays', 'Washington Nationals @ Miami Marlins', 'Minnesota Twins @ Los Angeles Dodgers', 'Pittsburgh Pirates @ Detriot Tigers', 'Los Angeles Angels @ Baltimore Orioles'],
      basketballGames: ['Los Angeles Lakers @ Denver Nuggets', 'Miami Heat @ Boston Celtics'],
      NFLGames: [],
      NCAAGames: [],
      footballGames: ['Internazionale v AC Milan', 'Luton Town v Sunderland', 'FC Groningen v Ajax Amsterdam', 'One Knoxville v Chattanooga Red Wolves']
    };
  },

  methods: {
    async getTodaysBaseballGames() {
      try {
        const response = await this.$http.get('http://localhost:8000/baseball_games_today/');
        this.baseballGames = response.data.response;
      } catch (error) {
        console.log(error);
      }
    },
    async getTodaysBasketballGames() {
      try {
        const response = await this.$http.get('http://localhost:8000/basketball_games_today/');
        this.basketballGames = response.data.response;
      } catch (error) {
        console.log(error);
      }
    },
    async getTodaysFootballGames() {
      try {
        const response = await this.$http.get('http://localhost:8000/football_games_today/');
        this.footballGames = response.data.response;
      } catch (error) {
        console.log(error);
      }
    },
    async getTodaysNFLGames() {
      // NFL
      try {
        const response = await this.$http.get('http://localhost:8000/ame_football_games_today/1/');
        if(response != null) {
          this.NFLGames = response.data.response;
        }
      } catch (error) {
        console.log(error);
      }
    },
    async getTodaysNCAAGames() {
      // NCAA
      try {
        const response = await this.$http.get('http://localhost:8000/ame_football_games_today/2/');
        if(response != null) {
          this.NCAAGames = response.data.response;
        }
      } catch (error) {
        console.log(error);
      }
    },

    sendCrawlerParams(homeTeam, awayTeam) {
      this.$emit("crawler-params", {homeTeam, awayTeam})
    },

    togglediv: function (name) {
      this.sendCrawlerParams("test", "test")
      
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
  background-color:blanchedalmond;
  border-bottom: .3em solid rgb(224, 193, 146) ;
}

.title{
  color: darkslateblue;
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
}

h1 {
  text-align: left;
}
h2 {
  color: darkslateblue;
  margin: .1rem;
  text-align: left;
}
h3 {
  color: darkslateblue;
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
  border-radius: 1px;
  border-style: solid;
  border-color: darkslateblue;
  background-color: rgb(255, 246, 233);
}
li a {
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
  background-color: lightblue;
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
  background-color: transparent;
  border-radius: 12px;
  vertical-align: center;
}
</style>
