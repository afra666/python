import random

user_num=input();
#print(user_num);

def rdm_key():
    rdm_char = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890");
    return rdm_char;

key_final="TmfVnk-OdXmPl-HccsCj-QbngNr";
key_len=len(key_final);

#list
for i in range(int(user_num)):
    key_final = list(key_final);
    for i in range(key_len):
        if (i == 6) | (i == 13) | (i == 20):
            key_final[i] = "-";
        else:
            key_final[i] = rdm_key();

    key_final = "".join(key_final);
    #print(key_final)

    my_file = open("key.txt", "a+");
    my_file.write(key_final + "\n");

