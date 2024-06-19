import os
from dataclasses import dataclass
from typing import Dict, List, Tuple

import requests
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Case:
    case_id: int
    name: str
    court: str
    docket_number: str
    download_url: str


class Cases:

    def __init__(self):
        self.cases: Dict[str, Case] = dict()
        self.cases_names: List[Tuple] = list()
        self.cases_ids: List[int] = list()

    def register_case(self, raw_case):
        case_id = raw_case["id"]
        self.cases_ids.append(case_id)

        case_name = raw_case["caseName"]
        self.cases_names.append(case_name)

        self.cases.update(
            {
                case_id: Case(
                    case_id, raw_case["caseName"], raw_case["court"], raw_case["docketNumber"], raw_case["download_url"]
                )
            }
        )

    def get_all_cases(self) -> Dict[str, Case]:
        return self.cases

    def get_all_names(self) -> List[str]:
        return self.cases_names

    def get_all_ids(self) -> List[int]:
        return self.cases_ids


def search_cases(search_query: str):
    load_dotenv()
    COURT_LISTENER_URL = "https://www.courtlistener.com/api/rest/v3"
    court_listener_api_token = os.getenv("COURT_LISTENER_API_TOKEN")
    try:
        response = requests.get(
            headers={"Authorization": "Token " + court_listener_api_token},
            url=f"{COURT_LISTENER_URL}/search/?q={search_query}&type=o",
        )
    except Exception as e:
        # TODO: Create a custom error
        raise e

    # TODO: Handle pagination
    results = response.json()["results"]

    cases = Cases()

    [cases.register_case(case) for case in results]

    return cases
