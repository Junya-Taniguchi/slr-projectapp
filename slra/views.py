from django.http import HttpResponse
from django.shortcuts import render
from .models import Slra
import numpy as np
import pandas as pd
import csv
import math

def home(request):
    slra = Slra.objects.all()
    return render(request, 'home.html',{'slras':slra})

def ask(request):
    data = Slra.objects.get(id=1,upload__contains='csv')
    csv = data.upload
    roomsize = request.GET['roomsize']
    roomsize = int(roomsize)
    # 学習モデル
    df = pd.read_csv(csv)
    xa = df['x']
    yb = df['y']
    # データフレームの平均を取得
    mean = df.mean()
    # 中心化
    df_c = df - df.mean()
    # データの抽出
    xd = df_c['x']
    yd = df_c['y']
    # 傾きaの計算
    xx = xd * xd
    xy = xd * yd
    a = xy.sum() / xx.sum()

    def predict(x):
        # 予測
        xm = mean['x']
        ym = mean['y']
        # 中心化
        xc = x - xm
        y_hat = a * xc + ym
        # 出力
        return math.floor(y_hat)
    return render(request, 'ask.html', {'rent' : predict(roomsize),'roomsize':roomsize})
