import os
while True:
    print("Hey! welcome to here. How can I help you? ",end="")
    p=input()
    if (("run" in p) or ("open" in p) or ("execute" in p) or ("launch" in p)) and (("notepad" in p) or ("editor" in p)):
        os.system("notepad")
    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("launch" in p)) and (("google" in p) or ("chrome" in p)):
        os.system("start chrome")
    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("launch" in p)) and (("wmplayer" in p) or ("wm" in p) or ("player" in p)):
        os.system("start wmplayer")
    
    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("launch" in p)) and ("python" in p):
        os.system("python")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("launch" in p)) and (("jupyter" in p) and ("notebook" in p)):
        os.system("jupyter notebook")
    
    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("launch" in p)) and (("calc" in p) or ("calculator" in p) or ("cal" in p)):
        os.system("calc")
    
    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("launch" in p)) and (("task" in p) and ("manager" in p)):
        os.system("taskmgr")
    
    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("launch" in p)) and ("paint" in p):
        os.system("mspaint")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("launch" in p)) and (("control" in p) and ("panel" in p)):
        os.system("control panel")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("launch" in p)) and (("excel" in p) or ("ms" in p) or ("msexcel" in p) or ("MSexcel" in p)):
        os.system("start excel")
    
    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("launch" in p)) and (("word" in p) or ("ms" in p) or ("msword" in p) or ("MSword" in p)):
        os.system("start winword")
    
    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("launch" in p)) and (("powerpoint" in p) or ("ms" in p) or ("mspowerpoint" in p) or ("MSpowerpoint" in p)):
        os.system("start powerpnt")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("launch" in p)) and (("file" in p) and ("browser" in p)):
        os.system("start explorer")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("launch" in p)) and (("internet" in p) and ("explorer" in p)):
        os.system("start iexplore")

    elif (("tell" in p) or ("display" in p) or ("show" in p)) and (("date" in p) or ("today date" in p)):
        os.system("date")
    
    elif ("exit" in p) or ("quit" in p) or ("esc" in p):
        break
    
    else:
        print("Don't Support")
