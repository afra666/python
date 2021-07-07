my_list=[100,"ABC",3.14,'python',False];
print(my_list);
print(my_list[1]);

#追加元素
my_list.append("good")
print(my_list);

#插入元素
my_list.insert(0,"word");
print(my_list);


输出
[100, 'ABC', 3.14, 'python', False]
ABC
[100, 'ABC', 3.14, 'python', False, 'good']
['word', 100, 'ABC', 3.14, 'python', False, 'good']
