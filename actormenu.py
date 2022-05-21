from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog, Tk, Frame, Menu
import os
import shutil
import sys
from tkinter.font import Font
import tkinter as tk
from tkinter import messagebox
from pynput.keyboard import Key, Controller
import sys
import subprocess
import time
from threading import Thread
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

precachemodels = []
precacheanims = []
def process():
    line=text.get("1.0", END)
    array = line.splitlines()
    output.delete("1.0", END)
    output.insert('end',"/*\n *	SASS' CINEMATIC MOD - Precache file (#301)\n */\n\n//   INFO & STUFF :\n//   All animations needs to be precached\n//   Normal MP playermodels don't need to be precached, but SP/Custom ones do\n//   List of MP models : https://pastebin.com/raw/0a53Npp8\n//   List of MP anims : https://pastebin.com/raw/KGbrSCdx\n\n//   HOW TO USE :\n//   Put your precache between the \"{ }\" brackets below\n//   PrecacheModel(\"name_of_model\");\n//   PrecacheMPAnim(\"name_of_anim\");\n\n\n#include maps\\mp\\_utility;\n#include common_scripts\\utility;\n#using_animtree(\"multiplayer\");\n\nprecache()\n{\n")
    
    for i in array[:-1]:
        for j in models:       
            if j[:-5] == i:
                precachemodels.append(j[:-5])
    toprecache = text.get('1.0', END)
    precachesplit = toprecache.splitlines(False)
    precacheanims = [element for element in precachesplit if element not in precachemodels]

    for i in precacheanims:
        output.insert('end',"PrecacheMPAnim(\"" + i + "\");\n");
    output.delete("end-2l","end-1l") 
    for i in precachemodels:
        output.insert('end',"PrecacheModel(\"" + i + "\");\n");
    output.insert('end',"}");
    fileloc = open_file + "/mods/Cinematic mod/_precache.gsc"
    file = open(fileloc, 'w')
    file.write(output.get(1.0, END))
    file.close()

def processmodcsv():
    line=modcsv.get("1.0", END)
    array = line.splitlines()
    output = ''
    for i in array:
        output = output + i[:-5] + '\n'
    fileloc = open_file + "/zone_source/mod.csv"
    file = open(fileloc, 'w')
    file.write(output)
    file.close()

def addtoprecache():
    content = modcsv.get("1.0",END)[:-2]
    splitcontent = content.split('\n')
    for i in splitcontent:
        if i[1] == 'a':
            i = i[6:]
            i = i[:-5]
        elif i[1] == 'm':
            i = i[7:]
            i = i[:-5]        
        text.insert(END, i + '\n')



### DIRECTORY ###

drives = [chr(x) + ':' for x in range(65, 90) if os.path.exists(chr(x) + ':')]


def listDirectories():
    listdir = os.listdir(os.getcwd())
    for x in listdir:
        print(x)


### MENU FUNCTIONS ###

def clear():
    text.delete("1.0", END)
    precachemodels.clear()
    precacheanims.clear()

def clearsp():
    modcsv.delete("1.0", END)
    precachemodels.clear()

def enter_refresh(e):
    refresh['bg'] = 'white'
    refresh['fg'] = '#1c1c1c'

def leave_refresh(e):
    refresh['bg'] = '#1c1c1c'
    refresh['fg'] = 'white'

def on_enter_process(e):
    process_button['bg'] = 'white'
    process_button['fg'] = '#1c1c1c'

def on_leave_process(e):
    process_button['bg'] = '#1c1c1c'
    process_button['fg'] = 'white'

def on_enter_processmodcsv(e):
    processmodcsv_button['bg'] = 'white'
    processmodcsv_button['fg'] = '#1c1c1c'

def on_leave_processmodcsv(e):
    processmodcsv_button['bg'] = '#1c1c1c'
    processmodcsv_button['fg'] = 'white'

def on_enter_clear(e):
    clear_button['bg'] = 'white'
    clear_button['fg'] = '#1c1c1c'

def on_leave_clear(e):
    clear_button['bg'] = '#1c1c1c'
    clear_button['fg'] = 'white'

def on_enter_clearsp(e):
    clearsp_button['bg'] = 'white'
    clearsp_button['fg'] = '#1c1c1c'

def on_leave_clearsp(e):
    clearsp_button['bg'] = '#1c1c1c'
    clearsp_button['fg'] = 'white'


def on_enter_dir(e):
    dir_button['bg'] = 'white'
    dir_button['fg'] = '#1c1c1c'

def on_leave_dir(e):
    dir_button['bg'] = '#1c1c1c'
    dir_button['fg'] = 'white'

def on_enter_run(e):
    run_button['bg'] = 'white'
    run_button['fg'] = '#1c1c1c'

def on_leave_run(e):
    run_button['bg'] = '#1c1c1c'
    run_button['fg'] = 'white'

def on_enterm_run(e):
    runm_button['bg'] = 'white'
    runm_button['fg'] = '#1c1c1c'

def on_leavem_run(e):
    runm_button['bg'] = '#1c1c1c'
    runm_button['fg'] = 'white'

def on_enter_pc(e):
    addtoprecache_button['bg'] = 'white'
    addtoprecache_button['fg'] = '#1c1c1c'

def on_leave_pc(e):
    addtoprecache_button['bg'] = '#1c1c1c'
    addtoprecache_button['fg'] = 'white'

def saveas():
    reopen_file = filedialog.askdirectory()
    fileloc = reopen_file + "/export.txt"
    file = open(fileloc, 'w')
    file.write(text.get(1.0, END))
    file.close()
    
def setdir():
    global open_file
    open_file = filedialog.askdirectory()
    userdir.delete("1.0", END)
    userdir.insert('end', open_file)
    zfilepath = open_file + "/zone/english"
    get_ddir()
    get_zdir()
    c.deselect()

