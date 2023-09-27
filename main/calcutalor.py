import copy
import random
import math
import operator
answer=[]



# 定义函数-计算答案
def calculatorFunction(mylist, cal):
    # -----定义参数-----
    cal_list = copy.deepcopy(mylist)  # 复制列表
    cal_cal = copy.deepcopy(cal)  # 复制列表
    cnt = 0  # 初始化-计数器
    ansu = 0  # 初始化-答案的分子
    ansd = 0  # 初始化-答案的分母

    # -----计算部分-----
    # 先计算乘除法
    while cnt < len(cal_cal):
        if cal_cal[cnt] == '×' or cal_cal[cnt] == '÷':
            # 计算答案的分子和分母
            u1 = cal_list[cnt][0]
            d1 = cal_list[cnt][1]
            u2 = cal_list[cnt + 1][0]
            d2 = cal_list[cnt + 1][1]

            if cal_cal[cnt] == '×':  # 计算乘法
                ansu = u1 * u2
                ansd = d1 * d2
            elif cal_cal[cnt] == '÷':  # 计算除法
                ansu = u1 * d2
                ansd = d1 * u2

            # 将答案的分子和分母存储在列表中
            ans = [ansu, ansd]

            # 删除运算当中已经计算的部分
            del cal_cal[cnt]
            del cal_list[cnt + 1]
            del cal_list[cnt]

            # 插入计算的答案
            cal_list.insert(cnt, ans)
        else:
            cnt = cnt + 1

    # 再计算加减法
    cnt = 0  # 初始化计算器
    while cnt < len(cal_cal):
        u1 = cal_list[cnt][0]
        d1 = cal_list[cnt][1]
        u2 = cal_list[cnt + 1][0]
        d2 = cal_list[cnt + 1][1]

        if cal_cal[cnt] == '+':  # 计算加法
            ansu = u1 * d2 + d1 * u2
            ansd = d1 * d2
        elif cal_cal[cnt] == '-':  # 计算减法
            ansu = u1 * d2 - d1 * u2
            ansd = d1 * d2

        # 将答案的分子和分母存储在列表中
        ans = [ansu, ansd]

        # 删除运算当中已经计算的部分
        del cal_cal[cnt]
        del cal_list[cnt + 1]
        del cal_list[cnt]

        # 插入计算的答案
        cal_list.insert(cnt, ans)
    #
    # global answer
    # type0=0
    # if ansd != 0:
    #
    #     answer0=ansu/ansd
    #     for q in answer:
    #         if answer0 == q:
    #             ansd= 0
    #             type0=1
    #     if answer0>=0 & type0==0:
    #         answer.append(answer0)


    ans1 = [[ansu, ansd]]
    return ans1


# 定义函数-约分
def reductionFunction(list_re):
    # -----定义参数-----
    reF = [[] for _ in range(len(list_re))]  # 数据结构，用来存储约分后的题目数据

    # -----计算部分-----
    for i in range(len(list_re)):  # 列表每一行遍历
        # 定义参数
        u = list_re[i][0]  # 分子`
        d = list_re[i][1]  # 分母
        a = 0  # 整数部分

        if d != 0:         # 分母不为0
            # 计算整数部分大小
            while u >= d:  # 分子大于分母
                u = u - d
                a = a + 1

            # 计算约分后的分子和分母
            gcd = math.gcd(u, d)  # 最大公约数
            reu = int(u / gcd)  # 约分后的分子
            red = int(d / gcd)  # 约分后的分母

            # 将约分后的数据存储进reF列表中
            if reu == 0:  # 整数
                reF[i].append(1)
                reF[i].append(a)
            elif reu > 0:  # 非整数
                if a > 0:  # 带分数
                    reF[i].append(3)
                    reF[i].append(reu)
                    reF[i].append(red)
                    reF[i].append(a)
                elif a == 0:  # 真分数
                    reF[i].append(2)
                    reF[i].append(reu)
                    reF[i].append(red)
                else:
                    print("ERROR: The reduction of the function is wrong.")
            else:
                reF[i].append(-1)  # 有负数
        else:
            reF[i].append(-1)   # 分母为0
    return reF


