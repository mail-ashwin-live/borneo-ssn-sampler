import s3

num_files, fileList = s3.get_file_count()
print(num_files)
print(s3.get_subset_files(fileList, 10))
