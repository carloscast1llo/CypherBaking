import base64
from cryptography.fernet import Fernet
import os

def menu():
    print("*********************************************************************")
    print("""
                       _               _           _    _             
                      | |             | |         | |  (_)            
       ___ _   _ _ __ | |__   ___ _ __| |__   __ _| | ___ _ __   __ _ 
      / __| | | | '_ \| '_ \ / _ \ '__| '_ \ / _` | |/ / | '_ \ / _` |
     | (__| |_| | |_) | | | |  __/ |  | |_) | (_| |   <| | | | | (_| |
      \___|\__, | .__/|_| |_|\___|_|  |_.__/ \__,_|_|\_\_|_| |_|\__, |
            __/ | |                                              __/ |
           |___/|_|                                             |___/ 

    """)
    print("  CypherBaking v1.0")
    print("  La Panaderia")
    print("  https://github.com/carloscast1llo/CypherBaking")
    print("*********************************************************************")
    print("Welcome to Cyberbaking")
    menu = True

    while menu:
        print("1) Encrypt message/file")
        print("2) Decrypt message/file")
        print("3) Exit")

        opcion = input()

        if opcion == "1":
            encryptMessage()
            menu = False

        elif opcion == "2":
            decryptMessage()
            menu = False

        elif opcion == "3":
            print("""
                        ewwEEweaaeeweeewwPEEE66UqpOdDDddRWWMR&&DddDddDRgWDK9k6qppKbDDdddbKpODRRDd6wwEkEh6OOKObDdbDRRRDKqpdWNNN#QQB####BQQBN##B#WDqhwweooyyjjjjjuFuujjuuujuujoooooyu{zi///i7v
            99q9kwaooaaaaeewPwwPE6kUKDgQQB#M&RDdOObOKbOOKKKKObKqpKKOK9qODDRRRRDDMgNNNNWDbKpOODK6kkqKODDdbdDD&NB#WR&#BBB##gM&RdUkk99EeayuuFFFFFF}Fjyyyyjjuuyyyyyyjjjjjs\+;:,,,,::
            DDbKqhweaaaaoaaewwwEEhk6qdgQQQQNROkew6bMgMdKKOOKkh6UOdbbOKpKD&gWW&RDRg#QQQQ#W&&WggRDpKbd&WRDDdDRWWgWRWg#gDOKq6EweayjujjjjF}tst}uujjjyooyyuuFFjoyF}{szzstsv/>;:,''.--
            RDbKqkEwwwwwwwwwEk66kEPwhUpbDDDR&WggNN###NgWgNNgDq66pObDWgW&RWNNNg&WN#QQQQQ@@@@@@@@@@QQQ@@QQQQQQ#WdpkwwweojuujjFFF}{ssst}IsssIjyyoyyjjuF}zvvvzzvli/\\iiiii\=;:,,''''
            DbKq6EwwewwEhkUU6996kwewwwwwwEkqdW#BB#gR&NBQQB#NNgWWRRMNBQB#WgBQQQQ@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@QQR6atsst}FFuuF}}I{}}FuuF}{}jyyyjuuF}FIssszzzv7v7vvzzvl/|r;;::::::
            6hwaoyjjyaewPh6kwweeewwEPwwwk69qqpqpKKbOObKKpqKpKOOOppqOdRBQQ@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#KeyjjyyyjFF}}FujyyjF}tIFFFFF}FFFFujjjjFFI{s{FuFFFF}tz(iii\=;
            s7i\|*=|/l7v}yewweeeewwwwwwhkhEweaoyoaeeweaoyjyoeeeaew9RQQ@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@QQgbEayyjuuFFjjjyyjjjujuFF}FuFujyyjyjju}}{}jyjjjjuuuuu}zl=;
            |+;:,''',,,~;|zIz7(l(v7l(7vvvvvvzt}Isz{}FF}}}}{FjyoawbQ@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@QQDejuujuFFuuujjjuFF}It{FjyyyjjFF}Itstszzzliiil(vzi/|^:
            =;:,'`````-',:;:_,,,,''''',:;;;+>|\|=>>*r^+r|\i7zFwWQQ@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@QRwuIzvvvzz{}FF}II}II}FFFFF}sz(l(i/|**>r++>*>r+;;::,
            |+:,'''',:_~,''-```      `-',::;;^++^;;::,_:;>\i}pQ@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@QRaFzzszvz}FuFIt{I}}Fu}{ssszvvv\+::_:::;::,'.`````
            /\*+;^+?\|+;:,'-````````.'~::;;^+=|\\||*+++=\ivyDQ@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@QBpouujFFFFF}3}t{}}}Fju}Izzzzv/>;~'''',,,'-`      
            F}{svv(vvi|+;::~,,_::;;^?/////illvzsszvzsFjoookNQ@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@NwjyyjFF}}{stzzzssstsv7i\+_'''''''--``````    
            svi\?>r=|\//\////i(zzzzIuujuuuuuuujyyyjjyoaewONQQ@@@@@@@@@@@@@@@@@@@QQQQ@@@QQ@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BkaojF}{szzzvzzzzvzv7l/|^,'..''.--````     ``
            szl/\||\/lzIFujyyooyyjjjyoooooyooooaaaaaeeaeOQQ@@@@@@@@@@@@@@@@@@@@@QQ#QQQQQQQQ@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@QDauF}{{tzzvzzssstsszzvir^;;;;;:_,,'.-``----
            eaayyyyooaaeeeeeeeeaaaaaaeeeaaaeeeeeaaaeeeepBQQ@@@@@@@@@@@@@@@QQQQQQQQQQQQ#Q#QQQQQQQQQQQ@QQQQ@@Q@@@@@@@@@@@@@@@@@@@@@@@@@@MuI{}F}Itsss{{Itssst}Ivll(vzvi\>;;:__~~,,,
            PwwwewwwwwwwwwPEwwwwwPwwwewweeewweeeeeeeewwOQ@@@@@@@@@@@QQQQQQQQQQQQQ##NDEowwekE6pdbD#NW#QQQ#QQQQQQQ@@@@@@@@@@@@@@@@@@@@@@@6zvztFujuujujFF}}I}FFtzzzsssv\+;::,~~_:_~
            hEEPwwPPwwwwwwwwwwwPwEEPwwwwwwwwweeeewwwwwwOQ@@@@@@@@Q#DKd&#BN###Q#KkEwwjv\//\\\lFFuoekwe6dR&D&#BQQQQ@@@@@@@@@@@@@@@@@@@@@@QesvsFjyooooyjujyoyju{viii|*r^;:~,''','''
            6669UUkEwwwEhkkhkkEPwh66kk6U6hkk6EwwwEEEEwwDQ@@@@@@Q&qkeaew66PO6awyzvv7\|*+r+++r?/lilvvFzzFFow9OR#QQQQQ@@@@@@@@@@@@@@@@@@@@@goF}I}FujyyyjujjjFF}z(/\|+^^^^;:,,',,'--
            9pKOOKp9hk6UqqqqqqU66UqpppppKppqU6hEEPEPwwepBQ@@@@#KwaeoyyyFFyyFi\|\?=|+^;;;;;^^+*|//\/7v(ll7toEqDNQQQQQQ@@@Q@@@@@@@@@@@@@@@QqyuF}FuujjjuF}Isst}szlllii//\|>;;;;^;_,
            OdbbdddOKppKbbdOOKppqppppqqU6666kkhPwwwwweePpQ@@@WkeoyjF}}}{zs7i|*>rrr+^;;;;;;;^^>=|\\\/iivvvsuohdR#QQQQQQQ@QQ@@@@@@@@@@@@@@@BaFFjjjuujyuFF}}}{Iz7i/illi\|=+;::::,.-
            OOKKObbbOppppOKpq9666UUU6kEPwwPhkkhEwPPwweeehB@@gEaojFFssszvli|?==>rr>r^;^^^^^+++>?=|\\/ii7zzs}uowbWQQQQQQQQQQQ@@@@@@@@@@@@@@QkF}}}FuuuFFFFFFuu}zv7li/\=^;;~'````   
            qqpqKOKOOKpqU6kkkkEEhk6kkhEPEEEhEhkEwwweeaaaw#@Q6eeojFtzsvvvi/||\|||*>>rr++++^+++?|=|\\\/i(vz}}FjeqDNQQQQQQQBQQQ@Q@@@@@@@@@@@@NyjuFyooojFFII}uuF}sssz7(i\?>;:~,,,,,,
            ppppKObddOp96k66UU6UUqq9kEEPEEPPwwPPwwwwwewwh#QOEwaoyjF{sv77i/|||?||?==*r++++++*++r>||\\ii(vtI}}Ijwdg#QQQQQQQ#QQQQQQQQQ@@@@@@@QeoaaeewweaouFFujjFtzz{FuF{zvvlii\\\/i
            pU6k6qpKKqU6kkk6UqKKKKppqU66666kkhhEPwwwwwPhOQQkweeayF}z7li\\\\||||?=*>+^;;;;;^+++r*||\\/iv(zzsz{FyPDWW#QQQBQQQQQQQQQQQQ@@@@@@Qqyoooooyyyyjjjyoyyju}FjyjFI{I}F}szvzt
            pq96U99Uqqq9q66k66UU6k66Uqq9UkkkhEweeaaaaewqB@BweeayjFs7/\\|\\||?=>+^;;;;::;;;^++rr*=|\ii(7vszzss}}ywK&##BQQ#QQQQQQQQQQQ@@@@@@QdojyyjFFFFjyoeeaooaaooooyjuFFjjjFFFFF
            KKOObbOKKOOOKp9kkk6kEEkk66kkhEwwwweaaaaaaaeDQ@#6weayu{vl\\|*==?>>+^;;;;;;;;^r?|/\|7FoojIz7vs{}I{F}}FuyebNQQQQBQQQQQQQQQQQ@@@@@@WooaoyuFFjjoaewaoaeeaaayyyyjjyyoyyyyy
            OOOObdbbOKKpqq6EEhkkkkhEEEwwwwweeeooooaaaewRQ@BKheeyFvi\|?r;^++^^;;;;^^r*iFeP9DNNRRDWWRRROEayuuFFF}FFuuyepNQQBQQQQQQQQQQQQQ@@@@gyjyyjFFujjyyoeweewweeaaaaeaoooaaaeee
            ppKpKKpppq9U666kkhhkkEweewwwwwwweeaaaaaewE6NQ@QKEwwaj{(/\\|>>?r;;;;+|iuhDQQ@@@@@@QQQQQQQQQ##gR9ey}{FFFFuuyE&BQQQQQQQQQQQQQQ@QQQ#eoooooyooooyoawwwwwweewwPwaojyoaewwE
            69ppqqqUU9966666kPEkEwwwPk69U6kEPweeeewwEEURQ@QdDdK6kPajsv7i/\|^;:;r/FbBQQQQQBNRdbKqppq96kEwePq9woItttIuyoaKQQQQQQQQQQQQQ@@@@@Q#waoooyoayuujjjoaaojyyooawwaojyaeeeaw
            6Uqqpq99qqqq9khEwwwwEwEkU9ppqqUkEPwwwEhEEPEOQ@QQ@QQ@QQQQB&peuz\+;:;^\syawooawhk66PeyuFyeEkwouFuyayFsz{s{jaaENQQQQQQQQQQQQQ@@@@QRj}tzi\i/||\\\\lzs7ilsFF}I{tIIFuF}ts}
            qqq99969pKOOK9kEEEEEhk69pp9U9U6kkhhhkk6EwEhq#@@@@@@@@@@@@QQNbwv=;::^|il(vzFeqKMgQ@@gQQWKEwPej}zzzzsz7(vsIuywDQQQQQQQQQQQQQQ@QQQgs/\?>r>>^;;;;;^r|||\\\?+^;;^^;;;::::
            ppqpqqpppqU66hwwwEk66kk6U9U666k66kEEEhEEweek#@@QBROqhPwkpdDDg&F|;:;+>||/7i}kgRj+vQ@QQQyegQB9{i\\\\\/ii(zs}FeKBQQQQQQQQQ@@QD9kqRd}l/\|||+;;^++;;^?ivzvi|+;:::,'.``` `
            ppqqqqp96hEEkkwwwPkU6PewwwwwwwewwwwwwwweeeewRQQN&dODRDOpqUwkDD(>;;^>|||l7|l6UwyFzaDwwuluaeau\*>r++*?|/ivvtuoEgQQQQQQQQQpF\\sjojjFzli(zvi\\i/?;;;>/7tF{vi=+++;:_,.```
            96666kEPPwwwEEwwwwwweooaayjjjjjyoaeewweewwwwEWQQBQQQ@@QR@&(zwj?^;;+|/\\/li\sjowwaaa}sIlvi\?r^;^^^^r=|\iv}{FawDQQQQQQQKvr=soeEkkwFvi/ivt{{}Fs(\/izzs}jjFtvi\|>;_'.-.'
            weewwwwweeaeeewwweeeeaoooyyyyooyoaaaewPhkkEPwqQQ@@qyB@@QBa(ua/^;;^r|//\||\ilvvli/\|=r+^;;;;;;;;;;+r=||/lsFFyahWQQQQ#e\*/at^>/}z\l/iiilvvzvzzztuyoj{s}}{tsv7i|^:,''''
            aaaaeeweeaaeewPPwwPEPeaaoaaeeeeeeewwwEwPwwwwwU#Q@QDkhDOkeeaoir;;;^r*=|\|+^+r=||=>r^;;;;:::;;;;;;^+=|\\/vtIjyyaERQQQkv/isu|^^ris+r|vs{IFjF{s{{}uyyjvii(szv7vzvi/\>+^:
            aeewwwwweeeewEkEEPEEEeeaaaewwweaewwwwweeeeeewhdW##NROqEwoyo{|>^^^+>?*=?=+^;;::;;;;;;;:::::::::;;^>|\/ileoFFjyoaEOROauyjwez?;;r7r^*syoyyyuyoaoyjujyuts}FFtvvvvzzz7i\^
            ewwEhEEEEEEkkk6kkEEEPweeaaeeweaaoaaeaaeeeeeewwUEEqpkejsvv{}l\=r>>||\|?>>+^^;::::::::::::_~,_::;;+r?//lvujyyoyoaewwatisowl=tzr;>\?=}eeaoyjyaeeayjujyjyyoyFFFFFIzzzvi\
            wEk6666kk6qq9U6kkhhhhwwweeeeweaaaaaeeeeeaooaewEyjjFsviiivtl\=+^^r|il/||=r^;;>;::_::::::__~_::;^+r>|ilz{}jyyaaaaeeoFir^|jzr:\ir;/\|uaooaoaaaaaaoyjyyjyyoooaoeeeaojjjy
            U666kPwwkUU966kk666666666kkEwwwwPEhkhPweeeaeeeeu}tv7liiivi\=^;;;+?/vzl/\\>;:;::::::::::_:_::;^^r==\lzzIFjjyaaaaaayIi+;?z|+:;?|;?/i}jjyyyoooaaooyjjuFuuujjjjoeweeayya
            q6kkweewEkkhEEEkhk6UqKKKKpUEweeeewwwweeewPwwweo}zv(iiilvv\*;:,:;^?\/i(iivl>;:::::::::_::::::;^^=\|i(vvz}FyaoaaooyjFz?|z/;:,:|=;ii7}FuujjyyyaaaoyyyyooyF}}IFuujjjuuuy
            qqqU666U9666UU6khk6UqKKpq9hwaoaaaeaaaeaaeEEwwwoF{sviiiizav|^;;=/ii\==|\ivF/;:::::::__:::::;;^+>*\\/\i(zFjoaooyyyjjyzlPF|r;^|>=/\(uyyyooaeeewhwweooaaaeaaaoaeaoyuuaew
            OOKpppKpq66699UkPhkkk66EPweaaewwPwwwwPPwE6kEPhEaj}zl(iilkpov/\ljdKqRdyzzjo|;;;;:::::::::::;^^+rr?\|\lvs}uyyooooyyoj/r|?+;;?\\|=ijyjyyoaewPE69UkPaaaaaaaeeePkEeojjoee
            OOKKpqqUU6kk66hEwwPkk6kPeaoaaePEPweewEkk66kPwEqEo}v(iiiiyD#&6waey\\zFawwws?^;;;;:::::::::;;^+rr>=\\\/lsFFjyoyeeeeaFr^^^^+;;;^|sujjjyjjyawwwEPweeaaaaoyooaaeweyyoaeao
            9kk666U996kk666kkk6966kkPeeeeewPEPwPPwwwweeeee6qejsvii/\7PRBQRav|r+?/vsv/=+;;;;;;;:::::::;;;++++>||\/l7I{joooewEPejr:;++;:;^|sFujyyujujoaaewPPweeweeeaaaaaaeeeeewkkw
            uuowk9ppq6hk69qUU6666666kEPwwwwPEE6qqUEwweeeeeEbUaFz(7i/zjeqOji\=^;;^+>>+^;;;;;;;;;;;;;;;;;;^++rr=\//ivvsFjyyeE6UkbOj\=>>?\}jyooaaayoaeaaaeewEhPEhPwwwwEhEPEEhhhEk69
            zsFaEUqqq666U9qq66k6k6kkkhEEhkkhEEkqKp6wwwewewEqbEyIsvlsFuyajir=?r;;;^+^^+;;;;;;;;;;;;;;;;;^^^>+r=\\\l(vzt}uyaP6q6Uw6ddqweeyjaewwPwwewPEPweeeePE69kEPwwkqOOK9Uq9hk6U
            weeEUppKbbOKq6hkk6kEEEkkhk6qppq6hwPkkkEEEPwwwPPhbqajFttFuyouv|=\i\>^;;;;;;;;;;::;;;;^^;;^;^^^^^++>||\ii7vs}jae6qKpP}vso6waouuoewhUUEeewhkEwPwwP6qq6kkkhkpbDbpq9hwwPP
            KqqpKKpKObbOp6Ehk6kwwPkU9U9pKpp6EwwEEwwwEk666666qpEayuujyaj{sz//\/iiii\|=+;;;^;;;;;^rr^^^^+rr>++r>?|\i/i}jFjaw9KdKaFsIjeayuFyaewEkkEwewwwewEkEE6kEwwEkkk9qqq6kkwawEw
            DdbbOKpqq9U6kEEhk6kEwwwPEwwwhk6khEwPPwwwEU9996666pUwaojyeewPEEPwaweaoooawPweoyuv|+^+rr+++r*?|=>++r*?||\ivs}jeEpbb6yttFywejjawk6kEEk66kk6kEE6U6hhwayoaeeeewwwwwwaoewe
            dKpq6EEEEweaoaaewwwwwwwwwwwwwEk66EwewwwewwweewEhkk9EEaujeKDRWRWRbpwayussuyeeUheu7\*r>>r+r*||\?>rrr>?||\ls}uaP9bdpwusz{yweoowPkU96UU6k6qpOp66U6kEPeojyyoooaeeeeeeyoea
            kwweaewPweeeeeeeeewwwPEEhhEwwwEkkPwwEhEweeoyoaeEhh6q6eFu6gBN6yuIszl\=??|/i7//|>>?|||=*rr=||\\|?=??\|\/(z}jawkpDd6o}zzty6woooyaeEk6kEPkUpqUkkkEPwPwaooyaaoaeeeeeeaaee
            eaewkk66hweaaoyyyoewEweeeeewEUqqq6Eh6qpq9kPwewEUpqqqK6yowpOEoujjjyyju{(i\?++++++r>>?|||||\\/ii\\\\/i(vz}jaEkORDkyIz7v}a9kwewou}FywwEPwwwPwwEhEEwwaaaaeeeoowwwaaaewEP
            aeEpbOqqpUwojjyoaaeE6wajujaeP6qq96wew6UU9U66669pp9UUppwawEPeojyoojjuFs/|?=*>r>*?**?|\\\////iiii/\il7zsuoaE6KM&qy{vl(z}apkEEUqkwwPPwPEPEk6kEEEkhhhEweeeeeewPhkEwwE9qq
            6kqD#BBBBWOU9ORRdUweeyuujoaeeaaeeeaaaaeewwwwE699UkhkhKqPwhEajsiiiii\\/|?=>>*==?|?||\\\\\/iilillillv}uyehUKDg&6aovi/lz}aKUEEqOdbddOq9qpODDbbKKKKp66kh6kPewPww6qUk66kq
            RdDgQQQQQBNN#QQQQBbeyFuyaeewPwwweeaaoaaaeweaeePk6hE66qDOqq6PaF7i/\\|=*+^^^^+>=???||||||\illlllvvzsuyeE9bRWgbeyoI\//iv}apqh6KdDbD&DdOKKd&RddDR&Rdqkk6KKKKKqkkqbbKKUkU
            QQQQQQQQQBBBQQQQQQ#KeyyoewwP6qq6kUkEwwwwEhEweewPPwwE6qKRRDKkeyIz/\||>^;^;;;^+=rr*=*r==|\\illzst}uyeEqdR#gbetii\\\\\i7ty9DKbDRDdDDDDKkEUbbKpODRDbUPwEkqKDDDDbbDMMRDdb
            QQQQQQQQ#RbOKKpKDRD9eoawkk66qObOKKppq9qkk6qUEwwewwEh6qqpDWRK6woIl\|=>^;^^;;;^r^+r>+r>=|\l(zsIFyoeUbRgNgpati/\|*=||\i(syEOk6pKq6k6KO9EwPEPPwwwhhkUUqKOKObDWNNWgN##NWW
            QQQQQQQQNDKpqq666hwayjow6qqpppKOOqU666kEEE6UUU6EPE9ObOqkkdMDO6wo{vi\\//?=>+++++r+>+=|\\lzsFjoeEKRN##Mpez/\\|>>|||\\i(suwKaaewPwwEqdbKOOOKKqq6PwaawqDRRMDRg####BB#WMM
            QQQQNWW#Q#WRdOddOqweaaewhqbDbKq999qq9UUU99U9p9wajywUKObbOqORDKEauFzvztvi/i\|||==?||\i7vIuoehpDg##Wb6a{l||=>rr+r==\\i(sFaKDb6wEhPaaPUpOdRWW&RRbpwyuawkUk6pObdDRRDbOOp
            QQQQ#MRNBBN&DDbODDDbOKqUUqODDbppU9qqqU69pkeaeeoF{FjaewkUU6hKRd9Eeu}F{}tvvvi///\\/i(s}jawkpDWN#gDOwosi\?r^^^;;^+r>|\ilzFokgBBWDDDOKKbDRMMRKEhKdbqeyyaaeawPEEPkk6hwwEP
            gdppbR&&RRDDDO9pDMgWMdp6UqKObbK6kkhEEwwE6EayaeeewwPEhhkk6kEh9Dbqkeojjjujy}tzvvsIFuawhpODMgggDKEaFv/||?*+^;;^;;^+*|\/lv}jwdggb6kKRN###N#gDwuj6WNDEwwweaaaaaewE6qhwwwP
            OUeaeqDdKppOKppdRMRDDdpqqpKpkeoyoooyooaaaeaooooePk6kkkPeayjjjoUdbUEwwwwwwwwwEkkqOdRWWWgMDOkeFsvi\|>+++^;^^;;;;;^>?\/ivsFepdDOppdWWDDWBQQWpewKMRKqdM&dp6weeewh9KKKqU6
            yyooooaaekqhayaeeayyoojFFyyjIzzI}IzsFju{zFjFszzFju}Iueauzvsuj}zuhpObdDDDR&WNN#####NWRb6eyIv7i\|\/|r^^+^;;;;;;;^^+>|\i(s}akpOOKdNQQBNBQQQQQBQQNdUPpRN#NRKhEEEE6Kbbbbb
            zsyyuI}uappwu}oajzllstzl7}jFs(zFFt77}yuzisyjsiivzviizoauzv}jjs7soeoEQQQQQQQQQQQ##WOkwy{7/\//\?|\?r+++r+^;;;;;;;^^r*|/iv{owEk9q66pDWN#BQQQQQQ#NRK9pdD&WDOqdDDDOqqpbWR
            vsyou{FykKhyzsaeyvii{Fsll{uFslvuut(lFouv/vyyti/ili//voejzzFyFz7tawoj#QQQQQB##gDK9wjFzi\?====??||???=*++r^;;;;;;^+?\|\/(sywwwEEEEEPEkqbR&gNRdDWMDbDRRWgRDd&NBBDPewq&B
            vzoaoFua9KwFvzawozilFy}7(zszvlvFu{77Fajv/vyyIiiili//voeyssuyFsvIe6wubQQQQB#&OEaFs7/\|>++r==*?\\\/\?rrr++^^^++;;^+||?|/izjaooooaaeeeewwwwPaur:;=iaDWg#NgMRDDWNREeekdB
            vsaweyyepKPuvsaEasilFj}v7z{zvlvFj}vl}aosi7yo}i/vsvi/vyajzzuousvtahwuw##NgNNRKe{/|=>>r>>r?|?=>?|\|=r>=>+^^^^+;;^;^+r=|\ivFF{s}IFFujyyyoaaaF+:::__:;;^/aDQQQB#WRDDDRNQ
            zFwkwyyeKOEjsIe6e}(7uyFv7sjF{vzjojsvFeejz{aajv(Fyuz7}ewoFFaEej{uPqwyyRgRddRRO6av\|*?=?||||||====*r>?=+++^;^^;;^^^++?|\/izzvilzzvsst{}Fjjl;__::::_:::::;zUNB#N###BQQQ
            kqRWRK9bgN&OUpRWD9wwqbKEw6OOKUqdRDK9ORMDpKdDdqkqK9PP9dDdKpdRDOqK&NMbpDROqU9ObKkyzi/i/iill/\\||??=r?**>+^^;;;;;;;+>>=||\/lli\\iiill(7vvz\:::::~_::_::;::::;|seORMggN#
            B#BQBB##BQQQQB#NgRddDWRdbbddOpqpDRbU666kweaeEEwaojjyaaeeeaaaeaaa6OpPeEDKkPePqOqEau{vi/i\||\|>*r>>>>r>*>+;;;;;;;^^+r*?||\///\\\//////i/=:::::,~~::::~_::::::_::^?i}a6
            RDOOOp9666pdDOkweeeeE96wwkkweaaek6keoyjjjuI}uuF}FFFFuuuuuuFFF}I}oaFvljdKkwaawqUwejszli/|?==>r+++++r+r+r^^;^^^^++++>==??|\\\||||||||||r::__::~,:~_::__::::::__::::::^
            OEoFFjaewEwaeeyziil(z}jaoj}zvvvvs}FF}}}{{{{FjuFFujjujjyooaaojIvi/||/\jDd9Eeeek9Eajt7i/\|?*+++^^++++++r+^;^^++r*>rrr*=?|||\|==**==*r*>;:_::::_,'_:,~~,,~_::_~::::::__
            dEyIsIuowwojakw{/\\\\izs(\?>=||\\\\\\\||==|\//\\/ii////ili\|?*|?||\\|uDDK6EeeP9Ueytvi/\?>+^;+++++rrrrr+^^++>r===*>>=????||?*****rr>^;;::::::::,~::__::~~~_:::::_::__
            DOkwoyoawweooeati\\\/7zzi\?===??||\ii//\\?|\i(ii/\|??=>+^;;;^+^^+^+>|zdDbq6wew6qkeuzli\|=*rr*==||??*>>rr+^+>*==>=???||||===*rr++r+;;;;::_~:::_,,,~::::::::~_:::_::::
            NNWDpkkq9qpUEhEa{vliivtF{vli/\\||\vFF}I}F}}}uuI(/\|>r^;;;^++^;;;;^^r?/KDDOp6PwwhU6eoFsvlii///\\\\||||?*>rr>===????|||\\|=>r>r++>^;;;:::~~:::_~_~~~~~::~,~_,~_::::_::
            ###WOqqOKqKKpKKkaIzv7ivzIFju}szvlisoPwaye96EeoIi|=r^;;;;;^+^;;;;;++>?|ODDdbKqkEEk6khwayuF}tz(li\||\\\|=>*=??=>*??|||\||?*>++r>+;:::_:::~~:;;::;;::;;;:::::_,_:::::::
            ###NgMDRRRWNgMRDKkPwaF}tFjyayu}vlivjPwoow6oz/?>+^^;^;;;;++;;;;;;;++*|*K&DdbOKpUkhhhEweoyuF{z7i/\\\|\|=*>*=?=>rrr>===|====>+++^;;;:_~_::_~_::~_:;^;;;;;;:;;:_::_::::;
            MRRRRR&Mg#BB#WMWggNNNMRdpqqqp9kEPweaaFzli>;;^++++>r+^^++^;::;;;^^r^+r+qMDdKpppp6EwaeeaoyuFsvliii\|||=>r>***>+^^^^++++++r+^+^;;:::_,,_:::_:_~:_:::;:::::::;;;::_:::;:
            RDddddDDDRgNNgWMg##NW&M&&&WgNgR6oz\>r+^;;;^^^^^;;^>+;^^;;;::;;;^;+^+*>eMDbq6k666EeyyyyyjuFFtviii/\||=++++^^^;;;;;;;^^^r>>^;;;;;:_:::__::_:_:::::::::;_:_:::;;;;;;;;;
            WgNNNW&RDddDDDddRWMDOKOddDd6jv|+^;^^^;;;;;;^^+^;:::;;:;::;::;;;;;^^+r?vWDOqkPwwwwau}I}FFF{zvli////\?+;;;;;;^^^;^^^++r==+;;;:;;::::::_::_:::::::::::;;:_,~::::::::::;
            BNNNNNNgDdbbbbdDRRRDRRRDKy/+^;^;;;+++^;;;::;+*^;::;;;;;:::::;;;;^;^^r+^aDp6Ewaaaoytvi\iiiii/\\|\\|*+;;;;;^++++>*?\\\>^;;::;:::__:::::::::_:~~,,~:~:;;___::::::::::;;


            Todos los derechos reservados a Merk®

            """)
            menu = False

        else:
            print("Invalid input")


