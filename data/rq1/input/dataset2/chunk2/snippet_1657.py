#Source: https://stackoverflow.com/questions/67953308/python-pywin32-typeerror-there-is-no-interface-object-registered-that-supports
import pythoncom
import pywintypes


clsid = pywintypes.IID('{9BA05972-F6A8-11CF-A442-00A0C90A8F39}')  # CLSID_ShellWindow
iid = pywintypes.IID('{85CB6900-4D95-11CF-960C-0080C7F4EE85}')  # IID_IShellWindow
pythoncom.CoCreateInstance(clsid, None, pythoncom.CLSCTX_ALL, iid)