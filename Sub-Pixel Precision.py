import cv2

def refine_subpixel(flow):
    refined_flow = cv2.resize(flow, (0, 0), fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    return refined_flow
