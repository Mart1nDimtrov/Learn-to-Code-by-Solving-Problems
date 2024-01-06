# 8.DMOJ problem dmopc14c4p1, New Key

# try two lists - one with the cipher and
# the other with cipher decrypted
message = input()
cipher_encrypted = "0123456789ABCDEFGHIJKLMNOPR"
cipher_decrypted = "9ABCDEFGHIJKLMNOPQRSTUVWXYZ"


for l in message:
	print(cipher_decrypted[cipher_encrypted.index(l)], end="")
