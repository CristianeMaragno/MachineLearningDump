from flask import Flask, render_template, request

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.show()
train = pd.read_csv('train.csv')

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hi</h1>"

if __name__ == "__main__":
    app.run(debug = True)