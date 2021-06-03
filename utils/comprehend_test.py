import comprehend

client = comprehend.init()
inFile = '../data/output/set1/file76.txt'
file = open(inFile, 'r')
text = file.read()

response = comprehend.detect_ssn(client, text)
print('processing file - ', inFile, response)

    