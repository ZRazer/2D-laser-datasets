#!/usr/bin/env python

import rosbag
import sys


def filter_topics(in_bag, out_bag, frames_we_want):
    with rosbag.Bag(out_bag, 'w') as outbag:
        print("Writing to " + out_bag)
        print("Reading from " + in_bag)
        for topic, msg, t in rosbag.Bag(in_bag).read_messages():
            if topic == "/tf" and msg.transforms:
                transforms_to_keep = []
                for i in range(len(msg.transforms)):
                    # if its one of the frames we want we keep it
                    if msg.transforms[i].header.frame_id in frames_we_want and msg.transforms[i].child_frame_id in frames_we_want:
                        transforms_to_keep.append(msg.transforms[i])
                        #print("Keeping: " + str(msg.transforms[i]))
                    # else:
                    #     print("Discarding: " + str(msg.transforms[i]))

                msg.transforms = transforms_to_keep
                outbag.write(topic, msg, t)
            elif topic != '/tf':
                outbag.write(topic, msg, t)


if __name__ == '__main__':
    in_bag = sys.argv[1]
    out_bag = sys.argv[2]
    filter_topics(in_bag, out_bag, ['odom','base_footprint','laser'])
    print("Done")
