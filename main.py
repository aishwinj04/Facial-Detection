import cv2
import os


def face_detect():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    images = os.listdir('images')
    for item in images:
        image = cv2.imread(f'images/{item}', 1) # read image for each item in folder
        faces = face_cascade.detectMultiScale(image, 1.1, 4)
        print(faces)


def main():
    os.makedirs('face-images', exist_ok=True)

    face_detect

    
if __name__ == '__main__':
    main()

