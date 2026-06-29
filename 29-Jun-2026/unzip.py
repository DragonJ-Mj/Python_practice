#unzip

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]

zipped = zip(names, scores)
unzipped_names, unzipped_scores = zip(*zipped)

print("Unzipped Names:", unzipped_names)
print("Unzipped Scores:", unzipped_scores)
