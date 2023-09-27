
import unittest

from calclass import calclass

class Testcal(unittest.TestCase):

    #测试题目的计算
    def test_calcutalor(self):
        strlist1=[
            [9,4],
            [8,4],
            [2,4]
        ]
        callist1=['+','÷']
        strlist2 = [
            [4, 3],
            [9, 7],
            [3, 3]
        ]
        callist2 = ['+', '×']
        answer1=calclass.calculatorFunction(strlist1,callist1)
        answer2=calclass.calculatorFunction(strlist2,callist2)
        print(answer1,answer2)


    #测试校对答案
    def test_answeJudge(self):
        a,b,c,d=calclass.answerJudge()
        print("正确的题目数：",c)
        print(a)
        print('\n')
        print("错误的题目数：", d)
        print(b)

      #测试传入一道完整的题目计算出答案
    def test_calcuta(self):
        str1=['4','÷','4','+',"4'7/6"]
        print(calclass.calcuta(str1))



    def test_saveJudge(self):
        C=[1,2,3,4,5]
        W=[6,7,8,9,10]
        Ccount=5
        Wcount=5
        calclass.saveJudge(C,W,Ccount,Wcount)

    def test_tofra(self):
        strNum1="5/8"
        strNum2="1'5/8"
        print(calclass.tofra(strNum1),calclass.tofra(strNum2))
    #测试是否能生成10000道题目
    def test_main(self):
        calclass.main()

    def test_compare(self):
        str1=['10','2',"1'4/7","4'8/8"]
        str2=['10','1',"1'4/7","4'1/8"]
        for i in range(4):
            if(calclass.compare_strings(str1[i],str2[i]))==True:
                print("相同")
            else:
                print("不相同")

