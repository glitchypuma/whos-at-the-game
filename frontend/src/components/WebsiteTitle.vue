<template>
    <body>
        <h1 v-if="selectedGameString">Who's at the {{ selectedGameString }}?</h1>
        <h1 v-if="!selectedGameString">Who's at the game?</h1>
    </body>
</template>

<script>
export default {
    name: 'WebsiteTitle',
    props: {
        selectedGameString: String
    },
}

</script>

<style scoped>
body {
    text-align: center;
}

</style>