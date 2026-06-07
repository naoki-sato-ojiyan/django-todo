# ベースイメージ：Python 3.14
FROM python:3.14-slim

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係ファイルをコピーしてインストール
COPY requirements.txt .
RUN pip install -r requirements.txt

# プロジェクトファイルを全てコピー
COPY . .

# 開発サーバーを起動
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]