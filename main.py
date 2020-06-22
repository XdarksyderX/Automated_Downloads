import os
import platform
import getpass
import folderSystem
import organizer


def main():
    media = ['.jpg', '.mp4', '.mp3', '.png', '.jpeg']
    programs = ['.deb', '.tar.gz', '.tar.bz2', '.exe', '.msi', '.AppImage', '.tar.xz', '.tgz']
    code = ['.py', '.js', '.html', '.css', '.jar', '.cpp', '.c', '.rs', '.cs', '.php', '.sh']
    compress = ['.zip', '.rar', '.7zip']
    text = ['.doc', '.docx', '.pdf', '.txt', '.log', '.odt', '.ppt', '.pptx']

    user_system_type = platform.system()
    user_name = getpass.getuser()
    folderSystem.detect_create_folders(user_name, user_system_type, 'MEDIA')
    folderSystem.detect_create_folders(user_name, user_system_type, 'PROGRAMS')
    folderSystem.detect_create_folders(user_name, user_system_type, 'TEXT')
    folderSystem.detect_create_folders(user_name, user_system_type, 'CODE')
    folderSystem.detect_create_folders(user_name, user_system_type, 'COMPRESS')
    folderSystem.detect_create_folders(user_name, user_system_type, 'OTHER')
    organizer.organizer(user_name, programs, 'PROGRAMS', user_system_type)
    organizer.organizer(user_name, text, 'TEXT', user_system_type)
    organizer.organizer(user_name, media, 'MEDIA', user_system_type)
    organizer.organizer(user_name, code, 'CODE', user_system_type)
    organizer.organizer(user_name, compress, 'COMPRESS', user_system_type)



main()
