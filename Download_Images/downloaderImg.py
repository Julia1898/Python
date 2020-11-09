# import modules
import pandas as pd 
import urllib.request

def url_to_jpg(i, url, file_path):
  '''
    Args: 
      -- i : number of image.
      --url : a URL address of a given image
      --file_path : where to save a final image

  '''

  filename = url.split("/")[-1].split("?")[0] 
  full_path = '{}{}'.format(file_path, filename)
  urllib.request.urlretrieve(url, full_path)

  print('{} saved.'.format(filename))

  return None

# Set constants
FILENAME = 'table.csv'
FILE_PATH = 'images/'

urls = pd.read_csv(FILENAME)

# Save images to the directory by iterating through the list 
for i, url in enumerate(urls.values):
  url_to_jpg(i, url[0], FILE_PATH)
