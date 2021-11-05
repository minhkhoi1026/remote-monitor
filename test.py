from win32com.shell import shell, shellcon
def get_document_path():
    return shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0)