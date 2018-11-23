# -*- coding: utf-8 -*-

"""!
For Maya2017- Maya Custom UV Editor V 2.2
              - Using workspaceControl dockToControl menu Top
              - Add Absolute Value Tools on Top
              - Add interactive mode with 2 Scriptjobs
              - Add Show Editting UVSet name
@file
@author Ritaro

"""

import maya.cmds as cmds
import maya.mel as mel
import sys

#*---  Absolute Value Tools --- *



def get_uv(*args):
    mel.eval('ConvertSelectionToUVs;')
    gs_selected = cmds.ls( hilite=True )
    if gs_selected == []:
        print "Nothing is Selected"
        sys.exit()

    seleced_uv = cmds.ls(sl=True,flatten=True)

    uv_list = []
    for sel_uv in seleced_uv:
        if ".map" not in sel_uv:
            s_uv = cmds.polyListComponentConversion(sel_uv,
                fromVertex=True,fromEdge=True,fromFace=True,fromVertexFace=True,
                toUV=True)[0]

            if ":" in s_uv:
                s_uv = (s_uv[:s_uv.index(':')]) + "]"

            if s_uv not in uv_list:
                uv_list.append(s_uv)
        if sel_uv not in uv_list:
            uv_list.append(sel_uv)

    if uv_list == []:
        print "No UV is Selected"
        sys.exit()

    seleced_uv_val = cmds.polyEditUV(uv_list[0],query=True)
#    print seleced_uv_val

    cmds.floatFieldGrp('u_number',e=True,precision=4,value1=seleced_uv_val[0])
    cmds.floatFieldGrp('v_number',e=True,precision=4,value1=seleced_uv_val[1])

    try:
        o_c_uvset = cmds.polyUVSet( query=True, currentUVSet=True )[0]
        cmds.text('c_uv',label=o_c_uvset,e=True)
    except:
        cmds.text('c_uv',label="",e=True)

def set_uv(*args):
    set_u = cmds.floatFieldGrp('u_number',q=True,value1=True)
    set_v = cmds.floatFieldGrp('v_number',q=True,value1=True)

    mel.eval('ConvertSelectionToUVs;')
    seleced_uv = cmds.ls(sl=True,flatten=True)
    for sel_uv in seleced_uv:
        cmds.polyEditUV(sel_uv, relative=False,uValue=set_u,vValue=set_v)

    try:
        o_c_uvset = cmds.polyUVSet( query=True, currentUVSet=True )[0]
        cmds.text('c_uv',label=o_c_uvset,e=True)
    except:
        cmds.text('c_uv',label="",e=True)

def set_u_only(*args):
    set_u = cmds.floatFieldGrp('u_number',q=True,value1=True)

    mel.eval('ConvertSelectionToUVs;')
    seleced_uv = cmds.ls(sl=True,flatten=True)
    for sel_uv in seleced_uv:
        cmds.polyEditUV(sel_uv, relative=False,uValue=set_u)

def set_v_only(*args):
    set_v = cmds.floatFieldGrp('v_number',q=True,value1=True)

    mel.eval('ConvertSelectionToUVs;')
    seleced_uv = cmds.ls(sl=True,flatten=True)
    for sel_uv in seleced_uv:
        cmds.polyEditUV(sel_uv, relative=False,vValue=set_v)

def set_as_group(*args):
    set_u = cmds.floatFieldGrp('u_number',q=True,value1=True)
    set_v = cmds.floatFieldGrp('v_number',q=True,value1=True)

    mel.eval('ConvertSelectionToUVs;')
    seleced_uv = cmds.ls(sl=True,flatten=True)

    count = 0
    for sel_uv in seleced_uv:
        if count == 0:
            master_uv_val = cmds.polyEditUV(sel_uv,query=True)
            cmds.polyEditUV(sel_uv, relative=False,uValue=set_u,vValue=set_v)
            count = 1
        elif count == 1:
            other_uv_val = cmds.polyEditUV(sel_uv,query=True)
            dif_uv_val = [other_uv_val[0] - master_uv_val[0],other_uv_val[1] - master_uv_val[1]]
            cmds.polyEditUV(sel_uv, relative=False,uValue=(set_u + dif_uv_val[0]),vValue=(set_v + dif_uv_val[1]))

