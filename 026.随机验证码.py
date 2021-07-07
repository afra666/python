import random
#生成随机字符
def rdm_key():
    rdm_char = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890");
    return rdm_char;
def key_24():
    for i in range(6):
        print(rdm_key(), end="");
    print("-", end="");
    for i in range(6):
        print(rdm_key(), end="");
    print("-", end="");
    for i in range(6):
        print(rdm_key(), end="");
    print("-", end="");
    for i in range(6):
        print(rdm_key(), end="");
    print("-", end="");
    for i in range(6):
        print(rdm_key(), end="");
    print("-", end="");
    for i in range(6):
        print(rdm_key(), end="");
key_24();



输出
369VPP-OdXmPl-HccsCj-QbngNr-2qml9c-gOMG5l
