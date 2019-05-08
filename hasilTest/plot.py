import matplotlib.pyplot as plt 

dot = []
with open('./doppler_compensator_test.txt', 'r') as f :
    data = f.readlines() 
    print(data)
    plt.plot(data, range(len(data)))
    plt.show()
