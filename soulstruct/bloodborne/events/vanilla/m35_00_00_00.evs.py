"""
linked:
180

strings:
0: ボス撃破_女性ハンター
24: PC情報_ボス撃破_女性ハンター
58: ボス_戦闘開始
74: ボス_撃破時間
90: ボス撃破_患者B
108: PC情報_ボス撃破_患者B
136: ボス戦闘開始_患者B
158: ボス撃破時間_患者B
180: N:\\SPRJ\\data\\Param\\event\\common.emevd
"""
from soulstruct.bloodborne.events import *
from soulstruct.bloodborne.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_13501810()
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    AddSpecialEffect(PLAYER, 9920)
    SkipLinesIfClient(2)
    SkipLinesIfFlagDisabled(1, 13500100)
    EnableFlag(13500101)
    RunEvent(7000, slot=60, args=(3500950, 3501950, 999, 13507800))
    RunEvent(7000, slot=61, args=(3500951, 3501951, 13501850, 13507820))
    RunEvent(7000, slot=62, args=(3500952, 3501952, 13501800, 13507840))
    RunEvent(7100, slot=60, args=(73500200, 3501950))
    RunEvent(7100, slot=61, args=(73500201, 3501951))
    RunEvent(7100, slot=62, args=(73500202, 3501952))
    RunEvent(7200, slot=60, args=(73500100, 3501950, 2102953))
    RunEvent(7200, slot=61, args=(73500101, 3501951, 2102953))
    RunEvent(7200, slot=62, args=(73500102, 3501952, 2102953))
    RunEvent(7300, slot=60, args=(72103500, 3501950))
    RunEvent(7300, slot=61, args=(72103501, 3501951))
    RunEvent(7300, slot=62, args=(72103502, 3501952))
    RunEvent(7600, slot=71, args=(3501990, 3503990))
    DisableMapCollision(collision=3504810)
    DisableMapCollision(collision=3504811)
    DisableMapCollision(collision=3504812)
    SetCollisionResState(collision=3504813, state=False)
    SetCollisionResState(collision=3504814, state=False)
    EnableFlag(3510)
    EnableFlag(3511)
    DisableFlag(3512)
    DisableFlag(3513)
    EnableFlag(3515)
    EnableFlag(3516)
    DisableFlag(3517)
    DisableFlag(3518)
    DisableMapCollision(collision=3504812)
    DisableMapCollision(collision=3504813)
    EnableMapCollision(collision=3504814)
    SkipLinesIfFlagDisabled(11, 9470)
    DisableFlag(3510)
    DisableFlag(3511)
    DisableFlag(3512)
    DisableFlag(3513)
    DisableFlag(3515)
    DisableFlag(3516)
    DisableFlag(3517)
    DisableFlag(3518)
    DisableMapCollision(collision=3504812)
    DisableMapCollision(collision=3504813)
    EnableMapCollision(collision=3504814)
    SkipLinesIfFlagDisabled(11, 13501850)
    EnableFlag(3510)
    EnableFlag(3511)
    EnableFlag(3512)
    DisableFlag(3513)
    DisableFlag(3515)
    DisableFlag(3516)
    EnableFlag(3517)
    DisableFlag(3518)
    EnableMapCollision(collision=3504812)
    DisableMapCollision(collision=3504813)
    DisableMapCollision(collision=3504814)
    SkipLinesIfFlagDisabled(11, 13501801)
    EnableFlag(3510)
    EnableFlag(3511)
    DisableFlag(3512)
    DisableFlag(3513)
    DisableFlag(3515)
    DisableFlag(3516)
    DisableFlag(3517)
    DisableFlag(3518)
    DisableMapCollision(collision=3504812)
    EnableMapCollision(collision=3504813)
    DisableMapCollision(collision=3504814)
    SkipLinesIfFlagDisabled(11, 13501800)
    EnableFlag(3510)
    EnableFlag(3511)
    EnableFlag(3512)
    EnableFlag(3513)
    DisableFlag(3515)
    DisableFlag(3516)
    DisableFlag(3517)
    DisableFlag(3518)
    DisableMapCollision(collision=3504812)
    EnableMapCollision(collision=3504813)
    DisableMapCollision(collision=3504814)
    RegisterLadder(start_climbing_flag=13501300, stop_climbing_flag=13501301, obj=3501080)
    RegisterLadder(start_climbing_flag=13501302, stop_climbing_flag=13501303, obj=3501081)
    RegisterLadder(start_climbing_flag=13501304, stop_climbing_flag=13501305, obj=3501082)
    RegisterLadder(start_climbing_flag=13501306, stop_climbing_flag=13501307, obj=3501083)
    RegisterLadder(start_climbing_flag=13501308, stop_climbing_flag=13501309, obj=3501084)
    Event_13504700(0, character=3500790, flag=13504701, flag_1=13504711, flag_2=3510, flag_3=999)
    Event_13504700(5, character=3500791, flag=13504702, flag_1=12604712, flag_2=3511, flag_3=999)
    Event_13504710(0, character=3500790, flag=13504701, flag_1=13504711, flag_2=13504721)
    Event_13504710(5, character=3500791, flag=13504702, flag_1=13504712, flag_2=13504722)
    Event_13504720(0, character=3500790, flag=13504701, flag_1=13504711, flag_2=13504721)
    Event_13504720(5, character=3500791, flag=13504702, flag_1=13504712, flag_2=13504722)
    Event_13504730(
        0,
        character=3500790,
        flag=13504701,
        flag_1=13504711,
        flag_2=3510,
        flag_3=13504810,
        flag_4=999,
        flag_5=999,
        flag_6=13504712
    )
    Event_13504730(
        5,
        character=3500791,
        flag=13504702,
        flag_1=13504712,
        flag_2=3511,
        flag_3=13504860,
        flag_4=999,
        flag_5=999,
        flag_6=13504711
    )
    Event_13504740()
    Event_13504742()
    Event_13501800()
    Event_13501801()
    Event_13504800()
    Event_13504801()
    Event_13504802()
    Event_13504803()
    Event_13504804()
    Event_13504805()
    Event_13504806()
    Event_13504807()
    Event_13501807()
    Event_13501802()
    Event_13501803()
    Event_13501805(0, obj=3501906)
    Event_13501805(1, obj=3501910)
    Event_13504822()
    Event_13501850()
    Event_13501851()
    Event_13501852()
    Event_13504850()
    Event_13504851()
    Event_13504852()
    Event_13504853()
    Event_13504854()
    Event_13504855()
    Event_13504856()
    Event_13504857()
    Event_13504880()
    Event_13504881()
    Event_13504885(1, character=3500852, flag=13504873)
    Event_13504885(2, character=3500853, flag=13504874)
    Event_13504890(0, character=3500851)
    Event_13504890(1, character=3500852)
    Event_13504890(2, character=3500853)
    Event_13504890(3, character=3500854)
    Event_13504865()
    Event_13505655()
    Event_13505656(0, character=3500851)
    Event_13505656(1, character=3500852)
    Event_13505656(2, character=3500853)
    Event_13505656(3, character=3500854)
    Event_13505661()
    Event_13505662()
    Event_13505680()
    Event_13504895(0, character=3500851)
    Event_13504895(1, character=3500852)
    Event_13504895(2, character=3500853)
    Event_13504895(3, character=3500854)
    Event_13501100()
    Event_13501105()
    Event_13501104()
    Event_13501140()
    Event_13501141()
    Event_13501142()
    SkipLinesIfFlagDisabled(3, 13501108)
    Event_13501101()
    Event_13501102()
    Event_13501103()
    EnableFlag(13501118)
    Event_13501110()
    Event_13501111()
    Event_13501112()
    Event_13501113()
    Event_13501114()
    Event_13501115()
    Event_13501120()
    Event_13501121()
    Event_13501122()
    Event_13501123()
    Event_13501124()
    Event_13501125()
    Event_13501200(0, 3501120, 13504220, 1, 3500020, 0, -1)
    Event_13501200(1, 3501130, 13504230, 1, 3500030, 0, -1)
    Event_13501200(2, 3501141, 13504241, 2, 3500040, 0, -1)
    Event_13501200(3, 3501142, 13504242, 2, 3500040, 0, -1)
    Event_13501200(4, 3501145, 13504245, 2, 3500041, 0, -1)
    Event_13501200(5, 3501146, 13504246, 2, 3500040, 0, -1)
    Event_13501200(6, 3501140, 13504242, 2, 3500040, 0, -1)
    Event_13501200(
        7,
        obj=3501161,
        obj_act_id=13504261,
        animation_id=1,
        obj_act_id_1=3500062,
        obj_act_id_2=13504271,
        obj_act_id_3=3500063
    )
    Event_13501200(
        8,
        obj=3501162,
        obj_act_id=13504262,
        animation_id=1,
        obj_act_id_1=3500062,
        obj_act_id_2=13504272,
        obj_act_id_3=3500063
    )
    Event_13501200(
        9,
        obj=3501163,
        obj_act_id=13504263,
        animation_id=1,
        obj_act_id_1=3500062,
        obj_act_id_2=13504273,
        obj_act_id_3=3500063
    )
    Event_13501200(
        10,
        obj=3501164,
        obj_act_id=13504264,
        animation_id=1,
        obj_act_id_1=3500062,
        obj_act_id_2=13504274,
        obj_act_id_3=3500063
    )
    Event_13501200(
        11,
        obj=3501165,
        obj_act_id=13504265,
        animation_id=1,
        obj_act_id_1=3500062,
        obj_act_id_2=13504275,
        obj_act_id_3=3500063
    )
    Event_13501200(
        12,
        obj=3501166,
        obj_act_id=13504266,
        animation_id=1,
        obj_act_id_1=3500062,
        obj_act_id_2=13504276,
        obj_act_id_3=3500063
    )
    Event_13501200(13, 3501170, 13504270, 1, 3500070, 0, -1)
    Event_13501250()
    Event_13501400(0, obj=3501350, obj_act_id=13500020, obj_act_id_1=9942)
    Event_13501400(1, obj=3501351, obj_act_id=13500021, obj_act_id_1=9942)
    Event_13501400(2, obj=3501352, obj_act_id=13500022, obj_act_id_1=9942)
    Event_13504799()
    Event_13500100()
    Event_13500105()
    Event_13500106()
    Event_13500110()
    Event_13500111()
    Event_13500130()
    Event_13500150()
    Event_13500410(0, character=3500310, character_1=3500339)
    Event_13500410(1, character=3500337, character_1=3500340)
    Event_13500410(2, character=3500351, character_1=3500341)
    Event_13500410(3, character=3500921, character_1=3500923)
    Event_13500410(4, character=3500935, character_1=3500933)
    Event_13500410(5, character=3500661, character_1=3500663)
    Event_13500420(0, entity=3500310, animation_id=9000, frames=40)
    Event_13500420(1, entity=3500337, animation_id=9000, frames=10)
    Event_13500430(0, flag=13500420, character=3500310, animation_id=9060)
    Event_13500430(1, flag=13500421, character=3500337, animation_id=9060)
    Event_13500450(0, character=3500740, flag=53501700)
    Event_13500450(1, character=3500741, flag=53501710)
    Event_13500450(2, character=3500742, flag=53501720)
    Event_13500450(3, character=3500781, flag=53508100)
    Event_13500460(0, character=3500930, animation_id=103170, flag=13501900)
    Event_13500500(0, entity=3501500, action_button_id=3500200, text=10010611)
    Event_13500500(1, entity=3501501, action_button_id=3500200, text=10010611)
    Event_13500500(2, entity=3501502, action_button_id=3500200, text=10010620)
    Event_13500500(3, entity=3501503, action_button_id=3500200, text=10010620)
    Event_13500500(4, entity=3501510, action_button_id=3500200, text=10010616)
    Event_13500500(5, entity=3501511, action_button_id=3500200, text=10010616)
    Event_13500500(6, entity=3501512, action_button_id=3500200, text=10010616)
    Event_13500500(7, entity=3501513, action_button_id=3500200, text=10010616)
    Event_13500500(8, entity=3501514, action_button_id=3500200, text=10010612)
    Event_13500500(9, entity=3501515, action_button_id=3500200, text=10010612)
    Event_13500500(10, entity=3501520, action_button_id=3500200, text=10010617)
    Event_13500500(11, entity=3501521, action_button_id=3500200, text=10010617)
    Event_13500500(12, entity=3501522, action_button_id=3500200, text=10010613)
    Event_13500500(13, entity=3501523, action_button_id=3500200, text=10010613)
    Event_13500500(14, entity=3501530, action_button_id=3500200, text=10010618)
    Event_13500500(15, entity=3501531, action_button_id=3500200, text=10010618)
    Event_13500500(16, entity=3501532, action_button_id=3500200, text=10010618)
    Event_13500500(17, entity=3501533, action_button_id=3500200, text=10010618)
    Event_13500500(18, entity=3501534, action_button_id=3500200, text=10010614)
    Event_13500500(19, entity=3501535, action_button_id=3500200, text=10010614)
    Event_13500500(20, entity=3501540, action_button_id=3500200, text=10010619)
    Event_13500500(21, entity=3501541, action_button_id=3500200, text=10010619)
    Event_13500500(22, entity=3501542, action_button_id=3500200, text=10010615)
    Event_13500500(23, entity=3501543, action_button_id=3500200, text=10010615)
    Event_13505050(0, character=3500451)
    Event_13505060()
    Event_13505410()
    Event_13505110(0, character=3500934, region=3502343)
    Event_13505300(0, character=3500661)
    Event_13505300(1, character=3500921)
    Event_13505300(2, character=3500935)
    Event_13505300(3, character=3500600)
    Event_13505300(4, character=3500301)
    Event_13505300(5, character=3500302)
    Event_13505300(6, character=3500306)
    Event_13505300(7, character=3500308)
    Event_13505300(8, character=3500309)
    Event_13505300(9, character=3500310)
    Event_13505300(10, character=3500311)
    Event_13505300(11, character=3500312)
    Event_13505300(12, character=3500313)
    Event_13505300(13, character=3500314)
    Event_13505300(14, character=3500315)
    Event_13505300(15, character=3500316)
    Event_13505300(16, character=3500321)
    Event_13505300(17, character=3500322)
    Event_13505300(18, character=3500323)
    Event_13505300(19, character=3500324)
    Event_13505300(20, character=3500325)
    Event_13505300(21, character=3500326)
    Event_13505300(22, character=3500327)
    Event_13505300(23, character=3500328)
    Event_13505300(24, character=3500331)
    Event_13505300(25, character=3500334)
    Event_13505300(26, character=3500335)
    Event_13505300(27, character=3500336)
    Event_13505300(28, character=3500337)
    Event_13505300(29, character=3500339)
    Event_13505300(30, character=3500340)
    Event_13505300(31, character=3500341)
    Event_13505300(32, character=3500342)
    Event_13505300(33, character=3500343)
    Event_13505300(34, character=3500344)
    Event_13505300(35, character=3500346)
    Event_13505300(36, character=3500347)
    Event_13505300(37, character=3500348)
    Event_13505300(38, character=3500349)
    Event_13505300(39, character=3500351)
    Event_13505300(40, character=3500353)
    Event_13505300(41, character=3500360)
    Event_13505300(42, character=3500362)
    Event_13505300(43, character=3500364)
    Event_13505300(44, character=3500365)
    Event_13505300(45, character=3500366)
    Event_13505300(46, character=3500371)
    Event_13505300(47, character=3500389)
    Event_13505300(48, character=3500392)
    Event_13505300(49, character=3500393)
    Event_13505300(50, character=3500395)
    Event_13505300(51, character=3500400)
    Event_13505300(52, character=3500401)
    Event_13505300(53, character=3500451)
    Event_13505300(54, character=3500452)
    Event_13505300(55, character=3500500)
    Event_13505300(56, character=3500501)
    Event_13505300(57, character=3500502)
    Event_13505300(58, character=3500771)
    Event_13505300(59, character=3500777)
    Event_13505400(0, 3500658, 3502251, 0.0, 3502255)
    Event_13505470(0, character=3500312, animation_id=9005, animation_id_1=2004, ai_param_id=402020)
    Event_13505470(2, character=3500390, animation_id=9001, animation_id_1=2004, ai_param_id=402020)
    Event_13505470(3, character=3500396, animation_id=9003, animation_id_1=2004, ai_param_id=402020)
    Event_13505470(4, character=3500397, animation_id=9006, animation_id_1=2004, ai_param_id=402020)
    Event_13505470(5, character=3500398, animation_id=9002, animation_id_1=2004, ai_param_id=402020)
    Event_13505470(6, character=3500502, animation_id=7001, animation_id_1=0, ai_param_id=402035)
    Event_13505470(7, character=3500503, animation_id=7001, animation_id_1=0, ai_param_id=402035)
    Event_13505510(0, 3500350, 3502301, 2.0, 0.0)
    Event_13505510(2, 3500360, 3502301, 2.0, 0.0)
    Event_13505510(3, 3500361, 3502301, 2.0, 0.0)
    Event_13505510(4, 3500363, 3502301, 2.0, 0.0)
    Event_13505510(5, 3500364, 3502301, 2.0, 0.0)
    Event_13505510(6, 3500366, 3502301, 2.0, 0.0)
    Event_13505510(7, 3500301, 3502312, 2.0, 0.0)
    Event_13505510(8, 3500302, 3502312, 2.0, 0.0)
    Event_13505510(9, 3500303, 3502305, 2.0, 0.0)
    Event_13505510(10, 3500409, 3502305, 2.0, 0.0)
    Event_13505510(11, 3500450, 3502305, 2.0, 0.0)
    Event_13505510(12, 3500346, 3502306, 2.0, 0.0)
    Event_13505510(13, 3500347, 3502306, 2.0, 0.0)
    Event_13505510(14, 3500348, 3502306, 2.0, 0.0)
    Event_13505510(15, 3500349, 3502306, 2.0, 0.0)
    Event_13505510(16, 3500371, 3502306, 2.0, 0.0)
    Event_13505510(17, 3500750, 3502307, 2.0, 0.0)
    Event_13505510(18, 3500760, 3502307, 2.0, 0.0)
    Event_13505510(19, 3500313, 3502309, 2.0, 0.0)
    Event_13505510(20, 3500314, 3502309, 2.0, 0.0)
    Event_13505510(21, 3500313, 3502310, 2.0, 0.0)
    Event_13505510(22, 3500314, 3502310, 2.0, 0.0)
    Event_13505510(23, 3500452, 3502313, 5.0, 0.0)
    Event_13505510(24, 3500356, 3502314, 2.0, 0.0)
    Event_13505510(25, 3500357, 3502314, 2.0, 0.0)
    Event_13505510(26, 3500359, 3502314, 2.0, 0.0)
    Event_13505510(27, 3500933, 3502304, 2.0, 0.0)
    Event_13505510(28, 3500935, 3502304, 2.0, 0.0)
    Event_13505510(35, 3500315, 3502321, 2.0, 1.0)
    Event_13505510(36, 3500316, 3502321, 2.0, 1.0)
    Event_13505510(37, 3500353, 3502325, 1.0, 0.0)
    Event_13505510(38, 3500770, 3502311, 5.0, 1.0)
    Event_13505510(39, 3500772, 3502311, 5.0, 1.0)
    Event_13505510(40, 3500311, 3502302, 2.0, 0.0)
    Event_13505510(41, 3500773, 3502329, 3.0, 0.0)
    Event_13505510(43, 3500776, 3502329, 3.0, 0.0)
    Event_13505510(44, 3500335, 3502315, 2.0, 0.0)
    Event_13505510(46, 3500334, 3502315, 2.0, 0.0)
    Event_13505510(47, 3500601, 3502336, 2.0, 0.0)
    Event_13505510(48, 3500607, 3502337, 2.0, 0.0)
    Event_13505510(49, 3500610, 3502337, 2.0, 1.0)
    Event_13505510(50, 3500606, 3502337, 2.0, 1.0)
    Event_13505510(51, 3500613, 3502339, 3.0, 0.0)
    Event_13505510(52, 3500614, 3502339, 3.0, 0.0)
    Event_13505510(53, 3500400, 3502341, 2.0, 0.0)
    Event_13505510(54, 3500401, 3502335, 2.0, 0.0)
    Event_13505510(55, 3500600, 3502391, 2.0, 1.0)
    Event_13505510(56, 3500329, 3502312, 2.0, 0.0)
    Event_13505200(0, character=3500301, patrol_information_id=3503431)
    Event_13505200(1, character=3500302, patrol_information_id=3503431)
    Event_13505200(2, character=3500313, patrol_information_id=3503431)
    Event_13505200(3, character=3500314, patrol_information_id=3503431)
    Event_13505200(4, character=3500364, patrol_information_id=3503430)
    Event_13505200(5, character=3500366, patrol_information_id=3503430)
    Event_13505200(6, character=3500452, patrol_information_id=3503432)
    Event_13505570(0, 3500310, 3502301, 2.0, 0.0, 3502380, 3502306, 3503380)
    Event_13505570(2, 3500362, 3502301, 2.0, 0.0, 3502381, 3502321, 3503380)
    Event_13505570(3, 3500365, 3502301, 2.0, 0.0, 3502381, 3502321, 3503380)
    Event_13505450(0, 3500781, 3502317, 2.0, 3001)
    Event_13505590(0, 3500389, 3502303, 2.0, 9006, 0, 0.0, 0.0, 0)
    Event_13505590(1, 3500780, 3502316, 2.0, 0, 3005, 0.0, 0.0, 0)
    Event_13505590(7, 3500360, 3502326, 2.0, 9000, 9060, 0.0, 0.0, 0)
    Event_13505590(8, 3500306, 3502302, 3.0, 9006, 0, 0.0, 0.0, 3502321)
    Event_13505590(10, 3500308, 3502302, 3.0, 9000, 9060, 0.0, 0.0, 3502321)
    Event_13505590(11, 3500309, 3502302, 3.0, 9002, 0, 0.0, 0.0, 3502321)
    Event_13505590(12, 3500337, 3502301, 3.0, 9002, 0, 0.0, 0.0, 0)
    Event_13505590(13, 3500605, 3502337, 0.0, 7000, 7001, 1.0, 2.0, 0)
    Event_13505590(14, 3500609, 3502337, 0.0, 7000, 7001, 2.0, 3.0, 0)
    Event_13505590(15, 3500612, 3502337, 0.0, 7000, 7001, 2.0, 3.0, 0)
    Event_13505590(16, 3500342, 3502319, 6.0, 9006, 0, 0.0, 0.0, 0)
    Event_13505590(17, 3500343, 3502319, 6.0, 9003, 0, 3.0, 0.0, 0)
    Event_13505590(18, 3500344, 3502319, 6.0, 9005, 0, 3.0, 0.0, 0)
    Event_13505590(19, 3500336, 0, 7.0, 9006, 0, 2.0, 0.0, 0)
    Event_13505590(20, 3500351, 3502301, 7.0, 9006, 0, 0.0, 0.0, 0)
    Event_13505590(22, 3500340, 0, 10.0, 9006, 0, 0.0, 0.0, 0)
    Event_13505610(0, 3500659, 3502251, 2.0, 9001, 9061, 1.0, 1.0)
    Event_13505610(1, 3500655, 3502251, 2.0, 9001, 9061, 3.0, 3.0)
    Event_13505610(2, 3500656, 3502251, 2.0, 9001, 9061, 2.0, 2.0)
    Event_13505640(0, character=3500550, animation_id=9013)
    Event_13505640(1, character=3500551, animation_id=9014)
    Event_13505640(3, character=3500553, animation_id=9001)
    Event_13505640(4, character=3500554, animation_id=9000)
    Event_13505640(5, character=3500555, animation_id=9011)
    Event_13505640(6, character=3500556, animation_id=9010)
    Event_13505700(0, character=3500400, animation_id=3022)
    Event_13505700(1, character=3500401, animation_id=3022)
    Event_13505750(4, 3500303, 3502312, 0, 3503420, 0.0, 0)
    Event_13505750(8, 3500380, 3502312, 0, 3503420, 8.0, 0)
    Event_13505750(9, 3500381, 3502312, 0, 3503420, 7.0, 0)
    Event_13505780(1, character=3500601)
    Event_13505780(2, character=3500602)
    Event_13505780(3, character=3500603)
    Event_13505780(4, character=3500604)
    Event_13505780(5, character=3500605)
    Event_13505780(6, character=3500606)
    Event_13505780(7, character=3500607)
    Event_13505780(8, character=3500608)
    Event_13505780(9, character=3500609)
    Event_13505780(10, character=3500610)
    Event_13505780(11, character=3500611)
    Event_13505780(12, character=3500612)
    Event_13505780(13, character=3500342)
    Event_13505780(14, character=3500343)
    Event_13505780(15, character=3500344)
    Event_13505780(16, character=3500345)
    Event_13505780(17, character=3500613)
    Event_13505780(18, character=3500614)
    Event_13505797(0, obj=3501270)
    Event_13505797(1, obj=3501271)
    Event_13505797(2, obj=3501272)
    Event_13505800(0, region=3502600, entity=3501600, obj=0, projectile_id=3501601, character=3500751)
    Event_13505800(1, region=3502610, entity=3501610, obj=0, projectile_id=3501611, character=0)
    Event_13505800(2, region=3502640, entity=3501640, obj=0, projectile_id=3501641, character=0)
    Event_13505810(
        0,
        region=3502630,
        entity=3501630,
        obj=0,
        projectile_id=3501631,
        projectile_id_1=3501621,
        character=3500764
    )
    Event_13505820(
        0,
        character=3500321,
        animation_id=9014,
        animation_id_1=9064,
        frames=10,
        patrol_information_id=3503421,
        region=3502431
    )
    Event_13505820(
        1,
        character=3500322,
        animation_id=9015,
        animation_id_1=0,
        frames=80,
        patrol_information_id=3503422,
        region=3502432
    )
    Event_13505820(
        2,
        character=3500323,
        animation_id=9014,
        animation_id_1=9064,
        frames=5,
        patrol_information_id=3503423,
        region=3502433
    )
    Event_13505820(
        3,
        character=3500324,
        animation_id=9015,
        animation_id_1=0,
        frames=45,
        patrol_information_id=3503424,
        region=3502434
    )
    Event_13505820(
        4,
        character=3500325,
        animation_id=9014,
        animation_id_1=9064,
        frames=8,
        patrol_information_id=3503425,
        region=3502435
    )
    Event_13505820(
        5,
        character=3500326,
        animation_id=9014,
        animation_id_1=9064,
        frames=3,
        patrol_information_id=3503426,
        region=3502436
    )
    Event_13505820(
        6,
        character=3500327,
        animation_id=9015,
        animation_id_1=0,
        frames=62,
        patrol_information_id=3503427,
        region=3502437
    )
    Event_13505820(
        7,
        character=3500328,
        animation_id=9014,
        animation_id_1=9064,
        frames=12,
        patrol_information_id=3503428,
        region=3502438
    )
    Event_13500942(0, character=10000, region=3502902, flag=73500410)
    Event_13500943(0, character=3500901)
    Event_13500944(0, character=3500901)
    Event_13500941()
    Event_13500978(0, flag=1730, flag_1=73500415, character=3500938)
    Event_13505900(0, flag=13505910, flag_1=13505911, flag_2=13505912, region=3502890, region_1=0, flag_3=6001)
    Event_13505901(0, flag=13505910, flag_1=13505911, flag_2=13505912, region=3502891, region_1=0)
    Event_13505902(
        0,
        character=3500936,
        flag=13505911,
        flag_1=13505912,
        region=3502892,
        region_1=3502896,
        flag_2=13505910,
        flag_3=13505913,
        destination=3502893
    )
    Event_13505903(
        0,
        character=3500936,
        flag=13505911,
        flag_1=13505912,
        region=3502894,
        region_1=3502895,
        flag_2=13505913
    )
    Event_13505904(0, character=3500936, flag=13505911, flag_1=13505912, item_lot_param_id=43710, character_1=3500937)
    Event_13501960()
    Event_13500963(0, character=3500910, first_flag=1750, last_flag=1769, last_flag_1=1752, flag=1750)
    Event_13500963(1, character=3500910, first_flag=1750, last_flag=1769, last_flag_1=1752, flag=1752)
    Event_13500965()
    Event_13500966()
    Event_13500968(0, character=3500910)
    Event_13500998()
    Event_13500999()
    Event_13500951(0, character=3500900, flag=73500621, flag_1=1722)
    Event_13500952(0, character=3500900)
    Event_13500946(0, character=3500905, obj=3501905)
    Event_13500948(0, entity=3501905)
    Event_13500949(0, character=3500905, flag=73500505)
    SetDistanceLimitForConversationStateChanges(character=3500552, distance=25.0)
    Event_13500980(0, 73500910, 73500911, 10.0)
    Event_13500980(1, 73500945, 73500946, 10.0)
    Event_13500990(0, character=3500661, flag=73500971, flag_1=6000)
    Event_13500990(1, character=3500662, flag=73500976, flag_1=6000)
    Event_13500990(2, character=3500911, flag=73500327, flag_1=1762)
    Event_13500990(3, character=3500663, flag=73500971, flag_1=6000)
    Event_13500994(0, 3500661, 3500921, 50002400, 73500974, 6000, 2.0, 2.0, 7010)
    Event_13500994(1, 3500662, 3500920, 50002450, 73500979, 6000, 2.0, 2.0, 7010)
    Event_13500994(2, 3500911, 3500922, 50002270, 73500339, 1762, 2.0, 2.0, 7010)
    Event_13500994(3, 3500663, 3500921, 50002400, 73500974, 6000, 2.0, 2.0, 7010)
    EnableImmortality(3500661)
    EnableImmortality(3500662)
    EnableImmortality(3500911)
    EnableImmortality(3500663)
    DisableFlag(73500970)
    DisableFlag(73500975)
    DisableFlag(73500971)
    DisableFlag(73500976)
    DisableFlag(73500974)
    DisableFlag(73500979)
    Event_13500900(0, character=3500900, first_flag=1710, last_flag=1729, last_flag_1=1719, flag=1712)
    Event_13500900(1, character=3500905, first_flag=1650, last_flag=1669, last_flag_1=1659, flag=1650)
    Event_13500900(2, character=3500901, first_flag=1730, last_flag=1749, last_flag_1=1734, flag=1730)
    Event_13500910(0, attacked_entity=3500900, flag=73500620)
    Event_13500920(0, character=3500900, flag=73500620, first_flag=1710, last_flag=1729, flag_1=1727)
    Event_13501900(0, character=3500930)
    Event_13501900(1, character=3500931)
    Event_13501900(2, character=3500932)
    Event_13501900(3, character=3500934)
    Event_13501900(4, character=3500935)
    Event_13501900(6, character=3500550)
    Event_13501900(7, character=3500551)
    Event_13501900(8, character=3500552)
    Event_13501900(9, character=3500553)
    Event_13501900(10, character=3500554)
    Event_13501900(11, character=3500555)
    Event_13501900(12, character=3500556)
    Event_13500977()
    Event_13501915(0, character=3500933, flag=13501904)
    Event_13500953(0, flag=1712, flag_1=73500630, item_lot_param_id=43200)
    Event_13501920(1, flag=73500321, item_lot_param_id=43010)
    Event_13501920(2, flag=73500322, item_lot_param_id=43020)
    Event_13501920(3, flag=13501900, item_lot_param_id=43830)
    Event_13501920(4, flag=13501903, item_lot_param_id=43820)
    Event_13501920(5, flag=13501905, item_lot_param_id=43710)
    Event_13501940(0, flag=73500320, item_lot_param_id=43000)
    DeleteVFX(3503910, erase_root_only=False)
    Event_13504400(0, flag=13504440, vfx_id=3503910, flag_1=13504420, flag_2=13504430, flag_3=13501850, flag_4=6001)
    Event_13504410(
        0,
        sign_type=5,
        character=3500940,
        region=3502920,
        summon_flag=13504420,
        dismissal_flag=13504430,
        flag=13504440,
        flag_1=13501850,
        action_button_id=10564
    )
    Event_13504450(0, character=3500940, region=3502930, flag=13504420, flag_1=13504430, flag_2=13504858)
    Event_13504460(
        0,
        character=3500940,
        region=3502930,
        region_1=3502810,
        region_2=3502811,
        animation=101130,
        flag=13504450,
        region_3=3502813
    )
    Event_13500000()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_13500940(0, character=3500901)
    Event_13500950(0, character=3500900)
    Event_13500945(
        0,
        character=3500905,
        obj=3501905,
        obj_1=3501906,
        obj_2=3501907,
        obj_3=3501908,
        obj_4=3501909,
        flag=13501801
    )
    Event_13500960(0, character=3500910, character_1=3500911)
    Event_13500400(0, character=3500331, destination=3502354, region=3502350)
    Event_13505630(0, 3500771, 3502318, 0.0, 5.0)
    Event_13505630(1, 3500777, 3502318, 3.0, 5.0)


