import sys, argparse, requests, json

def main(argv):
	parser = argparse.ArgumentParser(description='Search vocab on Shanbay')
	parser.add_argument('word', help='world to search')

	args = parser.parse_args()

	word = args.word

	url = 'https://api.shanbay.com/bdc/search/'

	data = requests.get(url=url, params={'word': word})
	result = json.loads(data.text)
	#print(result)
	print("https://www.shanbay.com/bdc/vocabulary/"+str(result['data']['content_id'])+"/")

if __name__ == "__main__":
	main(sys.argv[1:])
