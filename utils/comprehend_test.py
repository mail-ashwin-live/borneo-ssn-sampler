import comprehend

client = comprehend.init()

file = open('../data/output/set1/file11.txt', 'r')
text = file.read()

response = comprehend.detect_ssn(client, text)
print(response)