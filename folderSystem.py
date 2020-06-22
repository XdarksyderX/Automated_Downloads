import os


def detect_create_folders(username, os_user, folder_name):
    if os_user == 'Linux':
        os.chdir('/home/{}/Downloads'.format(username))
        if not (os.path.isdir('./{}'.format(folder_name))):
            os.mkdir(folder_name)

    elif os_user == 'Windows':
        os.chdir('C:\\Users\\{}\\Downloads'.format(username))
        if not (os.path.isdir('./{}'.format(folder_name))):
            os.mkdir(folder_name)
