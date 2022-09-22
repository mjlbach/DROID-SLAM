import os

def parse_colmap_intrinsics(camera_txt_filename: str)-> dict:
        # example output
        #1 RADIAL_FISHEYE 1440 1080 660.294 720 540 0.0352702 0.0046637\n
        with open(camera_txt_filename, 'r') as f:
            for _ in range(4):
                l = f.readline()
        e = l.split(' ')
        outputs = {
            'num_cameras': e[0],
            'type':e[1],
            'width':e[2],
            'height':e[3],
            'f':e[4],
            'cx':e[5],
            'cy':e[6],
            'k1':e[7],
            'k2':e[8][:-1],
        }
        return outputs

if __name__ == "__main__":
    datadir = "/vision/group/ego4d/v1/videos_sfm"
    for video_uid in os.listdir(datadir):
        intrinsic_txt = os.path.join(datadir, video_uid, 'sparse', '0', 'cameras.txt')
        try:
            print()
            print(video_uid)
            intrinsics = parse_colmap_intrinsics(intrinsic_txt)
            print(intrinsics)
            print()
            with open(f"./calib/ego4d/{video_uid}.txt", "w") as f:
                f.write(f"{intrinsics['f']} {intrinsics['f']} {intrinsics['cx']} {intrinsics['cy']}")
        except:
            print(f"No intrinsic found for {video_uid}")
