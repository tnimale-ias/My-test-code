import matplotlib.pyplot as plt

event_times = [int(i) for i in open('data/test_data/event_times.txt').read().split('\n') if i !='']
temp_ans = 1000/(event_times[-1]/len(event_times))
print(temp_ans)


batch_size = [5, 10, 20]
fig, ax = plt.subplots()
width = 0.2
x = [1, 2, 3]
ax.bar([i - width/2 for i in x], [temp_ans, temp_ans, temp_ans],width, label='Client Side')
ax.bar([i + width/2 for i in x], [20, 10, 5],width, label='Server Side')

# Add labels and a legend
plt.title("Event Frequency Comparison")
plt.xticks([i + width/2 for i in x], ["batch of "+str(i) for i in batch_size])
plt.xlabel('Batch Size')
plt.ylabel('Event Frequency (per second)')
plt.legend()

# Show the chart
plt.show()