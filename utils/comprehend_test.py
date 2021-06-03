import comprehend

client = comprehend.init()
inFile = '../data/output/set1/file11.txt'
file = open(inFile, 'r')
text = file.read()

response = comprehend.detect_ssn(client, text)
print('processing file - ', inFile)
if not response:
    print('No SSN Found')
for r in response:
    if r.get('Type') == 'SSN' and r.get("Score") > 0.98:
        print('Found SSN with Score - ', r.get("Score"))
    else:
        print('No SSN Found')
    