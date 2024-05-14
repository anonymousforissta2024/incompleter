#Source: https://stackoverflow.com/questions/75358233/ctypes-argumenterror-argument-1-typeerror-dont-know-how-to-convert-parameter
import ctypes
import win32security

h_token = win32security.OpenProcessToken(ctypes.windll.kernel32.GetCurrentProcess(), win32security.TOKEN_ALL_ACCESS)

lpApplicationName = ctypes.c_wchar_p(rf"C:\\Windows\\System32\\cmd.exe")
lpCommandLine = ctypes.c_wchar_p("")
dwCreationFlags = 0x00000010
lpEnvironment = None
lpProcessAttributes = None
lpThreadAttributes = None
bInheritHandles = False

ctypes.windll.advapi32.CreateProcessWithTokenW(h_token, 0, lpApplicationName, lpCommandLine, dwCreationFlags, lpEnvironment, None, lpProcessAttributes, lpThreadAttributes, bInheritHandles)