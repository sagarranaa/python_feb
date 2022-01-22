list=[]
for i in range(5):
    x=input("Enter 5 number:")
    list.append((x))
    # print(x)
def count(list):
    greater=0
    lesser=0
    for i in list:
        if len(i)>=5:
            greater+=1
        else:
            lesser+=1
        return greater,lesser
greater,lesser=count(list)
print("Greater:{} and lesser:{}".format(greater,lesser))