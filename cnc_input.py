import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import json
import sys
from PIL import Image
import optparse
class cnc_input:
    def __init__(self, photo_name):
        self.photo_name = photo_name
        img = mpimg.imread(self.photo_name)
        gray = img[:,:,2]
        plt.imshow(gray, cmap = plt.get_cmap('gray'))
        self.gray = gray
    
    def target_area(self, x, y, x2, y2):
        target_area = self.gray[ int(y) : int(y2), int(x): int(x2)]
        return target_area
    def target_roi(self, x, y, width, length):
        target_area = self.gray[ int(y) : int(y + length), int(x): int(x + width)]
        return target_area
def main(argv = None):
    if argv == None:
        argv = sys.argv
    try:
        target_areas = []
        parser = optparse.OptionParser()
        parser.add_option('-i', '--inputFile', action='store', type='string', dest='input',
                          help='read file from the input path')
        parser.add_option('-o', '--outputFile', action='store', type='string', dest='output',
                          help='output file to the output path')
        parser.add_option('-q', '--quiet', action='store_true', dest='quietMode', help='quiet mode', default=False)
        (options, args) = parser.parse_args(argv)
        if options.input:
            try:
                with open(options.input, 'r') as file:
                    data = json.load(file)
                shapes = data['shapes']
                photo = cnc_input('newchip.png')
                for item in shapes :
                    print(item['label'])
                    start_point = item['points'][0]
                    end_point = item['points'][2]
                    target_area = cnc_input.target_area(photo, start_point[0],start_point[1],end_point[0],end_point[1])
                    # 讓目標區域的高度值統一
                    temp = []
                    for i in range(len(target_area[0])):
                        if (target_area[int(target_area.shape[0]/3)][i] == target_area[int(target_area.shape[0]/2)][i]):
                            temp.append(i)
                    if len(temp) > int(target_area.shape[0]/2):
                        n,m = target_area.shape
                        target_area = [[target_area[0][temp[0]]] * m for i in range(n)]
                    #讓目標區域的高度值統一                      
                    target_areas.append((target_area,start_point[0],start_point[1]))
                return target_areas
            except Exception as e:
                print(e.with_traceback())
    except Exception as e:
        print(e.with_traceback())

        
     


    

    
    
    
if __name__ == '__main__':
    main()
