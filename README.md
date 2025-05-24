```sh
# venv を使った仮想環境の作成
$ uv venv

# 仮想環境のアクティベート
$ source .venv/bin/activate

# pip のアップグレード
$ uv pip install --upgrade pip

# ライブラリのインストール
$ uv pip install -r requirements.txt
```

```sh
# グリッドのクリックした場所を #(壁)として認識し、gridの文字列を作成
$ bokeh serve --show bokeh_make_grid_by_click.py

# エージェントの位置とゴール位置はどうやって設定しようか
# 壁とかち合わないようにする判定も入れるか？

# SVGのアニメーションを表示する
$ bokeh serve --show animation.py

# ボタンを押すとSVGのアニメーションを表示する
$ bokeh serve --show button_animation.py

# ボタンを押すと MAPF を実行して SVG を表示する
# ->Gridは画面で編集する
$ bokeh serve --show app.py
```
