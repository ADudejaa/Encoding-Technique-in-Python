import matplotlib.pyplot as plt

def Plotting(dataStream,lastSymbol):
    x=0
    dataStream = list(dataStream)
    DManchester = [0]*(2*len(dataStream)+1)
    for i in range(0,len(dataStream)):
        if lastSymbol == 1 and dataStream[i] == '1':
            DManchester[x] = 1
            DManchester[x+1]= 1
            DManchester[x+2]= 0
            lastSymbol =0
            x=x+2

        elif lastSymbol == 0 and dataStream[i] == '1':
            DManchester[x] = 0
            DManchester[x+1]= 0
            DManchester[x+2]= 1
            lastSymbol = 1
            x=x+2
            
        elif lastSymbol == 1 and dataStream[i] == '0':
            DManchester[x] = 1
            DManchester[x+1]= 0
            DManchester[x+2]= 1
            lastSymbol = 1
            x=x+2
            
        elif lastSymbol == 0 and dataStream[i] == '0':
            DManchester[x] = 0
            DManchester[x+1]= 1
            DManchester[x+2]= 0
            lastSymbol = 0
            x=x+2
            
    return DManchester

inputStream = input("Enter the 8 bit data stream: ")
lastSymbol=int(input("Enter the first symbol: "))

DManchester = Plotting(inputStream,lastSymbol)

inputStream = list(inputStream)
inputStream = [int(i) for i in inputStream]

fig, axs = plt.subplots(2)

fig.suptitle('Differential Manchester for 8 bit Stream')
axs[0].plot(inputStream, drawstyle='steps-pre')
axs[0].set_title("Input data stream")
axs[1].plot(DManchester, drawstyle='steps-pre')
axs[1].set_title("Differential Manchester Plot")


for ax in axs.flat:
    ax.label_outer()
print(Manchester)    
plt.show()
