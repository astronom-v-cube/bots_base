#!/usr/bin/python
# -*- coding: utf-8 -*-
import schedule
import time
from threading import Thread

print('Рассылка запущена...')

def run_threaded(job_func):
    job_thread = Thread(target = job_func)
    job_thread.start()

schedule.every().hour.at(":01").do(run_threaded, analise_sender)

def job_sending():
    while True:
        schedule.run_pending()
        time.sleep(30)
