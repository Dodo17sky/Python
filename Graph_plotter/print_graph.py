import matplotlib.pyplot as plt
import numpy as np

adcValues = [77,211,324,420,501,571,632,683,728,767,799,828,853,874,893,908,922,934,946,955,963,970,976,981,986,990,993,998,999,1002,]
adcTimestamps = [0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,]

plt.plot(adcTimestamps, adcValues)
xend = (adcTimestamps[-1] + adcTimestamps[1])

plt.axis([0, xend, 0, 1024])

plt.ylabel('Volts')
plt.xlabel('Time')
plt.show()
