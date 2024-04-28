# -*- mode: python ; coding: utf-8 -*-


a = Analysis( # type: ignore
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure) # type: ignore

exe = EXE( # type: ignore
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MahjongCopilot',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['resources\\icon.ico'],
)
coll = COLLECT( # type: ignore
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MahjongCopilot',
)
import os,sys
import shutil
import json,random
from common.settings import Settings
def changeRandomPort():
    settings = Settings()
    port= settings.mitm_port
    while True:
        new_port = random.randint(1000, 65535)    
        if  settings.valid_mitm_port(new_port) and port!=new_port :
            settings.mitm_port = new_port
            settings.save_json()
            break

dist_path =os.path.join('dist', coll.name)
if not os.path.exists(dist_path):
    os.makedirs(dist_path)
def copyList(datas):
    for data_file in datas:
        src, dest = data_file
        print("src=",src,"--->dist=",os.path.join(dist_path, dest))
        if os.path.isfile(src):
            shutil.copy(src, os.path.join(dist_path, dest))
        elif os.path.isdir(src):
            shutil.copytree(src, os.path.join(dist_path, dest), dirs_exist_ok=True)

my_datas= [
    ('version','.'),
    ('resources','resources'),
    ('liqi_proto','liqi_proto'),
    ('proxinject','proxinject'),
]
copyList(my_datas)

private_datas=[
    ('settings.json','.'),
    ('models','models'),
    ('libriichi3p','libriichi3p'),
    ('account_switch','account_switch'),
    ('browser_data','browser_data'),
]
copyList(private_datas)
changeRandomPort()
