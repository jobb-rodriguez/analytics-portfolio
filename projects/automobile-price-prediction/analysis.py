# rodriguez_analysis.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load(file_name):
    data = np.loadtxt(open(file_name, "rb"), dtype="float", delimiter=",")
    data = data[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]

    return data


def hyp(theta, x):
    theta_T = np.array(theta, ndmin=2)
    data_T = np.array(x).T
    if theta_T.shape[1] != data_T.shape[0]:
        theta_T = theta_T.T
    prod = np.dot(theta_T, data_T)
    return prod.T


def cost(theta, data, output):
    sum = 0.0

    rows = data.shape[0]

    for i in range(0, rows):
        sum += (hyp(theta, data[i]) - output[i]) ** 2

    sum = sum / (2.0 * rows)

    return sum


def der(theta, data, output, pos):
    sum = 0.0

    rows = data.shape[0]

    for i in range(0, rows):
        sum += (hyp(theta, data[i]) - output[i]) * data[i, pos]

    sum = sum / (1.0 * rows)

    return sum


data = load("cars_preprocessed.csv")
price = data[:, -1]
# Variables for Different Sets
feature_count = [6]
alphas = [0.02]
titles = ['Length and Width - Order 2 vs Price']
column_names = {
    '0': 'Filler', '1': 'Door Number', '2': 'Car Body', '3': 'Drive Wheel', '4': 'Wheel Base',
    '5': 'Car Length', '6': 'Car Width', '7': 'Car Height', '8': 'Car Volume', '9': 'Car Length Square',
    '10': 'Car Width Squared', '11': 'Curb Weight', '12': 'Cylinder Number', '13': 'Engine Size', '14': 'Horsepower',
    '15': 'City - MPG', '16': 'Price'
}
sets = [[0, 5, 6, 9, 10, 14]]
datas = [data[:, [0, 5, 6, 9, 10, 14]]]   # performance set with Drive Wheels

sns.set_theme(style='darkgrid', palette='pastel')

for gen_counter in range(0, len(feature_count)):
    cur_data = datas[gen_counter]
    cur_data_without_price = cur_data[:, :-1]
    cur_set = sets[gen_counter]
    cur_feature = feature_count[gen_counter]
    cur_alpha = alphas[gen_counter]

    theta = [0 for i in range(0, cur_feature - 1)]
    ntheta = [0 for i in range(0, cur_feature - 1)]

    costs = []
    rows, cols = cur_data.shape
    loops = 100

    x = [i/rows for i in range(0, rows)]
    learned_hypothesis = hyp(theta, cur_data_without_price)
    plt.plot(x, learned_hypothesis, label="Initial Hypothesis")

    print("The unoptimized cost is: " +
          str(cost(theta, cur_data_without_price, price)))

    for i in range(0, loops):
        for j in range(0, cur_feature - 1):
            ntheta[j] = theta[j] - cur_alpha * \
                der(theta, cur_data_without_price, price, j)
        for j in range(0, cur_feature - 1):
            theta[j] = float(ntheta[j])

        tc = float(cost(theta, cur_data_without_price, price))
        costs.append(tc)

        print("The optimized cost is: " + str(tc))

    print(theta)

    np.sort(cur_data, axis=-1)

    for i in range(1, cur_feature - 1):
        plt.scatter(cur_data[:, i], cur_data[:, -1],
                    label=f"{column_names[str(sets[gen_counter][i])]} vs Price")

    learned_hypothesis = np.sort(hyp(theta, cur_data_without_price))
    plt.plot(x, learned_hypothesis, label="Learned Hypothesis")
    plt.title(titles[gen_counter], fontsize=16, fontweight='bold')

    plt.legend()

    plt.show()

    plt.clf()
