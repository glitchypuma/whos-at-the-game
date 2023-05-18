<template>
  <div class="website-header">
    <!-- <h1 class="title">Who's at the game?</h1> -->
    <h2 style="border-bottom: .1rem solid black;">Today's Games</h2>
    <div class="games">
      <div>
        <h3 v-if="baseballGames.length">Baseball <button id="header-toggle" v-on:click="togglediv('baseball_list')">∇</button></h3>
      </div>
      <div>
        <h3 v-if="basketballGames.length">Basketball <button id="header-toggle" v-on:click="togglediv('basketball_list')">∇</button></h3>
      </div>
      <div>
        <h3 v-if="ameFootballGames.length">American Football <button id="header-toggle" v-on:click="togglediv('ame_football_list')">∇</button></h3>
      </div>
      <div>
        <h3 v-if="footballGames.length">Football <button id="header-toggle" v-on:click="togglediv('football_list')">∇</button></h3>
      </div>
    </div>

    <ul class="baseball_list">
      <li v-for="baseballGame in baseballGames" :key="baseballGame.id">
        {{ baseballGame }}
        <!-- {{ baseballGame.teams.away.name }} @ {{ baseballGame.teams.home.name }} -->
      </li>
    </ul>

    <ul class="basketball_list">
        <li v-for="basketballGame in basketballGames" :key="basketballGame.id">
          <!-- {{ basketballGame }} -->
          {{ basketballGame.teams.away.name }} @ {{ basketballGame.teams.home.name }}
        </li>
      </ul>
          
    <ul class="ame_football_list">
      <li v-for="ameFootballGame in ameFootballGames" :key="ameFootballGame.id">
        {{ ameFootballGame }}
      </li>
    </ul>
        
    <ul class="football_list">
      <li v-for="footballGame in footballGames" :key="footballGame.id">
        {{ footballGame }}
      </li>
    </ul>

  </div>
</template>

<script>
export default {
  name: 'SportsGamesHeader',

  data() {
    return {
      baseballGames: [],
      basketballGames: [],

      // baseballGames: ['New York Yankees @ Toronto Blue Jays', 'Washington Nationals @ Miami Marlins', 'Minnesota Twins @ Los Angeles Dodgers', 'Pittsburgh Pirates @ Detriot Tigers', 'Los Angeles Angels @ Baltimore Orioles'],
      // basketballGames: ['Los Angeles Lakers @ Denver Nuggets', 'Miami Heat @ Boston Celtics'],
      ameFootballGames: [],
      footballGames: ['Internazionale v AC Milan', 'Luton Town v Sunderland', 'FC Groningen v Ajax Amsterdam', 'One Knoxville v Chattanooga Red Wolves'],
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
.ame_football_list,
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
  margin: .1rem;
  text-align: left;
}
/* h3 {
  position: relative;
} */
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
}
a {
  color: #000000;
}

#header-toggle {
  background-color: transparent;
  border-radius: 12px;
  vertical-align: center;
}
</style>
