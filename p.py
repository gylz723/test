import base64
import subprocess
shell=base64.b64decode(b'cG93ZXJzaGVsbA==')
comm='Del HKCU:\Software\Policies\Microsoft\Windows\System -recurse';
comm=comm+'Del HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies -recurse';
comm=comm+'Del "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\SGTool.exe" -recurse;'
comm=comm+'Del "HKCU:\SOFTWARE\Policies\Microsoft\Internet Explorer\Restrictions" -recurse;'
comm=comm+'Del HKCU:\SOFTWARE\Policies\Microsoft\MMC -recurse;'
comm=comm+'Start-Sleep -s 1;taskkill /im DesktopMgr64.exe /t /f;'
comm=comm+'taskkill /im explorer.exe /t /f;'
comm=comm+'Start-Sleep -s 1;explorer;'
#print(comm)
p=subprocess.Popen([shell,comm] , stdout=subprocess.PIPE)
dt=p.stdout.read()
print(dt)
