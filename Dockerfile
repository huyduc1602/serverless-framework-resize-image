# Sử dụng hình ảnh lambci/lambda:build-python3.8 làm base image
FROM lambci/lambda:build-python3.8

# Cài đặt các gói phụ thuộc
RUN yum install -y libjpeg-turbo-devel zlib-devel libtiff-devel freetype-devel libwebp-devel openjpeg2-devel

# Cài đặt Pillow vào thư mục python
RUN pip install Pillow -t python/

# Tạo một file zip chứa thư mục python
CMD zip -r pillow_layer.zip python