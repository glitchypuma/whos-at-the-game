<template>
  <div class="website-header">
    <h1>Who's at the game?</h1>
    <!-- make the following lists dynamic, take in prop where we use some API to pull a list of current games -->
    <div class="games">
      <h2>Today's Games</h2>
      <h3>Baseball</h3>
      <ul class="baseball_games_header_list">
        <li v-for="baseballGame in baseballGames" :key="baseballGame.id">
          <!-- *** {{ baseballGame }} -->
          <p>{{ baseballGame.teams.away.name }} @ {{ baseballGame.teams.home.name }} </p>
        </li>
      </ul>

      <!-- <ul v-for="baseballGame in baseballGames" :key="baseballGame.id">
        <li v-if="baseballGame.id == 1">{{ baseballGame.teams.away.name }} @ {{ baseballGame.teams.home.name }}</li>
      </ul> -->
    </div>
  </div>
</template>

<!-- <div class="hello">
  <h1>{{ msg }}</h1>
  <p>
    For a guide and recipes on how to configure / customize this project,<br>
    check out the
    <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.
  </p>
  <h3>Installed CLI Plugins</h3>
  <ul>
    <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel" target="_blank" rel="noopener">babel</a></li>
    <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint" target="_blank" rel="noopener">eslint</a></li>
  </ul>
  <h3>Essential Links</h3>
  <ul>
    <li><a href="https://vuejs.org" target="_blank" rel="noopener">Core Docs</a></li>
    <li><a href="https://forum.vuejs.org" target="_blank" rel="noopener">Forum</a></li>
    <li><a href="https://chat.vuejs.org" target="_blank" rel="noopener">Community Chat</a></li>
    <li><a href="https://twitter.com/vuejs" target="_blank" rel="noopener">Twitter</a></li>
    <li><a href="https://news.vuejs.org" target="_blank" rel="noopener">News</a></li>
  </ul>
  <h3>Ecosystem</h3>
  <ul>
    <li><a href="https://router.vuejs.org" target="_blank" rel="noopener">vue-router</a></li>
    <li><a href="https://vuex.vuejs.org" target="_blank" rel="noopener">vuex</a></li>
    <li><a href="https://github.com/vuejs/vue-devtools#vue-devtools" target="_blank" rel="noopener">vue-devtools</a></li>
    <li><a href="https://vue-loader.vuejs.org" target="_blank" rel="noopener">vue-loader</a></li>
    <li><a href="https://github.com/vuejs/awesome-vue" target="_blank" rel="noopener">awesome-vue</a></li>
  </ul>
</div> -->

<script>
export default {
  name: 'SportsGamesHeader',
  // props: {
  //   baseballGames: []
  // },

  data() {
    return {
      baseballGames: [''],
    };
  },

  methods: {
    async getTodaysBaseballGames() {
      try {
        // const baseballGamesResponse = await this.axios.get(
        //   'http://localhost:8000/baseball_games/',
        //   {
        //     params: {
        //       timezone: 'America/Los_Angeles',
        //       date: '2023-05-12',
        //       season: '2023',
        //       league: '1',
        //     },
        //     headers: {
        //       'Content-Type': 'application/json',
        //       'x-rapidapi-key': 'e0a8f66d5dmsh53685da2f2425e3p138e6cjsnd3a33ec1fb3a',
        //       'x-rapidapi-host': 'api-baseball.p.rapidapi.com'
        //     }
        //   }
        // );
        // JSON responses are automatically parsed.
        const response = await this.$http.get('http://localhost:8000/baseball_games_today/');
        this.baseballGames = response.data.response;
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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
/* h3 {
  margin: 40px 0 0;
} */
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #000000;
}
</style>
