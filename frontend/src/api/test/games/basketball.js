export const nba =
{
    get: "games",
    parameters: {
        league: "12",
        timezone: "America/Los_Angeles",
        date: "2023-05-20",
        season: "2022-2023"
    },
    errors: [],
    results: 1,
    response: [
        {
        id: 349845,
        date: "2023-05-20T17:30:00-07:00",
        time: "17:30",
        timestamp: 1684629000,
        timezone: "America/Los_Angeles",
        stage: null,
        week: "NBA - Semi-finals",
        status: {
            long: "Game Finished",
            short: "FT",
            timer: null
        },
        league: {
            id: 12,
            name: "NBA",
            type: "League",
            season: "2022-2023",
            logo: "https://media-2.api-sports.io/basketball/leagues/12.png"
        },
        country: {
            id: 5,
            name: "USA",
            code: "US",
            flag: "https://media-3.api-sports.io/flags/us.svg"
        },
        teams: {
            home: {
            id: 145,
            name: "Los Angeles Lakers",
            logo: "https://media-2.api-sports.io/basketball/teams/145.png"
            },
            away: {
            id: 139,
            name: "Denver Nuggets",
            logo: "https://media-1.api-sports.io/basketball/teams/139.png"
            }
        },
        scores: {
            home: {
            quarter_1: 20,
            quarter_2: 35,
            quarter_3: 27,
            quarter_4: 26,
            over_time: null,
            total: 108
            },
            away: {
            quarter_1: 32,
            quarter_2: 26,
            quarter_3: 26,
            quarter_4: 35,
            over_time: null,
            total: 119
            }
        }
        }
    ]
}