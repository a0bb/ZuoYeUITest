ControlFocus("��", "","Edit1")
WinWait("[CLASS:#32770]","",10)
ControlSetText("��", "", "Edit1", $CmdLine[1])

Sleep(2000)
ControlClick("��", "","Button1")
Sleep(2000)
ControlFocus("��", "","DirectUIHWND2")
Send("^a")

ControlClick("��", "","Button1")