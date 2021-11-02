import math

array = []


def hitungMean(data):
    total = 0
    for i in data:
        total += i
    return total / len(data)


def hitungKorelasi(dataX, dataY):
    meanX = hitungMean(dataX)
    meanY = hitungMean(dataY)
    atas = 0
    bawah1 = 0
    bawah2 = 0

    for i in range(0, 50):
        atas += ((dataX[i] - meanX) * (dataY[i] - meanY))
        bawah1 += (dataX[i] - meanX) ** 2
        bawah2 += (dataY[i] - meanY) ** 2

    hasil = atas / (math.sqrt(bawah1 * bawah2))
    return hasil


def data(dataX, dataY, index):
    del dataX[:]
    del dataY[:]

    # Usia dan Tekanan Gula Darah
    if index == 1:
        dataX.extend([
            50, 31, 32, 21, 33, 30, 26, 29, 53, 54, 30, 34, 57, 59, 51,
            32, 31, 31, 33, 32, 27, 50, 41, 29, 51, 41, 43, 22, 57, 38,
            60, 28, 22, 28, 45, 33, 35, 46, 27, 56, 26, 37, 48, 54, 40,
            25, 29, 22, 31, 24
        ])
        dataY.extend([
            148, 85, 183, 89, 137, 116, 78, 115, 197, 125,
            110, 168, 139, 189, 166, 100, 118, 107, 103, 115,
            126, 99, 196, 119, 143, 125, 147, 97, 145, 117,
            109, 158, 88, 92, 122, 103, 138, 102, 90, 111,
            180, 133, 106, 171, 159, 180, 146, 71, 103, 105
        ])
        return True

    # Kulit dan Tekanan Gula Darah
    elif index == 2:
        dataX.extend([
            35, 29, 0, 23, 35, 0, 32, 0, 45, 0, 0, 0, 0, 23, 19,
            0, 47, 0, 38, 30, 41, 0, 0, 35, 33, 26, 0, 15, 19, 0,
            26, 36, 11, 0, 31, 33, 0, 37, 42, 47, 25, 0, 18, 24, 0,
            39, 0, 27, 32, 0
        ])
        dataY.extend([
            148, 85, 183, 89, 137, 116, 78, 115, 197, 125,
            110, 168, 139, 189, 166, 100, 118, 107, 103, 115,
            126, 99, 196, 119, 143, 125, 147, 97, 145, 117,
            109, 158, 88, 92, 122, 103, 138, 102, 90, 111,
            180, 133, 106, 171, 159, 180, 146, 71, 103, 105
        ])
        return True

    # Darah dan Tekanan Gula Darah
    elif index == 3:
        dataX.extend([
            72, 66, 64, 66, 40, 74, 50, 0, 70, 96, 92, 74, 80, 60, 72,
            0, 84, 74, 30, 70, 88, 84, 90, 80, 94, 70, 76, 66, 82, 92,
            75, 76, 58, 92, 78, 60, 76, 76, 68, 72, 64, 84, 92, 110, 64,
            66, 56, 70, 66, 0
        ])
        dataY.extend([
            148, 85, 183, 89, 137, 116, 78, 115, 197, 125,
            110, 168, 139, 189, 166, 100, 118, 107, 103, 115,
            126, 99, 196, 119, 143, 125, 147, 97, 145, 117,
            109, 158, 88, 92, 122, 103, 138, 102, 90, 111,
            180, 133, 106, 171, 159, 180, 146, 71, 103, 105
        ])
        return True

    else:
        return False


def hitungPCA(data, index):
    if index == 1:
        for x in data:
            array.append([x])
    else:
        for y in range(len(array)):
            array[y].append(data[y])


print("Data diabetes (50 dari 768 data)")
print("-------------------------------")
print("|      Korelasi Pearsson      |")
print("-------------------------------\n")

dataX = []
dataY = []
for index in range(1, 4):
    if data(dataX, dataY, index) == True:
        hasil = hitungKorelasi(dataX, dataY)
        hitungPCA(dataX, index)
        if (index == 1):
            print(
                "Korelasi Usia dengan Tekanan Gula Darah\n---------------------------------------")
            print("Data Usia : " + (str(dataX)))
        if (index == 2):
            print(
                "Korelasi Kulit dengan Tekanan Gula Darah\n----------------------------------------")
            print("Data Kulit : " + (str(dataX)))
        if (index == 3):
            print(
                "Korelasi Tekanan Darah dengan Tekanan Gula Darah\n------------------------------------------------")
            print("Data Tekanan Darah : " + (str(dataX)))

        print("Data Tekanan Gula Darah : " + (str(dataY)))
        print("Nilai Korelasi = %1.2f\n" % hasil)
    else:
        print("Tidak dapat menemukan hasil")

meanFitur = [0, 0, 0]
for x in array:
    for y in range(len(x)):
        meanFitur[y] += x[y]

for x in range(len(meanFitur)):
    meanFitur[x] /= len(array)

sum1 = [0, 0, 0]
sum2 = [0, 0, 0]
sum3 = [0, 0, 0]
for index in range(1, 4):
    if data(dataX, dataY, index) == True:
        for x in dataX:
            sum1[index - 1] += pow(x - meanFitur[index - 1], 2)
        sum1[index - 1] = 1/4 * sum1[index - 1]

print(str(sum1))
