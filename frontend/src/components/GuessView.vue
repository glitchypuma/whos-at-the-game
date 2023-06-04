<template>
    <body>
        <p id="typewriter"></p>
    </body>
</template>

<script>
// import api from '../api/api.js'

export default {
    name: 'GuessView',

    props: {
        guess: {}
    },

    // data() {
    //     return {
    //         bestGuess: [],
    //     };
    // },

    methods: {
        typewriter(guess){
            var i = 0;
            var txt =  guess.name;
            // var speed = 50;
            if (i < txt.length) {
                document.getElementById("typewriter").innerHTML += txt.charAt(i);
                i++;
                // setTimeout(typewriter, speed);
            }
        }

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
    },
    created() {
        this.typewriter();
    }
}

</script>

<style scoped>
/* body {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    text-align: center;
}
p {
    margin: 2rem 3rem;
    text-align: start;
} */
#typewriter {
    color: #337CA0;
}

/* The typing effect */
/* @keyframes typing {
  from { width: 0 }
  to { width: 100% }
} */

/* The typewriter cursor effect */
/* @keyframes blink-caret {
  from, to { border-color: transparent }
  50% { border-color: orange; }
} */
</style>