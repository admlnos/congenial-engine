import cv2
from main import my_stitch
import sys
capture = cv2.VideoCapture(0)
fram_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
fram_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)
print("帧的宽度：{}".format(fram_width))
print("帧的高度：{}".format(fram_height))
print("FPS：{}", format(fps))
if capture.isOpened() is False:
    print("the camera is error")
data_folder = sys.argv[1]
MAX_FEATURES = int(sys.argv[2])
GOOD_MATCH_PERCENT = float(sys.argv[3])
find_keypoint_algorithm = sys.argv[4]
warp = sys.argv[5]

frame_list = []
fgap_counter = 0

while capture.isOpened():
    ret, frame = capture.read()
    if ret is True:
        if fgap_counter >= 2:
            fgap_counter = 0
            frame_list.append(frame)
            if len(frame_list) >= 2:
                out_frame = my_stitch(frame_list, MAX_FEATURES, GOOD_MATCH_PERCENT,
                                      find_keypoint_algorithm, warp)
                frame_list = [out_frame]
        else:
            fgap_counter += 1
        if cv2.waitKey(20) & 0xFF == ord("q"):
            break
capture.release()
cv2.destroyAllWindows()
