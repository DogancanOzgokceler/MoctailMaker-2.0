Set oWS = WScript.CreateObject("WScript.Shell")
Dim scriptDir
scriptDir = Left(WScript.ScriptFullName, InStrRev(WScript.ScriptFullName, "\"))
Dim desktop
desktop = oWS.SpecialFolders("Desktop")
Dim oSC
Set oSC = oWS.CreateShortcut(desktop & "\Mocktail Maker 2.0.lnk")
oSC.TargetPath       = "wscript.exe"
oSC.Arguments        = """" & scriptDir & "Calistir.vbs"""
oSC.WorkingDirectory = scriptDir
oSC.IconLocation     = scriptDir & "icon.ico"
oSC.Description      = "Mocktail Maker 2.0 - by Dogancan Ozgokceler"
oSC.WindowStyle      = 1
oSC.Save
MsgBox "Tamamlandi! Masaustunde 'Mocktail Maker 2.0' ikonu olusturuldu.", 64, "Mocktail Maker 2.0"
