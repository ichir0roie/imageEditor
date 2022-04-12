import cv2
import glob
class AllRun:
    def __init__(self):
        self.beforeImagePaths=self.getBeforePath()
        self.afterImagePath="ImageAfter/"
        return
    
    def getBeforePath(self):
        path = glob.glob("ImageBefore/*")
        return path
    

    def runAllImage(self):
        for path in self.beforeImagePaths:
            self.reverseColor(path)

    def reverseColor(self,path:str):
        img=cv2.imread(path)
        img=cv2.bitwise_not(img)
        path=self.afterImagePath+"Reverse_"+path.split("\\")[-1]
        cv2.imwrite(path,img)


if __name__=="__main__":
    ar=AllRun()
    ar.runAllImage()