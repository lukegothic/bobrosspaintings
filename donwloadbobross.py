
'''
DOWNLOAD EVERY BOB ROSS PAINTING
Jeff Thompson | 2017 | jeffreythompson.org

Downloads all 411 paintings by Bob Ross from the
site Two Inch Brush.

'''

import urllib

for i in range(1, 412):
    try:
        print ('downloading painting ' + str(i) + '/' + str(num_images) + '...')
        url = 'http://www.twoinchbrush.com/images/painting' + str(i) + '.png'
        url = url.encode('utf-8')
        filename = ('%03d' % (i,)) + '.png'
        urllib.urlretrieve(url, filename)
    except:
        print ('- ERROR!')