<template>
    <body>
        <h2>Looking at the conversation on Twitter, here's our best guess:</h2>
    </body>
</template>

<script>
export default {
    name: 'GameAttendance',

    props: {
        /** Pass anything needed to scrape twitter */
        params: {
            homeTeam: String,
            awayTeam: String
        }
    }
}

</script>

<style scoped>
body {
    text-align: center;
}
</style>