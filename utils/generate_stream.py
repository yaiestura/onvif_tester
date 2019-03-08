import io
import rtsp

def generate_stream(url):
    client = rtsp.Client(rtsp_server_uri=url, verbose=False)

    while True:
        if client.read() is None:
            continue
            
        img = client.read().resize((640, 480))
        imgByteArr = io.BytesIO()
        img.save(imgByteArr, format='jpeg')
        b_img = imgByteArr.getvalue()

        yield (b'--frame\r\n' +
               b'Content-Type: image/jpeg\r\n\r\n' + b_img + b'\r\n')
    else:
        client.close()