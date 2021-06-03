import s3
import comprehend 

num_files, fileList = s3.get_file_count(False, '../data/output/')
print(num_files)
files = s3.get_subset_files(fileList, 1)
print(files)

text = ''
for file in files:
    text = s3.get_file_text(False, file)
    print(text)

client = comprehend.init()
print(comprehend.detect_ssn(client, text))