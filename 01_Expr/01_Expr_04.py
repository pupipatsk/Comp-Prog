import math

w = float(input())
h = float(input())

print((w*h)**.5/60) # Mosteller
print(.024265 * w**.5378 * h**.3964) # Haycock
print(.0333 * w**(.6157-.0188*math.log(w, 10)) * h**.3) # Boyd