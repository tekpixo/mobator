import matplotlib.pyplot as plt
from PIL import Image
import csv
import os
import pandas as pd
import requests


df = pd.read_csv('../assets/dataset/dataset.csv')


def generate_plots(labelGraph1, labelGraph2, valuesGraph1, valuesGraph2, labelX, labelY, MAX_GENERATIONS):
    fig, ax = plt.subplots()
    plt.plot(range(0, MAX_GENERATIONS + 1), valuesGraph1, label=labelGraph1)
    plt.plot(range(0, MAX_GENERATIONS + 1), valuesGraph2, label=labelGraph2)
    plt.legend()
    ax.set(xlabel=labelX, ylabel=labelY)
    plt.grid()

    fig.savefig("plot.pdf")


def save_time(times, strategy):
    csvfile = open('result-time-{}.csv'.format(strategy), 'w')
    csvwriter = csv.writer(csvfile)
    for item in times:
        csvwriter.writerow(item)
    csvfile.close()


def save_results(historicos, strategy):
    csvfile = open('result.-{}csv'.format(strategy), 'w')
    csvwriter = csv.writer(csvfile)
    for item in historicos:
        csvwriter.writerow(item[0])
    csvfile.close()


def print_population(population, POP_SIZE):
    fitnesses = [fitness_function(population[i]) for i in range(POP_SIZE)]
    print(list(zip(population, fitnesses)))


def generate_team_picture(best_global_individual, best_global_fit, strategy):
    images = []

    for im in best_global_individual:
        icon = df.loc[df.id == im].icon.values[0]
        images.append(Image.open(requests.get(icon, stream=True).raw))

    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height = max(heights)
    new_im = Image.new('RGB', (total_width, max_height))
    x_offset = 0

    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    new_im.save('team-fit-' + strategy + '.jpg')
