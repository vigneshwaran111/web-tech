def check_same_or_not(target,actual):
    if target[8::]==actual[8::]:
        return True
    else:
        return False
x1 = [0,0,1,1,0,0,1,1,0,0,1,1]  #input for 1st one
x2 = [0,1,0,1,0,1,0,1,0,1,0,1]  #input for 2nd one
target = [0,1,1,1,0,1,1,1,0,1,1,1] #the target output for OR gate
w1=[0.1] #takes a random value for weight 1
w2=[0.5] #takes a random value for weight 2
w3=[-0.8]  # bias - value initialising
alpha = 0.2  #activation factor value
#print(target[8::])
#print(x1[0])
initiating = 1
stopping = len(x1)    #4
output=[]
del_w1,del_w2,del_w3=[],[],[]  #initialising delta w1,w2,w3 for weight adjustment

while(not(check_same_or_not(target,output))):

    for i in range(initiating , stopping+1):
        net_input = 0
        net_input += round(( (w1[i-1]*x1[i-1]) + (w2[i-1]*x2[i-1])) + w3[i-1],1)   # 0.5-0.8 gives -0.3000...4 so i have used round() to give in 2 one decimal places   
        if(net_input<0):
            output.append(int(0))
        else:
            output.append(int(1))


        print(net_input)       #checking the logic is right or not
   
    
        del_w1.append(alpha*x1[i-1]*(target[i-1]-output[i-1]))         #caltulation of weight adjustment
        del_w2.append(alpha*x2[i-1]*(target[i-1]-output[i-1]))      # alpha * xi * [T-O]
        del_w3.append(alpha*(target[i-1]-output[i-1]))     
     
      #below code is to calculate the next row - 2nd 3rd...   
        w1.append(round(w1[i-1]+del_w1[i-1],1))     #new wi = old wi + delta_wi(which is weight adjusted)
        w2.append(round(w2[i-1]+del_w2[i-1],1))
        w3.append(round(w3[i-1]+del_w3[i-1],1))

    #when loop finishes the output will be resetted and we need to get from the previous values.so
    initiating += 4
    stopping +=4
    print("OUTPUT : ",output)
    print('w1',w1)
    print('w2',w2)
    print('w3',w3)
    print('delta w1' , del_w1)
    print('delta w2' , del_w2)
    print('delta w3' , del_w3)

print("THE TARGET OUTPUT EQUALS TO THE ACTUAL OUTPUT")
print(stopping)
print("THE EQUATION Y = ",w1[stopping-4], '*x1 + ',w2[stopping-4],'*x2 + ' , '(' , round(w3[stopping-4],1) , ')')


