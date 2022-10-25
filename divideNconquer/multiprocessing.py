from multiprocessing import Process, Pipe
from threading import Timer

ltp = 9878

def hello():
    print(ltp)
    Timer(1,hello).start()

def f(conn):
	i=0
	while i<1000000000:
		conn.send(i)
		i=i+1
	conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()

    t = Timer(1.0, hello)
    t.start()

    while True:
    	ltp = parent_conn.recv()
    	# print(parent_conn.recv())   # prints "[42, None, 'hello']"
    p.join()