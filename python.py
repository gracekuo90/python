new_account=input("請輸入新帳號:")
print("深石公司登入系統")
while (True):
	account=input("請輸入你的帳號:")
	if new_account!=account:
		print("你的帳號錯誤")
	else:
		print("歡迎進入深石系統")
		break

