import matplotlib.pyplot as plt
fig=plt.figure(figsize=(10,12))
ax1=fig.add_subplot(211)
ax2=fig.add_subplot(212)
ax1.bar([4,5,8],[3,8,9])
ax2.bar([3,4,5],[6,7,8])
plt.show()