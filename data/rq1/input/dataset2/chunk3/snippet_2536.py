#Source: https://stackoverflow.com/questions/70819746/python-builtins-attributeerror-tuple-object-has-no-attribute-win32-process
import os, wmi, time
connect = wmi.WMI()
empty = []
excluding = ['svchost.exe', 'lsass.exe', 'explorer.exe', 'sihost.exe', 'System', 'ntoskrnl.exe', 'winnit.exe', 'dwm.exe', 'smss.exe', 'services.exe', 'winlogon.exe', 'csrss.exe', 'RuntimeBroker.exe', 'ApplicationFrameHost.exe', 'ctfmon.exe', 'spoolsv.exe', 'SecurityHealthService.exe', 'System Idle Process', 'Registry', 'wininit.exe', 'fontdrvhost.exe', 'IntelCpHDCPSvc.exe', 'IntelCpHeciSvc.exe', 'igfxCUIService.exe', 'Memory Compression', 'hasplms.exe', 'armsvc.exe', 'IPROSetMonitor.exe', 'FNPLicensingService64.exe', 'jhi_service.exe', 'klnagent.exe', 'avp.exe', 'AdAppMgrSvc.exe', 'veyon-service.exe', 'sqlwriter.exe', 'WmiPrvSE.exe', 'hasplmv.exe', 'avpui.exe', 'PresentationFontCache.exe', 'taskhostw.exe', 'igfxEM.exe', 'rundll32.exe', 'veyon-server.exe', 'veyon-worker.exe', 'ShellExperienceHost.exe', 'SearchUI.exe', 'smartscreen.exe', 'chrome.exe', 'jusched.exe', 'GenuineService.exe', 'avpsus.exe', 'SgrmBroker.exe', 'WindowsInternal.ComposableShell.Experiences.TextInput.InputApp.exe', 'SystemSettingsBroker.exe', 'jucheck.exe', 'cmd.exe', 'conhost.exe', 'dllhost.exe']
process_dictionary = {}
while 1:
    for process in connect.Win32_Process():
        connect = str(process.ProcessId), process.Name
        if process.Name not in excluding:
            prNm = process.Name
            process_dictionary[prNm] = time.time()
    for i in process_dictionary.keys():
        print(i)
    print(process_dictionary)
    time.sleep(10)