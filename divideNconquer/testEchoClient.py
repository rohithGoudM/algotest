# Echo client program
import socket
import json

HOST = 'tocstream.edelweiss.in'    # The remote host
PORT = 9443              # The same port as used by the server

m = {
	"request":	{
		"streaming_type": "quote3",
		"data":	{
			"accType": "EQ",
			"symbols": [{"symbol":"3530_NSE"}]
			},
		"formFactor": "M",
		"appID": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHAiOjAsImZmIjoiVyIsImJkIjoid2ViLXBjIiwibmJmIjoxNjE2Mzk3MzMyLCJzcmMiOiJlbXRtdyIsImF2IjoiMS4wLjAiLCJhcHBpZCI6ImQ5MDM1NjFiZTFhYWUyYWY3M2RjZTJjOWJhODFiODViIiwiaXNzIjoiZW10IiwiZXhwIjoxNjE2NDM3ODAwLCJpYXQiOjE2MTYzOTc2MzJ9.iy2c_iialRdLSTLcHMHD0JM81DDUMHwGx9SrreVass8",
		"response_format": "json",
		"request_type": "subscribe"
	},
	"echo": {}
	}

body = json.dumps(m)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('connected')
    s.send(bytes(body,'UTF-8'))
    print('request sent')
    while True:
    	data = s.recv(1024)
    	if not data: break
    	print(data)
    	print(data.decode())
print('Received', repr(data))
