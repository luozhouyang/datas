import time
import argparse
import os

from urllib import request


class Downloader:

    def __init__(self, base_url, record_file, save_folder, ranges):
        cur_path = os.path.dirname(__file__)
        self.record_file = record_file
        if not self.record_file:
            self.record_file = os.path.join(cur_path, "record.txt")
        self.save_folder = save_folder
        if not save_folder:
            self.save_folder = os.path.join(cur_path, "download")
        if not base_url:
            raise TypeError("base url is NoneType")
        self.base_url = base_url
        if ranges and len(ranges) == 2:
            self.start_id = int(ranges[0])
            self.end_id = int(ranges[1])
        else:
            self.start_id = 700000
            self.end_id = 800000

    def download(self):
        start_id = self._read_start_id()
        print("Start id: %d" % start_id)
        success_count = 0
        prev_err_id = start_id
        continuous_err_count = 0
        for id in range(start_id, self.end_id):
            try:
                time.sleep(1)
                resp = request.urlopen(self.base_url + str(id), timeout=2.0)
                if resp.getcode() != 200:
                    continue
                page = resp.read().decode('gbk')
                if not os.path.exists(self.save_folder):
                    os.makedirs(self.save_folder)
                file = self.save_folder + "/" + str(id) + '.txt'
                with open(file, mode='wt', encoding='utf-8', buffering=8192) as f:
                    f.write(page)
            except Exception as e:
                print("Exception occurs in %d" % id)
                if id == prev_err_id + 1:
                    continuous_err_count += 1
                else:
                    continuous_err_count = 0
                if continuous_err_count == 50:
                    print("Continuous error count: %d" % continuous_err_count)
                    # print("Stop program")
                    # break
                    time.sleep(60 * 60)
                    self.download()
                prev_err_id = id
                continue
            else:
                print(str(id))
                success_count += 1
                if success_count % 100 == 0:
                    self._save_start_id(str(id))

    def _read_start_id(self):
        id = self.start_id
        if not os.path.exists(self.record_file):
            return id
        with open(self.record_file, mode="rt", encoding="utf8") as fin:
            id = fin.readline()
            if id:
                id = int(id)
        return id

    def _save_start_id(self, id):
        with open(self.record_file, mode="wt", encoding="utf8") as fout:
            fout.write(id)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_url", type=str, default="http://www.89yn.com/member.asp?id=")
    parser.add_argument("--record_file", type=str, default="/home/allen/PycharmProjects/datas/bajiuwang/record.txt",
                        help="A file to save latest download id.")
    parser.add_argument("--save_folder", type=str, default="/home/allen/PycharmProjects/datas/www89yn_data",
                        help="A folder to save download files.")
    parser.add_argument("--range", type=str, default="700000,800000", help="Comma-separated list of ids.")
    args, _ = parser.parse_known_args()
    downloader = Downloader(base_url=args.base_url, record_file=args.record_file, save_folder=args.save_folder,
                            ranges=args.range.split(","))
    downloader.download()