def toBase64():
    text = input("Write the text you want to encrypt: ")
    text_bytes = text.encode('ascii')
    base64_bytes = base64.b64encode(text_bytes)
    base64_text = base64_bytes.decode('ascii')
    print(base64_text)
    cont = input("Press ENTER to continue")
    menu()


def fromBase64():
    base64_text = input("Write the text you want to decrypt: ")
    base64_bytes = base64_text.encode('ascii')
    text_bytes = base64.b64decode(base64_bytes)
    decrypted_text = text_bytes.decode('ascii')
    print(decrypted_text)
    cont = input("Press ENTER to continue")
    menu()

def toFernet():
    # generacion de la clave
    key = Fernet.generate_key()

    # Se genera un archivo llamado *.key. La idea es que el archivo       
    # contenga una linea, que será un string, es decir, la clave.
    # Si ya existe dicho archivo y no está vacío, creará otro archivo.
    print("Escriba el nombre del archivo donde se generará la clave (.key): ")
    archivoClave = input()
    if os.stat(archivoClave).st_size == 0:
        with open(archivoClave, 'wb') as filekey:
            filekey.write(key)
    else:
        print("Ese archivo ya existe, ¿quieres reemplazar el archivo?[Y/n]: ")
        letra = input()
        if letra == 'Y' or letra == 'y':
            with open(archivoClave, 'wb') as filekey:
                filekey.write(key)
        elif letra == 'N' or letra == 'n':
            print("Escriba el nombre del archivo donde se generará la clave (.key): ")
            archivoClave = input()
            with open(archivoClave, 'wb') as filekey:
                filekey.write(key)  
        else:
            menu()             

    # lectura de la clave
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    # se guarda en variable la clave generada
    fernet = Fernet(key)

    # seleccionamos el archivo a encriptar
    print("Selecciona el archivo a encriptar: (Recuerda que si el archivo no está en esta carpeta, debes definir su 'path'): ")
    archivo = input()

    # lectura del archivo para encriptar
    with open(archivo, 'rb') as file:
        original = file.read()
    
    # función para encriptar el archivo
    encrypted = fernet.encrypt(original)

    # se abre el archivo en modo escritura y
    # se escribe el dato encriptado
    with open(archivo, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def fromFernet():
    # lectura de la clave
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    # seleccionamos el archivo a encriptar
    print("Selecciona el archivo a descriptar: (Recuerda que si el archivo no está en esta carpeta, debes definir su 'path'): ")
    archivo2 = input()

    # lecura del archivo encriptado
    with open(archivo2, 'rb') as enc_file:
	    encrypted = enc_file.read()

    # decriptacion del archivo encriptado
    decrypted = fernet.decrypt(encrypted)

    # abrir el archivo encriptado en modo escritura
    with open(archivo2, 'wb') as dec_file:
	    dec_file.write(decrypted)    


def encryptMessage():
    print("Which type of encryption you want to use: ")
    print("1. Base 64")
    print("2. Fernet (AES in CBC Mode:")
    
    option = input()

    if option == "1":
        toBase64()
    else: 
        toFernet()


def decryptMessage():
    print("Which type of decryption you want to use: ")
    print("1. Base 64")
    print("2. Fernet (AES in CBC Mode:")

    option = input()

    if option == "1":
        fromBase64()
    else:
        fromFernet()    

menu()
