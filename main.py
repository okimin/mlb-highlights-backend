import requests
import json

# Example: Get Dodgers roster
url = "https://statsapi.mlb.com/api/v1/teams/119/roster?season=2024"
response = requests.get(url).content
data = json.loads(response)


def main():
    print(data)

if __name__ == "__main__":
    main()