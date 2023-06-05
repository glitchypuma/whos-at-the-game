<template>
    <body>
        <h2>Judging by the conversation on Twitter, here's our best guess:</h2>
        <div class="guesses">
            <div class="guess" v-for="person in personGuesses" :key="person.id">
                <GuessView :guessName="person.name" />
            </div>
        </div>
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
    created() {
        
    }
}

</script>

<style scoped>
body {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}
p {
    margin: 2rem 3rem;
    text-align: start;
}

.guesses {
  display: flex;
  flex-flow: column wrap;
  align-items: baseline;
  gap: 1rem;
  padding: 0;
  margin: .5em;
}
/* .guess {
    display: flex;
    flex-direction: row;
} */
</style>