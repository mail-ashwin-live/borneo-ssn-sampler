import s3 

s3client = s3.init()
print(s3.get_file_count(s3client))
