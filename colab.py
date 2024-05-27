# 구글 마운트
# from google.colab import drive
# drive.mount('/content/drive')

# 현재 폴더 확인
# !ls

# 폴더 옮기고 url 다운로드
# !cd drive/MyDrive/datasets && wget URL

# 이어서 다운로드
# !wget -c URL

# 이미지넷 관련 코드
# !cd drive/MyDrive/datasets/ImageNet && wget https://image-net.org/data/ILSVRC/2012/ILSVRC2012_img_train.tar
# !cd drive/MyDrive/datasets/ImageNet && mkdir train && mv ILSVRC2012_img_train.tar train/ && cd train && tar -xvf ILSVRC2012_img_train.tar && rm -f ILSVRC2012_img_train.tar && find . -name "*.tar" | while read NAME ; do mkdir -p "${NAME%.tar}"; tar -xvf "${NAME}" -C "${NAME%.tar}"; rm -f "${NAME}"; done && cd ..
# !cd drive/MyDrive/datasets/ImageNet && wget https://image-net.org/data/ILSVRC/2012/ILSVRC2012_img_val.tar
# !cd drive/MyDrive/datasets/ImageNet && mkdir val && mv ILSVRC2012_img_val.tar val/ && cd val && tar -xvf ILSVRC2012_img_val.tar && wget -qO- https://raw.githubusercontent.com/soumith/imagenetloader.torch/master/valprep.sh | bash


