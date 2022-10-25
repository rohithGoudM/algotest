from multiprocessing import Process, Pipe
from threading import Timer
import socket
import csv
import json

ltp = range(1000)

token_set = []
print(token_set)

def hello():
    # Here I would print the data in 2 rows, 1st row would contain all the exchange tokens
    # Second row would contain their prices. Ex:
    #   exchange_token1     exchange_token2     ......
    #   ltp1                ltp2                ....
    print(ltp)
    Timer(1,hello).start()

def dummy_funtion(j):
    return j+1

def f(conn):
    with open('instruments.csv') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        line_count=0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
            elif line_count<=1000:
                symbolObj = {"symbol":row[0]}
                token_set.append(symbolObj)
            line_count += 1
        print(f'Processed {len(token_set)} lines')

    req = {
        "request":  {
            "streaming_type": "quote3",
            "data": {
                "accType": "EQ",
                "symbols": token_set
                },
            "formFactor": "M",
            "appID": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHAiOjAsImZmIjoiVyIsImJkIjoid2ViLXBjIiwibmJmIjoxNjE2Mzk3MzMyLCJzcmMiOiJlbXRtdyIsImF2IjoiMS4wLjAiLCJhcHBpZCI6ImQ5MDM1NjFiZTFhYWUyYWY3M2RjZTJjOWJhODFiODViIiwiaXNzIjoiZW10IiwiZXhwIjoxNjE2NDM3ODAwLCJpYXQiOjE2MTYzOTc2MzJ9.iy2c_iialRdLSTLcHMHD0JM81DDUMHwGx9SrreVass8",
            "response_format": "json",
            "request_type": "subscribe"
        },
        "echo": {}
        }
    req_body = json.dumps(m)
    rec_msg = ''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print('connected')
        s.send(bytes(body,'UTF-8'))
        print('request sent')
        while True:
            data = s.recv(1024)
            rec_msg += data.decode('UTF-8')
            res = json.loads(rec_msg)
            #here I would format the response into an array of json objects containing
            #exchangetokens and their respective ltps. Ex: [{\\exchange_token1: \\ltp1},{\\et2:\\ltp2},...]
            conn.send(data)
            if not data: break

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