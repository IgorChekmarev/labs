import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize = (10, 6))
    plt.plot(time, voltage)
    plt.title('График зависимости V(T)')
    plt.xlabel('Время, с')
    plt.ylabel('Напряжение, В')
    plt.axis([0, 60, 0, max_voltage])
    plt.grid(True)
    #plt.show()

def plot_sampling_period_hist(time):
    sampling_periods = []
    for i in range(len(time)):
        if i == 0:
            sampling = time[0]
        else:
            sampling = time[i] - time[i-1]
        sampling_periods.append(sampling)
    
    plt.figure(figsize = (10, 6))
    plt.hist(sampling_periods)
    plt.title('Распределение периодов дискретизации измерений по времени на одно измерение')
    plt.xlabel('Период измерения, с')
    plt.ylabel('Напряжение, В')
    #plt.xlim(0, 0.06)
    plt.grid(True)
    plt.show()