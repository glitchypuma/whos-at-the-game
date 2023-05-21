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
        game: {
            home: String, 
            away: String
        }
    }
}

</script>

<style scoped>
body {
    text-align: left;
}
</style>