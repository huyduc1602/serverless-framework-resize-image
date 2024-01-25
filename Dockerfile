# Sử dụng hình ảnh lambci/lambda:build-python3.8 làm hình ảnh cơ sở
FROM lambci/lambda:build-python3.8

# Cài đặt Pillow vào thư mục python/lib/python3.8/site-packages/
RUN pip install Pillow -t python/

# Tạo một file zip chứa thư mục python
CMD zip -r pillow_layer.zip python