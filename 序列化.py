import pickle

a={'apple':1,"banana":2}

with open('pickle_example.pickle','wb') as f:
    pickle.dump(a,f)

with open('pickle_example.pickle','rb') as f:
    b=pickle.load(f)

print(b)
