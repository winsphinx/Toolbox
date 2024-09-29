#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pywebio.output import put_button, put_file, put_loading, put_markdown, put_scope, put_text, use_scope
from pywebio.pin import pin, put_input


class ADDIMS:
    def __init__(self):
        put_markdown("# 手工IMS加号码脚本生成器")
        put_input(
            "telno",
            label="号码",
            placeholder="88881234",
            help_text="8位号码。",
        )
        put_input(
            "passwd",
            label="密码",
            placeholder="Fxxxxx",
            help_text="SIP的注册密码，在工单上有。",
        )
        put_input(
            "port",
            label="端口",
            placeholder="0/1/2",
            help_text="GPON的端口号，在工单上有。",
        )
        put_button(
            label="点击生成脚本",
            onclick=self.update,
        )
        put_markdown("----")
        put_scope("output")

    @use_scope("output", clear=True)
    def update(self):
        with put_loading():
            put_text("开始生成脚本...")
            telno = pin["telno"].strip()
            passwd = pin["passwd"].strip()
            port = pin["port"].strip()

            TXT = f"""
*****************
****   HSS   ****
*****************
ADD NEWPVI:PVITYPE=0,PVI=+86575{telno}@zj.ims.chinaunicom.cn,IREGFLAG=1,IDENTITYTYPE=0,PECFN=ccf01.zj.ims.chinaunicom.cn,SECFN=ccf02.zj.ims.chinaunicom.cn,PCCFN=ccf01.zj.ims.chinaunicom.cn,SCCFN=ccf02.zj.ims.chinaunicom.cn,SecVer=30,UserName=+86575{telno}@zj.ims.chinaunicom.cn,PassWord={passwd},Realm=zj.ims.chinaunicom.cn,ACCTypeList=*,ACCInfoList=*,ACCValueList=*;
ADD NEWPUI:IDENTITYTYPE=0,PUI=tel:+86575{telno},BARFLAG=0,REGAUTHFG=1,ROAMSCHEMEID=1,SPID=8,SPDesc=绍兴SP,PVIList=+86575{telno}@zj.ims.chinaunicom.cn,CapsIDList=575,CapsTypeList=0,LOOSEROUTEIND=0;
ADD NEWPUI:IDENTITYTYPE=0,PUI=sip:+86575{telno}@zj.ims.chinaunicom.cn,BARFLAG=0,REGAUTHFG=1,ROAMSCHEMEID=1,SPID=8,SPDesc=绍兴SP,PVIList=+86575{telno}@zj.ims.chinaunicom.cn,CapsIDList=575,CapsTypeList=0,LOOSEROUTEIND=0;
MOD PUIINFO:PUI=tel:+86575{telno},LOCALINFO=,LOOSEROUTEIND=0,DISPLAYNAME=*,MAXSESS=0,PHONECONTEXT=,MAXSIMULTREGS=0,SIFCIDList=5030$5600$5910,NATEMPLATEID=0;
MOD PUIINFO:PUI=sip:+86575{telno}@zj.ims.chinaunicom.cn,LOCALINFO=,LOOSEROUTEIND=0,DISPLAYNAME=*,MAXSESS=0,PHONECONTEXT=,MAXSIMULTREGS=0,SIFCIDList=5030$5600$5910,NATEMPLATEID=0;
SET IMPREGSET:PUIList=sip:+86575{telno}@zj.ims.chinaunicom.cn$tel:+86575{telno},DefaultPUI=sip:+86575{telno}@zj.ims.chinaunicom.cn;
SET ALIASEGROUP:PUIList=sip:+86575{telno}@zj.ims.chinaunicom.cn$tel:+86575{telno},AliasGroupID=+86575{telno}@zj.ims.chinaunicom.cn;


*****************
****   SLF   ****
*****************
ADD SLFUSER:USERIDTYPE=1,USERID=tel:+86575{telno},HSSID=1;
ADD SLFUSER:USERIDTYPE=1,USERID=sip:+86575{telno}@zj.ims.chinaunicom.cn,HSSID=1;


*****************
****   SSS   ****
*****************
ADD OSU SBR:PUI="tel:+86575{telno}",NETTYPE=1,CC=86,LATA=575,TYPE="IMS",ONLCHG="OFF",OFFLCHG="ON",NOTOPEN="OFF",OWE="OFF",TSS="TSS_OFF",IRCFS="ON",IRACFSC="OFF",NSOUTG="OFF",NSICO="OFF",CARDUSER="OFF",FORCEOL="OFF",OVLAP="OFF",CFFT="OFF",CORHT="LC"&"DDD"&"SPCS"&"HF"&"LT",CIRHT="LC"&"DDD"&"IDD"&"SPCS"&"HF"&"HKMACAOTW"&"LT",OWECIRHT="LC"&"DDD"&"IDD"&"SPCS"&"HF"&"HKMACAOTW"&"LT",CTXOUTRHT="GRPIN"&"GRPOUT"&"GRPOUTNUM",CTXINRHT="GRPIN"&"GRPOUT"&"GRPOUTNUM",OWECTXOUTRHT="GRPIN"&"GRPOUT"&"GRPOUTNUM",OWECTXINRHT="GRPIN"&"GRPOUT"&"GRPOUTNUM",ACOFAD="57501",COMCODE=0,CUSTYPE="B2C",LANGTYPE=0,SPELINE="NO",CALLERAS=0,CALLEDAS=0,CHARGCATEGORY="FREE",CPC=0,PREPAIDTYPE="0",MAXCOMNUM=1,MEDIACAPNO=0,ZONEINDEX=65535,IMSUSERTYPE="NMIMS",OUTGOINGBLACK="NO",NOANSWERTIMER=0,OPSMSININDEX=0;
SET OSU OIP:PUI="tel:+86575{telno}";


*****************
****   SDC   ****
*****************
MOD USR:MODE=BYDN,DN="{telno}",NEWLRN="116448{telno}",INCALLINGPREFIX=IN_1-0, INCALLEDPREFIX=IN_1-0;


*****************
****   EDS   ****
*****************
优先级：10
次优先级：100
标识：URI
名称：E2U+SIP
正则表达式：!^.*$!sip:+86575{telno}@zj.ims.chinaunicom.cn!
周期：3600000


*****************
****   PON   ****
*****************
esl user
sippstnuser add {port} 0 telno 86575{telno}
sippstnuser auth set {port} telno 86575{telno} password-mode password
+86575{telno}@zj.ims.chinaunicom.cn
{passwd} <- 密码
"""

            content = ""
            content += TXT

        put_text(content)
        put_file(f"{telno}.txt", content.encode(), ">> 点击下载脚本 <<")


if __name__ == "__main__":
    ADDIMS()
