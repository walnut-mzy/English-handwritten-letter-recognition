from captcha.image import ImageCaptcha
#import random,string
import os


list1=[
        "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","S","Y","Z"
       ]
for i in list1:
    print(i)
    num = 0
    while num<1000:
        char1=i
        image = ImageCaptcha().generate_image(char1)
        num+=1
        if not os.path.exists("C:/Users/mzy/Desktop/机器学习/"+char1+"1"):  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs("C:/Users/mzy/Desktop/机器学习/"+char1+"1")
        image.save("C:/Users/mzy/Desktop/机器学习/"+char1+"1/"+str(num)+".png")