@NeverRestart(13500000)
def Event_13500000():
    """Event 13500000"""
    GotoIfFlagEnabled(Label.L0, flag=9471)
    EnableInvincibility(3500930)
    DisableHealthBar(3500930)
    IfFlagEnabled(0, 9471)

    # --- 0 --- #
    DefineLabel(0)
    DisableInvincibility(3500930)
    EnableHealthBar(3500930)


@RestartOnRest(13504700)
def Event_13504700(_, character: int, flag: int, flag_1: int, flag_2: int, flag_3: int):
    """Event 13504700"""
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    DisableAI(character)
    ForceAnimation(character, 7010)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EndIfFlagEnabled(flag)
    DisableAI(character)
    ForceAnimation(character, 7010, loop=True)
    IfOnline(1)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfInsideMap(1, game_map=RESEARCH_HALL)
    IfCharacterHuman(2, PLAYER)
    IfPlayerLevelGreaterThanOrEqual(2, value=30)
    SkipLinesIfFlagDisabled(1, flag_3)
    IfClientTypeCountComparison(
        2,
        client_type=ClientType.Coop,
        comparison_type=ComparisonType.GreaterThanOrEqual,
        value=1,
    )
    IfCharacterHasSpecialEffect(3, PLAYER, 9025)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IfRandomTimeElapsed(0, min_seconds=10.0, max_seconds=10.0)
    SkipLinesIfFlagDisabled(1, flag_3)
    DisplayBattlefieldMessage(109000, display_location_index=0)
    ForceAnimation(character, 7011)
    WaitFrames(frames=59)
    EnableAI(character)
    EnableFlag(flag)


@RestartOnRest(13504710)
def Event_13504710(_, character: int, flag: int, flag_1: int, flag_2: int):
    """Event 13504710"""
    EndIfFlagEnabled(flag_1)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_1)
    IfInsideMap(1, game_map=RESEARCH_HALL)
    IfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(2, PLAYER)
    IfRandomTimeElapsed(2, min_seconds=10.0, max_seconds=10.0)
    IfConditionTrue(0, input_condition=2)
    AddSpecialEffect(PLAYER, 9020)
    AddSpecialEffect(character, 9100)
    ReplanAI(character)
    EnableFlag(flag_2)
    DisplayBattlefieldMessage(100002, display_location_index=0)
    Restart()


@RestartOnRest(13504720)
def Event_13504720(_, character: int, flag: int, flag_1: int, flag_2: int):
    """Event 13504720"""
    EndIfFlagEnabled(flag_1)
    IfFlagEnabled(1, flag)
    IfFlagEnabled(1, flag_2)
    IfFlagEnabled(-1, flag_1)
    IfClientTypeCountComparison(
        -1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.GreaterThanOrEqual,
        value=1,
    )
    IfOutsideMap(-1, game_map=RESEARCH_HALL)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(0, PLAYER)
    CancelSpecialEffect(PLAYER, 9020)
    CancelSpecialEffect(character, 9100)
    ReplanAI(character)
    DisableFlag(flag_2)
    Restart()


@RestartOnRest(13504730)
def Event_13504730(
    _,
    character: int,
    flag: int,
    flag_1: int,
    flag_2: int,
    flag_3: int,
    flag_4: int,
    flag_5: int,
    flag_6: int,
):
    """Event 13504730"""
    IfFlagEnabled(-15, flag_1)
    IfFlagEnabled(-15, flag_2)
    IfFlagEnabled(-15, flag_3)
    EndIfConditionTrue(-15)
    IfFlagEnabled(1, flag)
    IfFlagEnabled(1, flag_5)
    IfHealthEqual(2, character, value=0.0)
    IfFlagEnabled(-2, flag_3)
    IfFlagEnabled(-2, flag_6)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=-2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=-2)
    EnableFlag(flag_4)
    Wait(5.0)
    DisplayBattlefieldMessage(109001, display_location_index=0)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(character)
    ForceAnimation(character, 7012)
    WaitFrames(frames=88)
    ForceAnimation(character, 7010)


@RestartOnRest(13504740)
def Event_13504740():
    """Event 13504740"""
    IfCharacterHuman(1, PLAYER)
    IfStandingOnCollision(-1, 3504000)
    IfStandingOnCollision(-1, 3504001)
    IfStandingOnCollision(-1, 3504002)
    IfStandingOnCollision(-1, 3504003)
    IfStandingOnCollision(-1, 3504004)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13504741)
    IfCharacterHuman(2, PLAYER)
    IfStandingOnCollision(-2, 3504000)
    IfStandingOnCollision(-2, 3504001)
    IfStandingOnCollision(-2, 3504002)
    IfStandingOnCollision(-2, 3504003)
    IfStandingOnCollision(-2, 3504004)
    IfConditionFalse(2, input_condition=-1)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(13504741)
    Restart()


