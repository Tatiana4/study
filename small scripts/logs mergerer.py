import heapq, contextlib, glob2, datetime

now = datetime.datetime.now()
filenames = glob2.glob('*.log')

with contextlib.ExitStack() as stack:
    files = [stack.enter_context(open(fname)) for fname in filenames]
    with open(now.strftime('%Y-%m-%d %H-%M-%S') + '.log', 'w') as file:
        file.writelines(heapq.merge(*files))