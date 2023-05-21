import * as baseballGames from './baseball.js'
import * as basketballGames from './basketball.js'
import * as footballGames from './football.js'

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
               return { data: footballGames.mls };
       }
       return Error(sport + " was not recognized as a sport!")
   }
};