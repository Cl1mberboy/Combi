import numpy as np
import cv2 as cv

def traker(c_old, count, memory):
    cf = 10
    for ci in c_old:
        if len(memory) < 1:
          memory.append([ci[0],ci[1],count,cf])
          count += 1
          #print(memory,'f')
        else:
          d = []
          for i in memory:
            d.append(((ci[0] - i[0])**2 + (ci[1] - i[1])**2) ** 0.5)
          #print(d)
          if np.min(d) < 75:
            memory.append([ci[0],ci[1],memory[d.index(np.min(d))][2],cf])
            memory.remove(memory[d.index(np.min(d))])
            for x, y, id, u  in memory:
                uu = u
                if in_out(x,y) > 0:
                    print('out',id)
                    if u <= 0:
                        print('remove',id)
                        memory.remove([x,y,id,u])
                    else:
                        u -= 1 
                        memoria[memoria.index([x,y,id,uu])] = [x,y,id,u]
                        print('less 1',u)
                else:
                    print('in',id)
            #print(memory,'update')
          else:
            memory.append([ci[0],ci[1],count,cf])
            count += 1
            #print(memory,'add')
        
                

    return count, memory

def in_out(y,x):
  h = 320
  k = 300
  a = -85.325 
  p = pow((y - k), 2) - 4 * a * (x - h)
  return p

memoria = []
idp = 1
cuenta = 0

cap =cv.VideoCapture(1)
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

while(True):
    _, img = cap.read()
    #print(img.shape)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #gray = cv.GaussianBlur(gray,(5,5),0)
    faces = face_cascade.detectMultiScale(gray,1.3,6)

    c_old = []
    for (x,y,w,h) in faces:
        cx, cy =[x + (w // 2), y + (h // 2)]
        c_old.append([x + (w // 2), y + (h // 2)])
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        cv.circle(img,(cx, cy), 5, (255,228,0), -1)


    idp, memoria = traker(c_old, idp, memoria)

    for x, y, id, u in memoria:
        cv.putText(img,str(id),(x, y - 15),cv.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
            
    #Umbral
    cv.line(img,(213,300),(422,300),(255,255,255),2)
    cv.line(img,(320,0),(320,480),(255,255,255),2)

    cv.imshow('face',img)
    k = cv.waitKey(1)
    if k == ord("q"): 
        break
cap.release()
cv.destroyWindow()






