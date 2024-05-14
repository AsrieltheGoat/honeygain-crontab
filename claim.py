#!/usr/bin/env python3
import os
import requests

# Define the URLs
pot_url = "https://dashboard.honeygain.com/api/v1/contest_winnings"
balance_url = "https://dashboard.honeygain.com/api/v1/users/balances"


def get_headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


def pot_winnings(session: requests.Session, headers: dict) -> dict:
    response = session.get(pot_url, headers=headers)
    return response.json()


def pot_claim(session: requests.Session, headers: dict) -> dict:
    response = session.post(pot_url, headers=headers)
    return response.json()


def main() -> None:
    with requests.session() as session:
        headers = get_headers(os.getenv("TOKEN")) #! This propose a huge security risk

        # Check current pot winnings
        pot_winning = pot_winnings(session, headers)

        if "data" in pot_winning and "winning_credits" in pot_winning["data"]:
            if pot_winning["data"]["winning_credits"] is None:
                # Claim the pot
                claimed_pot = pot_claim(session, headers)
                print(f'Claimed {claimed_pot["data"]["credits"]} credits.')
                # Check balance
                balance = session.get(balance_url, headers=headers).json()
                print(f'You currently have {balance["data"]["payout"]["credits"]} credits.')
        else:
            print("Pot has already been claimed or not available.")

if __name__ == "__main__":
    main()
