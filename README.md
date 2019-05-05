# Mini-Tools

### Image-Edit

##### 几个基本的图片编辑工具，包括一下功能：

+ 文件：打开，保存，退出
+ 编辑：放大，缩小，灰度，亮度，旋转，截图
+ 变换：傅里叶变换，离散余弦变换，Radon变换
+ 噪声：高斯，椒盐，斑点，泊松
+ 滤波：高通，低通，平滑，锐化
+ 直方图统计：R直方图，G直方图，B直方图
+ 图像增强：伪彩色，真彩色，直方图均衡，NTSC颜色模型，YCbCr颜色模型，HSV颜色模型
+ 阈值分割
+ 生态学处理
+ 特征提取
+ 图像分类与识别

![Image-Edit](show_ImageEdit.jpg)

##### 库文件需要
```
 1. PyQt5
 2. sys
 3. os
 4. opencv2
 5. numpy
 6. scipy
 7. matplotlib
 ```
##### 主要代码分析
+ 亮度调节
```
#亮度
def brightImage(window):
    imageList=[]
    for img in window.originImages:
        imgs=[]   
        rows, cols, chunnel = img[0].shape
        blank = np.zeros([rows, cols, chunnel], img[0].dtype)   
        result = cv2.addWeighted(img[0], 1.3, blank, 1-1.3, 3)
        imgs.extend([img[0],result])
        imageList.append(imgs)
    resizeFromList(window, imageList)
    showImage(window,['原图','调整亮度后'])
 ```
+ 傅里叶变换
 ```
 #傅里叶变换
def change1Image(window):
    imageList=[]
    for img in window.originImages:
        imgs=[]
        b,g,r=cv2.split(img[0])
        b_freImg,b_recImg=oneChannelDft(b)
        g_freImg, g_recImg = oneChannelDft(g)
        r_freImg, r_recImg = oneChannelDft(r)
        freImg=cv2.merge([b_freImg,g_freImg,r_freImg])
        imgs.extend([img[0],freImg])
        imageList.append(imgs)
    resizeFromList(window, imageList)
    showImage(window,['原图','傅里叶变换后'])
  ```
+ 离散余弦变换
```
  #离散余弦变换
def change2Image(window):
    imageList=[]
    for img in window.originImages:
        imgs=[]
        img1 = cv2.cvtColor(img[0], cv2.COLOR_BGR2RGB)
        img_dct = cv2.dct(img1)         #进行离散余弦变换
        imgs.extend([img[0],img_dct])
        imageList.append(imgs)
    resizeFromList(window, imageList)
    showImage(window,['原图','离散余弦变换后'])
```
+ Radon变换
```
  #Radon变换
def change3Image(window):
    imageList=[]
    for img in window.originImages:
        imgs=[]
        img_dct = cv2.dct(img[0])         
        result = np.log(abs(img_dct)) 
        imgs.extend([img[0],result])
        imageList.append(imgs)
    resizeFromList(window, imageList)
    showImage(window,['原图','Radon变换后'])
```
+ 高通滤波
```
 #高通滤波
def smoothing1Image(window):
    imageList=[]
    for img in window.originImages:
        imgs=[]
        x=cv2.Sobel(img[0],cv2.CV_16S,1,0)
        y=cv2.Sobel(img[0],cv2.CV_16S,0,1)
        absx=cv2.convertScaleAbs(x)
        absy=cv2.convertScaleAbs(y)
        result = cv2.addWeighted(absx,0.5,absy,0.5,0)
        imgs.extend([img[0],result])
        imageList.append(imgs)
    resizeFromList(window, imageList)
    showImage(window,['原图','高通滤波后'])
```
 + 低通滤波
```
 #低通滤波
def smoothing2Image(window):
    imageList=[]
    for img in window.originImages:
        imgs=[]
        result = cv2.medianBlur(img[0],5)
        imgs.extend([img[0],result])
        imageList.append(imgs)
    resizeFromList(window, imageList)
    showImage(window,['原图','低通滤波后'])
```
+ 平滑滤波
```
#平滑滤波
def smoothing3Image(window):
    imageList=[]
    for img in window.originImages:
        imgs=[]
        result = cv2.blur(img[0], (5, 5))
        imgs.extend([img[0],result])
        imageList.append(imgs)
    resizeFromList(window, imageList)
    showImage(window,['原图','平滑滤波后'])
```
+ 锐化滤波
```
#锐化滤波
def smoothing4Image(window):
    imageList=[]
    for img in window.originImages:
        imgs=[]
        result = cv2.bilateralFilter(img[0],9,75,75)
        imgs.extend([img[0],result])
        imageList.append(imgs)
    resizeFromList(window, imageList)
    showImage(window,['原图','锐化滤波后'])
```
+ 其他不详细介绍

### Beautify-Camera

##### 主要功能

+ 文件：打开，保存，打开摄像头
+ 操作：还原，人脸识别
+ 滤镜：怀旧，木刻，灰色，彩色，风格化，增强细节
+ 调节：亮度，饱和度，伽马变换，边缘保持
+ 磨皮美白：美白度，磨皮程度，磨皮精度
+ 灰度直方图

![Beautify-Camera](show_BeautifyCamera.jpg)

##### 库文件需要
```
 1. PyQt5
 2. sys
 3. opencv2
 4. numpy
 5. matplotlib
```

#####相关代码说明
+ 人脸识别
```
# 人脸识别
    def detect_face(self):
        img = self.raw_image
        face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        return faces
   ```
+ 皮肤识别
```
# 皮肤识别
    def detect_skin(self):
        img = self.raw_image
        rows, cols, channals = img.shape
        for r in range(rows):
            for c in range(cols):
                B = img.item(r, c, 0)
                G = img.item(r, c, 1)
                R = img.item(r, c, 2)
                if (abs(R - G) > 15) and (R > G) and (R > B):
                    if (R > 95) and (G > 40) and (B > 20) and (max(R, G, B) - min(R, G, B) > 15):
                        self.imgskin[r, c] = (1, 1, 1)
                    elif (R > 220) and (G > 210) and (B > 170):
                        self.imgskin[r, c] = (1, 1, 1)
```
+ 其他不做详解
