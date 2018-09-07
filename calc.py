import sys
class Calc:
    def calc_price(self, b, output):

        for a in b:

            result = 0
            for i in a:
                result += i
            tmp=result
            result+=tmp//10
            if tmp%10>=5:
                result+=1
            output.write(str(result)+ "\n")


    def input_to_data(self,input):

        ret = []

        for arr in input:
            if len(arr.strip())>0:
                ret.append(arr.strip().split(","))
            else:
                ret.append([0])

        #if len(ret)==0:
        #    return []

        for i in range(len(ret)):
            for j in range(len(ret[i])):
                ret[i][j]=int(ret[i][j])

        return ret

if __name__ == '__main__':
    calc=Calc()
    calc.calc_price(calc.input_to_data(sys.stdin),sys.stdout)
