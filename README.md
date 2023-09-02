```sh
# venv を使った仮想環境の作成
python3 -m venv .venv

# 仮想環境のアクティベート
source .venv/bin/activate

# pip のアップグレード
python3 -m pip install --upgrade pip

# ライブラリのインストール
pip install -r requirements.txt
```

```sh
# pip-tools のインストール
pip install pip-tools

# requirements.in の作成(Mac)
touch requirements.in

# pip-tools による requirements.txt の作成
pip-compile requirements.in
```

```sh
# グリッドのクリックした場所を #(壁)として認識し、gridの文字列を作成
bokeh serve --show bokeh_make_grid_by_click.py

# エージェントの位置とゴール位置はどうやって設定しようか
# 壁とかち合わないようにする判定も入れるか？

# 画像を読み込み表示する
bokeh serve --show image.py

# ボタンを押すと画像を読み込み表示する
bokeh serve --show button_image.py

# SVGのアニメーションを表示する
bokeh serve --show animation.py

# ボタンを押すと MAPF を実行して SVG を保存する
bokeh serve --show button_mapf.py

# ボタンを押すとSVGのアニメーションを表示する
bokeh serve --show button_animation.py

# ボタンを押すと MAPF を実行して SVG を表示する
# ->Gridは画面で編集する
bokeh serve --show app.py
```
