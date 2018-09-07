
class Calc:
    def calc_price(self, a):
        result = 0
        for i in a:
            result += i
        tmp=result
        result+=tmp//10
        if tmp%10>=5:
            result+=1
        return result

