<template>
    <body>
        <h2>Judging by the conversation on Twitter, here's our best guess:</h2>
        <p>Game:<br>{{ selectedGame }}</p>
        <ul>
            <li v-for="person in bestGuess" :key="person.id">
                <GuessView :guess="person" />
                <!-- <p class="typewriter">{{ person.name }}</p> -->
            </li>
        </ul>
    </body>
</template>

<script>
// import api from '../api/api.js'
import GuessView from './GuessView.vue'

export default {
    name: 'GameAttendance',
    components: {
        GuessView
    },

    props: {
        selectedGame: { },
        bestGuess: [ ]
    },

    // data() {
    //     return {
    //         bestGuess: [],
    //     };
    // },

    methods: {
        // request an endpoint that returns desc ordered list of potential celebrities at the game
        // async getBestGuess() {
        //     // use selectedGame to construct query 
        //     try {
        //         const response = await api.get('scraper');
        //         console.log(response)
        //         this.bestGuess = response.data;
        //     } catch (error) {
        //         console.log(error);
        //     }
        // }
        // sendGuess() {
        //     this.$emit("guess", guess.name)
        // }
    },
    // created() {
    //     this.sendGuess();
    // }
}

</script>

<style scoped>
body {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    text-align: center;
}
p {
    margin: 2rem 3rem;
    text-align: start;
}
ul {
  display: flex;
  flex-direction: column;
  /* align-content: flex-start; */
  text-align: start;
  align-items: flex-start;
  align-self: center;
  gap: 1rem;
  list-style-type: none;
  padding: 0;
  /* min-width: 20rem; */
}
li {
    /* align-content: left; */
    color: #337CA0;
    font-size: 20px;
    /* text-align: left; */
    /* background-color: #F2EFE9; */
    /* padding: .5rem; */
    /* border-radius: .5rem; */
    border-bottom: 2px solid #337CA0;
}
</style>