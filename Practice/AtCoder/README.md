# atcoder-tools使い方

# 事前準備
Makefileの以下を変更する
```
CONTEST=<コンテストID>
```

# 雛形作成
```sh
make gen
```

# テスト
```sh
make {A..J}-test
```

# 提出
```sh
# 提出
make {A..J}

# 再提出
make {A..J}-u
```

# oj使い方
# テストケース拡張
```sh
oj g/i ./generate.py
```

# コーナーケース追加
```sh
# 愚直解
oj g/i ./generate.py --jobs 5
oj g/o -c "pypy ./main_tle.py" --jobs 5

# tleケース探し
oj g/i ./generate.py --hack "pypy main.py" --tle 2 --jobs 5
```

# テスト
```sh
oj t -c "pypy main.py" --tle 2 --jobs 5
```

# 提出
```sh
oj s https://atcoder.jp/contests/abc242/tasks/abc242_C main_pypy.py --language 4047 -y
```

# Atcoderのsystem testcaseをDL
リンク: https://www.dropbox.com/sh/arnpe0ef5wds8cv/AAAk_SECQ2Nc6SVGii3rHX6Fa?dl=0
問題単位でディレクトリ毎ダウンロードしてきたディレクトリの中で以下を実行
```sh
find ./in -name '*.txt' | cut -d '.' -f 2 | awk '{print "mv ."$1"\{.txt,.in\}"}' | sh
find ./out -name '*.txt' | cut -d '.' -f 2 | awk '{print "mv ."$1"\{.txt,.out\}"}' | sh
cp */*.{in,out} ./ && rm -r ./{in,out}
```
