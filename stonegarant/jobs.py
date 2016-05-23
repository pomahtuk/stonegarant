from django_rq import job

@job
def long_running_func1():
    pass

@job('high')
def long_running_func2():
    pass

# long_running_func2.delay()
