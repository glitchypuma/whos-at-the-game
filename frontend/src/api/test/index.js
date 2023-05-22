import * as baseballGames from './games/baseball.js'
import * as basketballGames from './games/basketball.js'
import * as footballGames from './games/football.js'

export default {
   get(path) {
       switch(path) {
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
       return Error(path + " is not a recognized path!")
   }
};