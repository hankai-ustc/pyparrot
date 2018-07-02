from Bebop import Bebop
import sys

if __name__=='__main__':
    bebop = Bebop()
    success = bebop.connect(10)
    bebop.smart_sleep(5)
    bebop.ask_for_state_update()
    while True:
        print ("piloting_cmd >>",)
        #print("connecting")
        try:
            info=input()
        except Exception as e:
            print("can\'t input")
            exit()
        try:
            [cmd,time]=info.split(' ')
            if cmd=='t':
                bebop.safe_takeoff(int(time))
            elif cmd=='L':
                bebop.safe_land(int(time))
            elif cmd=='f':
                bebop.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0, duration=float(time))
            elif cmd=='b':
                bebop.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=0, duration=float(time))
            elif cmd=='u':
                bebop.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=50, duration=float(time))
            elif cmd=='d':
                bebop.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-50, duration=float(time))
            elif cmd=='r':
                bebop.fly_direct(roll=0, pitch=0, yaw=50, vertical_movement=0, duration=float(time))
            elif cmd=='l':
                bebop.fly_direct(roll=0, pitch=0, yaw=-50, vertical_movement=0, duration=float(time))
            elif cmd=='m':
                bebop.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=float(time))
            elif cmd == 'n':
                bebop.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=float(time))
        except Exception as e:
            print(e)
    bebop.disconnect()
    exit()




    """
        bebop.safe_takeoff(10)

        print("Flying direct: going forward (positive pitch)")
        bebop.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0, duration=1)

        print("Flying direct: yaw")
        bebop.fly_direct(roll=0, pitch=0, yaw=50, vertical_movement=0, duration=1)

        print("Flying direct: going backwards (negative pitch)")
        bebop.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=0, duration=0.5)

        print("Flying direct: roll")
        bebop.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=1)

        print("Flying direct: going up")
        bebop.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=50, duration=1)

        # this works but requires a larger test space than I currently have. Uncomment with care and test only in large spaces!
        # print("Flying direct: going around in a circle (yes you can mix roll, pitch, yaw in one command!)")
        # bebop.fly_direct(roll=25, pitch=0, yaw=50, vertical_movement=0, duration=5)

        bebop.smart_sleep(5)
        bebop.safe_land(10)

        print("DONE - disconnecting")
        bebop.disconnect()
    """