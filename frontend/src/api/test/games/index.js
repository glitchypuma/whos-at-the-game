import * as baseballGames from './baseball.js'
import * as basketballGames from './basketball.js'

export default {
   get(sport) {
       switch(sport) {
           case 'baseball':
               return { data:  baseballGames.mlb }
           case 'basketball':
                return { data: basketballGames.nba }
           case 'nfl':
               return null;
           case 'ncaa':
               return null;
           case 'football':
               return null;
       }
       return Error(sport + " was not recognized as a sport!")
   }
};