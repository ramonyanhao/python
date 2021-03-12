import time
import requests
import os

def process_file(url, target_path):
    start = time.time()
    size_done = 0
    response = requests.get(url, stream=True)
    chunk_size = 1024
    content_length = int(response.headers["content-length"])
    file_size = content_length / 1024 / 1024
    if response.status_code == 200:
        with open(target_path, "wb")as file:
            for chunk_bytes in response.iter_content(chunk_size):
                file.write(chunk_bytes)
                size_done += chunk_size
                print("\r" + "[downloded%s%s%.2f%%]" % ('█' * int(size_done * 50 / content_length),  # 50代表共有50个█
                                                              '□'*int(50-(size_done * 50 / content_length)),float(size_done / content_length * 100)), end="")
    costs = float(time.time() - start)
    print("\nDownloaded %s Successfully, use time %.2fs,file size %.2fM." % (
    os.path.basename(target_path), costs, file_size), end="\n")


if __name__ == '__main__':
    url = "http://cdn2.ime.sogou.com/dl/index/1571302197/sogoupinyin_2.3.1.0112_amd64.deb?st=5Yzdh3CQffIhJFj1yH0t7w&e=1581503601&fn=sogoupinyin_2.3.1.0112_amd64.deb"
    target = os.path.join(os.getcwd(), "sougou_input.deb")
    process_file(url, target)