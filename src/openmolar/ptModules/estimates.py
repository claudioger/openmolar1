# -*- coding: utf-8 -*-
# Copyright (c) 2009 Neil Wallace. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. See the GNU General Public License
# for more details.

from __future__ import division
import copy
import re
import sys

from openmolar.settings import localsettings,fee_keys
from openmolar.ptModules import plan

import struct

class est():
    '''
    this class has attributes suitable for storing in the estimates table
    '''
    def __init__(self):
        self.ix=None
        self.serialno=None
        self.courseno=None
        self.type=""
        self.number=None
        self.itemcode="4001"
        self.description=None
        self.fee=None
        self.ptfee=None
        self.feescale=None
        self.csetype=None
        self.dent=None
        self.completed=None
        self.carriedover=None
        self.linked=False
    
    def __repr__(self):
        retarg="("
        for att in self.__dict__:
            retarg+="%s ,"%self.__dict__[att]
        return retarg+")"

    def __str__(self):
        retarg="("
        for att in ("ix","serialno","courseno","number","fee","ptfee","dent"):
            retarg+='%s ,'%self.__dict__[att]
        for att in ("type","itemcode","description","csetype","feescale"):
            retarg+='"%s" ,'%self.__dict__[att]
        for att in ("completed","carriedover"):
            retarg+="%s ,"%self.__dict__[att]
        return "%s)"%retarg.strip(",")

    def toHtmlRow(self):
        return '''<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td>
        <td>%s</td><td>&pound;%.02f</td><td>&pound;%.02f</td>
        <td>%s</td><td>%s</td><td>%s</td></tr>'''%(
        localsettings.ops.get(self.dent),self.number,self.itemcode,self.type,
        self.description,self.fee/100,self.ptfee/100,self.feescale,
        self.csetype,self.completed)
    def htmlHeader(self):
        return '''<tr><th>Dentist</th><th>number</th><th>code</th>
        <th>input</th><th>Description</th><th>fee</th><th>pt fee</th>
        <th>feescale</th><th>cset</th><th>completed</th></tr>'''
        
    def filteredDescription(self):
        '''
        removes {1 of 3} from the description
        '''
        retarg = copy.copy(self.description)
        gunks = re.findall(" {.*}", retarg)        
        for gunk in gunks:
            retarg = retarg.replace(gunk, "") 
        return retarg
    
    
def sorted(ests):
    '''
    compresses a list of estimates down into number*itemcode
    '''
    def cmp1(a,b): 
        'define how ests are sorted'
        return cmp(a.itemcode,b.itemcode)

    sortedEsts=[]
    def estInSortedEsts(est):
        for se in sortedEsts:
            if se.itemcode==est.itemcode and se.description==est.description:
                #--don't combine "custom items (where description has changed)"
                if est.number!=None and se.number!=None:
                    se.number +=est.number
                se.fee+=est.fee
                se.ptfee+=est.ptfee
                se.type+="|"+est.type
                return True
    for est in ests:
        if not estInSortedEsts(est):
            ce=copy.copy(est)
            sortedEsts.append(ce)
    sortedEsts.sort(cmp1)
    
    return sortedEsts
    
def toothTreatDict(pt):
    '''
    cycles through the patient attriubutes,
    and brings up planned / completed treatment on teeth only
    '''
    treats={"pl":[], "cmp":[]}
    for quadrant in ("ur","ul", "ll", "lr"):
        if "r" in quadrant:
            order=(8, 7, 6, 5, 4, 3, 2, 1)
        else:
            order=(1, 2, 3, 4, 5, 6, 7, 8)
        for tooth in order:
            for type in ("pl", "cmp"):
                att="%s%s%s"%(quadrant, tooth,type)
                if pt.__dict__[att] != "":
                    items=pt.__dict__[att].strip(" ").split(" ")
                    for item in items:
                        treats[type].append(("%s%s"%(quadrant, tooth), item), )
    #print "toothTreatDict"
    #print "returning ",treats
    return treats

def abandon_estimate(pt):
    pt.ests=()

def recalculate_estimate(pt):
    #########################needs wordk
    
    planned=plan.plannedDict(pt)
    completed=plan.completedDict(pt)
    if pt.dnt2!=0:
        dent=pt.dnt2
    else:
        dent=pt.dnt1
    for key in planned.keys():
        print key,planned[key]
    for key in completed.keys():
        print key,completed[key]
        
    return
    for treat in chosen:
        #-- treat[0]= the tooth name
        #-- treat[1] = item code
        #-- treat[2]= description
        #-- treat[3]= adjusted fee
        #-- treat[4]=adjusted ptfee
        
        pt.addToEstimate(1, treat[1], treat[2], treat[3], treat[4],
                               dent, self.pt.cset, treat[0])


def toBriefHtml(pt):
    '''
    returns an HTML table showing the estimate in a receptionist friendly format
    '''
    retarg = '<html><body>'
    if pt.underTreatment:
        retarg += "<h1>Current Estimate</h1>"
    else:
        retarg += "<h1>Estimate from previous course</h1>"
        
    if not pt.estimates:
        retarg += 'No estimate data found</body></html>'
        return retarg
    
    retarg +='''<table width ="100%" border="1">
    <tr><td colspan="7"><h3>ESTIMATE</h3></td></tr>
    <tr><th>No.</th><th>Description</th><th>Type</th><th>Course</th>
    <th>Fee</th><th>Pt Fee</th><th>Completed</th></tr>'''
    total=0
    pt_total=0
    for est in sorted(pt.estimates):
        total+=est.fee
        pt_total+=est.ptfee
        retarg+='<tr><td>%s</td><td>%s</td>'%(est.number,est.description)
        retarg+='<td align="center">%s</td>'%est.type
        if est.csetype==None:
            retarg+='<td align="center">?</td>'
        else:
            retarg+='<td align="center">%s</td>'%est.csetype
        retarg+='<td align="right">&pound;%.02f</td>'%(est.fee/100)
        retarg+='<td align="right"><b>&pound;%.02f</b></td>'%(est.ptfee/100)
        retarg+='<td align="center">'
        if est.completed:
            retarg+='YES'
        else:
            retarg+='NO'
        retarg+="</td></tr>"

    retarg+='<tr><td colspan="4"></td>'
    retarg+='<td align="right">&pound;%.02f</td>'%(total/100)
    retarg+='<td align="right"><b>&pound;%.02f</b></td>'%(pt_total/100)
    retarg+='<td></td></tr>'

    retarg+='</table></body></htsml>'

    return retarg

if __name__ == "__main__":
    from openmolar.dbtools import patient_class
    localsettings.initiate(False)
    try:
        serialno=int(sys.argv[len(sys.argv)-1])
    except:
        serialno=29833

    pt=patient_class.patient(serialno)
    #print pt.estimates
    #print toHtml(pt.estimates,pt.tsfees)

    print toBriefHtml(pt.estimates)
    
    recalculate_estimate(pt)