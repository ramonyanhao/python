import os,time
def cli():
    job = os.popen("curl http://127.0.0.1:8000/").readlines()
    job = ''.join(job)
    print(job)
    return job
try:
    cli()
except:
    cli=cli()
    cli='404'
    time.sleep(60)
