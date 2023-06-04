<template>
    <body>
        <h2>Judging by the conversation on Twitter, here's our best guess:</h2>
        <p>Game:<br>{{ selectedGame }}</p>

        {{ bestGuess }}
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
</style>