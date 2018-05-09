import argparse

from zuyou.fetcher import Fetcher

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str, default="zuyou", help="Which website you want to fetch data.")
    args, _ = parser.parse_known_args()
    if args.type == "zuyou":
        fetcher = Fetcher()
        fetcher.fetch_range()
