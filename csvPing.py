import requests, csv, argparse

#parse arguments
parser = argparse.ArgumentParser(description='A commandline tool to check if a host is accessible')
parser.add_argument('-f', type=str, help='CSV file containing only hostnames, IPs or URLs.')
args=parser.parse_args()

#set variables
csvIn = args.f

file = open(csvIn, "r")
data = list(csv.reader(file, delimiter=","))
file.close()

up = down = 0

for i in data[0]:

	print('Checking ' + i)
	try:

		url = f'https://{i}'
		r = requests.get(url, timeout=10)
		print(r.status_code)
		if r.status_code in [200, 301, 401, 403]:

			print(f'UP\n')
			with open("up.txt", "a") as myfile:
				myfile.write(i + '\n')
			up += 1

		else:
			print(f'DOWN\n')
			with open("down.txt", "a") as myfile:
				myfile.write(i + '\n')
			down += 1

	except:
		print(f'DOWN\n')
		with open("down.txt", "a") as myfile:
			myfile.write(i + '\n')
		down += 1

print(f"Complete - {up} UP and {down} DOWN")