def setxadir():
    pass
    #xa_filepath = open_file + "/dump/airport/XAnim"

def getxdirs(e, arg):
    get_xadir(1)
    get_xmdir(1)

xa_arr = []
def get_xadir(arg):
    global xa_arr
    open_file = userdir.get("1.0", END)
    open_file = open_file[:-1]
    xa_sp = dumplist.get(dumplist.curselection())
    if ".ff" in xa_sp:
        xa_filepath = open_file + "/dump/" + xa_sp[:-3] + "/XAnim"
    else:
        xa_filepath = open_file + "/dump/" + xa_sp + "/XAnim"
    
    xa_arr = os.listdir(xa_filepath)
    xa_update(xa_arr)

xm_arr = []
def get_xmdir(arg):
    global xm_arr
    open_file = userdir.get("1.0", END)
    open_file = open_file[:-1]
    xm_sp = dumplist.get(dumplist.curselection())
    if ".ff" in xm_sp:
        xm_filepath = open_file + "/dump/" + xm_sp[:-3] + "/XModel"
    else:
        xm_filepath = open_file + "/dump/" + xm_sp + "/XModel"
   
    xm_arr = os.listdir(xm_filepath)
    xm_update(xm_arr)
    
zonearray = []
def get_zdir():
    global zonearray
    open_file = userdir.get("1.0", END)
    open_file = open_file[:-1]
    zfilepath = open_file + "/zone/english"
    zonearray = os.listdir(zfilepath)
    def dfilter(variable):
        removedumps = dumparray
        if(variable in removedumps):
            return True
        else:
            return False
    
    if showdumped.get() == 'On':
        pass
    if showdumped.get() == 'Off':
        removedumps = dumparray
        for i in removedumps:
            for k in zonearray:
                if i == k:
                    zonearray.remove(i)

    
    zupdate(zonearray)

def deselect_item(e):
    previous_selected = zonelist.curselection()
    if zonelist.curselection() == previous_selected:
            zonelist.selection_clear(0, tkinter.END)
    previous_selected = zonelist.curselection()
    

dumparray = []
def get_ddir():
    global dumparray
    open_file = userdir.get("1.0", END)
    open_file = open_file[:-1]
    dfilepath = open_file + "/dump"
    try:
        dumparray = os.listdir(dfilepath)
    except:
        popup('ErrorCode 101: Misconstructed Directory\n(Ignore if program still works)')
    for i in range(len(dumparray)):
        dumparray[i] = dumparray[i] + '.ff'
    
    dupdate(dumparray)


 
### DUMPED SEARCH BAR ###

def dump_temp_text(e):
   dsearchbar.delete(0,"end")



def dupdate(dumps):
    #clear
    dumplist.delete(0, END)
    #add
    for dump in dumps:
        dumplist.insert(END, dump)

def insertdump(e):
    #text.insert("1.0", zonelist.get(ACTIVE) + "\n")
    pass

def dump_check(e):
    open_file = userdir.get("1.0", END)
    open_file = open_file[:-1]
    dfilepath = open_file + "/dump"
    dumparray = os.listdir(dfilepath)
    
    #userinput
    dusersearched = dsearchbar.get()
    
    if dusersearched == '':
        
        ddata = [dump + '.ff' for dump in dumparray]
    else:
        ddata = []
        for dump in dumparray:
            if dusersearched.lower() in dump.lower():
                ddata.append(dump + '.ff')
                
        
    #searched items update
    
    dupdate(ddata)


### ZONE SEARCH BAR ###

def zone_temp_text(e):
   zsearchbar.delete(0,"end")



def zupdate(zones):
    #clear
    zonelist.delete(0, END)

    
    #add
    for zone in zones:
        zonelist.insert(END, zone)

def insertzone(e):
    #text.insert("1.0", zonelist.get(ACTIVE) + "\n")
    pass

def zone_check(e):
    open_file = userdir.get("1.0", END)
    open_file = open_file[:-1]
    zfilepath = open_file + "/zone/english"
    
    zonearray = os.listdir(zfilepath)
    

    def dfilter(variable):
        removedumps = dumparray
        if(variable in removedumps):
            return True
        else:
            return False
    
    if showdumped.get() == 'On':
        pass
    if showdumped.get() == 'Off':
        filtered = filter(dfilter, zonearray)
        for s in filtered:
            zonearray.remove(s)

    
        
    #userinput
    zusersearched = zsearchbar.get()

    if zusersearched == '':
        zdata = zonearray
    else:
        zdata = []
        for zone in zonearray:
            if zusersearched.lower() in zone.lower():
                zdata.append(zone)
    #searched items update
    zupdate(zdata)




### XANIM/XMODELSEARCH BAR ###

def xa_temp_text(e):
    xa_searchbar.delete(0,"end")

def xm_temp_text(e):
    xm_searchbar.delete(0,"end")

def insertxanim(e):
    modcsv.insert("1.0", 'xanim,' + xa_list.get(xa_list.curselection()) + "\n")
    ldadd(ld)

models = []
def insertxmodel(e):
    global models
    modcsv.insert("1.0", 'xmodel,' + xm_list.get(xm_list.curselection()) + "\n")
    models.append(xm_list.get(xm_list.curselection()))
    ldadd(ld)

def xa_update(xanims):
    xa_list.delete(0, END)
    for anim in xanims:
        xa_list.insert(END, anim)

def xa_check(e):
    xa_usersearched = xa_searchbar.get()

    if xa_usersearched == '':
        xa_data = xa_arr
    else:
        xa_data = []
        for xanim in xa_arr:
            if xa_usersearched.lower() in xanim.lower():
                xa_data.append(xanim)
    xa_update(xa_data)


