from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from streamapp.camera import VideoCamera
                                            # , IPWebCam, MaskDetect, LiveWebCam

# Create your views here.
def home(request):
	return render(request, 'streamapp/home.html')

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
	resp = StreamingHttpResponse(gen(VideoCamera()))
	return render(request, 'livecamera.html', {'video': resp})
	# return StreamingHttpResponse(gen(VideoCamera()),
	# 				content_type='multipart/x-mixed-replace; boundary=frame')


def prequsites(request):
	return render(request, 'streamapp/prequsites.html')

def about(request):
	return render(request, 'streamapp/about.html')

# def webcam_feed(request):
# 	return StreamingHttpResponse(gen(IPWebCam()),
# 					content_type='multipart/x-mixed-replace; boundary=frame')
#
#
# def mask_feed(request):
# 	return StreamingHttpResponse(gen(MaskDetect()),
# 					content_type='multipart/x-mixed-replace; boundary=frame')
#
# def livecam_feed(request):
# 	return StreamingHttpResponse(gen(LiveWebCam()),
# 					content_type='multipart/x-mixed-replace; boundary=frame')