@RestartOnRest(13504742)
def Event_13504742():
    """Event 13504742"""
    IfCharacterHuman(1, PLAYER)
    IfStandingOnCollision(-1, 3504020)
    IfStandingOnCollision(-1, 3504021)
    IfStandingOnCollision(-1, 3504022)
    IfStandingOnCollision(-1, 3504023)
    IfStandingOnCollision(-1, 3504024)
    IfStandingOnCollision(-1, 3504025)
    IfStandingOnCollision(-1, 3504026)
    IfStandingOnCollision(-1, 3504027)
    IfStandingOnCollision(-1, 3504028)
    IfStandingOnCollision(-1, 3504029)
    IfStandingOnCollision(-1, 3504030)
    IfStandingOnCollision(-1, 3504031)
    IfStandingOnCollision(-1, 3504032)
    IfStandingOnCollision(-1, 3504033)
    IfStandingOnCollision(-1, 3504034)
    IfStandingOnCollision(-1, 3504035)
    IfStandingOnCollision(-1, 3504036)
    IfStandingOnCollision(-1, 3504037)
    IfStandingOnCollision(-1, 3504038)
    IfStandingOnCollision(-1, 3504039)
    IfStandingOnCollision(-1, 3504040)
    IfStandingOnCollision(-1, 3504041)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13504743)
    IfCharacterHuman(2, PLAYER)
    IfStandingOnCollision(-2, 3504020)
    IfStandingOnCollision(-2, 3504021)
    IfStandingOnCollision(-2, 3504022)
    IfStandingOnCollision(-2, 3504023)
    IfStandingOnCollision(-2, 3504024)
    IfStandingOnCollision(-2, 3504025)
    IfStandingOnCollision(-2, 3504026)
    IfStandingOnCollision(-2, 3504027)
    IfStandingOnCollision(-2, 3504028)
    IfStandingOnCollision(-2, 3504029)
    IfStandingOnCollision(-2, 3504030)
    IfStandingOnCollision(-2, 3504031)
    IfStandingOnCollision(-2, 3504032)
    IfStandingOnCollision(-2, 3504033)
    IfStandingOnCollision(-2, 3504034)
    IfStandingOnCollision(-2, 3504035)
    IfStandingOnCollision(-2, 3504036)
    IfStandingOnCollision(-2, 3504037)
    IfStandingOnCollision(-2, 3504038)
    IfStandingOnCollision(-2, 3504039)
    IfStandingOnCollision(-2, 3504040)
    IfStandingOnCollision(-2, 3504041)
    IfConditionFalse(2, input_condition=-1)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(13504743)
    Restart()


@NeverRestart(13501800)
def Event_13501800():
    """Event 13501800"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableCharacter(3500800)
    Kill(3500800)
    DisableObject(3501800)
    DeleteVFX(3503800)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 3500800)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(3501800)
    DeleteVFX(3503800)
    SetLockedCameraSlot(game_map=RESEARCH_HALL, camera_slot=0)
    Wait(3.0)
    KillBoss(game_area_param_id=3500800)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    AwardAchievement(achievement_id=37)
    RunEvent(9350, slot=0, args=(3,))
    EnableFlag(6675)
    EnableFlag(3510)
    EnableFlag(3511)
    EnableFlag(3512)
    EnableFlag(3513)
    DisableFlag(3515)
    DisableFlag(3516)
    DisableFlag(3517)
    DisableFlag(3518)
    StopPlayLogMeasurement(measurement_id=3500000)
    StopPlayLogMeasurement(measurement_id=3500001)
    StopPlayLogMeasurement(measurement_id=3500010)
    CreatePlayLog(name=0)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=24,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=24,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=24,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=24,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterWhitePhantom(0, PLAYER)
    Wait(0.0)


@NeverRestart(13501801)
def Event_13501801():
    """Event 13501801"""
    IfFlagDisabled(1, 13501800)
    IfThisEventFlagDisabled(1)
    GotoIfConditionTrue(Label.L5, input_condition=1)
    DeleteVFX(3503820, erase_root_only=False)
    End()

    # --- 5 --- #
    DefineLabel(5)
    DisableCharacter(3500800)
    DisableFlag(13500947)
    IfFlagEnabled(0, 13500947)
    DeleteObjectVFX(3501905, erase_root=False)
    DeleteVFX(3503820, erase_root_only=False)
    EnableFlag(9180)
    WaitFrames(frames=1)
    GotoIfFlagEnabled(Label.L0, flag=1651)
    PlayCutscene(35000010, cutscene_flags=0, player_id=10000, move_to_region=3502808, game_map=RESEARCH_HALL)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    PlayCutscene(35000010, cutscene_flags=0, player_id=10000, move_to_region=3502808, game_map=RESEARCH_HALL)

    # --- 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    DisableFlag(9180)
    EnableCharacter(3500800)
    DisableCharacter(3500905)
    DisableBackread(3500905)
    DisableObjectInvulnerability(3501906)
    DisableObject(3501907)
    DisableObject(3501908)
    EnableFlag(13504808)
    EnableFlag(3510)
    EnableFlag(3511)
    DisableFlag(3512)
    DisableFlag(3513)
    DisableFlag(3515)
    DisableFlag(3516)
    DisableFlag(3517)
    DisableFlag(3518)
    EndIfFlagEnabled(9346)
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9346)


@RestartOnRest(13501802)
def Event_13501802():
    """Event 13501802"""
    DisableSoundEvent(sound_id=3503204)
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(obj=3501200, animation_id=3)
    DisableMapCollision(collision=3504800)
    DisableObjectActivation(3501201, obj_act_id=3500100)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfPlayerHasGood(1, 4021)
    IfCharacterOutsideRegion(1, PLAYER, region=3502803)
    IfActionButtonParam(1, action_button_id=3500912, entity=3501802)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 3501802, animation=101340)
    WaitFrames(frames=120)
    PlaySoundEffect(PLAYER, 350000012, sound_type=SoundType.a_Ambient)
    WaitFrames(frames=60)
    ForceAnimation(3501200, 2, wait_for_completion=True)
    DisableMapCollision(collision=3504800)
    EnableFlag(9468)


@NeverRestart(13501803)
def Event_13501803():
    """Event 13501803"""
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfFlagEnabled(0, 13501800)
    CreateObjectVFX(3501801, vfx_id=200, model_point=900201)
    IfActionButtonParam(0, action_button_id=3500911, entity=3501801)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(3501800, host_only=False)
    DeleteObjectVFX(3501801)


@NeverRestart(13501804)
def Event_13501804():
    """Event 13501804"""
    DisableNetworkSync()
    IfFlagEnabled(1, 13501802)
    IfActionButtonParam(1, action_button_id=7100, entity=3501201)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(13501805)
def Event_13501805(_, obj: int):
    """Event 13501805"""
    IfFlagEnabled(1, 13501800)
    IfThisEventSlotFlagEnabled(1)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    IfObjectDestroyed(0, obj)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableObject(obj)
    End()


@NeverRestart(13501807)
def Event_13501807():
    """Event 13501807"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 13504808)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableCharacter(3500800)
    DisableCharacter(3500905)
    DisableBackread(3500905)
    DisableObjectInvulnerability(3501906)
    DisableObject(3501907)
    DisableObject(3501908)
    EnableFlag(13504808)
    EnableFlag(13501801)


@NeverRestart(13501810)
def Event_13501810():
    """Event 13501810"""
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfStandingOnCollision(0, 3504020)
    RunEvent(9350, slot=0, args=(2,))


@NeverRestart(13504800)
def Event_13504800():
    """Event 13504800"""
    EndIfFlagEnabled(13501800)
    GotoIfFlagEnabled(Label.L0, flag=13501801)
    SkipLinesIfClient(2)
    DisableObject(3501800)
    DeleteVFX(3503800, erase_root_only=False)
    IfFlagDisabled(1, 13501800)
    IfFlagEnabled(1, 13501801)
    IfConditionTrue(0, input_condition=1)
    EnableObject(3501800)
    CreateVFX(3503800)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 13501800)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParam(2, action_button_id=3500800, entity=3501800)
    IfFlagEnabled(3, 13501800)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    RotateToFaceEntity(PLAYER, 3502800, animation=101130)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=3502801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, seconds=2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, condition=5)
    EnableFlag(13504808)
    Restart()


@NeverRestart(13504801)
def Event_13504801():
    """Event 13504801"""
    DisableNetworkSync()
    EndIfFlagEnabled(13501800)
    IfFlagDisabled(1, 13501800)
    IfFlagEnabled(1, 13501801)
    IfFlagEnabled(1, 13504808)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButtonParam(1, action_button_id=3500800, entity=3501800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 3502800, animation=101130)
    IfCharacterWhitePhantom(2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=3502801)
    IfCharacterWhitePhantom(3, PLAYER)
    IfTimeElapsed(3, seconds=2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, condition=3)
    EnableFlag(13504809)
    Restart()


@NeverRestart(13504802)
def Event_13504802():
    """Event 13504802"""
    EndIfFlagEnabled(13501800)
    DisableAI(3500800)
    DisableHealthBar(3500800)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, 13504808)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagEnabled(1, 13504810)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(3500800, authority_level=UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(13504810)
    EnableFlag(13504808)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(3500800, 7500)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3500800)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(3500800, 7501)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3500800)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(3500800)
    EnableBossHealthBar(3500800, name=452000)
    DisableInvincibility(3500800)
    SetCharacterEventTarget(3500800, region=3500801)
    CreatePlayLog(name=58)
    StartPlayLogMeasurement(measurement_id=3500010, name=74, overwrite=True)


@NeverRestart(13504803)
def Event_13504803():
    """Event 13504803"""
    DisableNetworkSync()
    DisableSoundEvent(sound_id=3503802)
    DisableSoundEvent(sound_id=3503803)
    DisableSoundEvent(sound_id=3503804)
    DeleteVFX(3503501, erase_root_only=False)
    EndIfFlagEnabled(13501800)
    GotoIfThisEventFlagEnabled(Label.L1)
    GotoIfFlagEnabled(Label.L0, flag=13504811)
    IfFlagDisabled(1, 13501800)
    IfFlagEnabled(1, 13504802)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 13504809)
    IfCharacterInsideRegion(1, PLAYER, region=3502802)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(sound_id=3503802)
    IfCharacterHasTAEEvent(2, 3500800, tae_event_id=100)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 13501800)
    IfFlagEnabled(2, 13504802)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 13504809)
    IfCharacterInsideRegion(2, PLAYER, region=3502802)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(sound_id=3503802)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=3503803)
    CreateVFX(3503501)
    DeleteVFX(3503500)
    EnableFlag(13504811)
    IfCharacterHasTAEEvent(3, 3500800, tae_event_id=300)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagDisabled(3, 13501800)
    IfFlagEnabled(3, 13504802)
    SkipLinesIfHost(1)
    IfFlagEnabled(3, 13504809)
    IfCharacterInsideRegion(3, PLAYER, region=3502802)
    IfConditionTrue(0, input_condition=3)
    DisableBossMusic(sound_id=3503803)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=3503804)


@NeverRestart(13504804)
def Event_13504804():
    """Event 13504804"""
    DisableNetworkSync()
    EndIfFlagEnabled(13501800)
    IfCharacterAlive(1, 3500800)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=3500800, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=RESEARCH_HALL, camera_slot=1)
    IfCharacterDead(-1, 3500800)
    IfEntityBeyondDistance(-1, entity=PLAYER, other_entity=3500800, radius=10.0)
    IfConditionTrue(0, input_condition=-1)
    SetLockedCameraSlot(game_map=RESEARCH_HALL, camera_slot=0)
    Restart()


@NeverRestart(13504805)
def Event_13504805():
    """Event 13504805"""
    DisableNetworkSync()
    EndIfFlagEnabled(13501800)
    IfCharacterDead(0, 3500800)
    DisableBossMusic(sound_id=3503802)
    DisableBossMusic(sound_id=3503803)
    DisableBossMusic(sound_id=3503804)
    DisableBossMusic(sound_id=-1)
    CreateVFX(3503500)
    DeleteVFX(3503501)


@NeverRestart(13504806)
def Event_13504806():
    """Event 13504806"""
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=3501800, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(13504807)
def Event_13504807():
    """Event 13504807"""
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, entity=PLAYER, other_entity=3501800, radius=6.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=3501800, radius=12.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(13504822)
def Event_13504822():
    """Event 13504822"""
    EndIfFlagEnabled(13501800)
    IfCharacterHasTAEEvent(0, 3500800, tae_event_id=20)
    CancelSpecialEffect(3500800, 5526)
    Wait(0.10000000149011612)
    Restart()


@NeverRestart(13501850)
def Event_13501850():
    """Event 13501850"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableCharacter(3500850)
    DisableCharacter(3500851)
    DisableCharacter(3500852)
    DisableCharacter(3500853)
    DisableCharacter(3500854)
    Kill(3500850)
    Kill(3500851)
    Kill(3500852)
    Kill(3500853)
    Kill(3500854)
    DisableObject(3501810)
    DeleteVFX(3503810)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfHealthEqual(0, 3500850, value=0.0)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(3501810)
    DeleteVFX(3503810)
    SetLockedCameraSlot(game_map=RESEARCH_HALL, camera_slot=0)
    EnableMapCollision(collision=3504812)
    DisableMapCollision(collision=3504814)
    Wait(3.0)
    KillBoss(game_area_param_id=3500850)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    AwardAchievement(achievement_id=38)
    RunEvent(9350, slot=0, args=(2,))
    AwardItemLot(3501850, host_only=False)
    EnableFlag(3510)
    EnableFlag(3511)
    EnableFlag(3512)
    DisableFlag(3513)
    DisableFlag(3515)
    DisableFlag(3516)
    EnableFlag(3517)
    DisableFlag(3518)
    StopPlayLogMeasurement(measurement_id=3500002)
    StopPlayLogMeasurement(measurement_id=3500003)
    StopPlayLogMeasurement(measurement_id=3500011)
    CreatePlayLog(name=90)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=108,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=108,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=108,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=108,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterWhitePhantom(0, PLAYER)
    Wait(0.0)


@NeverRestart(13501851)
def Event_13501851():
    """Event 13501851"""
    DisableSoundEvent(sound_id=3503211)
    DisableSoundEvent(sound_id=3503212)
    EndIfFlagEnabled(13501850)
    EndIfThisEventFlagEnabled()
    ForceAnimation(3500851, 9000, loop=True)
    IfFlagDisabled(1, 13501850)
    IfThisEventFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=3502815)
    IfConditionTrue(0, input_condition=1)
    PlaySoundEffect(PLAYER, 350000020, sound_type=SoundType.a_Ambient)
    ForceAnimation(3500851, 9060)
    ReplanAI(3500851)
    EnableFlag(13504858)
    EndIfFlagEnabled(9348)
    RunEvent(9350, slot=0, args=(2,))
    EnableFlag(9348)


@NeverRestart(13501852)
def Event_13501852():
    """Event 13501852"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 13504858)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableFlag(13504858)
    EnableFlag(13501851)


@NeverRestart(13504850)
def Event_13504850():
    """Event 13504850"""
    EndIfFlagEnabled(13501850)
    GotoIfFlagEnabled(Label.L0, flag=13501851)
    SkipLinesIfClient(2)
    DisableObject(3501810)
    DeleteVFX(3503810, erase_root_only=False)
    IfFlagDisabled(1, 13501850)
    IfFlagEnabled(1, 13501851)
    IfConditionTrue(0, input_condition=1)
    EnableObject(3501810)
    CreateVFX(3503810)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 13501850)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParam(2, action_button_id=3500850, entity=3501810)
    IfFlagEnabled(3, 13501850)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    RotateToFaceEntity(PLAYER, 3502810, animation=101130)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=3502811)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, seconds=2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, condition=5)
    EnableFlag(13504858)
    Restart()


@NeverRestart(13504851)
def Event_13504851():
    """Event 13504851"""
    DisableNetworkSync()
    EndIfFlagEnabled(13501850)
    IfFlagDisabled(1, 13501850)
    IfFlagEnabled(1, 13501851)
    IfFlagEnabled(1, 13504858)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButtonParam(1, action_button_id=3500850, entity=3501810)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 3502810, animation=101130)
    IfCharacterWhitePhantom(2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=3502811)
    IfCharacterWhitePhantom(3, PLAYER)
    IfTimeElapsed(3, seconds=2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, condition=3)
    EnableFlag(13504859)
    Restart()


@NeverRestart(13504852)
def Event_13504852():
    """Event 13504852"""
    EndIfFlagEnabled(13501850)
    DisableGravity(3500850)
    DisableAI(3500850)
    DisableAI(3500851)
    DisableAI(3500852)
    DisableAI(3500853)
    DisableAI(3500854)
    DisableAI(3500860)
    DisableHealthBar(3500850)
    DisableHealthBar(3500851)
    DisableHealthBar(3500852)
    DisableHealthBar(3500853)
    DisableHealthBar(3500854)
    ReferDamageToEntity(3500851, target_entity=3500850)
    ReferDamageToEntity(3500852, target_entity=3500850)
    ReferDamageToEntity(3500853, target_entity=3500850)
    ReferDamageToEntity(3500854, target_entity=3500850)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, 13504858)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagEnabled(1, 13504860)
    NotifyBossBattleStart()

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(13504860)
    EnableFlag(13504858)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(3500850, 7500)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3500850)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(3500850, 7501)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3500850)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(3500851)
    EnableAI(3500852)
    EnableAI(3500853)
    EnableAI(3500854)
    EnableAI(3500860)
    SkipLinesIfClient(5)
    SetNetworkUpdateAuthority(3500851, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(3500852, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(3500853, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(3500854, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(3500860, authority_level=UpdateAuthority.Forced)
    EnableBossHealthBar(3500850, name=403000)
    CreatePlayLog(name=136)
    StartPlayLogMeasurement(measurement_id=3500011, name=158, overwrite=True)


@NeverRestart(13504853)
def Event_13504853():
    """Event 13504853"""
    DisableNetworkSync()
    DisableSoundEvent(sound_id=3503812)
    DisableSoundEvent(sound_id=3503813)
    DisableSoundEvent(sound_id=3503814)
    EndIfFlagEnabled(13501800)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagDisabled(1, 13501850)
    IfFlagEnabled(1, 13504852)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 13504859)
    IfCharacterInsideRegion(1, PLAYER, region=3502812)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(sound_id=3503812)
    IfFlagEnabled(2, 13504870)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 13501850)
    IfFlagEnabled(2, 13504852)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 13504859)
    IfCharacterInsideRegion(2, PLAYER, region=3502812)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(sound_id=3503812)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=3503813)


