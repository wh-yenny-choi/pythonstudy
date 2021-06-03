def sum(input,result):
    with open(result,'w',encoding='utf-8') as result:
        with open(input,'r',encoding='utf-8') as f:
            data = f.read().split().copy()
            for i in range(len(data)):
                if i%2==0:
                    if int(data[i+1])<0:
                        sic = data[i] + data[i+1]
                        sum_result = str(int(data[i])+int(data[i+1]))
                        result.write(sic)
                        result.write('=')
                        result.write(sum_result+'\n')
                    else:
                        sic = data[i] + '+' + data[i + 1]
                        sum_result = str(int(data[i]) + int(data[i + 1]))
                        result.write(sic)
                        result.write('=')
                        result.write(sum_result + '\n')

if __name__ == '__main__':
    sum('sum_test.txt','sum_result.txt')
