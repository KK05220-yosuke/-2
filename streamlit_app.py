import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Streamlitアプリケーションのタイトルを設定
st.title('y = x^n の3Dプロット')

# 3Dプロットを作成する関数
def plot_3d_graph(n):
    # x軸の範囲を設定（-10から10まで）
    x = np.linspace(-10, 10, 400)

    # y = x^n の計算
    y_positive = x**n
    y_negative = -x**n

    # データフレームを作成
    data = np.vstack((x, y_positive)).T
    data_negative = np.vstack((x, y_negative)).T
    df_positive = pd.DataFrame(data, columns=['X', 'Y'])
    df_negative = pd.DataFrame(data_negative, columns=['X', 'Y'])

    # Plotlyの3Dプロットを作成
    fig = px.line_3d(df_positive, x='X', y='Y', z=np.zeros_like(df_positive['X']), line_shape='linear', color_discrete_sequence=['blue'])
    fig.add_scatter3d(x=df_negative['X'], y=df_negative['Y'], z=np.zeros_like(df_negative['X']), mode='lines', line=dict(color='red'))

    # プロットを表示
    st.plotly_chart(fig)

# アプリケーションを実行する部分
if __name__ == '__main__':
    # nの値をユーザーに入力させる
    n = st.slider('nの値を選択してください', min_value=1, max_value=10, value=2)
    plot_3d_graph(n)