@NeverRestart(13504854)
def Event_13504854():
    """Event 13504854"""
    DisableNetworkSync()
    EndIfFlagEnabled(13501850)
    IfCharacterAlive(1, 3500850)
    IfEntityWithinDistance(-1, entity=PLAYER, other_entity=3500851, radius=8.0)
    IfEntityWithinDistance(-1, entity=PLAYER, other_entity=3500852, radius=8.0)
    IfEntityWithinDistance(-1, entity=PLAYER, other_entity=3500853, radius=8.0)
    IfEntityWithinDistance(-1, entity=PLAYER, other_entity=3500854, radius=8.0)
    IfConditionTrue(2, input_condition=1)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=RESEARCH_HALL, camera_slot=1)
    IfCharacterDead(-3, 3500850)
    IfEntityBeyondDistance(3, entity=PLAYER, other_entity=3500851, radius=10.0)
    IfEntityBeyondDistance(3, entity=PLAYER, other_entity=3500852, radius=10.0)
    IfEntityBeyondDistance(3, entity=PLAYER, other_entity=3500853, radius=10.0)
    IfEntityBeyondDistance(3, entity=PLAYER, other_entity=3500854, radius=10.0)
    IfConditionTrue(-4, input_condition=-3)
    IfConditionTrue(-4, input_condition=3)
    IfConditionTrue(0, input_condition=-4)
    SetLockedCameraSlot(game_map=RESEARCH_HALL, camera_slot=0)
    Restart()


@NeverRestart(13504855)
def Event_13504855():
    """Event 13504855"""
    DisableNetworkSync()
    EndIfFlagEnabled(13501850)
    IfCharacterDead(0, 3500850)
    DisableBossMusic(sound_id=3503812)
    DisableBossMusic(sound_id=3503813)
    DisableBossMusic(sound_id=-1)


@NeverRestart(13504856)
def Event_13504856():
    """Event 13504856"""
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=3501810, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(13504857)
def Event_13504857():
    """Event 13504857"""
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, entity=PLAYER, other_entity=3501810, radius=6.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=3501810, radius=12.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(13504865)
def Event_13504865():
    """Event 13504865"""
    IfCharacterHasTAEEvent(-15, 3500851, tae_event_id=50)
    IfCharacterHasTAEEvent(-15, 3500852, tae_event_id=50)
    IfCharacterHasTAEEvent(-15, 3500853, tae_event_id=50)
    IfCharacterHasTAEEvent(-15, 3500854, tae_event_id=50)
    IfConditionTrue(15, input_condition=-15)
    IfCharacterHuman(15, PLAYER)
    IfConditionTrue(0, input_condition=15)
    EnableFlag(13504870)
    IfCharacterHasTAEEvent(-1, 3500851, tae_event_id=30)
    IfCharacterHasTAEEvent(-1, 3500852, tae_event_id=30)
    IfCharacterHasTAEEvent(-1, 3500853, tae_event_id=30)
    IfCharacterHasTAEEvent(-1, 3500854, tae_event_id=30)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterHuman(1, PLAYER)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 8035)
    CreateVFX(3503854)
    EnableFlag(13504866)
    IfFlagDisabled(0, 13504866)

    # --- 0 --- #
    DefineLabel(0)
    DeleteVFX(3503854)
    CancelSpecialEffect(PLAYER, 8035)
    Restart()


@NeverRestart(13504880)
def Event_13504880():
    """Event 13504880"""
    DisableNetworkSync()
    DeleteVFX(3503850, erase_root_only=False)
    DeleteVFX(3503851, erase_root_only=False)
    DeleteVFX(3503852, erase_root_only=False)
    DeleteVFX(3503853, erase_root_only=False)
    DeleteVFX(3503854, erase_root_only=False)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagEnabled(Label.L0, flag=13504869)
    EnableRandomFlagInRange(flag_range=(13504873, 13504874))
    Goto(Label.L2)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=13504868)
    EnableRandomFlagInRange(flag_range=(13504875, 13504878))
    EnableFlag(13504868)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    EnableRandomFlagInRange(flag_range=(13504873, 13504878))
    Goto(Label.L2)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagRangeAllDisabled(0, flag_range=(13504873, 13504878))
    WaitFrames(frames=900)
    Restart()


@NeverRestart(13504881)
def Event_13504881():
    """Event 13504881"""
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagRangeAnyEnabled(0, flag_range=(13504873, 13504878))
    Wait(5.0)
    IfCharacterDoesNotHaveSpecialEffect(1, 3500851, 8069)
    IfCharacterDoesNotHaveSpecialEffect(1, 3500852, 8069)
    IfCharacterDoesNotHaveSpecialEffect(1, 3500853, 8069)
    IfCharacterDoesNotHaveSpecialEffect(1, 3500854, 8069)
    IfCharacterDoesNotHaveSpecialEffect(1, 3500851, 8070)
    IfCharacterDoesNotHaveSpecialEffect(1, 3500852, 8070)
    IfCharacterDoesNotHaveSpecialEffect(1, 3500853, 8070)
    IfCharacterDoesNotHaveSpecialEffect(1, 3500854, 8070)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((13504873, 13504878))
    ReplanAI(3500851)
    ReplanAI(3500852)
    ReplanAI(3500853)
    ReplanAI(3500854)
    Restart()


@NeverRestart(13504885)
def Event_13504885(_, character: int, flag: int):
    """Event 13504885"""
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, flag)
    AICommand(character, command_id=110, command_slot=0)
    ReplanAI(character)
    IfFlagDisabled(0, flag)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    Restart()


@NeverRestart(13504890)
def Event_13504890(_, character: int):
    """Event 13504890"""
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagRangeAnyEnabled(0, flag_range=(13504875, 13504878))
    IfCharacterHasSpecialEffect(-1, character, 52)
    IfCharacterHasSpecialEffect(-1, character, 57)
    SkipLinesIfConditionTrue(1, -1)
    ForceAnimation(character, 3013)
    AICommand(character, command_id=120, command_slot=0)
    ReplanAI(character)
    IfFlagRangeAllDisabled(0, flag_range=(13504875, 13504878))
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    Restart()


@NeverRestart(13504895)
def Event_13504895(_, character: int):
    """Event 13504895"""
    DisableNetworkSync()
    EndIfFlagEnabled(13501850)
    IfHealthEqual(0, 3500850, value=0.0)
    Kill(character, award_souls=True)


@NeverRestart(13505655)
def Event_13505655():
    """Event 13505655"""
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L1, flag=13501850)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, 13504852)
    EnableFlag(13505669)
    Wait(3.0)
    IfTimeElapsed(-1, seconds=5.0)
    IfEventValueEqual(1, flag=13505690, bit_count=3, value=0)
    IfFlagDisabled(1, 13505669)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFlagEnabled(Label.L1, flag=13504895)
    EnableFlag(13505668)
    Wait(1.0)
    IfTimeElapsed(-3, seconds=20.0)
    IfTimeElapsed(2, seconds=10.0)
    IfEventValueEqual(2, flag=13505690, bit_count=3, value=1)
    IfFlagDisabled(2, 13505669)
    IfEventValueEqual(3, flag=13505690, bit_count=3, value=0)
    IfFlagDisabled(3, 13505669)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFlagEnabled(Label.L1, flag=13504895)
    EnableFlag(13505668)
    Wait(1.0)
    IfTimeElapsed(-5, seconds=20.0)
    IfTimeElapsed(4, seconds=10.0)
    IfEventValueEqual(4, flag=13505690, bit_count=3, value=2)
    IfFlagDisabled(4, 13505669)
    IfTimeElapsed(5, seconds=5.0)
    IfEventValueEqual(5, flag=13505690, bit_count=3, value=1)
    IfFlagDisabled(5, 13505669)
    IfEventValueEqual(6, flag=13505690, bit_count=3, value=0)
    IfFlagDisabled(6, 13505669)
    IfConditionTrue(-5, input_condition=4)
    IfConditionTrue(-5, input_condition=5)
    IfConditionTrue(-5, input_condition=6)
    IfConditionTrue(0, input_condition=-5)
    GotoIfFlagEnabled(Label.L1, flag=13504895)
    EnableFlag(13505668)
    Wait(1.0)
    IfTimeElapsed(7, seconds=15.0)
    IfEventValueEqual(7, flag=13505690, bit_count=3, value=3)
    IfFlagDisabled(7, 13505669)
    IfTimeElapsed(8, seconds=10.0)
    IfEventValueEqual(8, flag=13505690, bit_count=3, value=2)
    IfFlagDisabled(8, 13505669)
    IfTimeElapsed(9, seconds=5.0)
    IfEventValueEqual(9, flag=13505690, bit_count=3, value=1)
    IfFlagDisabled(9, 13505669)
    IfEventValueEqual(10, flag=13505690, bit_count=3, value=0)
    IfFlagDisabled(10, 13505669)
    IfConditionTrue(-7, input_condition=7)
    IfConditionTrue(-7, input_condition=8)
    IfConditionTrue(-7, input_condition=9)
    IfConditionTrue(-7, input_condition=10)
    IfConditionTrue(0, input_condition=-7)
    GotoIfFlagEnabled(Label.L1, flag=13504895)
    EnableFlag(13505668)

    # --- 0 --- #
    DefineLabel(0)
    Wait(1.0)
    IfTimeElapsed(12, seconds=9.0)
    IfEventValueEqual(12, flag=13505690, bit_count=3, value=3)
    IfFlagDisabled(12, 13505669)
    IfTimeElapsed(13, seconds=6.0)
    IfEventValueEqual(13, flag=13505690, bit_count=3, value=2)
    IfFlagDisabled(13, 13505669)
    IfTimeElapsed(14, seconds=3.0)
    IfEventValueEqual(14, flag=13505690, bit_count=3, value=1)
    IfFlagDisabled(14, 13505669)
    IfEventValueEqual(15, flag=13505690, bit_count=3, value=0)
    IfFlagDisabled(15, 13505669)
    IfConditionTrue(-13, input_condition=12)
    IfConditionTrue(-13, input_condition=13)
    IfConditionTrue(-13, input_condition=14)
    IfConditionTrue(-13, input_condition=15)
    IfConditionTrue(0, input_condition=-13)
    GotoIfFlagEnabled(Label.L1, flag=13504895)
    EnableFlag(13505668)
    IfHealthLessThan(-15, 3500850, value=0.6000000238418579)
    SkipLinesIfConditionFalse(1, -15)
    EnableFlag(13504869)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    DisableSpawner(entity=3503814)
    DisableSpawner(entity=3503815)
    DisableSpawner(entity=3503816)
    DisableSpawner(entity=3503817)
    End()


@NeverRestart(13505656)
def Event_13505656(_, character: int):
    """Event 13505656"""
    DisableNetworkSync()
    IfCharacterAlive(1, character)
    IfHasAIStatus(1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13505669)
    IfCharacterDead(0, character)
    EnableFlag(13505669)
    Restart()


@NeverRestart(13505661)
def Event_13505661():
    """Event 13505661"""
    DisableNetworkSync()
    IfFlagEnabled(0, 13505669)
    ClearEventValue(13505690, bit_count=3)
    IfHasAIStatus(1, 3500851, ai_status=AIStatusType.Battle)
    IfCharacterAlive(1, 3500851)
    SkipLinesIfConditionFalse(1, 1)
    IncrementEventValue(13505690, bit_count=3, max_value=6)
    IfHasAIStatus(2, 3500852, ai_status=AIStatusType.Battle)
    IfCharacterAlive(2, 3500852)
    SkipLinesIfConditionFalse(1, 2)
    IncrementEventValue(13505690, bit_count=3, max_value=6)
    IfHasAIStatus(3, 3500853, ai_status=AIStatusType.Battle)
    IfCharacterAlive(3, 3500853)
    SkipLinesIfConditionFalse(1, 3)
    IncrementEventValue(13505690, bit_count=3, max_value=6)
    IfHasAIStatus(4, 3500854, ai_status=AIStatusType.Battle)
    IfCharacterAlive(4, 3500854)
    SkipLinesIfConditionFalse(1, 4)
    IncrementEventValue(13505690, bit_count=3, max_value=6)
    DisableFlag(13505669)
    Wait(1.0)
    Restart()


@NeverRestart(13505662)
def Event_13505662():
    """Event 13505662"""
    IfFlagEnabled(0, 13505668)
    IfCharacterHuman(2, PLAYER)
    IfHasAIStatus(2, 3500852, ai_status=AIStatusType.Battle)
    IfCharacterAlive(2, 3500852)
    SkipLinesIfConditionTrue(2, 2)
    EnableSpawner(entity=3503815)
    Goto(Label.L0)
    IfCharacterHuman(3, PLAYER)
    IfHasAIStatus(3, 3500853, ai_status=AIStatusType.Battle)
    IfCharacterAlive(3, 3500853)
    SkipLinesIfConditionTrue(2, 3)
    EnableSpawner(entity=3503816)
    Goto(Label.L0)
    IfCharacterHuman(4, PLAYER)
    IfHasAIStatus(4, 3500854, ai_status=AIStatusType.Battle)
    IfCharacterAlive(4, 3500854)
    SkipLinesIfConditionTrue(2, 4)
    EnableSpawner(entity=3503817)
    Goto(Label.L0)
    IfCharacterHuman(1, PLAYER)
    IfHasAIStatus(1, 3500851, ai_status=AIStatusType.Battle)
    IfCharacterAlive(1, 3500851)
    SkipLinesIfConditionTrue(2, 1)
    EnableSpawner(entity=3503814)
    Goto(Label.L0)

    # --- 0 --- #
    DefineLabel(0)
    Wait(3.0)
    DisableSpawner(entity=3503814)
    DisableSpawner(entity=3503815)
    DisableSpawner(entity=3503816)
    DisableSpawner(entity=3503817)
    EnableFlag(13505669)
    DisableFlag(13505668)
    Restart()


@NeverRestart(13505670)
def Event_13505670(_, projectile_id: int, behavior_id: int, frames: int, character: int):
    """Event 13505670"""
    IfFlagEnabled(1, 13504866)
    IfCharacterAlive(1, character)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(frames=frames)
    ShootProjectile(
        owner_entity=character,
        projectile_id=projectile_id,
        model_point=200,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(frames=180)
    Restart()


@NeverRestart(13505680)
def Event_13505680():
    """Event 13505680"""
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    IfFlagEnabled(15, 13504866)
    IfConditionTrue(0, input_condition=15)
    ClearEventValue(13505694, bit_count=3)
    IfCharacterHasSpecialEffect(-1, 3500851, 8070)
    SkipLinesIfConditionFalse(1, -1)
    IncrementEventValue(13505694, bit_count=3, max_value=10)
    IfCharacterHasSpecialEffect(-2, 3500852, 8070)
    SkipLinesIfConditionFalse(1, -2)
    IncrementEventValue(13505694, bit_count=3, max_value=10)
    IfCharacterHasSpecialEffect(-3, 3500853, 8070)
    SkipLinesIfConditionFalse(1, -3)
    IncrementEventValue(13505694, bit_count=3, max_value=10)
    IfCharacterHasSpecialEffect(-4, 3500854, 8070)
    SkipLinesIfConditionFalse(1, -4)
    IncrementEventValue(13505694, bit_count=3, max_value=10)
    IfEventValueEqual(1, flag=13505694, bit_count=3, value=1)
    SkipLinesIfConditionFalse(1, 1)
    AICommand(3500860, command_id=10, command_slot=0)
    IfEventValueEqual(2, flag=13505694, bit_count=3, value=2)
    SkipLinesIfConditionFalse(1, 2)
    AICommand(3500860, command_id=20, command_slot=0)
    IfEventValueEqual(3, flag=13505694, bit_count=3, value=3)
    SkipLinesIfConditionFalse(1, 3)
    AICommand(3500860, command_id=30, command_slot=0)
    IfEventValueEqual(4, flag=13505694, bit_count=3, value=4)
    SkipLinesIfConditionFalse(1, 4)
    AICommand(3500860, command_id=40, command_slot=0)
    ReplanAI(3500860)
    IfCharacterDoesNotHaveSpecialEffect(5, 3500851, 8070)
    IfCharacterDoesNotHaveSpecialEffect(5, 3500852, 8070)
    IfCharacterDoesNotHaveSpecialEffect(5, 3500853, 8070)
    IfCharacterDoesNotHaveSpecialEffect(5, 3500854, 8070)
    IfCharacterHasTAEEvent(-5, 3500851, tae_event_id=40)
    IfCharacterHasTAEEvent(-5, 3500852, tae_event_id=40)
    IfCharacterHasTAEEvent(-5, 3500853, tae_event_id=40)
    IfCharacterHasTAEEvent(-5, 3500854, tae_event_id=40)
    IfConditionTrue(-6, input_condition=5)
    IfConditionTrue(-6, input_condition=-5)
    IfConditionTrue(0, input_condition=-6)
    SkipLinesIfFinishedConditionTrue(1, condition=5)
    WaitFrames(frames=600)
    AICommand(3500860, command_id=-1, command_slot=0)
    ReplanAI(3500860)
    ForceAnimation(3500860, 0)
    DisableFlag(13504866)
    Restart()


@NeverRestart(13501100)
def Event_13501100():
    """Event 13501100"""
    SkipLinesIfFlagDisabled(3, 13504100)
    SetCollisionResState(collision=3504100, state=False)
    SetCollisionResState(collision=3504101, state=False)
    End()
    GotoIfFlagEnabled(Label.L0, flag=13501108)
    DisableFlag(13501106)
    DisableFlag(13501107)
    EndOfAnimation(obj=3501100, animation_id=0)
    EndOfAnimation(obj=3501104, animation_id=0)
    EndOfAnimation(obj=3501108, animation_id=0)
    DisableObjectActivation(3501101, obj_act_id=100)
    DisableObjectActivation(3501102, obj_act_id=100)
    DisableObjectActivation(3501103, obj_act_id=100)
    SetCollisionResState(collision=3504101, state=False)
    DisableMapCollision(collision=3504301)
    DisableMapCollision(collision=3504302)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13501106)
    GotoIfConditionTrue(Label.L1, input_condition=1)
    DisableFlag(13501107)
    EndOfAnimation(obj=3501100, animation_id=0)
    EndOfAnimation(obj=3501104, animation_id=0)
    EndOfAnimation(obj=3501108, animation_id=0)
    EnableObjectActivation(3501101, obj_act_id=100)
    DisableObjectActivation(3501102, obj_act_id=100)
    DisableObjectActivation(3501103, obj_act_id=100)
    SetCollisionResState(collision=3504101, state=False)
    DisableMapCollision(collision=3504301)
    DisableMapCollision(collision=3504302)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(13501107)
    EndOfAnimation(obj=3501100, animation_id=2)
    EndOfAnimation(obj=3501104, animation_id=2)
    EndOfAnimation(obj=3501108, animation_id=2)
    DisableObjectActivation(3501101, obj_act_id=100)
    EnableObjectActivation(3501102, obj_act_id=100)
    EnableObjectActivation(3501103, obj_act_id=100)
    SetCollisionResState(collision=3504100, state=False)
    DisableMapCollision(collision=3504300)
    DisableMapCollision(collision=3504301)


