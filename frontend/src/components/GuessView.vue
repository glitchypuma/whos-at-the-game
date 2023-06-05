<template>
    <body>
        <div class="guessTitle" ref="typewriter" id="typewriter">
        </div>
    </body>
</template>

<script>
import Typewriter from 'typewriter-effect/dist/core'

export default {
    name: 'GuessView',
    props: {
        guessName: String
    },

    data() {
        return {
            guessTitle: this.guessName
        }
    },

    methods: {
        async typewriter(){
            try {
                const typeContainer = await this.$refs.typewriter;
                const type = this.guessTitle;
                var typewriter = new Typewriter(typeContainer, {
                    cursor: "",
                    autoStart: true,
                    loop: false
                })
                typewriter
                    .typeString(type)
                    .start()
            } catch (error) {
                console.log(error);
            }    
        },
    },
    mounted() {
        this.typewriter();
    },
}

</script>

<style scoped>
/* #typewriter {
    
} */
.guessTitle {
    font-family: var(--feature-font);
    font-size: 2rem;
    color: var(--feature-text);
}
</style>