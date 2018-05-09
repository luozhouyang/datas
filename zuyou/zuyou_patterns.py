import re


class Patterns:
    # <li>可去地区：<span>待议 </span></li>
    # <li>是否收费：<span>收费<FONT COLOR=#888888>..</FONT></span></li>
    # <li>服务时间：<span>待议 </span></li>
    # <li>使用语种：<span>普通话  </span></li>
    # <li>提供服务：<span>待议</span></li>
    # <li>兴趣爱好：<span>聊天, 赚钱 </span></li>
    # <li>性格类型：<span>阳光, 活泼可爱 </span></li>
    # <li>心情留言：<span>找工作  </span></li>

    PATTERN_AREA = re.compile("可去地区")
    PATTERN_PAYMENT = re.compile("是否收费")
    PATTERN_SERVE_TIME = re.compile("服务时间")
    PATTERN_LANGUAGE = re.compile("使用语种")
    PATTERN_SERVE_TYPE = re.compile("提供服务")
    PATTERN_HOBBITS = re.compile("兴趣爱好")
    PATTERN_CHARACTERISTIC = re.compile("性格类型")
    PATTERN_MESSAGE = re.compile("心情留言")

    # <li class="li539"><span>昵　　称：鑫大宝</span> </li>
    # <li class="li539"><SPAN>Ｉ　　Ｄ：</SPAN>700002&nbsp;&nbsp;
    # <!--诚意 登陆时间-->
    # 诚意:22<IMG alt="" src="imageszny/images/cy2.gif" align="absMiddle">
    #
    # </li>
    # </li>
    # <li class="li265"><SPAN>性　　别：</SPAN>女</li>
    # <li class="li265"><SPAN>年　　龄：</SPAN>24岁</li>
    # <li class="li265"><SPAN>出生年月：</SPAN>1987-8-19</li>
    # <li class="li265"><SPAN>星　　座：</SPAN>狮子</li>
    # <li class="li265"><SPAN>身　　高：</SPAN>162CM</li>
    # <li class="li265"><SPAN>体　　重：</SPAN>55KG</li>
    # <li class="li265"><SPAN>体　　形：</SPAN>匀称</li>
    # <li class="li265"><SPAN>学　　历：</SPAN>中专</li>
    # <li class="li265"><SPAN>婚　　姻：</SPAN>未婚</li>
    # <li class="li265"><SPAN>职　　业：</SPAN>医生</li>
    # <li class="li265"><SPAN>居住城市：</SPAN>黑龙江&nbsp;哈尔滨
    # </li>
    # <li class="li265"><SPAN>籍　　贯：</SPAN>山东</li>
    # <li class="li265"><SPAN>注册日期：</SPAN>VIP会员可见</li>
    # <li class="li265"><SPAN>登陆日期：</SPAN>VIP会员可见</li>
    # </ul>

    PATTERN_NAME = re.compile("昵　　称")
    PATTERN_ID = re.compile("Ｉ　　Ｄ")
    PATTERN_GENDER = re.compile("性　　别")
    PATTERN_AGE = re.compile("年　　龄")
    PATTERN_BIRTH = re.compile("出生年月")
    PATTERN_CONSTELLATION = re.compile("星　　座")
    PATTERN_HEIGHT = re.compile("身　　高")
    PATTERN_WEIGHT = re.compile("体　　重")
    PATTERN_SIZE = re.compile("体　　形")
    PATTERN_DEGREE = re.compile("学　　历")
    PATTERN_MARRIAGE = re.compile("婚　　姻")
    PATTERN_OCCUPATIONAL = re.compile("职　　业")
    PATTERN_LIVES = re.compile("居住城市")
    PATTERN_ORIGIN = re.compile("籍　　贯")

    PATTERN_TYPE_1 = re.compile("[/<>SPANlispan;&b\"]")
    PATTERN_TYPE_ID = re.compile("[</>a-zA-Z&;]")
    PATTERN_TYPE_PAYMENT = re.compile("[</>a-zA-Z0-9=.#]")
