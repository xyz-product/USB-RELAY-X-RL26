import serial
import time
# リレーA～Zを順番にON/OFFしていくプログラム

# お使いのCOMポートに合わせて変更してください
ser = serial.Serial(r"\\.\COM10")

# リレーA
ser.write("A1".encode("ascii"))
time.sleep(1)
ser.write("A0".encode("ascii"))
time.sleep(1)

# リレーB
ser.write("B1".encode("ascii"))
time.sleep(1)
ser.write("B0".encode("ascii"))
time.sleep(1)

# リレーC
ser.write("C1".encode("ascii"))
time.sleep(1)
ser.write("C0".encode("ascii"))
time.sleep(1)

# リレーD
ser.write("D1".encode("ascii"))
time.sleep(1)
ser.write("D0".encode("ascii"))
time.sleep(1)

# リレーE
ser.write("E1".encode("ascii"))
time.sleep(1)
ser.write("E0".encode("ascii"))
time.sleep(1)

# リレーF
ser.write("F1".encode("ascii"))
time.sleep(1)
ser.write("F0".encode("ascii"))
time.sleep(1)

# リレーG
ser.write("G1".encode("ascii"))
time.sleep(1)
ser.write("G0".encode("ascii"))
time.sleep(1)

# リレーH
ser.write("H1".encode("ascii"))
time.sleep(1)
ser.write("H0".encode("ascii"))
time.sleep(1)

# リレーI
ser.write("I1".encode("ascii"))
time.sleep(1)
ser.write("I0".encode("ascii"))
time.sleep(1)

# リレーJ
ser.write("J1".encode("ascii"))
time.sleep(1)
ser.write("J0".encode("ascii"))
time.sleep(1)

# リレーK
ser.write("K1".encode("ascii"))
time.sleep(1)
ser.write("K0".encode("ascii"))
time.sleep(1)

# リレーL
ser.write("L1".encode("ascii"))
time.sleep(1)
ser.write("L0".encode("ascii"))
time.sleep(1)

# リレーM
ser.write("M1".encode("ascii"))
time.sleep(1)
ser.write("M0".encode("ascii"))
time.sleep(1)

# リレーN
ser.write("N1".encode("ascii"))
time.sleep(1)
ser.write("N0".encode("ascii"))
time.sleep(1)

# リレーO
ser.write("O1".encode("ascii"))
time.sleep(1)
ser.write("O0".encode("ascii"))
time.sleep(1)

# リレーP
ser.write("P1".encode("ascii"))
time.sleep(1)
ser.write("P0".encode("ascii"))
time.sleep(1)

# リレーQ
ser.write("Q1".encode("ascii"))
time.sleep(1)
ser.write("Q0".encode("ascii"))
time.sleep(1)

# リレーR
ser.write("R1".encode("ascii"))
time.sleep(1)
ser.write("R0".encode("ascii"))
time.sleep(1)

# リレーS
ser.write("S1".encode("ascii"))
time.sleep(1)
ser.write("S0".encode("ascii"))
time.sleep(1)

# リレーT
ser.write("T1".encode("ascii"))
time.sleep(1)
ser.write("T0".encode("ascii"))
time.sleep(1)

# リレーU
ser.write("U1".encode("ascii"))
time.sleep(1)
ser.write("U0".encode("ascii"))
time.sleep(1)

# リレーV
ser.write("V1".encode("ascii"))
time.sleep(1)
ser.write("V0".encode("ascii"))
time.sleep(1)

# リレーW
ser.write("W1".encode("ascii"))
time.sleep(1)
ser.write("W0".encode("ascii"))
time.sleep(1)

# リレーX
ser.write("X1".encode("ascii"))
time.sleep(1)
ser.write("X0".encode("ascii"))
time.sleep(1)

# リレーY
ser.write("Y1".encode("ascii"))
time.sleep(1)
ser.write("Y0".encode("ascii"))
time.sleep(1)

# リレーZ
ser.write("Z1".encode("ascii"))
time.sleep(1)
ser.write("Z0".encode("ascii"))
time.sleep(1)

ser.close()