def xm_update(xmodels):
    xm_list.delete(0, END)
    for model in xmodels:
        xm_list.insert(END, model)

def xm_check(e):
    xm_usersearched = xm_searchbar.get()

    if xm_usersearched == '':
        xm_data = xm_arr
    else:
        xm_data = []
        for xmodel in xm_arr:
            if xm_usersearched.lower() in xmodel.lower():
                xm_data.append(xmodel)
    xm_update(xm_data)
                
        

### SEARCH BAR ###

def temp_text(e):
   searchbar.delete(0,"end")

def update(anims):
    #clear
    animlist.delete(0, END)
    #add
    for anim in anims:
        animlist.insert(END, anim)

def insertanim(e):
    text.insert("1.0", animlist.get(animlist.curselection()) + "\n")

def check(e):
    #userinput
    usersearched = searchbar.get()

    if usersearched == '':
        data = animarray
    else:
        data = []
        for anim in animarray:
            if usersearched.lower() in anim.lower():
                data.append(anim)
    #searched items update
    update(data)
   
#actually zone tool
def zonebuilder():
    pass


def zonedump(e):
    keyboard = Controller()
    userfilepath = userdir.get(1.0, END)
    userfilearray = userfilepath.split('/')
    userfilearray[len(userfilearray)-1] = userfilearray[len(userfilearray)-1].replace("\n","")
    userfilearray.append('zonetool_iw4.exe')    
    inp = userfilearray[0]
    
    if inp in drives:
        os.chdir(inp + '\\')
    else:
        popup('Error102: Game directory is either not complete or not defined.')        
    for i in range(len(userfilearray)-2):
        res = userfilearray[i+1]
        if res in os.listdir(os.getcwd()):
            os.chdir(res)    
    res = userfilearray[len(userfilearray)-1]
    if os.path.isfile(res):
        if zonelist.curselection():
            proc = subprocess.Popen('"' + res + '"')
    time.sleep(2)
    zonetodump = zonelist.get(ACTIVE)[:-3]
    typetext = 'dumpzone ' + zonetodump
    zonelist.selection_clear(0, 'end')
    keyboard.type(typetext)
    keyboard.press(Key.enter)

def migratemod():
    ogfilepath = userdir.get(1.0, END)
    shutil.copy2(ogfilepath[:-1] + '/zone/mod.ff', ogfilepath[:-1] + '/zone/english/')
    shutil.copy2(ogfilepath[:-1] + '/zone/mod.ff', ogfilepath[:-1] + '/mods/Cinematic mod/')
    

def openzonebuilder():
    
    keyboard = Controller()
    ogfilepath = userdir.get(1.0, END)
    ogfilearray = ogfilepath.split('/')
    ogfilearray[len(ogfilearray)-1] = ogfilearray[len(ogfilearray)-1].replace("\n","")
    ogfilearray.append('iw4x.exe - Shortcut.lnk')
    oginp = ogfilearray[0]
    
    if oginp in drives:
        os.chdir(oginp + '\\')
    else:
        popup('Game directory is either not complete or not defined.')
        
    for i in range(len(ogfilearray)-2):
        ogres = ogfilearray[i+1]
        if ogres in os.listdir(os.getcwd()):
            os.chdir(ogres)
    
    ogres = ogfilearray[len(ogfilearray)-1]
    extendedfp = ogfilepath[:-1]+'/iw4x.exe - Shortcut.lnk'
    pproc = os.startfile('"' + ogres + '"')
    time.sleep(4)
    zonestobuild = dict.fromkeys(ld)
    for i in zonestobuild:
        keyboard.type('loadzone ' + i[:-3] + ';')
    keyboard.press(Key.enter)
    time.sleep(1 * len(zonestobuild))
    keyboard.type('buildzone mod')
    keyboard.press(Key.enter)

def openzonebuilderm():
    
    keyboard = Controller()
    ogfilepath = userdir.get(1.0, END)
    ogfilearray = ogfilepath.split('/')
    ogfilearray[len(ogfilearray)-1] = ogfilearray[len(ogfilearray)-1].replace("\n","")
    ogfilearray.append('iw4m.exe - Shortcut.lnk')
    oginp = ogfilearray[0]
    
    if oginp in drives:
        os.chdir(oginp + '\\')
    else:
        popup('Game directory is either not complete or not defined.')
        
    for i in range(len(ogfilearray)-2):
        ogres = ogfilearray[i+1]
        if ogres in os.listdir(os.getcwd()):
            os.chdir(ogres)
    
    ogres = ogfilearray[len(ogfilearray)-1]
    extendedfp = ogfilepath[:-1]+'/iw4m.exe - Shortcut.lnk'
    #if os.path.isfile(ogfilepath[:-1]+'/iw4m.exe - Shortcut.lnk'):
    
    #print(ogfilepath[:-1]+'/iw4m.exe - Shortcut.lnk')
    pproc = os.startfile('"' + ogres + '"')
    
    #pproc = subprocess.Popen('"' + extendedfp + '"')
    time.sleep(4)
    zonestobuild = dict.fromkeys(ld)
    for i in zonestobuild:
        keyboard.type('loadzone ' + i[:-3] + ';')
    keyboard.press(Key.enter)
    time.sleep(1 * len(zonestobuild))
    keyboard.type('buildzone mod')
    keyboard.press(Key.enter)
    time.sleep(0/7 * len(zonestobuild))
    shutil.copy2(ogfilepath[:-1] + '/zone/mod.ff', ogfilepath[:-1] + '/zone/english/')
    shutil.copy2(ogfilepath[:-1] + '/zone/mod.ff', ogfilepath[:-1] + '/mods/Cinematic mod/')
    

    


