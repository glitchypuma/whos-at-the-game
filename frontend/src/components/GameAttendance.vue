<template>
    <body>

    </body>
</template>

<script>
export default {
    name: 'GameAttendance',

    props: {
        /** Pass anything needed to scrape twitter */
        crawlerParams: {
            homeTeam: String,
            awayTeam: String
        }
    }
}

</script>