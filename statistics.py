market_segments = list()
market_segments.append(('M_Y_L',1836))
market_segments.append(('M_Y_H',517))
market_segments.append(('M_O_L',1795))
market_segments.append(('M_O_H',808))
market_segments.append(('F_Y_L',1980))
market_segments.append(('F_Y_H',256))
market_segments.append(('F_O_L',2401))
market_segments.append(('F_O_H',407))

market_segments.append(('M_Y',2353))
market_segments.append(('M_O',2603))
market_segments.append(('F_Y',2236))
market_segments.append(('F_O',2808))
market_segments.append(('M_L',3631))
market_segments.append(('M_H',1325))
market_segments.append(('F_L',4381))
market_segments.append(('F_H',663))
market_segments.append(('L_Y',3816))
market_segments.append(('L_O',4196))
market_segments.append(('H_Y',773))
market_segments.append(('H_O',1215))

market_segments.append(('M',4956))
market_segments.append(('F',5044))
market_segments.append(('L',8012))
market_segments.append(('H',1988))
market_segments.append(('Y',4589))
market_segments.append(('O',5411))

ms = input("Enter market segment: ")

mss = ms.split('_')

res = list()

for m in market_segments:
    passed = True
    for s in mss:
        if s not in m[0]:
            passed = False
    if(passed):
        res.append(m)

res.sort(key = lambda x: x[1],reverse = True)
for m in res:
    print(m)


