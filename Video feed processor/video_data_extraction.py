
import tensorflow
from imageai.Detection import ObjectDetection
import os
import cv2
from datetime import datetime, date, time, timedelta


# starting ObjectDetection module
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath('Model/resnet50_coco_best_v2.1.0.h5')
detector.loadModel()


vid = cv2.VideoCapture('Input_video.mp4')

def sort_(images):
  ss = {}
  for img in images:
    img1 = int(img.split('.')[0].split('w')[1])
    ss[img1] = img

  ll = []
  for i in sorted (ss.keys()):
    ll.append(ss[i])

  return ll




def generate_out_video():
    ''' generating video from Images '''

    image_folder = 'Store/'
    video_name = 'Output_Video.avi'

    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    images = sort_(images)

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 1, (width,height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()


#Data = []
i = 0
j = 10



User = 'DisJoin'
Pass = '1234'
conn = MongoClient('mongodb+srv://'+User +':'+  Pass + '@cluster0-bk4u2.mongodb.net/<dbname>?retryWrites=true&w=majority')

mydb = conn["DisJoin_data"]
mycol = mydb["Current_data"]
Col2 = mydb["Predict_data"]
mycol.delete_many({})

while(vid.isOpened()):

    ret, frame = vid.read()

    if ret == True:

        if(j%10 == 0):# taking every 10th frame (for one min Long video )

          t = datetime.now()
          t =  t +  timedelta(seconds=1)

          in_img = "Supply/"+  "imagenew"+str(i)+".jpg"
          cv2.imwrite(in_img,frame)

          out_img = "Store/"+  "imagenew"+str(i)+".jpg"

          detections = detector.detectObjectsFromImage(input_image= in_img , output_image_path= out_img)


          #display(Image(out_img))
          mod_img = cv2.imread(out_img)

          cv2.imshow('F' , mod_img)

          i+=1
          #person =[]
          count = 0
          print(i)
          for eachObject in detections:
              if eachObject["name"] == 'person':
                  #person.append(eachObject["percentage_probability"])
                  count+=1



          d = t.strftime("%m/%d/%Y, %H:%M:%S")
          mydict = { "_id": i ,"count": count, "Date_time": d }

          x = mycol.insert_one(mydict) # inserting into database



          #Data.append([count,t])
          #clear_output(wait = True)

          if cv2.waitKey(25) & 0xFF == ord('q'):
              break
        j+=1
    else:

        break

vid.release()
#out.release()

cv2.destroyAllWindows()

# generate_out_video()
