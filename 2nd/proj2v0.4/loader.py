from numpy import load
data = load ('Q1.npz')
lst = data.files
for item in lst:
    print(item)
    print(data[item])


data = load ('traj.npz')
lst = data.files
for item in lst:
    print(item)
    print(data[item])
