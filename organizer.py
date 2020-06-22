import os
import shutil


def organizer(username, file_type, folder_name, type_os):

    if type_os == 'Linux':
        os.chdir('/home/{}/Downloads'.format(username))
        downloads = '/home/{}/Downloads'.format(username)

    elif type_os == 'Windows':
        downloads = 'C:\\Users\\{}\\Downloads'.format(username)
        os.chdir(downloads)

    container = os.listdir()
    for i in container:
        for j in file_type:
            if os.path.isfile(os.path.join(downloads, i)) and i.endswith(j):
                shutil.move(src=downloads + '\\' + i, dst=downloads + '\\' + folder_name)


def organizer_other(username, type_os):
    if type_os == 'Linux':
        os.chdir('/home/{}/Downloads'.format(username))
        downloads = '/home/{}/Downloads'.format(username)

    elif type_os == 'Windows':
        downloads = 'C:\\Users\\{}\\Downloads'.format(username)
        os.chdir(downloads)

    container = os.listdir()
    for i in container:
        if i != 'MEDIA' and i != 'PROGRAMS' and i != 'TEXT' and i != 'CODE' and i != 'COMPRESS' and i != 'OTHER':
            shutil.move(src=downloads + '\\' + i, dst=downloads + '\\' + 'OTHER')

