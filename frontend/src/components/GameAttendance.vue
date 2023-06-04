<template>
    <body>
        <h2>Judging by the conversation on Twitter, here's our best guess:</h2>
        <ul>
            <template v-for="person in personGuesses" :key="person.id">
                <GuessView :guessName="person.name" />
            </template>
        </ul>
        <p>Game:<br>{{ game }}</p>
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

    data() {
        return {
            game: this.selectedGame,
            personGuesses: this.bestGuess
        }
    },
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