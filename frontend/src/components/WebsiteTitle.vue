<template>
    <body>
        <h1 v-if="selectedGameString">Who's at {{ selectedGameString }}?</h1>
        <h1 v-if="!selectedGameString">Who's at the game?</h1>
    </body>
</template>

<script>
export default {
    name: 'WebsiteTitle',
    props: {
        /** Pass anything needed to scrape twitter */
        selectedGameString: String
    }
}

</script>

<style scoped>
body {
    /* color: #552583; */
    text-align: center;
}

</style>