def zonedump_threaded(*a, **k):
  Thread(target=zonedump, args=a, kwargs=k).start()
        
def zonebuild_threaded(*a, **k):
  Thread(target=openzonebuilder, args=a, kwargs=k).start()

def zonebuildm_threaded(*a, **k):
  Thread(target=openzonebuilderm, args=a, kwargs=k).start()


###### LOAD DUMPED #######

def removeDuplicates(listofElements):
    uniqueList = []
    for elem in listofElements:
        if elem not in uniqueList:
            uniqueList.append(elem)

    return uniqueList

delete = []
def ldadd(ld):
    selection = dumplist.get(dumplist.curselection())


            
    ld.append(selection)
    
    ldupdate(dict.fromkeys(ld))
        

def ldupdate(ld):
    load_dumps.delete(0, END)
    for i in ld:
        load_dumps.insert(END, i)



window = customtkinter.CTk()

########################################################################################## WINDOW ###############################################################################################################################
window.geometry("1600x650");
height = 1600
width = 650
window.minsize(height, width)
window.maxsize(height, width)

font1 = Font(family = "Helvetica")

window.title("MW2 Actor Console")
icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)
window.config(background="#19181a");

def popup(message):
    window.bell()
    messagebox.showinfo('Exception Handled', message)



anims = """pb_stand_alert_RPG\npb_stand_alert_mg\npb_stand_alert\npb_stand_ads\npb_stand_ads_mg\npb_stand_grenade_idle\npb_stand_grenade_pullpin\npb_stand_stickgrenade_idle\npb_stand_alert_pistol\npb_stand_ads_pistol\npb_stand_alert_unarmed\npb_stand__shoot_ads_pistol\npb_rifle_idleA_ads\npb_rifle_idleB_ads\npb_crouch_grenade_idle\npb_crouch_stickgrenade_idle\npb_crouch_grenade_pullpin\npb_prone_pullout_knife\npb_crouch_alert\npb_crouch_ads\npb_crouch_alert_pistol\npb_crouch_ads_pistol\npb_crouch_alert_unarmed\npb_prone_hold\npb_stand_alert_akimbo\npb_crouch_alert_akimbo\npb_stand_alert_shield\npb_crouch_alert_shield\npb_chicken_dance\npb_chicken_dance_crouch\npb_prone_bombplant\npb_stand_bombplant\npb_crouch_bombplant\npb_crouch_remotecontroller\npb_prone_remotecontroller\npb_stand_remotecontroller\npb_hold_idle\npb_crouch_hold_idle\npb_crouch_alert_RPG\npb_crouch_ads_RPG\npb_stand_ads_RPG\npb_prone_aim_RPG\npb_prone_aim_sniper\npb_stand_pullout_knife\npb_shield_grenade_pullpin\npb_shield_knife_pullout\npb_pistol_run_fast\npb_run_fast\npb_run_rifle\npb_run_smg\npb_run_heavy\npb_run_forward_m\npb_run_right_m\npb_run_left_m\npb_run_back_m\npb_crouchwalk_loop\npb_sprint\npb_sprint_B\npb_sprint_gundown\npb_sprint_stickgrenade\npb_sprint_grenade\npb_sprint_RPG\npb_sprint_pistol\npb_sprint_hold\npb_sprint_akimbo\npb_runjump_takeoff\npb_runjump_land\npb_standjump_takeoff\npb_standjump_land\npb_runjump_takeoff_pistol\npb_runjump_land_pistol\npb_standjump_takeoff_pistol\npb_standjump_land_pistol\npb_combatrun_forward_loop\npb_combatrun_back_loop\npb_combatrun_left_loop\npb_combatrun_right_loop\npb_combatrun_forward_loop_pistol\npb_combatrun_back_loop_pistol\npb_combatrun_left_loop_pistol\npb_combatrun_right_loop_pistol\npb_combatrun_forward_loop_unarmed\npb_combatrun_forward_loop_heavy\npb_combatrun_forward_loop_light\npb_combatrun_forward_loop_rifles\npb_combatrun_forward_loop_stickgrenade\npb_combatrun_left_loop_grenade\npb_combatrun_right_loop_grenade\npb_combatrun_back_loop_grenade\npb_combatrun_forward_RPG\npb_combatrun_back_RPG\npb_combatrun_left_RPG\npb_combatrun_right_RPG\npb_walk_forward_RPG_ads\npb_walk_back_RPG_ads\npb_walk_left_RPG_ads\npb_walk_right_RPG_ads\npb_walk_forward_akimbo\npb_walk_back_akimbo\npb_walk_left_akimbo\npb_walk_right_akimbo\npb_walk_forward_mg\npb_sprint_mg\npb_combatrun_forward_mg\npb_combatrun_right_mg\npb_combatrun_left_mg\npb_combatrun_back_mg\npb_crouch_run_forward\npb_crouch_run_back\npb_crouch_run_left\npb_crouch_run_right\npb_crouch_run_forward_pistol\npb_crouch_run_forward_grenade\npb_crouch_run_forward_stickgrenade\npb_crouch_run_back_pistol\npb_crouch_run_left_pistol\npb_crouch_run_right_pistol\npb_crouch_walk_forward_pistol\npb_crouch_walk_back_pistol\npb_crouch_walk_left_pistol\npb_crouch_walk_right_pistol\npb_crouch_run_forward_unarmed\npb_crouch_run_back_grenade\npb_crouch_run_left_grenade\npb_crouch_run_right_grenade\npb_crouch_shoot_run_forward\npb_crouch_shoot_run_back\npb_crouch_shoot_run_left\npb_crouch_shoot_run_right\npb_crouch_walk_forward_unarmed\npb_crouch_grenade_throw\npb_stand_grenade_throw\npb_stand_stickgrenade_throw\npb_stand_shoot_walk_forward\npb_stand_shoot_walk_back\npb_stand_shoot_walk_left\npb_stand_shoot_walk_right\npb_stand_shoot_walk_forward_unarmed\npb_combatwalk_forward_loop_pistol\npb_combatwalk_back_loop_pistol\npb_combatwalk_left_loop_pistol\npb_combatwalk_right_loop_pistol\npb_walk_right\npb_walk_left\npb_walk_back\npb_walk_forward\npb_pull_stand_intro\npb_pull_stand_loop\npb_pull_stand_end\npb_hold_run\npb_hold_run_back\npb_hold_run_right\npb_hold_run_left\npb_crouch_hold_run\npb_crouch_hold_run_back\npb_crouch_hold_run_left\npb_crouch_hold_run_right\npb_crouch_walk_forward_shield\npb_crouch_walk_back_shield\npb_crouch_walk_left_shield\npb_crouch_walk_right_shield\npb_crouch_run_back_RPG\npb_crouch_run_forward_RPG\npb_crouch_run_left_RPG\npb_crouch_run_right_RPG\npb_crouch_walk_right_RPG\npb_crouch_walk_left_RPG\npb_crouch_walk_forward_RPG\npb_crouch_walk_back_RPG\npb_prone_crawl_hold\npb_prone_crawl_back_hold\npb_prone_crawl_left_hold\npb_prone_crawl_right_hold\npb_prone_crawl_akimbo\npb_prone_crawl_back_akimbo\npb_prone_crawl_left_akimbo\npb_prone_crawl_right_akimbo\npb_combatrun_forward_akimbo\npb_combatrun_right_akimbo\npb_combatrun_left_akimbo\npb_combatrun_back_akimbo\npb_crouch_walk_right_akimbo\npb_crouch_walk_left_akimbo\npb_crouch_walk_forward_akimbo\npb_crouch_walk_back_akimbo\npb_walk_forward_shield\npb_walk_left_shield\npb_walk_right_shield\npb_walk_back_shield\npb_combatrun_forward_shield\npb_combatrun_left_shield\npb_combatrun_right_shield\npb_combatrun_back_shield\npb_sprint_shield\npb_climbdown\npb_climbup\npb_prone_crawl\npb_prone_grenade_crawl\npb_prone_crawl_left\npb_prone_crawl_right\npb_prone_crawl_back\npb_prone_aim\npb_prone_aim_akimbo\npb_prone_aim_pistol\npb_prone_aim_grenade\npb_prone_grenade_crawl_left\npb_prone_grenade_crawl_right\npb_prone_crawl_pistol\npb_prone_crawl_pistol_back\npb_prone_pistol_crawl_left\npb_prone_pistol_crawl_right\npb_prone_grenade_crawl_back\npb_crouch2prone\npb_prone2crouch\npb_prone2crouchrun\npb_prone2crouch_shield\npb_laststand_death\npb_laststand_idle\npb_laststand_crawl\npb_laststand_crawl_back\npb_laststand_crawl_right\npb_laststand_crawl_left\npt_laststand_melee\npb_laststand_idle_RPG\npb_laststand_crawl_RPG\npb_laststand_crawl_right_RPG\npb_laststand_crawl_left_RPG\npb_laststand_crawl_back_RPG\npb_laststand_idle_akimbo\npb_laststand_crawl_akimbo\npb_laststand_crawl_right_akimbo\npb_laststand_crawl_left_akimbo\npb_laststand_crawl_back_akimbo\npb_laststand_crawl_back_shield\npb_laststand_crawl_shield\npb_laststand_idle_shield\npb_laststand_crawl_right_shield\npb_laststand_crawl_left_shield\npb_deadhands_idle\npb_deadhands_crawl_back\npb_deadhands_crawl_forward\npb_deadhands_crawl_left\npb_deadhands_crawl_right\nmp_mantle_up_57\nmp_mantle_up_51\nmp_mantle_up_45\nmp_mantle_up_39\nmp_mantle_up_33\nmp_mantle_up_27\nmp_mantle_up_21\nmp_mantle_over_high\nmp_mantle_over_mid\nmp_mantle_over_low\nmp_mantle_up_57_fr\nmp_mantle_up_51_fr\nmp_mantle_up_45_fr\nmp_mantle_up_39_fr\nmp_mantle_up_33_fr\nmp_mantle_up_27_fr\nmp_mantle_up_21_fr\nmp_mantle_over_high_fr\nmp_mantle_over_mid_fr\nmp_mantle_over_low_fr\npb_saw_gunner_aim_down_right45\npb_saw_gunner_aim_down_right30\npb_saw_gunner_aim_down_right15\npb_saw_gunner_aim_down_center\npb_saw_gunner_aim_down_left15\npb_saw_gunner_aim_down_left30\npb_saw_gunner_aim_down_left45\npb_saw_gunner_aim_level_right45\npb_saw_gunner_aim_level_right30\npb_saw_gunner_aim_level_right15\npb_saw_gunner_aim_level_center\npb_saw_gunner_aim_level_left15\npb_saw_gunner_aim_level_left30\npb_saw_gunner_aim_level_left45\npb_saw_gunner_aim_up_right45\npb_saw_gunner_aim_up_right30\npb_saw_gunner_aim_up_right15\npb_saw_gunner_aim_up_center\npb_saw_gunner_aim_up_left15\npb_saw_gunner_aim_up_left30\npb_saw_gunner_aim_up_left45\npb_saw_gunner_prone_aim_down_left40\npb_saw_gunner_prone_aim_down_left20\npb_saw_gunner_prone_aim_down_center\npb_saw_gunner_prone_aim_down_right20\npb_saw_gunner_prone_aim_down_right40\npb_saw_gunner_prone_aim_level_left40\npb_saw_gunner_prone_aim_level_left20\npb_saw_gunner_prone_aim_level_center\npb_saw_gunner_prone_aim_level_right20\npb_saw_gunner_prone_aim_level_right40\npb_saw_gunner_prone_aim_up_left40\npb_saw_gunner_prone_aim_up_left20\npb_saw_gunner_prone_aim_up_center\npb_saw_gunner_prone_aim_up_right20\npb_saw_gunner_prone_aim_up_right40\npb_saw_gunner_lowwall_aim_down_left45\npb_saw_gunner_lowwall_aim_down_left30\npb_saw_gunner_lowwall_aim_down_left15\npb_saw_gunner_lowwall_aim_down_center\npb_saw_gunner_lowwall_aim_down_right15\npb_saw_gunner_lowwall_aim_down_right30\npb_saw_gunner_lowwall_aim_down_right45\npb_saw_gunner_lowwall_aim_level_left45\npb_saw_gunner_lowwall_aim_level_left30\npb_saw_gunner_lowwall_aim_level_left15\npb_saw_gunner_lowwall_aim_level_center\npb_saw_gunner_lowwall_aim_level_right15\npb_saw_gunner_lowwall_aim_level_right30\npb_saw_gunner_lowwall_aim_level_right45\npb_saw_gunner_lowwall_aim_up_left45\npb_saw_gunner_lowwall_aim_up_left30\npb_saw_gunner_lowwall_aim_up_left15\npb_saw_gunner_lowwall_aim_up_center\npb_saw_gunner_lowwall_aim_up_right15\npb_saw_gunner_lowwall_aim_up_right30\npb_saw_gunner_lowwall_aim_up_right45\npb_proneMG42gunner_fire_40left_15down\npb_proneMG42gunner_fire_20left_15down\npb_proneMG42gunner_fire_forward_15down\npb_proneMG42gunner_fire_20right_15down\npb_proneMG42gunner_fire_40right_15down\npb_proneMG42gunner_fire_40left_level\npb_proneMG42gunner_fire_20left_level\npb_proneMG42gunner_fire_forward_level\npb_proneMG42gunner_fire_20right_level\npb_proneMG42gunner_fire_40right_level\npb_proneMG42gunner_fire_40left_15up\npb_proneMG42gunner_fire_20left_15up\npb_proneMG42gunner_fire_forward_15up\npb_proneMG42gunner_fire_20right_15up\npb_proneMG42gunner_fire_40right_15up\npb_proneMG42gunner_aim_40left_15down\npb_proneMG42gunner_aim_20left_15down\npb_proneMG42gunner_aim_forward_15down\npb_proneMG42gunner_aim_20right_15down\npb_proneMG42gunner_aim_40right_15down\npb_proneMG42gunner_aim_40left_level\npb_proneMG42gunner_aim_20left_level\npb_proneMG42gunner_aim_forward_level\npb_proneMG42gunner_aim_20right_level\npb_proneMG42gunner_aim_40right_level\npb_proneMG42gunner_aim_40left_15up\npb_proneMG42gunner_aim_20left_15up\npb_proneMG42gunner_aim_forward_15up\npb_proneMG42gunner_aim_20right_15up\npb_proneMG42gunner_aim_40right_15up\npb_standMG42gunner_fire_45left_15down\npb_standMG42gunner_fire_30left_15down\npb_standMG42gunner_fire_15left_15down\npb_standMG42gunner_fire_forward_15down\npb_standMG42gunner_fire_15right_15down\npb_standMG42gunner_fire_30right_15down\npb_standMG42gunner_fire_45right_15down\npb_standMG42gunner_fire_45left_level\npb_standMG42gunner_fire_30left_level\npb_standMG42gunner_fire_15left_level\npb_standMG42gunner_fire_forward_level\npb_standMG42gunner_fire_15right_level\npb_standMG42gunner_fire_30right_level\npb_standMG42gunner_fire_45right_level\npb_standMG42gunner_fire_45left_15up\npb_standMG42gunner_fire_30left_15up\npb_standMG42gunner_fire_15left_15up\npb_standMG42gunner_fire_forward_15up\npb_standMG42gunner_fire_15right_15up\npb_standMG42gunner_fire_30right_15up\npb_standMG42gunner_fire_45right_15up\npb_standMG42gunner_aim_45left_15down\npb_standMG42gunner_aim_30left_15down\npb_standMG42gunner_aim_15left_15down\npb_standMG42gunner_aim_forward_15down\npb_standMG42gunner_aim_15right_15down\npb_standMG42gunner_aim_30right_15down\npb_standMG42gunner_aim_45right_15down\npb_standMG42gunner_aim_45left_level\npb_standMG42gunner_aim_30left_level\npb_standMG42gunner_aim_15left_level\npb_standMG42gunner_aim_forward_level\npb_standMG42gunner_aim_15right_level\npb_standMG42gunner_aim_30right_level\npb_standMG42gunner_aim_45right_level\npb_standMG42gunner_aim_45left_15up\npb_standMG42gunner_aim_30left_15up\npb_standMG42gunner_aim_15left_15up\npb_standMG42gunner_aim_forward_15up\npb_standMG42gunner_aim_15right_15up\npb_standMG42gunner_aim_30right_15up\npb_standMG42gunner_aim_45right_15up\npb_explosion_death_B1\npb_explosion_death_B2\npb_explosion_death_B3\npb_explosion_death_F1\npb_explosion_death_L1\npb_explosion_death_L2\npb_explosion_death_R1\npb_explosion_rundeath_B1\npb_explosion_rundeath_B2\npb_explosion_rundeath_F1\npb_explosion_rundeath_F2\npb_explosion_rundeath_F3\npb_explosion_rundeath_L1\npb_explosion_rundeath_R1\npb_shotgun_death_back1\npb_shotgun_death_back2\npb_shotgun_death_legs\npb_shotgun_death_spinL\npb_shotgun_death_spinR\npb_shotgun_death_front\npb_explosive_round_death_leg\npb_explosive_round_death_jaw\npb_explosive_round_death_chestB\npb_explosive_round_death_chestA\npb_prone_death_quickdeath\npb_crouch_death_headshot_front\npb_crouch_death_clutchchest\npb_crouch_death_flip\npb_crouch_death_fetal\npb_crouch_death_falltohands\npb_crouchrun_death_drop\npb_crouchrun_death_crumple\npb_stand_death_spin\npb_stand_death_legs\npb_stand_death_lowerback\npb_stand_death_lowertorso\npb_stand_death_head_collapse\npb_stand_death_neckdeath_thrash\npb_stand_death_neckdeath\npb_stand_death_nervedeath\npb_stand_death_frontspin\npb_stand_death_headchest_topple\npb_stand_death_chest_blowback\npb_stand_death_chest_spin\npb_stand_death_shoulder_stumble\npb_stand_death_head_straight_back\npb_stand_death_tumbleback\npb_stand_death_kickup\npb_stand_death_stumbleforward\npb_stand_death_leg\npb_stand_death_leg_kickup\npb_stand_death_headshot_slowfall\npb_stand_death_shoulderback\npb_death_run_forward_crumple\npb_death_run_onfront\npb_death_run_stumble\npb_death_run_back\npb_death_run_left\npb_death_run_right\nMP_shotgun_death_back\nMP_shotgun_death_front\nMP_shotgun_death_left\nMP_shotgun_death_right\npb_stumble_forward\npb_stumble_back\npb_stumble_left\npb_stumble_right\npb_stumble_walk_forward\npb_stumble_walk_back\npb_stumble_walk_left\npb_stumble_walk_right\npb_stumble_pistol_walk_right\npb_stumble_pistol_walk_left\npb_stumble_pistol_walk_forward\npb_stumble_pistol_walk_back\npb_stumble_pistol_right\npb_stumble_pistol_left\npb_stumble_pistol_forward\npb_stumble_pistol_back\npb_stumble_grenade_right\npb_stumble_grenade_left\npb_stumble_grenade_forward\npb_stumble_grenade_back\npb_dive_right\npb_dive_right_impact\npb_dive_left\npb_dive_left_impact\npb_dive_back\npb_dive_back_impact\npb_dive_front\npb_dive_front_impact\npb_prone_painA_holdchest\npb_prone_painB_holdhead\npb_crouch_pain_holdStomach"""

