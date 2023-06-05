<template>
    <body>
        created by <a alt="GitHub repository with this website's code (opens in new tab)" target="_blank" href="https://github.com/glitchypuma/whos-at-the-game">glitchyPuma</a>
    </body>
</template>

<script>
export default {
    name: 'WebsiteFooter',
    props: {
        /** Pass anything needed to scrape twitter */
        selectedGameString: String
    }
}

</script>

<style scoped>
body {
    color: gray;
    text-align: center;
}
a {
    text-decoration: none;
}

</style>