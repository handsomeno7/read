def read_file(filename):
	data = []
	count = 0
	with open(filename, 'r') as f:
		for line in f:
			data.append(line)
			count += 1
			if count % 1000 == 0:#每一千筆印一次(進度條)
				print(len(data))
	print('檔案讀取完了，總共有', len(data), '筆資料')
	print(data[0])
	return(data)


def word(data):
	wc = {} # word_count
	for d in data:
		words = d.split()
		for word in words:
			if word in wc:
				wc[word] += 1
			else:
				wc[word] = 1 #新增新的Key進wc字典

	for word in wc:
		if wc[word] > 100000:# 若字出現過100次
			print(word, wc[word])

	print (len(wc))
	while True:
		word = input('請問你想查什麼字: ')
		if word == 'q':
			break
		if word in wc:
			print(word, '出現過的次數為', wc[word])
		else:
			print('這個字沒有出現過喔!')



def sum_len(data):
	sum_len = 0
	for d in data:
		sum_len = sum_len + len(d)
	print('留言平均長度為', sum_len/len(data), '個字')


def main():
	data = read_file('reviews.txt')
	word(data)
	#avg = sum_len(data)


main()

