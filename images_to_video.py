import argparse
import os
import tqdm
import cv2


def main(pic_dir, save_dir, rate):
    video_name = 'annotated.avi'
    if save_dir:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        video_path = os.path.join(save_dir, video_name)
    else:
        video_path = video_name

    images = [img for img in os.listdir(pic_dir) if
              img.endswith(".png")
              or img.endswith('.jpg')]

    # sort images to appear in list in order they were taken
    images = sorted(images, key=lambda x: int(x.split('.')[0]))
    frame = cv2.imread(os.path.join(pic_dir, images[0]))
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_path, 0, rate, (width, height))

    for img in tqdm.tqdm(images):
        video.write(cv2.imread(os.path.join(pic_dir, img)))

    cv2.destroyAllWindows()
    video.release()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', type=str,
                        help='Directory holding images')
    parser.add_argument('-r', '--rate', type=int, default=5,
                        help='Frame rate. Defaults to 5')
    parser.add_argument('-s', '--save', default=None,
                        help='Save path. Defaults to current path')
    args = parser.parse_args()
    pic_dir, save_dir, rate = args.dir, args.save, args.rate

    main(pic_dir, save_dir, args.rate)
