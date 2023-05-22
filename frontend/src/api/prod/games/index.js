import axios from "axios";

 const root = 'http://localhost:8000/'

 export default {
    baseballPath: 'baseball_games_today/',
    basketballPath: 'basketball_games_today/',
    nflPath: 'football_games_today/',
    ncaaPath: 'ame_football_games_today/1/',
    footballPath: 'ame_football_games_today/2/',
    get(sport) {
        switch(sport) {
            case 'baseball':
                return axios.get(root + this.baseballPath)
            case 'basketball':
                return axios.get(root + this.basketballPath)
            case 'nfl':
                return axios.get(root + this.nflPath)
            case 'ncaa':
                return axios.get(root + this.ncaaPath)
            case 'football':
                return axios.get(root + this.footballPath)
        }
        return Error(sport + " was not recognized as a sport!")
    }
 };