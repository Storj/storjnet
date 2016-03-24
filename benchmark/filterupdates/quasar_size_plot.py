# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt  # pip install matplotlib
import json


x = []
y_success = []
y_redundant = []
y_spam = []


samples = [
    json.load(open("benchmark/filterupdates_quasar_size_a.json", "r")),
    json.load(open("benchmark/filterupdates_quasar_size_b.json", "r")),
    json.load(open("benchmark/filterupdates_quasar_size_c.json", "r")),
    json.load(open("benchmark/filterupdates_quasar_size_d.json", "r")),
    json.load(open("benchmark/filterupdates_quasar_size_e.json", "r")),
    json.load(open("benchmark/filterupdates_quasar_size_f.json", "r")),
    json.load(open("benchmark/filterupdates_quasar_size_g.json", "r")),
    json.load(open("benchmark/filterupdates_quasar_size_h.json", "r")),
    json.load(open("benchmark/filterupdates_quasar_size_i.json", "r")),
    json.load(open("benchmark/filterupdates_quasar_size_j.json", "r")),
]


for sample in samples:
    x.append(sample["quasar"]["constants"]["size"])
    success = sample["quasar"]["update_successful"]
    redundant = sample["quasar"]["update_redundant"]
    spam = sample["quasar"]["update_spam"]
    y_success.append(redundant + spam + success)
    y_redundant.append(redundant + spam)
    y_spam.append(spam)


# setup
fig = plt.figure()
plot = fig.add_subplot(111)
plot.set_xlabel('Bloom filter size')
plot.set_ylabel('Update calls')
# plot.set_xscale('log')
# plot.set_yscale('log')
plot.axis([8, 512, 0, 200000])


# add plots
lines = plot.plot(x, y_success, 'k', label='Success')
plt.setp(lines, color='green', linewidth=2.0)
plot.fill_between(x, y_redundant, y_success, facecolor="#00FF00", alpha=0.5)

lines = plot.plot(x, y_redundant, 'k', label='Redundant')
plt.setp(lines, color='orange', linewidth=2.0)
plot.fill_between(x, y_spam, y_redundant, facecolor="#FFFF00", alpha=0.5)

lines = plot.plot(x, y_spam, 'k', label='Spam')
plt.setp(lines, color='red', linewidth=2.0)
plot.fill_between(x, 0, y_spam, facecolor="#FF0000", alpha=0.5)


# create legend
plot = plot.legend(loc='upper center', shadow=False, fontsize='small')
plot.get_frame().set_facecolor('#00FFFF')


# render
plt.savefig("benchmark/filterupdates/quasar_size_plot.png")
plt.show()
