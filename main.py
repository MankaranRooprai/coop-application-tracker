import matplotlib.pyplot as plt





status = ["Applied", "Rejected", "Interview", "Offer", "No Response"]
responses = [3, 1, 5, 7, 2]
fig, ax = plt.subplots()
ax.barh(status, responses, color = ["blue", "Red", "cyan", "green", "black"])
plt.show()