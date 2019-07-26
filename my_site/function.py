# from django.http import HttpResponse
from django.shortcuts import render
# render 传递、递交一个网页


# def home(request):
#     return HttpResponse('你好')

def home(request):
    return render(request, 'home.html')
# 需要传入request参数，是用户发出的请求
# 得到请求后进入home.html这个网页


def about(request):
    return render(request, 'about.html')


def count(request):
    user_text = request.GET['text']
    # 将requestGET的输入信息赋值给user_text
    # 再用字典将用户输入的信息打印出来
    total_count = len(user_text)
    word_dict = word_num(user_text)
    # 自己写的方法 参考视频
    word_value = sorted(word_dict.items(),
                        key=lambda word: word[1], reverse=True)
    # key是排序的条件，reversed=True表达升序。word_value将结果赋值给它
    # 而这个字典排序条件是字符的值
    # 写成lambda表达式就是lambda word: word[1]
    # 其中Word就是每一个字符，在字典里就是键
    # 排序是需要一个标准的，
    # 而标准必须可以比较，在字典word_dict里，
    # 值是数字，可以比较，将它作为标准
    return render(request, 'count.html',
                  {'total_count': total_count,
                   'user_text': user_text,
                   'wordict': word_dict,
                   'sorted': word_value})

# 通过len方法得到request参数发送get的test的长度，并且赋值给total_count
# {'total_count': total_count}以字典的形式将len方法得出的长度返回给
# count.HTML里


def word_num(user_text):
    word_dict = {}
    # 创立一个空字典，用来存放遍历的字符
    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
            # 当字典里从来没有的这个字，遍历到它了
            # 就给它一个1的值，记录第一次遍历到它
            # []拿键值对中的值记录
        else:
            word_dict[word] += 1
            # 如果有就在word_dict[word]值中给它加1
    return word_dict
# 获得用户输入的字符
# 将字符存入字典，将记录的次数存入值，字符为键
