import getFrames, panoramaMapper, sobelFilter
import os


cwd = os.getcwd()
join = os.path.join

def main():
    videos = os.listdir("./video_source")
    if len(videos) == 1:
        video = join(cwd, join("video_source", videos[0]))
        vid2pano(video)
    else:
        for i in range(len(videos)):
            print(str(i)+". "+str(videos[i]))
        index = int(input("Choose Video to Convert: "))
        try:
            video = join(cwd, join("video_source", videos[index]))
            vid2pano(video)
        except Exception as e:
            print(e)
            
def vid2pano(path):
    getFrames.main(path)
    image_name = panoramaMapper.main()
    sobelFilter.main(image_name)

    for f in os.listdir("./frames/"):
        os.remove(join(cwd, join("frames", f)))

if __name__ == "__main__":
    main()