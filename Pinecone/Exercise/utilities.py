import itertools

def chunks(iterable, batch_size=100):
    it = iter(iterable)
    chunk = tuple(itertools.islice(it,batch_size))
    while chunk:
        yield chunk #This acts as a return but without finishing the execution
        chunk = tuple(itertools.islice(it, batch_size))