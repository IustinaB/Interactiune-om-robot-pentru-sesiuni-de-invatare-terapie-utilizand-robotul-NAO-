#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

import qi
import argparse
import sys
import time


def main(session, behavior_name):
    # Utilizare serviciul ALBehavior
    behavior_mng_service = session.service("ALBehaviorManager")
    getBehaviors(behavior_mng_service)
    launchBehavior(behavior_mng_service, behavior_name)


def getBehaviors(behavior_mng_service):
    names = behavior_mng_service.getInstalledBehaviors()
    print("Behaviors on the robot:")
    print(names)

    names = behavior_mng_service.getRunningBehaviors()
    print("Running behaviors:")
    print(names)


def launchBehavior(behavior_mng_service, behavior_name):
    if (behavior_mng_service.isBehaviorInstalled(behavior_name)):
        # Verific daca behavior-ul nu a fost accesat deja
        if (not behavior_mng_service.isBehaviorRunning(behavior_name)):
            behavior_mng_service.runBehavior(behavior_name, _async=True)
            time.sleep(0.5)
        else:
            print("Behavior is already running.")

    else:
        print("Behavior not found.")
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.100",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")
    parser.add_argument("--behavior_name", type=str, default="animalsrecognitionn1-b6fc4a/behavior_1",
                        help="Name of the behavior")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session, args.behavior_name)



