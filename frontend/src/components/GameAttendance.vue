<template>
    <body>
        <h2>Judging by the conversation on Twitter, here's our best guess:</h2>
        <p>Game:<br>{{ selectedGame }}</p>
    </body>
</template>

<script>
// import api from '../api/api.js'

export default {
    name: 'GameAttendance',

    props: {
        selectedGame: { }
    },

    methods: {
        // TODO: implement output of scraper results
        // async getScraperResults() {
        //     try {
        //         const response = await api.get('baseball');
        //         this.baseballGames = response.data;
        //     } catch (error) {
        //         console.log(error);
        //     }
        // },
    }
}

</script>

<style scoped>
body {
    text-align: center;
}
</style>