animarray = anims.splitlines()


ct = Label(window, text = "Show dumped", bg="#19181a", fg="white")
ct.pack()
ct.place(x=855, y=27-10)

showdumped = StringVar()

dsearchbar = Entry(window, width=29, bg="#2a282b", fg="white", relief="flat")
dsearchbar.insert(0, "Search Dumped...")
dsearchbar.pack()
dsearchbar.place(x = 644, y = 316-10)
dsearchbar.bind("<FocusIn>", dump_temp_text)
dsearchbar.config(highlightthickness=1, highlightbackground="#322f33")


#Dump List
dumplist = Listbox(window, width=50, height=18, bg="#2a282b", fg="white", bd=0, selectmode = 'SINGLE', exportselection=False, relief = "flat")
dumplist.pack(fill="both", expand=True)
dumplist.place(x = 644, y = 347-10)
dupdate(dumparray)
dumplist.bind("<<ListboxSelect>>", lambda event, arg = dumplist.get(ACTIVE): getxdirs(event, arg))
dumplist.config(highlightthickness=3, highlightbackground="#322f33")


c = Checkbutton(window, text="", variable = showdumped, bg="#19181a", onvalue = "On", offvalue = "Off", command = get_zdir, cursor="center_ptr")
c.deselect()
c.pack()
c.place(x=831, y=25-10)


