import cv2

thres=0.45 # threshold to detect object

def Object_detect():
    cap=cv2.VideoCapture(1)
    cap.set(3,1280)
    cap.set(4,720)
    cap.set(10,70)

    className=[]
    classFile='coco.names'
    with open (classFile,'rt') as f:
        className = f.read().rstrip('\n').split('\n')

    


    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break

    vc.release()
    cv2.destroyWindow("preview")
