import s3

num_files, fileList = s3.get_file_count(True, '../data/output/')
print(num_files)
print(s3.get_subset_files(fileList, 10))

for file in s3.get_subset_files(fileList, 10):
    print(s3.get_file_text(True, file))