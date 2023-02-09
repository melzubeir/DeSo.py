### Media

1. Upload image to images.deso.org

```python
import deso

SEED_HEX = 'YOUR SEED SEED_HEX'
PUBLIC_KEY = 'YOUR PUBLIC_KEY'
desoMedia = deso.Media(  PUBLIC_KEY, SEED_HEX)
imageFileList = [
    ('file', ('screenshot.jpg', open("img.png", "rb"), 'image/png'))
]  # 'img.png' is the image we are uploading to images.bitclout.com
urlResponse = desoMedia.uploadImage(imageFileList)
print(urlResponse.json())
```
