import argparse

from www89yn.fetcher import Fetcher

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str, default="www89yn", help="Which website you want to fetch data.")
    args, _ = parser.parse_known_args()
    if args.type == "www89yn":
        fetcher = Fetcher()
        fetcher.fetch_range()
