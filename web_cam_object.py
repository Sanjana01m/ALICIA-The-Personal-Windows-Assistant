import cv2

def object_detect():

    net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights","dnn_model/yolov4-tiny.cfg")
    model=cv2.dnn_DetectionModel(net)
    model.setInputParams(size=(320,320),scale=1/255)

    classes=[]
    with open("dnn_model/classes.txt","r") as file:
        for class_name in file.readlines():
            class_name=class_name.strip()
            classes.append(class_name)


    cap=cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
    #For FULL HD, set the resolution to 1920*1080
    
    while True:
        
        ret,frame= cap.read()
        #detecting in object
        (class_ids, scores, bboxes) = model.detect(frame)
        for class_id,score,bbox in zip(class_ids, scores, bboxes):
            (x,y,w,h) = bbox
            class_name=classes[class_id]
            print(x,y,w,h)
            cv2.putText(frame, class_name,(x,y-5), cv2.FONT_ITALIC,2,(0,255,0), 4 )
            cv2.rectangle(frame,(x,y),(x+w,y + h),(0,255,0), 4)

        print("class ids", class_ids)
        print("scores", scores)
        print("bounding boxes", bboxes)



        cv2.imshow("Frame",frame)
        cv2.waitKey(1)

