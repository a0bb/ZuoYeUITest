ControlFocus("打开", "","Edit1")
WinWait("[CLASS:#32770]","",10)
ControlSetText("打开", "", "Edit1", $CmdLine[1])

Sleep(2000)
ControlClick("打开", "","Button1")
Sleep(2000)
ControlFocus("打开", "","DirectUIHWND2")
Send("^a")

ControlClick("打开", "","Button1")