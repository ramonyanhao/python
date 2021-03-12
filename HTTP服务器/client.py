import os,time
def get_job():
    url = 'http://127.0.0.1:5088'
    job = os.popen("curl {0}".format(url)).readlines()
    job=job[0]
    print(job)
    return job
while True:
    try:
        job = get_job()
    except:
        job = '404'
    time.sleep(60)
