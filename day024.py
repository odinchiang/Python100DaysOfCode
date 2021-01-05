# Intermediate - Files, Directories and Paths

# file = open("day024.txt")
# contents = file.read()
# print(contents)
# file.close()

# 用 with 不需要用 close
# with open("day024.txt") as file:
#     contents = file.read()
#     print(contents)

# mode:
# "r": read (預設值，若 open 時沒有該檔案會報錯)
# "w": write (若 open 時沒有該檔案，會自動新增檔案)
# "a": append (若 open 時沒有該檔案，會自動新增檔案)
with open("day024.txt", mode="a") as file:
    file.write("\nNew text.")
