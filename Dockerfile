FROM python:3.7.4-alpine

# ソースを置くディレクトリを変数として格納                                                  
ARG project_dir=/web/front/

# 必要なファイルをローカルからコンテナにコピー
ADD app.py $project_dir

# requirements.txtに記載されたパッケージをインストール                         
WORKDIR $project_dir
RUN pip install Flask requests aws-xray-sdk

CMD ["python", "/web/front/app.py"]

