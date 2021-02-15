import argparse
import os
import os.path as osp
import imageio
import tqdm


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument('video_file', type=str,
                        help='Path to file of video')
    parser.add_argument('s', '--save_dir', type=str, 
                        help='Parent directory for saving')
    parser.add_argument('-r', '--rate', type=float, 
                        help='Frame rate')
    args = parser.parse_args()

    video_file = args.video_file
    save_dir = args.save_dir
    rate = args.rate

    out_dir = osp.splitext(osp.basename(video_file))[0]
    if save_dir:
        out_dir = osp.join(save_dir, out_dir)
    os.makedirs(out_dir)

    reader = imageio.get_reader(video_file)
    meta_data = reader.get_meta_data()
    fps = meta_data['fps']
    print(fps)
    n_frames = meta_data['nframes']

    for i, img in tqdm.tqdm(enumerate(reader), total=n_frames):
        if rate is None or i % int(round(fps / rate)) == 0:
            imageio.imsave(osp.join(out_dir, '%08d.png' % i), img)


if __name__ == '__main__':
    main()