zsearchbar = Entry(window, width=29, bg="#2a282b", fg="white", relief = "flat")
zsearchbar.insert(0, "Search Zones...")
zsearchbar.pack()
zsearchbar.place(x = 645, y = 28-10)
zsearchbar.bind("<FocusIn>", zone_temp_text)
zsearchbar.config(highlightthickness=1, highlightbackground="#322f33")


#Zones List
zonelist = Listbox(window, width=50, height=15, bg="#2a282b", fg="white", bd=0, selectmode = 'SINGLE', borderwidth=0)
zonelist.pack(fill="both", expand=True)
zonelist.place(x = 645, y = 59-10)
zupdate(zonearray)
zonelist.bind("<<ListboxSelect>>", zonedump_threaded)
zonelist.config(highlightthickness=3, highlightbackground="#322f33")

#zonelist.bind('<ButtonPress-1>', deselect_item)


searchbar = Entry(window, width=50, bg="#2a282b", fg="white", relief = "flat")
searchbar.insert(0, "Search Animations...")
searchbar.pack()
searchbar.place(x = 320, y = 28-10)
searchbar.bind("<FocusIn>", temp_text)
searchbar.config(highlightthickness=1, highlightbackground="#322f33")

#Anims List
animlist = Listbox(window, width=50, height=36, bg="#2a282b", fg="white", bd=0, selectmode = 'SINGLE', relief = "flat")
animlist.pack(fill="both", expand=True)
animlist.place(x = 320, y = 59-10)
animlist.config(highlightthickness=3, highlightbackground="#322f33")
update(animarray)



