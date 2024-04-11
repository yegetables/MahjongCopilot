import os,sys,shutil
from common.utils import ACCOUNT_RECORDS,sub_folder,CHROME_DB,list_folders
from common.log_helper import LOGGER

# 保存当前用户（起个名字）
def saveUserAccount(name):
        newAccountPathStr=ACCOUNT_RECORDS+"/"+name
        if os.path.exists(CHROME_DB):
            if not os.path.exists(newAccountPathStr):
                # mkdir parent folder
                sub_folder(newAccountPathStr)
            shutil.rmtree(newAccountPathStr, ignore_errors=True)
            shutil.copytree(CHROME_DB, newAccountPathStr, dirs_exist_ok=True)
        else:
            LOGGER.info(str("save account "+name+" fail,chrome DB not found"))
            return
        LOGGER.info(str("save account "+name+" success"))    
        return
    
# 切换账号
def switchAccountLogin(name):
    users=listUser()
    if name not in users:
        LOGGER.error(str("switch "+name+" fail,not found in the list of users"))
        return
    newAccountPathStr=ACCOUNT_RECORDS+"/"+name
    if os.path.exists(newAccountPathStr):
        if not os.path.exists(CHROME_DB):
            # mkdir parent folder
            sub_folder(CHROME_DB)
        shutil.rmtree(CHROME_DB, ignore_errors=True)        
        shutil.copytree(newAccountPathStr, CHROME_DB, dirs_exist_ok=True)
    else:
        LOGGER.error(str("switch "+name+" fail,account not found"))
        return

# 列出所有保存的用户
def listUser():
    try:
        return list_folders(str(sub_folder(ACCOUNT_RECORDS).resolve()))
    except:
        LOGGER.error(str("list user fail"))
        return

if len(sys.argv) > 1:
    argument = sys.argv[1]
    users=listUser()
    if argument=='save':
        saveUserAccount(sys.argv[2])
    if argument=='switch':
        switchAccountLogin(sys.argv[2])
    if argument=='list':
        listUser()
    exit(0)