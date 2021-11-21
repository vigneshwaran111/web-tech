import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
 
def update_line(i,data,dx,line):
    data +=dx
    line.set_data(data)
    return line,
 
dx = np.random.rand(2, 500)
data = np.random.rand(2, 500)*-3
fig = plt.figure()
 
 
line, = plt.plot([], [], 'r*')
ax = fig.add_subplot(111)
#ax.set_axis_bgcolor(&amp;quot;white&amp;quot;)
 
plt.xlim(-3, 6)
plt.ylim(-3,6)
 
 
fig.suptitle('H a p p y    D i w a l i', fontsize=20)
line_ani = animation.FuncAnimation(fig, update_line,fargs=(data,dx, line),
interval=50, blit=False)
plt.axis('off')
plt.show()