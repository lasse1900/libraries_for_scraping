import requests
import os
import json
from dotenv import load_dotenv
import time
import sys
import inspect
import argparse
token = os.environ.get("X-RapidAPI-Key")
url = "https://indeed-jobs-api-finland.p.rapidapi.com/indeed-fi/"
job_data = []

def get_results_page(*, offset: int, keyword: str, location: str):
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": os.environ["X-RapidAPI-Key"],
        "X-RapidAPI-Host": "indeed-jobs-api-finland.p.rapidapi.com"
    }
    print(f"Getting results for {keyword} in {location} at offset {offset}")
    response = requests.request("GET", url, headers=headers, params={
        "offset": str(offset),
        "keyword": keyword,
        "location": location,
    })
    response.raise_for_status()
    return response.json()

def get_all_results(keyword: str, location: str, offset: int = 0):
    while True:
        response = get_results_page(offset=offset, keyword=keyword, location=location)
        yield response
        if response[0]['next_page'] == 'True':
            offset += 10
            continue
        print("No more pages")
        break

def get_all_results_into_file(filename: str, keyword: str, location: str):
    job_data = []
    for i, page in enumerate(get_all_results(keyword=keyword, location=location), 1):
        job_data.extend(page)
        print(f"Got page {i}, total jobs {len(job_data)}")

    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(job_data, fp, indent=2, ensure_ascii=False, sort_keys=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-k", "--keyword", required=True, help="Keyword to search for")
    ap.add_argument("-l", "--location", required=True, help="Location to search in")
    ap.add_argument("-o", "--output", required=True, help="Output file")
    args = ap.parse_args()
    get_all_results_into_file(filename=args.output, keyword=args.keyword, location=args.location)

if __name__ == '__main__':
    main()
