Set oWS = WScript.CreateObject("WScript.Shell")
Dim scriptDir
scriptDir = Left(WScript.ScriptFullName, InStrRev(WScript.ScriptFullName, "\"))
oWS.Run "pythonw """ & scriptDir & "MocktailMaker.py""", 0, False
