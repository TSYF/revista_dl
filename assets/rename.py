import os

# Rename every scss file except main.scss to have a _ prefix

for dir, subdirs, fileNames, in os.walk('./scss'):

    for fileName in fileNames:
        if fileName != 'main.scss':
            os.rename(os.path.join(dir, fileName), os.path.join(dir, '_' + fileName))