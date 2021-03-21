import cv2
import time
import dropbox
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time()
        result = False

    return img_name
    print("snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "fDAv_fdQk3wAAAAAAAAAAejyzs3fU4v8UOef6I4jgRoWIAV4_wGxUjPoduPtBRiv"
    file = img_name
    file_from = file
    file_to = "/TestFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
    dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
    print("file uploaded")

def main():
    while(true):
        if((time.time()-start_time)>=)
        name = take_snapshot()
        upload_file(name)


main()