@NeverRestart(13501101)
def Event_13501101():
    """Event 13501101"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 13501108)
    IfFlagEnabled(1, 13504100)
    IfConditionTrue(0, input_condition=1)
    IfFlagEnabled(2, 13501106)
    SkipLinesIfConditionTrue(2, 2)
    DisableFlag(13501107)
    SkipLines(1)
    EnableFlag(13501107)
    IfCharacterHuman(3, PLAYER)
    IfFlagEnabled(3, 13501108)
    IfFlagDisabled(3, 13504100)
    IfConditionTrue(0, input_condition=3)
    Restart()


@NeverRestart(13501102)
def Event_13501102():
    """Event 13501102"""
    IfFlagEnabled(4, 13504100)
    IfFlagEnabled(4, 13501106)
    GotoIfConditionFalse(Label.L0, input_condition=4)
    DisableObjectActivation(3501101, obj_act_id=100)
    DisableObjectActivation(3501102, obj_act_id=100)
    DisableObjectActivation(3501103, obj_act_id=100)
    EnableMapCollision(collision=3504301)
    EnableMapCollision(collision=3504302)
    SetCollisionResState(collision=3504100, state=False)
    SetCollisionResState(collision=3504101, state=True)
    DisableMapCollision(collision=3504300)
    DisableMapCollision(collision=3504301)
    EndOfAnimation(obj=3501108, animation_id=1)
    EndOfAnimation(obj=3501104, animation_id=1)
    EndOfAnimation(obj=3501100, animation_id=1)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13501108)
    IfFlagDisabled(1, 13504100)
    IfFlagDisabled(1, 13501106)
    IfCharacterInsideRegion(-1, PLAYER, region=3502102)
    IfCharacterInsideRegion(-1, PLAYER, region=3502103)
    IfObjectActivated(-1, obj_act_id=13504101)
    IfFlagState(2, FlagState.Change, FlagType.Absolute, 13501107)
    IfFlagEnabled(2, 13501107)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13504100)
    EnableFlag(13501106)
    DisableObjectActivation(3501101, obj_act_id=100)
    DisableObjectActivation(3501102, obj_act_id=100)
    DisableObjectActivation(3501103, obj_act_id=100)
    EnableMapCollision(collision=3504301)
    EnableMapCollision(collision=3504302)
    ForceAnimation(3501108, 1)
    ForceAnimation(3501104, 1)
    ForceAnimation(3501100, 1, wait_for_completion=True)
    SetCollisionResState(collision=3504100, state=False)
    SetCollisionResState(collision=3504101, state=True)
    DisableMapCollision(collision=3504300)
    DisableMapCollision(collision=3504301)

    # --- 1 --- #
    DefineLabel(1)
    IfAllPlayersOutsideRegion(3, region=3502101)
    IfAllPlayersOutsideRegion(3, region=3502102)
    IfConditionTrue(0, input_condition=3)
    Wait(1.0)
    DisableFlag(13504100)
    DisableObjectActivation(3501101, obj_act_id=100)
    EnableObjectActivation(3501102, obj_act_id=100)
    EnableObjectActivation(3501103, obj_act_id=100)
    Restart()


@NeverRestart(13501103)
def Event_13501103():
    """Event 13501103"""
    IfFlagEnabled(4, 13504100)
    IfFlagDisabled(4, 13501106)
    GotoIfConditionFalse(Label.L0, input_condition=4)
    DisableObjectActivation(3501101, obj_act_id=100)
    DisableObjectActivation(3501102, obj_act_id=100)
    DisableObjectActivation(3501103, obj_act_id=100)
    EnableMapCollision(collision=3504300)
    EnableMapCollision(collision=3504301)
    SetCollisionResState(collision=3504101, state=False)
    SetCollisionResState(collision=3504100, state=True)
    DisableMapCollision(collision=3504301)
    DisableMapCollision(collision=3504302)
    EndOfAnimation(obj=3501108, animation_id=3)
    EndOfAnimation(obj=3501104, animation_id=3)
    EndOfAnimation(obj=3501100, animation_id=3)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13501108)
    IfFlagDisabled(1, 13504100)
    IfFlagEnabled(1, 13501106)
    IfCharacterInsideRegion(-1, PLAYER, region=3502101)
    IfObjectActivated(-1, obj_act_id=13504102)
    IfObjectActivated(-1, obj_act_id=13504103)
    IfFlagState(2, FlagState.Change, FlagType.Absolute, 13501107)
    IfFlagDisabled(2, 13501107)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13504100)
    DisableFlag(13501106)
    DisableObjectActivation(3501101, obj_act_id=100)
    DisableObjectActivation(3501102, obj_act_id=100)
    DisableObjectActivation(3501103, obj_act_id=100)
    EnableMapCollision(collision=3504300)
    EnableMapCollision(collision=3504301)
    ForceAnimation(3501108, 3)
    ForceAnimation(3501104, 3)
    ForceAnimation(3501100, 3, wait_for_completion=True)
    SetCollisionResState(collision=3504101, state=False)
    SetCollisionResState(collision=3504100, state=True)
    DisableMapCollision(collision=3504301)
    DisableMapCollision(collision=3504302)

    # --- 1 --- #
    DefineLabel(1)
    IfAllPlayersOutsideRegion(3, region=3502102)
    IfAllPlayersOutsideRegion(3, region=3502103)
    IfConditionTrue(0, input_condition=3)
    Wait(1.0)
    DisableFlag(13504100)
    EnableObjectActivation(3501101, obj_act_id=100)
    DisableObjectActivation(3501102, obj_act_id=100)
    DisableObjectActivation(3501103, obj_act_id=100)
    Restart()


@NeverRestart(13501104)
def Event_13501104():
    """Event 13501104"""
    DisableNetworkSync()
    IfFlagDisabled(1, 13501108)
    IfActionButtonParam(1, action_button_id=7100, entity=3501101)
    IfFlagDisabled(2, 13501108)
    IfActionButtonParam(2, action_button_id=7100, entity=3501102)
    IfFlagDisabled(3, 13501108)
    IfActionButtonParam(3, action_button_id=7100, entity=3501103)
    IfFlagEnabled(4, 13504100)
    IfActionButtonParam(4, action_button_id=7100, entity=3501101)
    IfFlagEnabled(5, 13504100)
    IfActionButtonParam(5, action_button_id=7100, entity=3501102)
    IfFlagEnabled(6, 13504100)
    IfActionButtonParam(6, action_button_id=7100, entity=3501103)
    IfFlagEnabled(7, 13501106)
    IfActionButtonParam(7, action_button_id=7100, entity=3501101)
    IfFlagDisabled(8, 13501106)
    IfActionButtonParam(8, action_button_id=7100, entity=3501102)
    IfFlagDisabled(9, 13501106)
    IfActionButtonParam(9, action_button_id=7100, entity=3501103)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(13501105)
def Event_13501105():
    """Event 13501105"""
    EndIfFlagEnabled(13501108)
    IfPlayerHasGood(1, 4017)
    IfActionButtonParam(1, action_button_id=3500101, entity=3501100)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9180)
    WaitFrames(frames=1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(35000000, cutscene_flags=0, player_id=10000, move_to_region=3502104, game_map=RESEARCH_HALL)
    Goto(Label.L0)
    IfCharacterHuman(2, PLAYER)
    SkipLinesIfConditionFalse(2, 2)
    PlayCutscene(
        35000000,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=3502104,
        game_map=RESEARCH_HALL,
    )
    Goto(Label.L0)
    IfCharacterInsideRegion(3, PLAYER, region=3502102)
    SkipLinesIfConditionTrue(2, 3)
    PlayCutscene(35000000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    Goto(Label.L0)
    EnableRandomFlagInRange(flag_range=(13505830, 13505833))
    SkipLinesIfFlagDisabled(2, 13505830)
    PlayCutscene(
        35000000,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=3502124,
        game_map=RESEARCH_HALL,
    )
    Goto(Label.L0)
    SkipLinesIfFlagDisabled(2, 13505831)
    PlayCutscene(
        35000000,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=3502125,
        game_map=RESEARCH_HALL,
    )
    Goto(Label.L0)
    SkipLinesIfFlagDisabled(2, 13505832)
    PlayCutscene(
        35000000,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=3502126,
        game_map=RESEARCH_HALL,
    )
    Goto(Label.L0)
    SkipLinesIfFlagDisabled(2, 13505833)
    PlayCutscene(
        35000000,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=3502127,
        game_map=RESEARCH_HALL,
    )
    Goto(Label.L0)

    # --- 0 --- #
    DefineLabel(0)
    WaitFrames(frames=1)
    DisableFlag(9180)
    EndOfAnimation(obj=3501100, animation_id=2)
    EndOfAnimation(obj=3501104, animation_id=2)
    EndOfAnimation(obj=3501108, animation_id=2)
    EnableFlag(13501106)
    EnableFlag(13501107)
    DisableObjectActivation(3501101, obj_act_id=100)
    EnableObjectActivation(3501102, obj_act_id=100)
    SetCollisionResState(collision=3504100, state=False)
    SetCollisionResState(collision=3504101, state=True)
    DisableMapCollision(collision=3504300)
    EnableMapCollision(collision=3504302)
    EnableFlag(13501108)
    Event_13501101()
    Event_13501102()
    Event_13501103()
    RestartEvent(event_id=13501104)


@NeverRestart(13501140)
def Event_13501140():
    """Event 13501140"""
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfPlayerDoesNotHaveGood(1, 4017)
    IfFlagDisabled(1, 13501105)
    IfActionButtonParam(1, action_button_id=3500100, entity=3501100)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010601, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(13501141)
def Event_13501141():
    """Event 13501141"""
    GotoIfFlagEnabled(Label.L0, flag=53502000)
    IfCharacterHuman(1, PLAYER)
    IfActionButtonParam(1, action_button_id=3500102, entity=3501104)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(3502000, host_only=False)
    EnableFlag(13401852)
    DisableFlag(3400)
    DisableFlag(3401)
    EnableFlag(3402)
    DisableFlag(3403)

    # --- 0 --- #
    DefineLabel(0)
    DisableObject(3501104)


@NeverRestart(13501142)
def Event_13501142():
    """Event 13501142"""
    GotoIfFlagEnabled(Label.L0, flag=53502000)
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    CreateObjectVFX(3501104, vfx_id=200, model_point=900201)
    IfFlagEnabled(0, 53502000)

    # --- 0 --- #
    DefineLabel(0)
    DeleteObjectVFX(3501104)


@NeverRestart(13501110)
def Event_13501110():
    """Event 13501110"""
    EndIfFlagEnabled(13504110)
    GotoIfFlagEnabled(Label.L0, flag=13501118)
    EnableFlag(13501116)
    EnableFlag(13501117)
    EndOfAnimation(obj=3501105, animation_id=0)
    DisableObjectActivation(3501106, obj_act_id=100)
    DisableObjectActivation(3501107, obj_act_id=100)
    Goto(Label.L2)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13501116)
    GotoIfConditionTrue(Label.L1, input_condition=1)
    DisableFlag(13501117)
    EndOfAnimation(obj=3501105, animation_id=4)
    EnableObjectActivation(3501106, obj_act_id=100)
    DisableObjectActivation(3501107, obj_act_id=100)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(13501117)
    EndOfAnimation(obj=3501105, animation_id=0)
    DisableObjectActivation(3501106, obj_act_id=100)
    EnableObjectActivation(3501107, obj_act_id=100)


@NeverRestart(13501111)
def Event_13501111():
    """Event 13501111"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 13501118)
    IfFlagEnabled(1, 13504110)
    IfConditionTrue(0, input_condition=1)
    IfFlagEnabled(2, 13501116)
    SkipLinesIfConditionTrue(2, 2)
    DisableFlag(13501117)
    SkipLines(1)
    EnableFlag(13501117)
    IfCharacterHuman(3, PLAYER)
    IfFlagEnabled(3, 13501118)
    IfFlagDisabled(3, 13504110)
    IfConditionTrue(0, input_condition=3)
    Restart()


@NeverRestart(13501112)
def Event_13501112():
    """Event 13501112"""
    IfFlagEnabled(3, 13504110)
    IfFlagEnabled(3, 13501116)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    DisableObjectActivation(3501106, obj_act_id=100)
    DisableObjectActivation(3501107, obj_act_id=100)
    EndOfAnimation(obj=3501105, animation_id=6)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13501118)
    IfFlagDisabled(1, 13504110)
    IfFlagDisabled(1, 13501116)
    IfCharacterInsideRegion(-1, PLAYER, region=3502107)
    IfObjectActivated(-1, obj_act_id=13504111)
    IfFlagState(2, FlagState.Change, FlagType.Absolute, 13501117)
    IfFlagEnabled(2, 13501117)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13504110)
    EnableFlag(13501116)
    DisableObjectActivation(3501106, obj_act_id=100)
    DisableObjectActivation(3501107, obj_act_id=100)
    ForceAnimation(3501105, 5, wait_for_completion=True)
    ForceAnimation(3501105, 6, wait_for_completion=True)

    # --- 1 --- #
    DefineLabel(1)
    IfAllPlayersOutsideRegion(0, region=3502106)
    DisableFlag(13504110)
    ForceAnimation(3501105, 7, wait_for_completion=True)
    DisableObjectActivation(3501106, obj_act_id=100)
    EnableObjectActivation(3501107, obj_act_id=100)
    Restart()


@NeverRestart(13501113)
def Event_13501113():
    """Event 13501113"""
    IfFlagEnabled(3, 13504110)
    IfFlagDisabled(3, 13501116)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    DisableObjectActivation(3501106, obj_act_id=100)
    DisableObjectActivation(3501107, obj_act_id=100)
    EndOfAnimation(obj=3501105, animation_id=2)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13501118)
    IfFlagDisabled(1, 13504110)
    IfFlagEnabled(1, 13501116)
    IfCharacterInsideRegion(-1, PLAYER, region=3502106)
    IfObjectActivated(-1, obj_act_id=13504112)
    IfFlagState(2, FlagState.Change, FlagType.Absolute, 13501117)
    IfFlagDisabled(2, 13501117)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13504110)
    DisableFlag(13501116)
    DisableObjectActivation(3501106, obj_act_id=100)
    DisableObjectActivation(3501107, obj_act_id=100)
    ForceAnimation(3501105, 1, wait_for_completion=True)
    ForceAnimation(3501105, 2, wait_for_completion=True)

    # --- 1 --- #
    DefineLabel(1)
    IfAllPlayersOutsideRegion(0, region=3502107)
    DisableFlag(13504110)
    ForceAnimation(3501105, 3, wait_for_completion=True)
    EnableObjectActivation(3501106, obj_act_id=100)
    DisableObjectActivation(3501107, obj_act_id=100)
    Restart()


@NeverRestart(13501114)
def Event_13501114():
    """Event 13501114"""
    DisableNetworkSync()
    IfFlagDisabled(1, 13501118)
    IfActionButtonParam(1, action_button_id=7100, entity=3501106)
    IfFlagDisabled(2, 13501118)
    IfActionButtonParam(2, action_button_id=7100, entity=3501107)
    IfFlagEnabled(3, 13504110)
    IfActionButtonParam(3, action_button_id=7100, entity=3501106)
    IfFlagEnabled(4, 13504110)
    IfActionButtonParam(4, action_button_id=7100, entity=3501107)
    IfFlagEnabled(5, 13501116)
    IfActionButtonParam(5, action_button_id=7100, entity=3501106)
    IfFlagDisabled(6, 13501116)
    IfActionButtonParam(6, action_button_id=7100, entity=3501107)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(13501115)
def Event_13501115():
    """Event 13501115"""
    EndIfFlagEnabled(13501118)
    IfCharacterInsideRegion(0, PLAYER, region=3502105)
    DisableObjectActivation(3501106, obj_act_id=100)
    EnableObjectActivation(3501107, obj_act_id=100)
    EnableFlag(13501118)


@NeverRestart(13501120)
def Event_13501120():
    """Event 13501120"""
    EndIfFlagEnabled(13504120)
    GotoIfFlagEnabled(Label.L0, flag=13501128)
    EnableFlag(13501126)
    EnableFlag(13501127)
    EndOfAnimation(obj=3501110, animation_id=0)
    DisableObjectActivation(3501111, obj_act_id=100)
    DisableObjectActivation(3501112, obj_act_id=100)
    Goto(Label.L2)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13501126)
    GotoIfConditionTrue(Label.L1, input_condition=1)
    DisableFlag(13501127)
    EndOfAnimation(obj=3501110, animation_id=4)
    EnableObjectActivation(3501111, obj_act_id=100)
    DisableObjectActivation(3501112, obj_act_id=100)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(13501127)
    EndOfAnimation(obj=3501110, animation_id=0)
    DisableObjectActivation(3501111, obj_act_id=100)
    EnableObjectActivation(3501112, obj_act_id=100)


