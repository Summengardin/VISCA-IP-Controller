from visca_over_ip.camera import Camera
import time

cam = Camera('10.1.3.78', 1000)



def test_zoom(cam: Camera):
    print(f"\nZoom position: {cam.get_zoom_position()}")
    print(f"Zooming st speed 7\n")
    cam.zoom(7)
    time.sleep(5)

    print(f"\nZoom position: {cam.get_zoom_position()}")
    print(f"Zooming st speed -7\n")
    cam.zoom(-7)
    time.sleep(5)

    print(f"\nZoom position: {cam.get_zoom_position()}")
    print(f"Zooming to 0.5 ({0.5*16384})\n")
    cam.zoom_to(0.5)
    time.sleep(5)

    print(f"\nZoom position: {cam.get_zoom_position()}")
    print(f"Zooming to 1 ({1*16384})\n")
    cam.zoom_to(1)
    time.sleep(5)
    
    print(f"\nZoom position: {cam.get_zoom_position()}")
    print(f"Zooming to 0 ({0*16384})\n")
    cam.zoom_to(0)



def test_shutter(cam: Camera):
    cam.autoexposure_mode('manual')
    time.sleep(3)

    cam.set_shutter(21)
    time.sleep(10)

    cam.set_shutter(6)


def test_exposure_compensation(cam: Camera):
    cam.autoexposure_mode('auto')
    time.sleep(3)

    for i in range(3):
        cam.increase_exposure_compensation()
        time.sleep(2)

    time.sleep(3)

    for i in range(3):
        cam.decrease_exposure_compensation()
        time.sleep(2)


def test_gain(cam: Camera):
    cam.autoexposure_mode('manual')
    for i in range(5):
        cam.increase_gain()
        time.sleep(1)
        print(f"\nGain: {cam.get_gain()} \n")

    time.sleep(3)

    for i in range(5):
        cam.decrease_gain()
        time.sleep(1)
        print(f"\nGain: {cam.get_gain()} \n")

    time.sleep(3)

    cam.reset_gain()

    time.sleep(1)

    cam.set_gain(14)
    print(f"\nGain: {cam.get_gain()} \n")

    time.sleep(3)

    cam.set_gain(1)
    print(f"\nGain: {cam.get_gain()} \n")


def test_iris(cam: Camera):
    cam.autoexposure_mode('manual')

    for i in range(5):
        cam.increase_iris()
        time.sleep(2)

    time.sleep(3)

    for i in range(5):
        cam.decrease_iris()
        time.sleep(2)

    time.sleep(3)

    cam.set_iris(17)

    time.sleep(3)

    cam.set_iris(5)

    time.sleep(3)

    cam.reset_iris()


def test_set_autoexposure_mode(cam: Camera):
    print(f"\nSetting autoexposure mode to 'manual'")
    cam.autoexposure_mode('manual')
    print(f"Autoexposure mode: {cam.get_autoexposure_mode()}\n")

    time.sleep(3)

    print(f"\nSetting autoexposure mode to 'auto'")
    cam.autoexposure_mode('auto')
    print(f"Autoexposure mode: {cam.get_autoexposure_mode()}\n")

    time.sleep(3)

    print(f"\nSetting autoexposure mode to 'shutter priority'")
    cam.autoexposure_mode('shutter priority')
    print(f"Autoexposure mode: {cam.get_autoexposure_mode()}\n")

    time.sleep(3)

    print(f"\nSetting autoexposure mode to 'iris priority'")
    cam.autoexposure_mode('iris priority')
    print(f"Autoexposure mode: {cam.get_autoexposure_mode()}\n")


def test_autoexposure_mode(cam: Camera, mode: str):
    print(f"\nSetting autoexposure mode to '{mode}'")
    cam.autoexposure_mode(mode)
    print(f"Autoexposure mode: {cam.get_autoexposure_mode()}\n")

    time.sleep(3)
    try:
        while True:
            print()
            print(f"Gain:       {cam.get_gain()}")
            print(f"Iris:       {cam.get_iris()}")
            print(f"Shutter:    {cam.get_shutter()}")
            print()
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    

def test_min_shutter(cam: Camera):
    cam.autoexposure_mode('auto')

    time.sleep(5)

    cam.set_min_shutter_position(5)
    cam.set_min_shutter_on()

    time.sleep(3)

    print(f"\nMin shutter:      {cam.get_min_shutter()}")
    print(f"Min shutter pos     {cam.get_min_shutter_position()}\n")

    cam.set_min_shutter_off()

    time.sleep(3)

    print(f"\nMin shutter:      {cam.get_min_shutter()}")
    print(f"Min shutter pos     {cam.get_min_shutter_position()}\n")


    cam.set_min_shutter_position(20)
    cam.set_min_shutter_on()

    time.sleep(3)

    print(f"\nMin shutter:      {cam.get_min_shutter()}")
    print(f"Min shutter pos     {cam.get_min_shutter_position()}\n")

    cam.set_min_shutter_off()
    time.sleep(3)
 
    print(f"\nMin shutter:      {cam.get_min_shutter()}")
    print(f"Min shutter pos     {cam.get_min_shutter_position()}\n")

    





# test_zoom(cam) # : OK
# test_shutter(cam) # : OK
# test_exposure_compensation(cam)
# test_gain(cam) # : OK
# test_iris(cam) # : OK
# test_autoexposure_modes(cam) # : OK
# test_autoexposure_mode(cam, 'auto') # : OK
# test_min_shutter(cam) # : OK