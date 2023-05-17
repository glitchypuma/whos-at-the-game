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
        <h3 v-if="!footballGames.length">Football <button id="header-toggle" v-on:click="togglediv('football_list')">∇</button></h3>
      </div>
      <div>
        <h3 v-if="soccerGames.length">Soccer <button id="header-toggle" v-on:click="togglediv('soccer_list')">∇</button></h3>
      </div>
    </div>

    <ul class="baseball_list">
      <li v-for="baseballGame in baseballGames" :key="baseballGame.id">
        {{ baseballGame }}
        <!-- <p>{{ baseballGame.teams.away.name }} @ {{ baseballGame.teams.home.name }} </p> -->
      </li>
    </ul>

    <ul class="basketball_list">
        <li v-for="basketballGame in basketballGames" :key="basketballGame.id">
          {{ basketballGame }}
        </li>
      </ul>
          
    <ul class="football_list">
      <li v-for="footballGame in footballGames" :key="footballGame.id">
        {{ footballGame }}
      </li>
    </ul>
        
    <ul class="soccer_list">
      <li v-for="soccerGame in soccerGames" :key="soccerGame.id">
        {{ soccerGame }}
      </li>
    </ul>

  </div>
</template>

<script>
export default {
  name: 'SportsGamesHeader',

  data() {
    return {
      baseballGames: ['New York Yankees @ Toronto Blue Jays', 'Washington Nationals @ Miami Marlins', 'Minnesota Twins @ Los Angeles Dodgers', 'Pittsburgh Pirates @ Detriot Tigers', 'Los Angeles Angels @ Baltimore Orioles'],
      basketballGames: ['Los Angeles Lakers @ Denver Nuggets', 'Miami Heat @ Boston Celtics'],
      footballGames: [''],
      soccerGames: ['Internazionale v AC Milan', 'Luton Town v Sunderland', 'FC Groningen v Ajax Amsterdam', 'One Knoxville v Chattanooga Red Wolves'],
    
      // baseballGames: ['']
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
.football_list,
.soccer_list
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
  list-style-type: none;
  padding: 0;
  column-gap: 1rem;
}
li {
  flex-flow: row wrap;
  justify-content: flex-start;
  align-content: center;
  gap: 1rem;
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
