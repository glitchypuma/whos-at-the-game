<template>
  <div class="website-header">
    <h1>Who's at the game?</h1>
    <div class="games">
      <h2>Today's Games</h2>

      <h3 v-if="baseballGames.length">Baseball <button id="header-toggle" v-on:click="togglediv('baseball_list')">∇</button></h3>
      <ul class="baseball_list">
        <li v-for="baseballGame in baseballGames" :key="baseballGame.id">
          {{ baseballGame }}
          <!-- <p>{{ baseballGame.teams.away.name }} @ {{ baseballGame.teams.home.name }} </p> -->
        </li>
      </ul>

      <h3 v-if="basketballGames.length">Basketball <button id="header-toggle" v-on:click="togglediv('basketball_list')">∇</button></h3>
      <ul class="basketball_list">
        <li v-for="basketballGame in basketballGames" :key="basketballGame.id">
          {{ basketballGame }}
        </li>
      </ul>

      <h3 v-if="!footballGames.length">Football <button id="header-toggle" v-on:click="togglediv('football_list')">∇</button></h3>
      <ul class="football_list">
        <li v-for="footballGame in footballGames" :key="footballGame.id">
          {{ footballGame }}
        </li>
      </ul>

      <h3 v-if="soccerGames.length">Soccer <button id="header-toggle" v-on:click="togglediv('soccer_list')">∇</button></h3>
      <ul class="soccer_list">
        <li v-for="soccerGame in soccerGames" :key="soccerGame.id">
          {{ soccerGame }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SportsGamesHeader',

  data() {
    return {
      baseballGames: ['New York Yankees @ Toronto Blue Jays', 'Washington Nationals @ Miami Marlins', 'Minnesota Twins @ Los Angeles', 'Pittsburgh Pirates @ Detriot Tigers', 'Los Angeles Angels @ Baltimore Orioles'],
      basketballGames: ['Los Angeles Lakers @ Denver Nuggets', 'Miami Heat @ Boston Celtics'],
      footballGames: [''],
      soccerGames: ['Internazionale v AC Milan', 'Luton Town v Sunderland', 'FC Groningen v Ajax Amsterdam', 'One Knoxville v Chattanooga Red Wolves'],
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

    togglediv: function (name) {
      var div = document.getElementsByClassName(name)[0]
      div.style.display = div.style.display == "block" ? "none" : "block";
    }
  },

  created() {
    this.getTodaysBaseballGames();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.baseball_list,
.basketball_list,
.football_list,
.soccer_list
{
  display: none;
}
.website-header{
  padding: 10px 40px;
  background-color:blanchedalmond;
}
h1 {
  color: darkslateblue;
  text-align: left;
}
h2 {
  text-align: left;
}
h3 {
  position: relative;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: .2rem .5rem;
  padding: .3rem;
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
  position: absolute;
  top: 50%;
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
  margin-left: .5rem;
}
</style>
