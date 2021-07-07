import random
#生成随机字符
key_lis=[1]*27;
def rdm_key():
    rdm_char = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890");
    return rdm_char;

for i in range(27):
        key_lis[i] = rdm_key();

box="-";

print(box.join(key_lis))