@NeverRestart(13501121)
def Event_13501121():
    """Event 13501121"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 13501128)
    IfFlagEnabled(1, 13504120)
    IfConditionTrue(0, input_condition=1)
    IfFlagEnabled(2, 13501126)
    SkipLinesIfConditionTrue(2, 2)
    DisableFlag(13501127)
    SkipLines(1)
    EnableFlag(13501127)
    IfCharacterHuman(3, PLAYER)
    IfFlagEnabled(3, 13501128)
    IfFlagDisabled(3, 13504120)
    IfConditionTrue(0, input_condition=3)
    Restart()


@NeverRestart(13501122)
def Event_13501122():
    """Event 13501122"""
    IfFlagEnabled(3, 13504120)
    IfFlagEnabled(3, 13501126)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    DisableObjectActivation(3501111, obj_act_id=100)
    DisableObjectActivation(3501112, obj_act_id=100)
    EndOfAnimation(obj=3501110, animation_id=6)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13501128)
    IfFlagDisabled(1, 13504120)
    IfFlagDisabled(1, 13501126)
    IfCharacterInsideRegion(-1, PLAYER, region=3502112)
    IfObjectActivated(-1, obj_act_id=13504121)
    IfFlagState(2, FlagState.Change, FlagType.Absolute, 13501127)
    IfFlagEnabled(2, 13501127)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13504120)
    EnableFlag(13501126)
    DisableObjectActivation(3501111, obj_act_id=100)
    DisableObjectActivation(3501112, obj_act_id=100)
    ForceAnimation(3501110, 5, wait_for_completion=True)
    ForceAnimation(3501110, 6, wait_for_completion=True)

    # --- 1 --- #
    DefineLabel(1)
    IfAllPlayersOutsideRegion(0, region=3502111)
    DisableFlag(13504120)
    ForceAnimation(3501110, 7, wait_for_completion=True)
    DisableObjectActivation(3501111, obj_act_id=100)
    EnableObjectActivation(3501112, obj_act_id=100)
    Restart()


@NeverRestart(13501123)
def Event_13501123():
    """Event 13501123"""
    IfFlagEnabled(3, 13504120)
    IfFlagDisabled(3, 13501126)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    DisableObjectActivation(3501111, obj_act_id=100)
    DisableObjectActivation(3501112, obj_act_id=100)
    EndOfAnimation(obj=3501110, animation_id=2)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13501128)
    IfFlagDisabled(1, 13504120)
    IfFlagEnabled(1, 13501126)
    IfCharacterInsideRegion(-1, PLAYER, region=3502111)
    IfObjectActivated(-1, obj_act_id=13504122)
    IfFlagState(2, FlagState.Change, FlagType.Absolute, 13501127)
    IfFlagDisabled(2, 13501127)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13504120)
    DisableFlag(13501126)
    DisableObjectActivation(3501111, obj_act_id=100)
    DisableObjectActivation(3501112, obj_act_id=100)
    ForceAnimation(3501110, 1, wait_for_completion=True)
    ForceAnimation(3501110, 2, wait_for_completion=True)

    # --- 1 --- #
    DefineLabel(1)
    IfAllPlayersOutsideRegion(0, region=3502112)
    DisableFlag(13504120)
    ForceAnimation(3501110, 3, wait_for_completion=True)
    EnableObjectActivation(3501111, obj_act_id=100)
    DisableObjectActivation(3501112, obj_act_id=100)
    Restart()


@NeverRestart(13501124)
def Event_13501124():
    """Event 13501124"""
    DisableNetworkSync()
    IfFlagDisabled(1, 13501128)
    IfActionButtonParam(1, action_button_id=7100, entity=3501111)
    IfFlagDisabled(2, 13501128)
    IfActionButtonParam(2, action_button_id=7100, entity=3501112)
    IfFlagEnabled(3, 13504120)
    IfActionButtonParam(3, action_button_id=7100, entity=3501111)
    IfFlagEnabled(4, 13504120)
    IfActionButtonParam(4, action_button_id=7100, entity=3501112)
    IfFlagEnabled(5, 13501126)
    IfActionButtonParam(5, action_button_id=7100, entity=3501111)
    IfFlagDisabled(6, 13501126)
    IfActionButtonParam(6, action_button_id=7100, entity=3501112)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(13501125)
def Event_13501125():
    """Event 13501125"""
    EndIfFlagEnabled(13501128)
    IfCharacterInsideRegion(-1, PLAYER, region=3502110)
    IfFlagEnabled(-1, 13500100)
    IfConditionTrue(0, input_condition=-1)
    DisableObjectActivation(3501111, obj_act_id=100)
    EnableObjectActivation(3501112, obj_act_id=100)
    EnableFlag(13501128)


@NeverRestart(13501200)
def Event_13501200(
    _,
    obj: int,
    obj_act_id: int,
    animation_id: int,
    obj_act_id_1: int,
    obj_act_id_2: int,
    obj_act_id_3: int,
):
    """Event 13501200"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_3)
    NotifyDoorEventSoundDampening(obj=obj, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(-1, obj_act_id=obj_act_id)
    IfObjectActivated(-1, obj_act_id=obj_act_id_2)
    IfConditionTrue(0, input_condition=-1)
    Wait(1.0)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_3)


@NeverRestart(13501250)
def Event_13501250():
    """Event 13501250"""
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(obj=3501160, animation_id=1)
    DisableObjectActivation(3501160, obj_act_id=3500062)
    DisableObjectActivation(3501160, obj_act_id=3500061)
    NotifyDoorEventSoundDampening(obj=3501160, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(1, obj_act_id=13504269)
    IfFlagEnabled(2, 13500100)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=2)

    # --- 1 --- #
    DefineLabel(1)
    Wait(1.0)
    DisableObjectActivation(3501160, obj_act_id=3500062)
    DisableObjectActivation(3501160, obj_act_id=3500061)
    End()

    # --- 2 --- #
    DefineLabel(2)
    ForceAnimation(3501160, 1)
    DisableObjectActivation(3501160, obj_act_id=3500062)
    DisableObjectActivation(3501160, obj_act_id=3500061)
    NotifyDoorEventSoundDampening(obj=3501160, state=DoorState.DoorOpening)
    End()


@NeverRestart(13501400)
def Event_13501400(_, obj: int, obj_act_id: int, obj_act_id_1: int):
    """Event 13501400"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    EnableTreasure(obj=obj)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@RestartOnRest(13504799)
def Event_13504799():
    """Event 13504799"""
    CreateProjectileOwner(entity=3500799)


@NeverRestart(13500100)
def Event_13500100():
    """Event 13500100"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableObjectActivation(3501210, obj_act_id=3500110)
    EndOfAnimation(obj=3501210, animation_id=3)
    EndOfAnimation(obj=3501211, animation_id=2)
    EndOfAnimation(obj=3501212, animation_id=2)
    EndOfAnimation(obj=3501220, animation_id=2)
    EndOfAnimation(obj=3501221, animation_id=2)
    EndOfAnimation(obj=3501231, animation_id=2)
    EndOfAnimation(obj=3501232, animation_id=2)
    EndOfAnimation(obj=3501233, animation_id=2)
    EndOfAnimation(obj=3501234, animation_id=2)
    EndOfAnimation(obj=3501235, animation_id=2)
    SetCollisionResState(collision=3504200, state=False)
    SetCollisionResState(collision=3504201, state=False)
    SetCollisionResState(collision=3504202, state=False)
    SetCollisionResState(collision=3504203, state=False)
    SetCollisionResState(collision=3504204, state=False)
    SetCollisionResState(collision=3504210, state=False)
    SetCollisionResState(collision=3504211, state=False)
    SetCollisionResState(collision=3504212, state=False)
    SetCollisionResState(collision=3504213, state=False)
    SetCollisionResState(collision=3504214, state=False)
    DisableMapCollision(collision=3504210)
    DisableMapCollision(collision=3504211)
    DisableMapCollision(collision=3504212)
    DisableMapCollision(collision=3504213)
    DisableMapCollision(collision=3504214)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SetCollisionResState(collision=3504205, state=False)
    SetCollisionResState(collision=3504206, state=False)
    SetCollisionResState(collision=3504207, state=False)
    SetCollisionResState(collision=3504208, state=False)
    SetCollisionResState(collision=3504209, state=False)
    SetCollisionResState(collision=3504215, state=False)
    SetCollisionResState(collision=3504216, state=False)
    SetCollisionResState(collision=3504217, state=False)
    SetCollisionResState(collision=3504218, state=False)
    SetCollisionResState(collision=3504219, state=False)
    DisableMapCollision(collision=3504215)
    DisableMapCollision(collision=3504216)
    DisableMapCollision(collision=3504217)
    DisableMapCollision(collision=3504218)
    DisableMapCollision(collision=3504219)
    IfObjectActivated(0, obj_act_id=13504280)
    EnableFlag(13505500)
    ForceAnimation(3501210, 2)
    ForceAnimation(3501211, 1)
    ForceAnimation(3501212, 1)
    ForceAnimation(3501220, 1)
    ForceAnimation(3501221, 1)
    ForceAnimation(3501231, 1)
    ForceAnimation(3501232, 1)
    ForceAnimation(3501233, 1)
    ForceAnimation(3501234, 1)
    ForceAnimation(3501235, 1, wait_for_completion=True)
    SetCollisionResState(collision=3504200, state=False)
    SetCollisionResState(collision=3504201, state=False)
    SetCollisionResState(collision=3504202, state=False)
    SetCollisionResState(collision=3504203, state=False)
    SetCollisionResState(collision=3504204, state=False)
    SetCollisionResState(collision=3504210, state=False)
    SetCollisionResState(collision=3504211, state=False)
    SetCollisionResState(collision=3504212, state=False)
    SetCollisionResState(collision=3504213, state=False)
    SetCollisionResState(collision=3504214, state=False)
    DisableMapCollision(collision=3504210)
    DisableMapCollision(collision=3504211)
    DisableMapCollision(collision=3504212)
    DisableMapCollision(collision=3504213)
    DisableMapCollision(collision=3504214)
    SetCollisionResState(collision=3504205, state=True)
    SetCollisionResState(collision=3504206, state=True)
    SetCollisionResState(collision=3504207, state=True)
    SetCollisionResState(collision=3504208, state=True)
    SetCollisionResState(collision=3504209, state=True)
    EnableMapCollision(collision=3504215)
    EnableMapCollision(collision=3504216)
    EnableMapCollision(collision=3504217)
    EnableMapCollision(collision=3504218)
    EnableMapCollision(collision=3504219)
    DisableFlag(13505500)
    End()


@NeverRestart(13500105)
def Event_13500105():
    """Event 13500105"""
    DisableSoundEvent(sound_id=3503202)
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    IfStandingOnCollision(1, 3504020)
    IfConditionTrue(0, input_condition=1)
    PlaySoundEffect(PLAYER, 350000010, sound_type=SoundType.a_Ambient)


@NeverRestart(13500106)
def Event_13500106():
    """Event 13500106"""
    DisableSoundEvent(sound_id=3503203)
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    IfStandingOnCollision(1, 3504815)
    IfConditionTrue(0, input_condition=1)
    PlaySoundEffect(PLAYER, 350000011, sound_type=SoundType.a_Ambient)


@RestartOnRest(13500110)
def Event_13500110():
    """Event 13500110"""
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableObject(3501751)
    IfFlagEnabled(0, 9469)
    EnableObject(3501751)

    # --- 0 --- #
    DefineLabel(0)
    DisableMapPiece(map_piece_id=3501750)
    End()


