import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Streamlitアプリケーションのタイトルを設定
st.title('y = x^2 の3Dプロット')

# 3Dプロットを作成する関数
def plot_3d_graph():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # x軸の範囲を設定（-10から10まで）
    x = np.linspace(-10, 10, 400)

    # y = x^2 の計算
    y_positive = x**2
    y_negative = -x**2

    # y > 0 の領域をプロット
    ax.plot(x, y_positive, zs=0, zdir='y', label='y = x^2 (y > 0)', color='b')

    # y < 0 の領域をプロット
    ax.plot(x, y_negative, zs=0, zdir='y', label='y = -x^2 (y < 0)', color='r')

    # グラフを90°傾ける
    ax.view_init(elev=20, azim=-90)

    # x, y, z軸のラベルを設定
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # グラフを表示
    plt.legend()
    plt.tight_layout()
    st.pyplot(fig)

# アプリケーションを実行する部分
if __name__ == '__main__':
    plot_3d_graph()






