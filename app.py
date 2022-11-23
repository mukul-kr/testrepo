import yaml
import os
with open('config2.yml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    print("Load successful")

# def recursiveFolderFileCreator(config):
#     if config is None:
#         return
#     for f in config['Folder']:
#         os.mkdir(f['Name'])
#         recursiveFolderFileCreator(f['Folder'])
#         # print("Folder created: " + folder)

#     for file in config['Files']:
#         open(file, 'a').close()
#         print("File created: " + file)

# recursiveFolderFileCreator(config['Folder'])


def recursor(config, path):
    if config is None or config == []:
        return
    # if path is not '':
    #     path += '/'
    for f in config if type(config) is list else []:
        os.mkdir(path+f['Name'])
        npath = path+f['Name']+ '/'
        if f is not None:
            for file in f['Files'] if 'Files' in f else []:
                with open(npath+file['Name'], 'a') as curFile:
                    if 'Content' in file:
                        curFile.write(file['Content'])
                # print(file['Content'])
            recursor(f['Folders'], npath) if 'Folders' in f else []
            

recursor(config['Folders'], '')


# print(config)

# for i in config['Folder']:
#     print(i)