# 定义函数-打印题目
def printFunction(mylist, cal, cnt):
    # 打印题目序号
    with open(r'D:\ruangong\Exercises.txt', 'a', encoding='utf-8') as file:
        file.write(f"{cnt}. ")
        file.close()

    # 约分处理
    list_re = reductionFunction(mylist)

    # 打印题目
    for i in range(len(list_re)):
        # 打印数字
        if list_re[i][0] == 1:  # 整数
            a = list_re[i][1]  # 整数数值
            with open(r'D:\ruangong\Exercises.txt', 'a', encoding='utf-8') as file:
                file.write(f"{a} ")
                file.close()
        elif list_re[i][0] == 2:  # 真分数
            u = list_re[i][1]  # 真分数的分子
            d = list_re[i][2]  # 真分数的分母
            with open(r'D:\ruangong\Exercises.txt', 'a', encoding='utf-8') as file:
                file.write(f"{u}/{d} ")
                file.close()
        elif list_re[i][0] == 3:  # 带分数
            a = list_re[i][3]  # 带分数的整数
            u = list_re[i][1]  # 带分数的分子
            d = list_re[i][2]  # 带分数的分母
            with open(r'D:\ruangong\Exercises.txt', 'a', encoding='utf-8') as file:
                file.write(f"{a}'{u}/{d} ")
                file.close()
        else:
            print("ERROR:The part of printing test is wrong.")

        # 打印运算符
        if i < len(cal):
            operation = cal[i]
            with open(r'D:\ruangong\Exercises.txt', 'a', encoding='utf-8') as file:
                file.write(f"{operation} ")
                file.close()

    # 打印等号
    with open(r'D:\ruangong\Exercises.txt', 'a', encoding='utf-8') as file:
        file.write(f"= \n")
        file.close()


# 定义函数-打印答案
def printAnswer(ans, cnt):
    # 打印答案
    ans_type = ans[0][0]
    if ans_type == 1:  # 整数
        with open(r'D:\ruangong\Answers.txt', 'a', encoding='utf-8') as file:
            file.write(f"{cnt}. {ans[0][1]} \n")
            file.close()
    elif ans_type == 2:  # 真分数
        with open(r'D:\ruangong\Answers.txt', 'a', encoding='utf-8') as file:
            file.write(f"{cnt}. {ans[0][1]}/{ans[0][2]} \n")
            file.close()
    elif ans_type == 3:
        with open(r'D:\ruangong\Answers.txt', 'a', encoding='utf-8') as file:
            file.write(f"{cnt}. {ans[0][3]}'{ans[0][1]}/{ans[0][2]}\n")
            file.close()
    else:
        print("ERROR: The part of printing answer is wrong.")


def answerJudge(cnt):
    list_an = []
    list_an_calcutalor = []
    # 输入答案
    # for i in range(0,cnt):
    #     str1 = input("请输入答案：")
    #     list_an_input.append(str1)

    for i in open(r'D:\ruangong\answer.txt', encoding='utf-8'):
        i, an = i.split('.')
        an = an.lstrip()

        # if i != 10:
        an = an.replace('\n', '')
        list_an.append(an)
    list_an_calcutalor = calcutalorFileExercise()
    list_zuihou=[]
    for line in list_an_calcutalor:
        list_yuan=reductionFunction(line)
        ans_type =list_yuan[0][0]
        if ans_type == 1:
            list_zuihou.append(str(list_yuan[0][1]))
        elif ans_type==2:
            str1="{}/{}".format(list_yuan[0][1],list_yuan[0][2])
            list_zuihou.append(str1)
        elif ans_type==3 :
            str2="{}'{}/{}".format(list_yuan[0][3],list_yuan[0][1],list_yuan[0][2])
            list_zuihou.append(str2)



    # 校对答案
    i = 1
    CCount = 0
    WCount = 0
    Correct = []
    Wrong = []
    for i in range(1, cnt + 1):
        str1=list_an[i-1]
        str2=list_zuihou[i-1]
        #使用正则表达式来比较两个字符串的大小
        if compare_strings(str1,str2) == False:
            WCount += 1
            Wrong.append(i)
        else:
            CCount += 1
            Correct.append(i)

    separator = ', '
    Wrong = separator.join((str(x) for x in Wrong))
    Correct = separator.join((str(x) for x in Correct))

    return Correct, Wrong, CCount, WCount


