"""
Flies the bebop in a fairly wide arc.  You want to be sure you have room for this. (it is commented
out but even what is here is still going to require a large space)
"""
from Bebop import Bebop

bebop = Bebop()

print("connecting")
success = bebop.connect(10)
print(success)

print("sleeping")
bebop.smart_sleep(5)
bebop.ask_for_state_update()
bebop.start_video_stream()
bebop.set_video_stream_mode('low_latency')
bebop.set_video_stream_resolutions('rec1080_stream480')
bebop.set_vide_stream_framerate('30_FPS')

bebop.smart_sleep(120)
bebop.stop_video_stream()
print("DONE - disconnecting")
bebop.disconnect()