xa_searchbar = Entry(window, width=50, bg="#2a282b", fg="white", relief = "flat")
xa_searchbar.insert(0, "Search XAnims...")
xa_searchbar.pack()
xa_searchbar.place(x = 968, y = 313-10)
xa_searchbar.config(highlightthickness=1, highlightbackground="#322f33")

#XAnims List
xa_list = Listbox(window, width=50, height=18, bg="#2a282b", fg="white", bd=0, selectmode = 'SINGLE', exportselection=False)
xa_list.place(x = 968, y = 346-10)
xa_list.config(highlightthickness=3, highlightbackground="#322f33")

xa_update(xa_arr)
xa_searchbar.bind("<KeyRelease>", xa_check)


xa_searchbar.bind("<FocusIn>", xa_temp_text)



xm_searchbar = Entry(window, width=50, bg="#2a282b", fg="white", relief = "flat")
xm_searchbar.insert(0, "Search XModels...")
xm_searchbar.pack()
xm_searchbar.place(x = 968, y = 28-10)
xm_searchbar.config(highlightthickness=1, highlightbackground="#322f33")

#XModels List
xm_list = Listbox(window, width=50, height=15, bg="#2a282b", fg="white", bd=0, selectmode = 'SINGLE', exportselection=False)
xm_list.place(x = 968, y = 59-10)
xm_list.config(highlightthickness=3, highlightbackground="#322f33")

