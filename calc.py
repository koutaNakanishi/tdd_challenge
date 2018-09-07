
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

    def input_to_data(self,input):

        ret = []
        for arr in input:
            ret.append(arr.strip().split(","))


        for i in range(len(ret)):
            for j in range(len(ret[i])):
                ret[i][j]=int(ret[i][j])
                
        return ret
