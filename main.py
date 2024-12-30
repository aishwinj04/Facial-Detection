import cv2
import os


def draw_rect(image, faces):
   for (x, y, w, h) in faces:
      cv2.rectangle(image, (x,y), (x+w, y+h), (255,255,255), 10)

def face_detect():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    images = os.listdir('images')
    for item in images:
        image = cv2.imread(f'images/{item}', 0) # better results in greyscale
        faces = face_cascade.detectMultiScale(image, 1.3, 4) # shrink 1/1.3 original size, minNeighbours of 4 overlapping rectangles
        draw_rect(image,faces)

        if(len(faces) >= 1):
         cv2.imwrite(f'face-images/{item}', image)
        




def main():
    os.makedirs('face-images', exist_ok=True)
    face_detect()



    
if __name__ == '__main__':
    main()