xm_update(xm_arr)
xm_searchbar.bind("<KeyRelease>", xm_check)

xm_searchbar.bind("<FocusIn>", xm_temp_text)


#Add to output
animlist.bind("<<ListboxSelect>>", insertanim)

xa_list.bind("<<ListboxSelect>>", insertxanim)
xm_list.bind("<<ListboxSelect>>", insertxmodel)

#Search binding
searchbar.bind("<KeyRelease>", check)
zsearchbar.bind("<KeyRelease>", zone_check)
dsearchbar.bind("<KeyRelease>", dump_check)


##################################################################### TEXT #####################################################################
text = Text(window, bg="#2a282b", fg="white", padx=20, pady=20, width=30, relief = "flat")
text.place(anchor="nw", x = 20, y = 28-10)
text.config(highlightthickness=1, highlightbackground="#322f33")

userdir = Text(window, bg="#2a282b", fg="white", padx=20, pady=20, width=30, height = 5, relief = "flat")
userdir.place(anchor="nw", x = 20, y = 487-10)
userdir.config(highlightthickness=1, highlightbackground="#322f33")

output = Text(window, bg="#2a282b", fg="white", padx=20, pady=20)
output.pack()
output.place(x=width, y=height)

modcsv = Text(window, bg="#2a282b", fg="white", padx=20, pady=20, width=30, height=22, relief = "flat")
modcsv.place(anchor="nw", x = 1290, y = 28-10)
modcsv.config(highlightthickness=1, highlightbackground="#322f33")


ld = []
load_dumps = Listbox(window, width=47, height=6, bg="#2a282b", fg="white", bd=0, selectmode = 'SINGLE')
load_dumps.pack(fill="both", expand=True)
load_dumps.place( x = 1289, y = 528)
load_dumps.config(highlightthickness=3, highlightbackground="#322f33")



##################################################################### BUTTONS #####################################################################
process_button = customtkinter.CTkButton(window, text="Precache", command=process, width = 130, height = 10, corner_radius = 10)
process_button.pack(side=RIGHT)
process_button.place(x=25, y=461-10)



clear_button =  customtkinter.CTkButton(window, text="Clear Cache", command=clear, width = 130, height = 10, corner_radius = 10)
clear_button.pack(side=RIGHT)
clear_button.place(x=165, y=461-10)



dir_button = customtkinter.CTkButton(window, text="Select MW2 File Directory", command=setdir, width = 281, height = 10, corner_radius = 10)
dir_button.pack(side=RIGHT)
dir_button.place(x=20, y=618-10)

displace = 3
processmodcsv_button = customtkinter.CTkButton(window, text="Load", command=processmodcsv, width = 138, height = 10, corner_radius = 10)
processmodcsv_button.pack(side=RIGHT)
processmodcsv_button.place(x=1290, y=455-10 + displace)

addtoprecache_button = customtkinter.CTkButton(window, text="Migrate", command=addtoprecache, width = 138, height = 10, corner_radius = 10)
addtoprecache_button.pack(side=RIGHT)
addtoprecache_button.place(x=1435, y=455-10+ displace)

clearsp_button = customtkinter.CTkButton(window, text="Clear SP", command=clearsp, width = 284, height = 10, corner_radius = 10)
clearsp_button.pack(side=RIGHT)
clearsp_button.place(x=1290, y=429-10+ displace)

gamedir = userdir.get(1.0, END)

run_button = customtkinter.CTkButton(window, text="IW4X Zone Builder", command = zonebuild_threaded, width = 138, height = 10, corner_radius = 10)
run_button.pack(side=RIGHT)
run_button.place(x=1290, y=481-10+ displace)


runm_button = customtkinter.CTkButton(window, text="IW4M Zone Builder", command = zonebuildm_threaded, width = 138, height = 10, corner_radius = 10)
runm_button.pack(side=RIGHT)
runm_button.place(x=1435, y=481-10+ displace) 

mod_button = customtkinter.CTkButton(window, text="Move Mod",command = migratemod , width = 284, height = 10, corner_radius = 10)
mod_button.pack(side=RIGHT)
mod_button.place(x=1290, y=481-10 + (481-455)+ displace)

refresh = customtkinter.CTkButton(window, text="Refresh", command=get_ddir, width = 120, height = 10, corner_radius = 10)
refresh.pack(side=RIGHT)
refresh.place(x=829, y=316-10)


window.mainloop()
