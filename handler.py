import PIL
import io
import json
import boto3

s3 = boto3.client('s3')

def resize_image(event, context):
    try:
        # Lấy dữ liệu hình ảnh từ yêu cầu
        body = json.loads(event['body'])
        image_data = body['image_data']

        # Xử lý hình ảnh
        image = PIL.Image.open(io.BytesIO(image_data))
        new_width = 100
        new_height = int((float(image.size[1]) * float(new_width / float(image.size[0]))))
        resized_image = image.resize((new_width, new_height))

        # Chuyển hình ảnh đã xử lý thành dạng bytes
        resized_image_bytes = io.BytesIO()
        resized_image.save(resized_image_bytes, format='JPEG')
        resized_image_data = resized_image_bytes.getvalue()

        # Lưu hình ảnh đã xử lý vào S3
        s3.put_object(
            Bucket='duchh-pj-internal-resize-image',
            Key='resized/image.jpg',
            Body=resized_image_data,
            ContentType='image/jpeg'
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Resize hình ảnh thành công"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