import re


def compare_strings(str1, str2):
    pattern = r'\d+'
    digits1 = re.findall(pattern, str1)
    digits2 = re.findall(pattern, str2)

    return digits1 == digits2

# 将验证的结果保存在文件中
# 输入的内容：正确的数量，错误的数量，列表对的题目的题号，错误的题目的题号
# 形式：
# Correct: 5 (1, 3, 5, 7, 9)
# Wrong: 5 (2, 4, 6, 8, 10)
def saveJudge(C, W, Ccount, Wcount):
    with open(r'D:\ruangong\Grade.txt', 'a', encoding='utf-8') as file:
        file.write(f"Correct: {Ccount} ({C})\n")
        file.write(f"Wrong: {Wcount} ({W})\n")
        file.close()


# 传入指定的题目文件，计算出答案结果返回结果列表
def calcutalorFileExercise():
    answerList = []
    for i in open(r'D:\ruangong\exercise.txt', encoding='utf-8'):
        qu = i.split('.')
        qu = qu.pop()
        qu = qu.split(' ')
        # qu=[u.strip()for u in qu]
        del qu[0]
        del qu[-1]
        del qu[-1]
        answerList.append(calcuta(qu))
    return answerList


def calcuta(list):
    # 传入一个文件的题目
    # 如果一行
    # ['0','÷','4','+','2'1/4','×‘，’1‘1/7’]
    list_cal = []
    list_num = []

    for i in list:
        if i == '+':
            list_cal.append(i)
        elif i == '-':
            list_cal.append(i)
        elif i == '×':
            list_cal.append(i)
        elif i == '÷':
            list_cal.append(i)
        else:
            list_num.append(i)
    i = 0
    mylist = [[] for _ in range(len(list_num))]
    for j in list_num:
        if j == '0':
            mylist[i].append(0)
            mylist[i].append(1)

        else:

            a, b = tofra(j)
            mylist[i].append(a)
            mylist[i].append(b)
        i += 1
    answer = calculatorFunction(mylist, list_cal)
    return answer


# 将整数字符和带分数字符转化为分数形式
def tofra(strNum):
    list = []
    qu = strNum.split(' ')
    qu = [u.strip() for u in strNum]
    if len(qu) == 1:
        return (int(qu[0])), 1
    elif len(qu) == 3:
        return int(qu[0]),int(qu[2])
    else:
        a = int(qu[0])
        b = int(qu[4])
        c = int(qu[2])
        d = a * b + c
        return d, b


# 定义函数-主函数
def main():
    # 定义参数
    n = int(input("请输入您所需要打印的题目数目："))  # n确定需要打印的题目
    r = int(input("请输入您所需要控制的数值（自然数、真分数和真分数分母）的范围："))  # r控制题目中数值（自然数、真分数和真分数分母）的范围
    cnt = 1  # 题目计数器

    while cnt <= n:
        # -----定义参数-----
        # num用来确定需要运算的数字的个数
        num = random.randint(2, 4)
        mylist = [[] for _ in range(num)]  # 数据结构，用来存储需要运算的数字
        cal = []  # 数据结构，用于存储运算符

        # 定义运算符
        operators = ['+', '-', '×', '÷']
        for i in range(num - 1):
            cal.append(random.choice(operators))

        # 定义运算数字(用分数表示)
        for i in range(num):
            u = random.randint(0, r)  # 分子
            d = random.randint(1, r)  # 分母
            while u / d > r:          # 保证这个数小于r
                u = random.randint(0, r)
                d = random.randint(1, r)
            mylist[i].append(u)
            mylist[i].append(d)

        # -----计算部分-----
        # 计算答案
        list_ans = calculatorFunction(mylist, cal)
        #判断题目是否相同，如果一样将list_ans中的第二个数即分母乘以-1




        # 答案约分
        ans_re = reductionFunction(list_ans)

        # 打印题目和答案
        if ans_re[0][0] != -1:
            printFunction(mylist, cal, cnt)
            printAnswer(ans_re, cnt)
            cnt = cnt + 1


# -----执行主函数-----
#main()
a,b,c,d=answerJudge(15)
saveJudge(a,b,c,d)
