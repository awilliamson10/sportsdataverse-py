import json
from urllib.error import ContentTooShortError, HTTPError, URLError

import pandas as pd

from sportsdataverse.dl_utils import download, underscore


def espn_mbb_matchup(event_id: str) -> pd.DataFrame:
    """espn_mbb_matchup - look up the teams and their stats in a given matchup

    Args:
        event_id (str): Event ID

    Returns:
        pd.DataFrame: Pandas dataframe containing the matchup data

    https://gist.github.com/akeaswaran/b48b02f1c94f873c6655e7129910fc3b
    https://twitter.com/brunotorious/status/1601805418006687745/photo/1
    """
    ev = pd.DataFrame()
    url = "http://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/summary?event={}".format(event_id)
    resp = download(url=url)

    event = json.loads(resp)
    return {
        "teams": {
            "home": {
                "Team Name": event["boxscore"]["teams"][0]["team"]["displayName"],
                "Record Streak": event["boxscore"]["teams"][0]["statistics"][0]["displayValue"],
                "Points": event["boxscore"]["teams"][0]["statistics"][1]["displayValue"],
                "Field Goal %": event["boxscore"]["teams"][0]["statistics"][2]["displayValue"],
                "3 Point %": event["boxscore"]["teams"][0]["statistics"][3]["displayValue"],
                "Rebounds": event["boxscore"]["teams"][0]["statistics"][4]["displayValue"],
                "Assists": event["boxscore"]["teams"][0]["statistics"][5]["displayValue"],
                "Blocks": event["boxscore"]["teams"][0]["statistics"][6]["displayValue"],
                "Steals": event["boxscore"]["teams"][0]["statistics"][7]["displayValue"],
                "Turnovers": event["boxscore"]["teams"][0]["statistics"][9]["displayValue"],
                "Opponent Points": event["boxscore"]["teams"][0]["statistics"][10]["displayValue"],
            },
            "away": {
                "Team Name": event["boxscore"]["teams"][1]["team"]["displayName"],
                "Record Streak": event["boxscore"]["teams"][1]["statistics"][0]["displayValue"],
                "Points": event["boxscore"]["teams"][1]["statistics"][1]["displayValue"],
                "Field Goal %": event["boxscore"]["teams"][1]["statistics"][2]["displayValue"],
                "3 Point %": event["boxscore"]["teams"][1]["statistics"][3]["displayValue"],
                "Rebounds": event["boxscore"]["teams"][1]["statistics"][4]["displayValue"],
                "Assists": event["boxscore"]["teams"][1]["statistics"][5]["displayValue"],
                "Blocks": event["boxscore"]["teams"][1]["statistics"][6]["displayValue"],
                "Steals": event["boxscore"]["teams"][1]["statistics"][7]["displayValue"],
                "Turnovers": event["boxscore"]["teams"][1]["statistics"][9]["displayValue"],
                "Opponent Points": event["boxscore"]["teams"][1]["statistics"][10]["displayValue"],
            },
        },
    }