def set_as_group_u_only(*args):
    set_u = cmds.floatFieldGrp('u_number',q=True,value1=True)

    mel.eval('ConvertSelectionToUVs;')
    seleced_uv = cmds.ls(sl=True,flatten=True)

    count = 0
    for sel_uv in seleced_uv:
        if count == 0:
            master_uv_val = cmds.polyEditUV(sel_uv,query=True)
            cmds.polyEditUV(sel_uv, relative=False,uValue=set_u)
            count = 1
        elif count == 1:
            other_uv_val = cmds.polyEditUV(sel_uv,query=True)
            dif_uv_val = [other_uv_val[0] - master_uv_val[0]]
            cmds.polyEditUV(sel_uv, relative=False,uValue=(set_u + dif_uv_val[0]))

def set_as_group_v_only(*args):
    set_v = cmds.floatFieldGrp('v_number',q=True,value1=True)

    mel.eval('ConvertSelectionToUVs;')
    seleced_uv = cmds.ls(sl=True,flatten=True)

    count = 0
    for sel_uv in seleced_uv:
        if count == 0:
            master_uv_val = cmds.polyEditUV(sel_uv,query=True)
            cmds.polyEditUV(sel_uv, relative=False,vValue=set_v)
            count = 1
        elif count == 1:
            other_uv_val = cmds.polyEditUV(sel_uv,query=True)
            dif_uv_val = [other_uv_val[1] - master_uv_val[1]]
            cmds.polyEditUV(sel_uv, relative=False,vValue=(set_v + dif_uv_val[0]))

def sel_changed(*args):
    print "Selected Object has Changed !!!"

    cmds.checkBoxGrp('intract_check',e=True,v1=False)
    if cmds.scriptJob(exists = jobNum_b):
        cmds.scriptJob(kill = int(jobNum_b), force=True)

def interactive_on(*arge):
    global jobNum_b
    
    jobs = cmds.scriptJob( listJobs=True )
    for o_job in jobs:
        if "Custom_UV_Editor" in o_job:
            jobNum = (o_job[:o_job.index(':')])
            cmds.scriptJob( kill=int(jobNum), force=True)

    mel.eval('ConvertSelectionToUVs;')
    seleced_uv = cmds.ls(sl=True,flatten=True)

    if seleced_uv == []:
        cmds.checkBoxGrp('intract_check',e=True,v1=False)
        print "No UV is Selected"
        sys.exit()

    o_obj_name = (seleced_uv[0][:seleced_uv[0].index('.')])
    o_obj_shape_uv_pivot = cmds.listRelatives(o_obj_name,shapes=True)[0] + ".uvPivot"

    if cmds.checkBoxGrp('intract_check',q=True,v1=True):
        jobNum_a = cmds.scriptJob(event = ["DragRelease",sel_changed],
            protected=False,killWithScene=True,parent="Custom_UV_Editor")
#        print jobNum_a
        jobNum_b = cmds.scriptJob(attributeChange = [o_obj_shape_uv_pivot,get_uv],
            protected=False,killWithScene=True,parent="Custom_UV_Editor")
#        print jobNum_b
    else:
        jobs = cmds.scriptJob( listJobs=True )
        for o_job in jobs:
            if "Custom_UV_Editor" in o_job:
                jobNum = (o_job[:o_job.index(':')])
                cmds.scriptJob( kill=int(jobNum), force=True)


