import cv2
from cv2 import cv
import numpy as np
from selenium.webdriver import ActionChains

def locate_to_screen(snapshot_file, template_file, result_file):
	method = cv.CV_TM_CCOEFF_NORMED
	
	large_image = cv2.imread(snapshot_file)
	small_image = cv2.imread(template_file)
	
	result = cv2.matchTemplate(small_image, large_image, method)

	trows,tcols = small_image.shape[:2]
	
	threshold = .8
	loc = np.where(result >= threshold)
	
	center = []
	
	for pt in zip(*loc[::-1]):
		centerPt = (pt[0] + tcols/2,pt[1] + trows/2)
		center.append(centerPt)
		cv2.rectangle(large_image, pt, (pt[0] + tcols, pt[1] + trows), (255, 0, 255), 2)
		cv2.circle(large_image, centerPt, 5, (0,0,0), 2)
	
	cv2.imwrite(result_file,large_image)
	
	# return the first center value
	if len(center) > 0:
		return center[0]
	return None
	
def check_mouse_pos(driver, injectVar="myVar"):
	return driver.execute_script("return document.%s" % injectVar)
	
def capture_mouse_move(driver, injectFunc="myFunc", injectVar="myVar"):
	# inject the onmouseover function and its result to "document"
	command = """		
function %s(e) {
var x = e.clientX;
var y = e.clientY;
document.%s = [x, y];
}
document.onmousemove =  %s;
	""" % (injectFunc, injectVar, injectFunc)
	driver.execute_script(command)
	
def sniff(driver, injectVar="myVar"):
	x,y = check_mouse_pos(driver, injectVar)

	command = """
		elem = document.elementFromPoint(%d, %d);
		return elem;
	""" % (x, y)	
	
	return driver.execute_script(command)

def move_mouse_to_pos_and_sniff(driver, x, y, injectVar="myVar"):
	# reset the mouse to 1,1
	currPos = check_mouse_pos(driver, injectVar)
	offsetX = -currPos[0] + 0.5 # don't know why it had 0.5 different
	offsetY = -currPos[1] + 0.5
	builder = ActionChains(driver);
	builder.move_by_offset(offsetX, offsetY).perform();
	
	# move mouse to x,y
	builder = ActionChains(driver);
	builder.move_by_offset(x-1, y-1).perform();
	
	# get the WebElement
	return sniff(driver, injectVar)



if __name__ == '__main__':
	main()