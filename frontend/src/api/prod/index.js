import axios from "axios";

 const root = 'https://www.gameapi.buzz/'

 export default {
    baseballPath: 'baseball_games_today/',
    basketballPath: 'basketball_games_today/',
    footballPath: 'football_games_today/',
    nflPath: 'ame_football_games_today/1/',
    ncaaPath: 'ame_football_games_today/2/',
    scraperPath: '', // TODO
    get(path) {
        switch(path) {
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
            case 'scraper': //TODO
                return axios.get(root + this.scraperPath)
        }
        return Error(path + " was not recognized as a path!")
    }
 };