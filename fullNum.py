import sys,getopt

def execDic(numLen):
    print("正在写入……")
    # for i in range(int(str(1)+("0"*numLen))):
    #     if i/10 < 1:
    #         s = "0"*(numLen-1) + str(i)
    #         writeFile(numLen,s)
    #     elif 1 < i/10 < 10:
    #         s = "0"*(numLen-2) + str(i)
    #         writeFile(numLen,s)
    #     elif 1 < i/10 < 100:
    #         s = "0"*(numLen-3) + str(i)
    #         writeFile(numLen,s)
    #     elif 1 < i/10 < 1000:
    #         s = "0"*(numLen-4) + str(i)
    #         writeFile(numLen,s)
    #     elif 1 < i/10 < 10000:
    #         s = "0"*(numLen-5) + str(i)
    #         writeFile(numLen,s)
    #     elif 1 < i/10 < 100000:
    #         s = "0"*(numLen-6) + str(i)
    #         writeFile(numLen,s)
    for i in range(int("9"*int(numLen))+1):
        s = str(i).rjust(numLen,"0")
        writeFile(numLen,s)
    print("Done! OK!")
            
def writeFile(numLen,password):
    with open("password_"+str(numLen)+".txt","a") as f:
        f.write(password + "\n")


def _h():
    print("Usage: fullNum.py -h    --help")
    print("       fullNum.py -n 4, A num of length 4")
    #print("        fullNum.py 4,A num of length 4")


def main():
    argv = sys.argv[1:]
    if argv:
        try:
            opts,args = getopt.getopt(argv,"-h-n:",["help","num"])
        except getopt.GetoptError:
            _h()
            sys.exit()

        for opt,arg in opts:
            if opt in  ("-h","--help"):
                _h()
                sys.exit()
            elif opt in ("-n","--num"):
                try:
                    if 0 < int(arg) <= 6:
                        #print(int(arg))
                        execDic(int(arg))
                    else:
                        print("请输入长度大于0小于等于6的数字！")
                except ValueError:
                    print("请输入数字！")
    else:
        _h()
            


if __name__ == "__main__":
    main()
