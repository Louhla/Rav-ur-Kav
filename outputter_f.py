from PricesGushDan import prices
import numpy as np
import pandas as pd


def outputter(passenger):
    size = len(passenger)
    packages = list(prices.keys())
    chosen_package_num = np.random.choice(list(prices.keys()))
    chosen_package = prices[chosen_package_num]
    freq = ['daily', 'weekly', 'monthly']
    ran_freq = np.random.choice([0, 1, 2])
    print(f'Recommended plan: {chosen_package_num}\nName: {chosen_package["name"]}\nAreas covered: {chosen_package["areas"]}\nFrequency: {freq[ran_freq]}\nPrice: {chosen_package[freq[ran_freq]]}')