@RestartOnRest(13500111)
def Event_13500111():
    """Event 13500111"""
    DisableNetworkSync()
    GotoIfThisEventFlagDisabled(Label.L0)
    DeleteVFX(3503120, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfEntityWithinDistance(0, entity=PLAYER, other_entity=3502120, radius=7.0)
    DeleteVFX(3503120)


@RestartOnRest(13500120)
def Event_13500120():
    """Event 13500120"""
    GotoIfFlagDisabled(Label.L0, flag=53500840)
    EndOfAnimation(obj=3501280, animation_id=2)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(3501280, 0, loop=True)
    IfFlagEnabled(0, 53500840)
    ForceAnimation(3501280, 1, wait_for_completion=True)
    End()


@RestartOnRest(13500130)
def Event_13500130():
    """Event 13500130"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=13500101)
    Move(3500552, destination=3502420, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(3500552, 9008, loop=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(3500552, 9008, loop=True)
    IfFlagEnabled(0, 13500100)
    ForceAnimation(3500552, 2004)
    ChangePatrolBehavior(3500552, patrol_information_id=3503320)
    ReplanAI(3500552)
    IfCharacterInsideRegion(0, 3500552, region=3502420)
    ForceAnimation(3500552, 9008, loop=True)


@RestartOnRest(13500140)
def Event_13500140():
    """Event 13500140"""
    IfHasAIStatus(0, 3500764, ai_status=AIStatusType.Battle)
    ForceAnimation(3500764, 3010, loop=True)
    IfHasAIStatus(-1, 3500764, ai_status=AIStatusType.Normal)
    IfHasAIStatus(-1, 3500764, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, 3500764, ai_status=AIStatusType.Search)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(3500764, 0, loop=True)
    Restart()


@RestartOnRest(13500150)
def Event_13500150():
    """Event 13500150"""
    ForceAnimation(3500932, 103020, loop=True)
    AddSpecialEffect(3500932, 8015)
    DisableAI(3500932)
    DisableAI(3500931)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=3502308)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=3500932, radius=5.0)
    IfAttackedWithDamageType(-2, attacked_entity=3500932)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(3, input_condition=-1)
    IfCharacterInsideRegion(3, PLAYER, region=3502328)
    IfEntityWithinDistance(-3, entity=PLAYER, other_entity=3500931, radius=2.0)
    IfAttackedWithDamageType(-3, attacked_entity=3500931)
    IfConditionTrue(4, input_condition=-3)
    IfConditionTrue(-4, input_condition=1)
    IfConditionTrue(-4, input_condition=2)
    IfConditionTrue(-4, input_condition=3)
    IfConditionTrue(-4, input_condition=4)
    IfConditionTrue(0, input_condition=-4)
    ForceAnimation(3500932, 103023)
    EnableAI(3500932)
    IfFramesElapsed(0, frames=40)
    EnableAI(3500931)


@RestartOnRest(13500400)
def Event_13500400(_, character: int, destination: int, region: int):
    """Event 13500400"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    Kill(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(0, input_condition=1)

    # --- 1 --- #
    DefineLabel(1)
    EnableCharacter(character)


@RestartOnRest(13500410)
def Event_13500410(_, character: int, character_1: int):
    """Event 13500410"""
    GotoIfFlagEnabled(Label.L0, flag=13500101)
    DisableBackread(character_1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableBackread(character)
    End()


@RestartOnRest(13500418)
def Event_13500418(_, character: int, character_1: int, destination: int):
    """Event 13500418"""
    GotoIfFlagEnabled(Label.L0, flag=13500101)
    DisableAI(character_1)
    EnableGravity(character_1)
    DisableHealthBar(character_1)
    EnableImmortality(character_1)
    ReferDamageToEntity(character, target_entity=character_1)
    IfFlagEnabled(1, 13500100)
    IfCharacterAlive(1, character)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    EnableAI(character_1)
    DisableGravity(character_1)
    EnableHealthBar(character_1)
    DisableImmortality(character_1)
    Move(character_1, destination=destination, destination_type=CoordEntityType.Region, set_draw_parent=0)
    ReplanAI(character_1)
    End()


@RestartOnRest(13500420)
def Event_13500420(_, entity: int, animation_id: int, frames: int):
    """Event 13500420"""
    EndIfFlagEnabled(13500101)
    EndIfThisEventSlotFlagEnabled()
    IfObjectActivated(0, obj_act_id=13504280)
    WaitFrames(frames=frames)
    ForceAnimation(entity, animation_id)


@RestartOnRest(13500430)
def Event_13500430(_, flag: int, character: int, animation_id: int):
    """Event 13500430"""
    EndIfFlagEnabled(flag)
    IfAttackedWithDamageType(1, attacked_entity=character)
    IfConditionTrue(-1, input_condition=1)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(2, input_condition=-1)
    IfFlagEnabled(2, flag)
    IfConditionTrue(0, input_condition=2)
    EndIfFinishedConditionTrue(input_condition=1)
    ForceAnimation(character, animation_id)


@RestartOnRest(13500450)
def Event_13500450(_, character: int, flag: int):
    """Event 13500450"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableCharacter(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(1, PLAYER)
    SkipLinesIfClient(1)
    IfFlagEnabled(1, flag)
    IfConditionTrue(0, input_condition=1)
    Wait(0.0)


@RestartOnRest(13500460)
def Event_13500460(_, character: int, animation_id: int, flag: int):
    """Event 13500460"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    ForceAnimation(character, animation_id, loop=True)
    IfAttackedWithDamageType(0, attacked_entity=character)
    Kill(character, award_souls=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SetDistanceLimitForConversationStateChanges(character=character, distance=1.0)
    DisableCharacter(character)
    DisableBackread(character)


@NeverRestart(13500500)
def Event_13500500(_, entity: int, action_button_id: int, text: int):
    """Event 13500500"""
    DisableNetworkSync()
    IfActionButtonParam(0, action_button_id=action_button_id, entity=entity)
    DisplayDialog(text=text, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest(13505050)
def Event_13505050(_, character: int):
    """Event 13505050"""
    AddSpecialEffect(character, 5410)
    SetAIParamID(character, ai_param_id=402040)
    ReplanAI(character)
    IfObjectDestroyed(-1, 3501700)
    IfObjectDestroyed(-1, 3501701)
    IfObjectDestroyed(-1, 3501702)
    IfObjectDestroyed(-1, 3501703)
    IfObjectDestroyed(-1, 3501704)
    IfObjectDestroyed(-1, 3501705)
    IfHasAIStatus(-2, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-2, character, ai_status=AIStatusType.Search)
    IfHasAIStatus(-2, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(-3, input_condition=-1)
    IfConditionTrue(-3, input_condition=-2)
    IfConditionTrue(0, input_condition=-3)
    CancelSpecialEffect(character, 5410)
    SetCharacterEventTarget(character, region=PLAYER)
    SetAIParamID(character, ai_param_id=402005)
    ReplanAI(character)


@RestartOnRest(13505060)
def Event_13505060():
    """Event 13505060"""
    IfCharacterTargeting(-1, targeting_character=3500750, targeted_character=PLAYER)
    IfCharacterTargeting(-1, targeting_character=3500760, targeted_character=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(3500750, ai_param_id=270352)
    SetAIParamID(3500760, ai_param_id=262912)


@RestartOnRest(13505100)
def Event_13505100(_, character: int):
    """Event 13505100"""
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Search)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(character, 8014)

    # --- 0 --- #
    DefineLabel(0)
    IfHasAIStatus(-2, character, ai_status=AIStatusType.Normal)
    IfCharacterDead(-2, character)
    IfCharacterBackreadDisabled(-2, character)
    IfConditionTrue(0, input_condition=-2)
    CancelSpecialEffect(character, 8014)
    Restart()


@RestartOnRest(13505110)
def Event_13505110(_, character: int, region: int):
    """Event 13505110"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    EnableInvincibility(character)
    DisableAI(character)
    DisableHealthBar(character)
    DisableAnimations(character)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    DisableInvincibility(character)
    EnableAI(character)
    EnableHealthBar(character)
    EnableAnimations(character)


@RestartOnRest(13505200)
def Event_13505200(_, character: int, patrol_information_id: int):
    """Event 13505200"""
    IfFlagEnabled(0, 13500100)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    ReplanAI(character)


@NeverRestart(13505300)
def Event_13505300(_, character: int):
    """Event 13505300"""
    EndIfFlagEnabled(13500101)
    IfFlagEnabled(1, 13505500)
    IfCharacterInsideRegion(1, character, region=3502390)
    IfConditionTrue(0, input_condition=1)
    SetBackreadStateAlternate(character, True)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableCharacterCollision(character)
    DisableAI(character)
    IfFlagDisabled(0, 13505500)
    EnableAI(character)
    SetBackreadStateAlternate(character, False)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    ReplanAI(character)
    End()


@RestartOnRest(13505400)
def Event_13505400(_, character: int, region: int, radius: float, region_1: int):
    """Event 13505400"""
    IfThisEventSlotFlagDisabled(5)
    IfCharacterAlive(5, character)
    GotoIfConditionTrue(Label.L0, input_condition=5)
    EnableGravity(character)
    EnableCharacterCollision(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacterCollision(character)
    DisableGravity(character)
    ForceAnimation(character, 9000, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character, radius=radius)
    IfAttackedWithDamageType(-2, attacked_entity=character)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region_1)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character, radius=radius)
    IfAttackedWithDamageType(-2, attacked_entity=character)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    ForceAnimation(character, 9060, wait_for_completion=True)
    EnableGravity(character)
    WaitFrames(frames=15)
    EnableCharacterCollision(character)


@RestartOnRest(13505410)
def Event_13505410():
    """Event 13505410"""
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=3502342)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(0, input_condition=-2)
    SetTeamType(3500764, TeamType.Enemy2)
    Wait(1.0)
    IfCharacterHuman(-3, PLAYER)
    IfCharacterWhitePhantom(-3, PLAYER)
    IfConditionTrue(2, input_condition=-3)
    IfCharacterInsideRegion(2, PLAYER, region=3502342)
    IfConditionTrue(-4, input_condition=2)
    IfConditionFalse(0, input_condition=-4)
    SetTeamType(3500764, TeamType.Enemy1)
    Restart()


@RestartOnRest(13505450)
def Event_13505450(_, character: int, region: int, radius: float, animation_id: int):
    """Event 13505450"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EnableAI(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(character)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character, radius=radius)
    IfAttackedWithDamageType(-2, attacked_entity=character)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    SkipLinesIfFinishedConditionTrue(1, condition=2)
    ForceAnimation(character, animation_id)
    EnableAI(character)
    ReplanAI(character)


@RestartOnRest(13505470)
def Event_13505470(_, character: int, animation_id: int, animation_id_1: int, ai_param_id: int):
    """Event 13505470"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(character, animation_id)
    SetAIParamID(character, ai_param_id=402040)
    IfAttackedWithDamageType(1, attacked_entity=character)
    IfConditionTrue(-1, input_condition=1)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    ForceAnimation(character, animation_id_1)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(character, ai_param_id=ai_param_id)
    ReplanAI(character)


@RestartOnRest(13505510)
def Event_13505510(_, character: int, region: int, radius: float, seconds: float):
    """Event 13505510"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character, radius=radius)
    IfAttackedWithDamageType(-2, attacked_entity=character)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    Wait(seconds)
    EnableAI(character)


@RestartOnRest(13505570)
def Event_13505570(
    _,
    character: int,
    region: int,
    radius: float,
    seconds: float,
    region_1: int,
    region_2: int,
    patrol_information_id: int,
):
    """Event 13505570"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character, radius=radius)
    IfAttackedWithDamageType(-2, attacked_entity=character)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    Wait(seconds)
    EnableAI(character)
    IfCharacterInsideRegion(4, character, region=region_1)
    IfHasAIStatus(4, character, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=4)
    DisableAI(character)
    IfCharacterHuman(-5, PLAYER)
    IfCharacterWhitePhantom(-5, PLAYER)
    IfConditionTrue(5, input_condition=-5)
    IfCharacterInsideRegion(5, PLAYER, region=region_2)
    IfEntityWithinDistance(-6, entity=PLAYER, other_entity=character, radius=radius)
    IfAttackedWithDamageType(-6, attacked_entity=character)
    IfConditionTrue(-7, input_condition=5)
    IfConditionTrue(-7, input_condition=-6)
    IfConditionTrue(0, input_condition=-7)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    EnableAI(character)


@RestartOnRest(13505580)
def Event_13505580(_, character: int, region: int, radius: float):
    """Event 13505580"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfFlagEnabled(0, 13500100)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character, radius=radius)
    IfAttackedWithDamageType(-2, attacked_entity=character)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    ForceAnimation(character, 0)
    EnableAI(character)


@RestartOnRest(13505590)
def Event_13505590(
    _,
    character: int,
    region: int,
    radius: float,
    animation_id: int,
    animation_id_1: int,
    seconds: float,
    seconds_1: float,
    region_1: int,
):
    """Event 13505590"""
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(character, animation_id)
    DisableAI(character)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character, radius=radius)
    IfAttackedWithDamageType(-2, attacked_entity=character)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(3, input_condition=-1)
    IfCharacterInsideRegion(3, PLAYER, region=region_1)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(0, input_condition=-3)
    Wait(seconds)
    ForceAnimation(character, animation_id_1)
    Wait(seconds_1)
    EnableAI(character)


@RestartOnRest(13505610)
def Event_13505610(
    _,
    character: int,
    region: int,
    radius: float,
    animation_id: int,
    animation_id_1: int,
    seconds: float,
    seconds_1: float,
):
    """Event 13505610"""
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(character, animation_id)
    DisableAI(character)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character, radius=radius)
    IfAttackedWithDamageType(-2, attacked_entity=character)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    IfFlagEnabled(0, 53500820)
    IfTimeElapsed(0, seconds=seconds)
    ForceAnimation(character, animation_id_1)
    IfTimeElapsed(0, seconds=seconds_1)
    EnableAI(character)


@RestartOnRest(13505630)
def Event_13505630(_, character: int, region: int, seconds: float, seconds_1: float):
    """Event 13505630"""
    EndIfThisEventSlotFlagEnabled()
    DisableCharacter(character)
    EndIfFlagEnabled(13500101)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(0, input_condition=1)
    Wait(seconds)
    EndIfFlagEnabled(13500100)
    EnableCharacter(character)
    EnableInvincibility(character)
    Wait(seconds_1)
    DisableInvincibility(character)


@RestartOnRest(13505640)
def Event_13505640(_, character: int, animation_id: int):
    """Event 13505640"""
    ForceAnimation(character, animation_id, loop=True)
    AddSpecialEffect(character, 5300)


@RestartOnRest(13505650)
def Event_13505650(_, character: int):
    """Event 13505650"""
    AddSpecialEffect(character, 5410)
    IfHasAIStatus(-1, 0, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, 0, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, 0, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(character, 5410)


@RestartOnRest(13505700)
def Event_13505700(_, character: int, animation_id: int):
    """Event 13505700"""
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(character, animation_id, wait_for_completion=True)
    SetAIParamID(character, ai_param_id=402011)
    ReplanAI(character)


@RestartOnRest(13505740)
def Event_13505740(_, character: int):
    """Event 13505740"""
    Kill(character)


@RestartOnRest(13505750)
def Event_13505750(
    _,
    character: int,
    region: int,
    region_1: int,
    patrol_information_id: int,
    seconds: float,
    left: int,
):
    """Event 13505750"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=region)
    IfCharacterInsideRegion(-2, PLAYER, region=region_1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    Wait(seconds)

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfEqual(1, left=left, right=0)
    AddSpecialEffect(character, 5000)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    ReplanAI(character)


@RestartOnRest(13505780)
def Event_13505780(_, character: int):
    """Event 13505780"""
    EndIfFlagEnabled(13500100)
    DisableCharacter(character)
    IfFlagEnabled(0, 13500100)
    EnableCharacter(character)


@RestartOnRest(13505797)
def Event_13505797(_, obj: int):
    """Event 13505797"""
    EndIfFlagEnabled(13500100)
    DisableObject(obj)
    DisableTreasure(obj=obj)
    IfFlagEnabled(0, 13500100)
    EnableObject(obj)
    EnableTreasure(obj=obj)


@RestartOnRest(13505800)
def Event_13505800(_, region: int, entity: int, obj: int, projectile_id: int, character: int):
    """Event 13505800"""
    RestoreObject(obj)
    ForceAnimation(entity, 2)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(0, PLAYER, region=region)
    ForceAnimation(entity, 1, wait_for_completion=True)
    WaitFrames(frames=25)
    DestroyObject(obj)
    SkipLinesIfFlagEnabled(2, 6603)
    ShootProjectile(
        owner_entity=3500799,
        projectile_id=projectile_id,
        model_point=200,
        behavior_id=6350,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L1)
    ShootProjectile(
        owner_entity=3500799,
        projectile_id=projectile_id,
        model_point=200,
        behavior_id=6352,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- 1 --- #
    DefineLabel(1)
    SetCharacterEventTarget(character, region=PLAYER)
    ReplanAI(character)


@RestartOnRest(13505810)
def Event_13505810(_, region: int, entity: int, obj: int, projectile_id: int, projectile_id_1: int, character: int):
    """Event 13505810"""
    RestoreObject(obj)
    ForceAnimation(entity, 2)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(0, PLAYER, region=region)
    ForceAnimation(entity, 1, wait_for_completion=True)
    WaitFrames(frames=25)
    ShootProjectile(
        owner_entity=3500799,
        projectile_id=projectile_id,
        model_point=200,
        behavior_id=6350,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(frames=20)
    ShootProjectile(
        owner_entity=3500799,
        projectile_id=projectile_id_1,
        model_point=200,
        behavior_id=6350,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SetCharacterEventTarget(character, region=PLAYER)
    ReplanAI(character)


@RestartOnRest(13505820)
def Event_13505820(
    _,
    character: int,
    animation_id: int,
    animation_id_1: int,
    frames: int,
    patrol_information_id: int,
    region: int,
):
    """Event 13505820"""
    ForceAnimation(character, animation_id, loop=True)
    IfCharacterInsideRegion(-1, PLAYER, region=3502322)
    IfCharacterInsideRegion(-1, PLAYER, region=3502323)
    IfCharacterInsideRegion(-1, PLAYER, region=3502324)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=frames)
    ForceAnimation(character, animation_id_1)
    SetCharacterEventTarget(character, region=PLAYER)
    ReplanAI(character)
    WaitFrames(frames=frames)
    IfCharacterOutsideRegion(0, PLAYER, region=3502327)
    WaitFrames(frames=20)
    ClearTargetList(character)
    ReplanAI(character)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    WaitFrames(frames=120)
    IfCharacterInsideRegion(0, character, region=region)
    WaitFrames(frames=20)
    Restart()


@NeverRestart(13500900)
def Event_13500900(_, character: int, first_flag: int, last_flag: int, last_flag_1: int, flag: int):
    """Event 13500900"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagRangeAnyEnabled(flag_range=(first_flag, last_flag_1))
    IfCharacterDead(1, character)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    SaveRequest()


@NeverRestart(13500910)
def Event_13500910(_, attacked_entity: int, flag: int):
    """Event 13500910"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(0, attacked_entity=attacked_entity, attacker=PLAYER)
    WaitFrames(frames=1)
    IfAttackedWithDamageType(0, attacked_entity=attacked_entity, attacker=PLAYER)
    WaitFrames(frames=1)
    IfAttackedWithDamageType(0, attacked_entity=attacked_entity, attacker=PLAYER)
    WaitFrames(frames=1)
    EnableFlag(flag)


@NeverRestart(13500920)
def Event_13500920(_, character: int, flag: int, first_flag: int, last_flag: int, flag_1: int):
    """Event 13500920"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(flag)
    IfFlagEnabled(-1, flag)
    IfHealthLessThanOrEqual(-1, character, value=0.8999999761581421)
    IfConditionTrue(1, input_condition=-1)
    IfHealthNotEqual(1, character, value=0.0)
    IfConditionTrue(0, input_condition=1)
    SetTeamType(character, TeamType.HostileNPC)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag_1)
    SaveRequest()


@NeverRestart(13500940)
def Event_13500940(_, character: int):
    """Event 13500940"""
    GotoIfFlagRangeAnyEnabled(Label.L0, flag_range=(1730, 1749))
    EnableFlag(1735)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=1730)
    GotoIfFlagEnabled(Label.L6, flag=1735)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    DisableAnimations(character)
    DisableGravity(3500938)
    DropMandatoryTreasure(3500938)
    ForceAnimation(character, 103162, loop=True, skip_transition=True)
    End()

    # --- 6 --- #
    DefineLabel(6)
    ForceAnimation(character, 103160, loop=True, skip_transition=True)
    DisableGravity(3500938)
    EndIfFlagEnabled(73500412)
    EnableInvincibility(character)
    End()


@NeverRestart(13500942)
def Event_13500942(_, character: int, region: int, flag: int):
    """Event 13500942"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagRangeAnyEnabled(flag_range=(1730, 1734))
    DisableFlag(flag)
    IfCharacterInsideRegion(0, character, region=region)
    EnableFlag(flag)
    IfCharacterOutsideRegion(0, character, region=region)
    DisableFlag(flag)
    Restart()


@NeverRestart(13500941)
def Event_13500941():
    """Event 13500941"""
    GotoIfFlagDisabled(Label.L0, flag=73500412)
    EndOfAnimation(obj=3501300, animation_id=2)
    DisableObjectActivation(3501300, obj_act_id=3500010)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=13504245)
    DisableInvincibility(3500901)
    DisableObjectActivation(3501300, obj_act_id=3500010)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    Wait(2.0)
    EnableFlag(73500412)


@NeverRestart(13500943)
def Event_13500943(_, character: int):
    """Event 13500943"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagRangeAnyEnabled(flag_range=(1730, 1734))
    DisableFlag(73500411)
    GotoIfFlagEnabled(Label.L0, flag=13601400)
    ForceAnimation(character, 103164, loop=True, skip_transition=True)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 103160, loop=True, skip_transition=True)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(0, 73500411)
    IfHealthEqual(1, character, value=0.0)
    EndIfConditionTrue(1)
    ForceAnimation(character, 103161, loop=True, skip_transition=True)
    IfFlagDisabled(0, 73500411)
    IfHealthEqual(1, character, value=0.0)
    EndIfConditionTrue(1)
    Restart()


@NeverRestart(13500944)
def Event_13500944(_, character: int):
    """Event 13500944"""
    EndIfFlagRangeAnyEnabled(flag_range=(1730, 1734))
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(1, attacked_entity=character)
    IfConditionTrue(0, input_condition=1)
    Kill(character, award_souls=True)
    ForceAnimation(character, 103162, skip_transition=True)


@NeverRestart(13500945)
def Event_13500945(_, character: int, obj: int, obj_1: int, obj_2: int, obj_3: int, obj_4: int, flag: int):
    """Event 13500945"""
    IfCharacterHuman(-15, PLAYER)
    GotoIfConditionFalse(Label.L9, input_condition=-15)
    GotoIfFlagRangeAnyEnabled(Label.L0, flag_range=(1650, 1669))
    DisableFlagRange((1650, 1669))
    EnableFlag(1651)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 1660)
    IfFlagRangeAnyEnabled(1, flag_range=(1722, 1723))
    IfFlagEnabled(1, 73500602)
    GotoIfConditionFalse(Label.L8, input_condition=1)
    DisableFlagRange((1650, 1669))
    EnableFlag(1651)

    # --- 8 --- #
    DefineLabel(8)

    # --- 9 --- #
    DefineLabel(9)
    DisableObject(obj)
    DisableObject(obj_2)
    DisableObject(obj_3)
    DisableObject(obj_4)
    GotoIfFlagEnabled(Label.L0, flag=1660)
    GotoIfFlagEnabled(Label.L1, flag=1650)
    GotoIfFlagEnabled(Label.L2, flag=1651)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SetTeamType(character, TeamType.Ally)
    DisableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, 7000)
    EnableObjectInvulnerability(obj_1)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    EndIfFlagEnabled(flag)
    CreateObjectVFX(obj, vfx_id=200, model_point=900201)
    EnableObjectInvulnerability(obj_1)
    EnableObject(obj_2)
    EnableObjectInvulnerability(obj_2)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    EnableObject(obj_4)
    EnableObjectInvulnerability(obj_4)
    EndIfFlagEnabled(flag)
    EnableObjectInvulnerability(obj_1)
    EnableObject(obj_3)
    EnableObjectInvulnerability(obj_3)
    End()


@NeverRestart(13500946)
def Event_13500946(_, character: int, obj: int):
    """Event 13500946"""
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    IfFlagEnabled(1, 1660)
    IfAttackedWithDamageType(1, attacked_entity=character)
    IfConditionTrue(0, input_condition=1)
    Kill(character, award_souls=True)
    IfFlagEnabled(0, 1650)
    CreateObjectVFX(obj, vfx_id=200, model_point=900201)


@NeverRestart(13500948)
def Event_13500948(_, entity: int):
    """Event 13500948"""
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    EndIfFlagEnabled(13501801)
    IfFlagRangeAnyEnabled(1, flag_range=(1650, 1651))
    IfActionButtonParam(1, action_button_id=3500910, entity=entity)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13500947)


@NeverRestart(13500949)
def Event_13500949(_, character: int, flag: int):
    """Event 13500949"""
    DisableFlag(flag)
    IfFlagEnabled(0, flag)
    IfHealthEqual(1, character, value=0.0)
    EndIfConditionTrue(1)
    ForceAnimation(character, 7003, loop=True, skip_transition=True)
    IfFlagDisabled(0, flag)
    IfHealthEqual(2, character, value=0.0)
    EndIfConditionTrue(2)
    ForceAnimation(character, 7000, loop=True, skip_transition=True)
    Restart()


@NeverRestart(13500950)
def Event_13500950(_, character: int):
    """Event 13500950"""
    IfCharacterHuman(-15, PLAYER)
    GotoIfConditionFalse(Label.L9, input_condition=-1)
    GotoIfFlagRangeAnyEnabled(Label.L0, flag_range=(1710, 1729))
    DisableFlagRange((1710, 1729))
    EnableFlag(1720)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagRangeAnyEnabled(1, flag_range=(1720, 1721))
    IfFlagEnabled(1, 73400403)
    IfFlagEnabled(1, 13500100)
    GotoIfConditionFalse(Label.L1, input_condition=1)
    DisableFlagRange((1710, 1729))
    EnableFlag(1722)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(3, 1722)
    IfFlagEnabled(-3, 13501800)
    IfConditionTrue(3, input_condition=-3)
    IfFlagEnabled(3, 73500602)
    GotoIfConditionFalse(Label.L2, input_condition=3)
    DisableFlagRange((1710, 1729))
    EnableFlag(1723)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagRangeAnyEnabled(4, flag_range=(1720, 1722))
    IfFlagEnabled(4, 73400403)
    IfFlagEnabled(4, 13501800)
    GotoIfConditionFalse(Label.L8, input_condition=4)
    DisableFlagRange((1710, 1729))
    EnableFlag(1723)

    # --- 8 --- #
    DefineLabel(8)

    # --- 9 --- #
    DefineLabel(9)
    GotoIfFlagEnabled(Label.L0, flag=1722)
    GotoIfFlagEnabled(Label.L1, flag=1727)
    GotoIfFlagEnabled(Label.L2, flag=1712)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SetTeamType(character, TeamType.Ally)
    ForceAnimation(character, 103150)
    End()

    # --- 1 --- #
    DefineLabel(1)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    End()


