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

.guesses {
  display: flex;
  flex-direction: column;
  align-items: baseline;
  align-self: center;
  gap: 2rem;
  padding: 0;
  margin: 0;
}
</style>