import matplotlib.pyplot as plt
import pandas as pd

OUTLIER_THRESHOLD = 10000

data_dir = "data/test_data/"
client_dir = "client_side"
server_dir = "server_side"

ad_test_size = [1, 2, 5, 10, 20]

client_avg = []
server_avg = []



def cal_avg(values):
    temp_sum = 0
    temp_n = 0
    for value in values:
        if value < OUTLIER_THRESHOLD:
            temp_sum += value
            temp_n += 1
    return temp_sum/temp_n


for size in ad_test_size:

    client_values = [int(value) for value in open(data_dir+client_dir+str(size)+".txt").read().split('\n') if value!='']
    client_avg.append(cal_avg(client_values)*size)
    server_values = [int(value) for value in open(data_dir+server_dir+str(size)+".txt").read().split('\n') if value!='']
    server_avg.append(cal_avg(server_values)*size)


print(client_avg)
print(server_avg)

csv_dir = {"Number of Ads":ad_test_size, "Client Side Time": client_avg, "Server Side Time":server_avg}
df = pd.DataFrame(csv_dir)

df.to_csv(data_dir+"Results.csv", index=False)
# Create the chart
fig, ax = plt.subplots()
width = 0.2
x = [1, 2, 3, 4, 5]
ax.bar([i - width/2 for i in x], client_avg,width, label='Client Side')
ax.bar([i + width/2 for i in x], server_avg,width, label='Server Side')

# Add labels and a legend
plt.title("Number of cycles taken by both approaches")
plt.xticks([i + width/2 for i in x], [str(i)+" Ads" for i in ad_test_size])
plt.xlabel('Number of Ads')
plt.ylabel('Number of clock cycles (per calculation)')
plt.legend()

# Show the chart
plt.show()