def custom_uv_editor_menu(*args):
    try:
        o_c_uvset = cmds.polyUVSet( query=True, currentUVSet=True )[0]
    except:
        o_c_uvset = ""
    cmds.columnLayout(columnAttach=('both', 5), height=40,
        rowSpacing=4, columnWidth=10, adjustableColumn=True)
    cmds.text(label='Custom UV Editor V 2.2',width=220,bgc=[0.2,0.2,0.2],align='center',height=10)
    cmds.rowLayout(numberOfColumns=20,adjustableColumn=20)
    cmds.text(label='',width=2)
    cmds.text(label='Current UV Set ; ',width=100)
    cmds.text('c_uv',label=o_c_uvset,width=90,font="boldLabelFont")
    cmds.checkBoxGrp('intract_check',columnWidth2=[120, 40],numberOfCheckBoxes=1,
        label='Interactive >', v1=False,changeCommand1=interactive_on)
    cmds.floatFieldGrp('u_number',label='U',precision=4,value1=0.00,columnWidth2=[10,80])
    cmds.floatFieldGrp('v_number',label='v',precision=4,value1=0.00,columnWidth2=[10,80])
    cmds.button('get_uv',label='GET',width=30,command=get_uv)
    cmds.text(label='',width=5)
    cmds.button('set_uv',label='SET',width=30,command=set_uv)
    cmds.text(label='',width=10)
    cmds.button('set_u',label='Set U only',bgc=[0.4,0.2,0.2],width=70,command=set_u_only)
    cmds.text(label='',width=5)  
    cmds.button('set_v',label='Set V only',bgc=[0.2,0.4,0.2],width=70,command=set_v_only)
    cmds.text(label='',width=18)
    cmds.button('set_as_group',label='Set as Group',bgc=[0.3,0.3,0.2],width=85,command=set_as_group)
    cmds.text(label='',width=10)
    cmds.button('set_as_group_u',label='SetGroup U only',bgc=[0.4,0.2,0.2],width=98,command=set_as_group_u_only)
    cmds.text(label='',width=5)  
    cmds.button('set_as_group_v',label='SetGroup V only',bgc=[0.2,0.4,0.2],width=97,command=set_as_group_v_only)
    cmds.text(label='',width=8)

def custom_uv_editor(*args):

    mel.eval('refresh;')

    if cmds.workspaceControlState("Custom_UV_Editor",q=True,exists=True):
        cmds.workspaceControlState("Custom_UV_Editor",e=True,remove=True)

    if cmds.workspaceControl("UVToolkitDockControl",q=True,exists=True):
        if cmds.workspaceControlState("UVToolkitDockControl",q=True,exists=True):
            cmds.workspaceControlState("UVToolkitDockControl",e=True,remove=True)

    if cmds.window('Custom_UV_Editor',exists=True):
        cmds.deleteUI('Custom_UV_Editor')

    mel.eval('string $textureEditorTitle = localizedPanelLabel("UV Editor" );')
    mel.eval('tearOffRestorePanel $textureEditorTitle polyTexturePlacementPanel true;')
    uvTextureViews = cmds.getPanel(scriptType='polyTexturePlacementPanel')[0]
    texWinName = uvTextureViews + "Window"

    if cmds.workspaceControl(texWinName ,q=True,exists=True):
        cmds.workspaceControl(texWinName ,e=True,checksPlugins=True)

    if not cmds.workspaceControl("Custom_UV_Editor",q=True,exists=True):
        cmds.workspaceControl("Custom_UV_Editor",retain=False,initialWidth=120,initialHeight=45,width=120,height=40,
            dockToControl=[texWinName,'top'],
            widthProperty="fixed",uiScript="custom_uv_editor_menu()")
    elif not cmds.workspaceControl("Custom_UV_Editor",q=True,visible=True):
        cmds.workspaceControl("Custom_UV_Editor",e=True,visible=True)
        mel.eval('refresh;')
        cmds.workspaceControl("Custom_UV_Editor",retain=False,initialWidth=120,initialHeight=45,width=120,height=40,
            dockToControl=[texWinName,'top'],
            widthProperty="fixed",uiScript="custom_uv_editor_menu()")

    if not cmds.workspaceControl("UVToolkitDockControl",q=True,exists=True):
        mel.eval('UVToolkitPanel();')
        cmds.workspaceControl("UVToolkitDockControl",e=True,dockToControl=[texWinName,'right'])
    elif not cmds.workspaceControl("UVToolkitDockControl",q=True,visible=True):
        cmds.workspaceControl("UVToolkitDockControl",e=True,visible=True)
        mel.eval('refresh;')
        cmds.workspaceControl("UVToolkitDockControl",e=True,dockToControl=[texWinName,'right'])