@NeverRestart(13500951)
def Event_13500951(_, character: int, flag: int, flag_1: int):
    """Event 13500951"""
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    DisableFlag(flag)
    IfFlagEnabled(1, flag_1)
    IfFlagEnabled(1, flag)
    IfCharacterHasSpecialEffect(1, character, 151)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(character, 103155)
    IfFlagEnabled(2, flag_1)
    IfFlagDisabled(2, flag)
    IfCharacterHasSpecialEffect(2, character, 152)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(character, 103150)
    Restart()


@NeverRestart(13500952)
def Event_13500952(_, character: int):
    """Event 13500952"""
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    IfFlagRangeAnyEnabled(1, flag_range=(1720, 1722))
    IfFlagEnabled(1, 13501800)
    IfFlagEnabled(1, 73400403)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1710, 1729))
    EnableFlag(1723)
    DisableCharacter(character)
    DisableBackread(character)


@NeverRestart(13500953)
def Event_13500953(_, flag: int, flag_1: int, item_lot_param_id: int):
    """Event 13500953"""
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(flag_1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, flag_1)
    AwardItemLot(item_lot_param_id, host_only=False)
    SaveRequest()


@NeverRestart(13500960)
def Event_13500960(_, character: int, character_1: int):
    """Event 13500960"""
    IfCharacterHuman(-1, PLAYER)
    GotoIfConditionFalse(Label.L9, input_condition=-1)
    GotoIfFlagRangeAnyEnabled(Label.L1, flag_range=(1750, 1769))
    DisableFlagRange((1750, 1769))
    EnableFlag(1760)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(1, 73500301)
    IfFlagEnabled(1, 1760)
    GotoIfConditionFalse(Label.L1, input_condition=1)
    GotoIfFlagDisabled(Label.L2, flag=73500330)
    GotoIfFlagDisabled(Label.L3, flag=73500331)
    DisableFlagRange((1750, 1769))
    EnableFlag(1761)

    # --- 3 --- #
    DefineLabel(3)
    EnableFlag(73500331)

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(73500330)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(2, 73500309)
    IfFlagEnabled(2, 1761)
    GotoIfConditionFalse(Label.L4, input_condition=2)
    GotoIfFlagDisabled(Label.L2, flag=73500335)
    GotoIfFlagDisabled(Label.L3, flag=73500336)
    DisableFlagRange((1750, 1769))
    EnableFlag(1762)

    # --- 3 --- #
    DefineLabel(3)
    EnableFlag(73500336)

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(73500335)

    # --- 4 --- #
    DefineLabel(4)
    DisableFlag(73500305)

    # --- 9 --- #
    DefineLabel(9)
    GotoIfFlagEnabled(Label.L0, flag=1760)
    GotoIfFlagEnabled(Label.L1, flag=1761)
    GotoIfFlagEnabled(Label.L2, flag=1762)
    GotoIfFlagEnabled(Label.L3, flag=1750)
    GotoIfFlagEnabled(Label.L4, flag=1751)
    GotoIfFlagEnabled(Label.L5, flag=1752)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableBackread(character)
    DisableBackread(character_1)
    End()

    # --- 1 --- #
    DefineLabel(1)
    ForceAnimation(character, 7002, loop=True, skip_transition=True)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    EnableCharacter(character_1)
    DisableBackread(character)
    EnableBackread(character_1)
    End()

    # --- 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    ForceAnimation(character, 2250, loop=True, skip_transition=True)
    DisableCharacter(character_1)
    EnableBackread(character)
    DisableBackread(character_1)
    DropMandatoryTreasure(character)
    End()

    # --- 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    EnableInvincibility(character_1)
    End()

    # --- 5 --- #
    DefineLabel(5)
    DisableCharacter(character)
    EnableCharacter(character_1)
    DisableBackread(character)
    EnableBackread(character_1)
    ForceAnimation(character_1, 7011, loop=True, skip_transition=True)
    End()


@NeverRestart(13500963)
def Event_13500963(_, character: int, first_flag: int, last_flag: int, last_flag_1: int, flag: int):
    """Event 13500963"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagRangeAnyEnabled(flag_range=(first_flag, last_flag_1))
    IfCharacterDead(1, character)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    SaveRequest()


@NeverRestart(13500965)
def Event_13500965():
    """Event 13500965"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(1752)
    IfFlagEnabled(0, 73500318)
    DisableFlagRange((1750, 1769))
    EnableFlag(1752)
    EnableInvincibility(3500911)
    ForceAnimation(3500911, 7002, skip_transition=True)
    WaitFrames(frames=178)
    ForceAnimation(3500911, 7011, loop=True, skip_transition=True)
    SaveRequest()


@NeverRestart(13500966)
def Event_13500966():
    """Event 13500966"""
    EndIfThisEventFlagEnabled()
    DisableObject(3500912)
    DisableObject(3500913)
    IfFlagEnabled(0, 1762)
    EnableObject(3500912)
    EnableObject(3500913)


@NeverRestart(13500967)
def Event_13500967(_, character: int):
    """Event 13500967"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagDisabled(0, 73500325)
    IfHealthEqual(1, character, value=0.0)
    EndIfConditionTrue(1)
    ForceAnimation(character, 0, loop=True, skip_transition=True)
    IfFlagEnabled(0, 73500325)
    IfHealthEqual(2, character, value=0.0)
    EndIfConditionTrue(2)
    ForceAnimation(character, 7000, loop=True, skip_transition=True)
    Restart()


@NeverRestart(13500968)
def Event_13500968(_, character: int):
    """Event 13500968"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(73500326)
    IfFlagEnabled(0, 73500326)
    IfHealthEqual(1, character, value=0.0)
    EndIfConditionTrue(1)
    ForceAnimation(character, 7001, loop=True)
    IfFlagDisabled(0, 73500326)
    IfHealthEqual(2, character, value=0.0)
    EndIfConditionTrue(2)
    ForceAnimation(character, 0, loop=True, skip_transition=True)
    DisableFlag(73500326)


@NeverRestart(13500977)
def Event_13500977():
    """Event 13500977"""
    GotoIfFlagEnabled(Label.L0, flag=13500101)
    SetEventPoint(3500935, region=3502907, reaction_range=3.0)
    IfFlagEnabled(0, 13500100)
    SetEventPoint(3500935, region=3502909, reaction_range=3.0)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SetEventPoint(3500933, region=3502909, reaction_range=3.0)


@NeverRestart(13500978)
def Event_13500978(_, flag: int, flag_1: int, character: int):
    """Event 13500978"""
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(flag_1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, flag_1)
    IfCharacterDead(1, 3500901)
    IfConditionTrue(0, input_condition=1)
    DropMandatoryTreasure(character)
    SaveRequest()


@RestartOnRest(13500980)
def Event_13500980(_, flag: int, flag_1: int, seconds: float):
    """Event 13500980"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(flag)
    IfFlagEnabled(0, flag_1)
    Wait(seconds)
    DisableFlag(flag_1)
    Restart()


@NeverRestart(13500990)
def Event_13500990(_, character: int, flag: int, flag_1: int):
    """Event 13500990"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagDisabled(flag_1)
    IfFlagDisabled(0, flag)
    IfHealthEqual(1, character, value=0.0)
    EndIfConditionTrue(1)
    ForceAnimation(character, 7013, loop=True, skip_transition=True)
    IfFlagEnabled(0, flag)
    EndIfFlagDisabled(flag_1)
    IfHealthEqual(2, character, value=0.0)
    EndIfConditionTrue(2)
    ForceAnimation(character, 9002, loop=True, skip_transition=True)
    Restart()


@NeverRestart(13500994)
def Event_13500994(
    _,
    destination: int,
    character: int,
    flag: int,
    flag_1: int,
    flag_2: int,
    seconds: float,
    seconds_1: float,
    animation_id: int,
):
    """Event 13500994"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagDisabled(flag_2)
    IfAttackedWithDamageType(1, attacked_entity=destination, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(flag_1)
    WaitFrames(frames=1)
    ForceAnimation(destination, animation_id, skip_transition=True)
    WaitFrames(frames=74)
    ForceAnimation(destination, 7011, loop=True, skip_transition=True)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    Move(
        character,
        destination=destination,
        destination_type=CoordEntityType.Character,
        model_point=90,
        short_move=True,
    )
    WaitFrames(frames=1)
    DropMandatoryTreasure(character)
    IfFlagEnabled(0, flag)
    Wait(seconds)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    Wait(seconds_1)

    # --- 1 --- #
    DefineLabel(1)
    ForceAnimation(destination, 7012, skip_transition=True)
    WaitFrames(frames=109)
    ForceAnimation(destination, 7013, loop=True, skip_transition=True)
    DisableFlag(flag_1)
    Restart()


@NeverRestart(13500998)
def Event_13500998():
    """Event 13500998"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(73500338)
    IfCharacterInsideRegion(0, PLAYER, region=3502911)
    EnableFlag(73500338)
    IfCharacterOutsideRegion(0, PLAYER, region=3502911)
    DisableFlag(73500338)
    Restart()


@NeverRestart(13500999)
def Event_13500999():
    """Event 13500999"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 73500317)
    RunEvent(9350, slot=0, args=(2,))


@NeverRestart(13501900)
def Event_13501900(_, character: int):
    """Event 13501900"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableBackread(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, character)
    Wait(0.0)


@NeverRestart(13501915)
def Event_13501915(_, character: int, flag: int):
    """Event 13501915"""
    IfFlagEnabled(-1, flag)
    IfThisEventFlagEnabled(-1)
    GotoIfConditionFalse(Label.L0, input_condition=-1)
    DisableBackread(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, character)
    EnableFlag(13501904)


@NeverRestart(13501920)
def Event_13501920(_, flag: int, item_lot_param_id: int):
    """Event 13501920"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfFlagEnabled(0, flag)
    AwardItemLot(item_lot_param_id, host_only=False)


@NeverRestart(13501940)
def Event_13501940(_, flag: int, item_lot_param_id: int):
    """Event 13501940"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, flag)
    DisableFlag(flag)
    AwardItemLot(item_lot_param_id, host_only=False)
    End()


@RestartOnRest(13501960)
def Event_13501960():
    """Event 13501960"""
    GotoIfThisEventFlagEnabled(Label.L0)
    IfPlayerHasGood(0, 4015)

    # --- 0 --- #
    DefineLabel(0)
    Kill(3500750)
    Kill(3500760)


@RestartOnRest(13505900)
def Event_13505900(_, flag: int, flag_1: int, flag_2: int, region: int, region_1: int, flag_3: int):
    """Event 13505900"""
    EndIfFlagEnabled(1730)
    EndIfFlagEnabled(flag_2)
    EndIfFlagEnabled(flag_1)
    IfPlayerHasGood(1, 4015)
    IfFlagDisabled(1, 1730)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_3)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfCharacterInsideRegion(-1, PLAYER, region=region_1)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(flag)


@RestartOnRest(13505901)
def Event_13505901(_, flag: int, flag_1: int, flag_2: int, region: int, region_1: int):
    """Event 13505901"""
    EndIfFlagEnabled(1730)
    EndIfFlagEnabled(flag_2)
    EndIfFlagEnabled(flag_1)
    IfPlayerHasGood(1, 4015)
    IfFlagDisabled(1, 1730)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagEnabled(1, flag)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfCharacterInsideRegion(-1, PLAYER, region=region_1)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    PlaySoundEffect(PLAYER, 10306, sound_type=SoundType.s_SFX)
    WaitRandomSeconds(min_seconds=2.0, max_seconds=4.0)
    Restart()


@RestartOnRest(13505902)
def Event_13505902(
    _,
    character: int,
    flag: int,
    flag_1: int,
    region: int,
    region_1: int,
    flag_2: int,
    flag_3: int,
    destination: int,
):
    """Event 13505902"""
    AICommand(character, command_id=30, command_slot=0)
    ReplanAI(character)
    EnableInvincibility(character)
    DisableAnimations(character)
    AddSpecialEffect(character, 5560)
    EndIfFlagEnabled(1730)
    EndIfFlagEnabled(flag_1)
    EndIfFlagEnabled(flag)
    IfPlayerHasGood(1, 4015)
    IfFlagDisabled(1, 1730)
    IfFlagEnabled(1, flag_2)
    IfFlagDisabled(1, flag_1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=region)
    IfConditionTrue(-1, input_condition=2)
    IfCharacterInsideRegion(3, PLAYER, region=region_1)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFinishedConditionTrue(2, condition=3)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, set_draw_parent=3504000)
    SkipLines(1)
    Move(character, destination=3502897, destination_type=CoordEntityType.Region, set_draw_parent=3504000)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    DisableInvincibility(character)
    EnableAnimations(character)
    CancelSpecialEffect(character, 5560)
    AddSpecialEffect(character, 8060)
    PlaySoundEffect(PLAYER, 777777777, sound_type=SoundType.s_SFX)
    ForceAnimation(character, 101203)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    DisableInvincibility(character)
    EnableAnimations(character)
    CancelSpecialEffect(character, 5560)
    EnableFlag(flag)
    DisableFlag(flag_3)
    IfFlagEnabled(0, flag_3)
    Restart()


@RestartOnRest(13505903)
def Event_13505903(_, character: int, flag: int, flag_1: int, region: int, region_1: int, flag_2: int):
    """Event 13505903"""
    EndIfFlagEnabled(1730)
    EndIfFlagEnabled(flag_1)
    IfFlagEnabled(1, flag)
    IfHealthGreaterThan(1, character, value=0.0)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfCharacterInsideRegion(-1, PLAYER, region=region_1)
    IfCharacterInsideRegion(-1, PLAYER, region=3502898)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    AICommand(character, command_id=30, command_slot=0)
    ReplanAI(character)
    Wait(2.0)
    EnableInvincibility(character)
    DisableAnimations(character)
    AddSpecialEffect(character, 5560)
    CancelSpecialEffect(character, 8060)
    CancelSpecialEffect(character, 1130)
    CancelSpecialEffect(character, 1150)
    PlaySoundEffect(PLAYER, 122, sound_type=SoundType.s_SFX)
    Wait(4.0)
    EnableFlag(flag_2)
    DisableFlag(flag)
    IfFlagEnabled(0, flag)
    Restart()


@RestartOnRest(13505904)
def Event_13505904(_, character: int, flag: int, flag_1: int, item_lot_param_id: int, character_1: int):
    """Event 13505904"""
    DisableBackread(character_1)
    GotoIfFlagDisabled(Label.L0, flag=1730)
    DropMandatoryTreasure(character_1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EndIfFlagEnabled(flag_1)
    IfFlagEnabled(1, flag)
    IfCharacterDead(1, character)
    IfFlagEnabled(2, 1730)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    CancelSpecialEffect(character, 8060)
    PlaySoundEffect(PLAYER, 122, sound_type=SoundType.s_SFX)
    EnableFlag(flag_1)
    IfCharacterHuman(2, PLAYER)
    EndIfConditionFalse(2)
    AwardItemLot(item_lot_param_id, host_only=True)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DropMandatoryTreasure(character_1)


@NeverRestart(13504400)
def Event_13504400(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 13504400"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    IfPlayerHasGood(1, 4312)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_3)
    IfClientTypeCountComparison(1, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfFlagEnabled(1, 13501900)
    IfFlagEnabled(1, 13500100)
    IfFlagDisabled(-1, flag_4)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(flag)
    CreateVFX(vfx_id)
    IfPlayerHasGood(2, 4312)
    IfFlagDisabled(2, flag_1)
    IfFlagDisabled(2, flag_2)
    IfFlagDisabled(2, flag_3)
    IfClientTypeCountComparison(2, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(2, PLAYER, 6142)
    IfFlagEnabled(2, 13501900)
    IfFlagEnabled(2, 13500100)
    IfFlagDisabled(-3, flag_4)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@NeverRestart(13504410)
def Event_13504410(
    _,
    sign_type: int,
    character: int,
    region: int,
    summon_flag: int,
    dismissal_flag: int,
    flag: int,
    flag_1: int,
    action_button_id: int,
):
    """Event 13504410"""
    SkipLinesIfFlagEnabled(1, summon_flag)
    DisableCharacter(character)
    SkipLinesIfFlagEnabled(3, dismissal_flag)
    IfClient(1)
    IfFlagEnabled(1, summon_flag)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(character)
    EndIfFlagEnabled(flag_1)
    IfClient(3)
    SkipLinesIfConditionTrue(1, 3)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    IfPlayerHasGood(2, 4312)
    IfFlagDisabled(2, summon_flag)
    IfFlagDisabled(2, dismissal_flag)
    IfFlagEnabled(2, flag)
    IfFlagDisabled(2, flag_1)
    IfActionButtonParam(2, action_button_id=action_button_id, entity=character)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(PLAYER, 100111)
    AddSpecialEffect(PLAYER, 4682)
    SummonNPC(sign_type, character, region=region, summon_flag=summon_flag, dismissal_flag=dismissal_flag)
    CancelSpecialEffect(PLAYER, 9005)
    CancelSpecialEffect(PLAYER, 9025)
    Wait(5.0)
    DisplayBattlefieldMessage(100051, display_location_index=0)


@NeverRestart(13504450)
def Event_13504450(_, character: int, region: int, flag: int, flag_1: int, flag_2: int):
    """Event 13504450"""
    EndIfThisEventSlotFlagEnabled()
    EndIfClient()
    SetEventPoint(character, region=region, reaction_range=1.0)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfFlagEnabled(1, flag_2)
    IfConditionTrue(0, input_condition=1)
    AICommand(character, command_id=990, command_slot=0)
    ReplanAI(character)


@NeverRestart(13504460)
def Event_13504460(
    _,
    character: int,
    region: int,
    region_1: int,
    region_2: int,
    animation: int,
    flag: int,
    region_3: int,
):
    """Event 13504460"""
    EndIfClient()
    IfFlagEnabled(1, flag)
    IfCharacterInsideRegion(1, character, region=region)
    IfConditionTrue(0, input_condition=1)
    ResetAnimation(character)
    RotateToFaceEntity(character, region_1, animation=animation, wait_for_completion=True)
    IfCharacterInsideRegion(2, character, region=region_2)
    RestartIfConditionFalse(2)
    SetEventPoint(character, region=region_1, reaction_range=1.0)
    AICommand(character, command_id=990, command_slot=0)
    ReplanAI(character)
    DisableGravity(character)
    DisableCharacterCollision(character)
    IfCharacterInsideRegion(0, character, region=region_3)
    EnableGravity(character)
    EnableCharacterCollision(character)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
