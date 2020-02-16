from Functions.ResTest import restest
import numpy as np

# tester to see the effect of circle resolution on the accuracy of the program

res = range(1, 100, 1);
accuracy = []

for resn in res:
    accuracy.append(restest(resn))

file = open("/home/dan/HWAProj/Accuracy.txt","w");

for acc in accuracy:
    file.write(str(acc))
    file.write(str(", "))

print(accuracy)
