<template>
    <body>
        <h2>Judging by the conversation on Twitter, here's our best guess:</h2>
        <!-- <p>Game:<br>{{ selectedGame }}</p> -->
        <ul>
            <li v-for="person in bestGuess" :key="person.id">
                {{ person.name }}
            </li>
        </ul>
    </body>
</template>

<script>
// import api from '../api/api.js'

export default {
    name: 'GameAttendance',

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
    }
}

</script>

<style scoped>
body {
    text-align: center;
}
p{
    margin: 2rem 3rem;
    text-align: start;
}
ul {
  display: flex;
  align-items: stretch;
  flex-direction: column;
  gap: .5rem;
  list-style-type: none;
  padding: 0;
  column-gap: 1rem;
  margin: 2rem 25%;
}
li {
    text-align: left;
  background-color: #F2EFE9;
  border-radius: .5rem;
}
</style>