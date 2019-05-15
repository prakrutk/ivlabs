text = "X-DSPAM-Confidence:    0.8475"
num = text.find("0")
t = text[num:]
print(float(t))