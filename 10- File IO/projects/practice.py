# practice_text = open(mode="r+", file="./p.txt")

# # print(practice_text.read())
# # print(practice_text.readline())
# # print(practice_text.readline())
# # print(practice_text.readline())
# # print(practice_text.readline())
# # print(practice_text.readline())
# # print(practice_text.readline())
# # print(practice_text.readline())
# # print(practice_text.readline())

# for text_line in practice_text.readlines():
#     print(text_line)

# practice_text.close()

# # print(practice_text.readlines())


with open("./p.txt", "a") as p_f:
    p_f.write("\n new1")
    p_f.write("\n new1")
    p_f.write("\n new1")
    p_f.write("\n new1")
    p_f.write("\n new1")
