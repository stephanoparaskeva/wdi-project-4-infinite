from app import app, db

from models.coin import Coin
from models.transaction import Transaction
from models.user import UserSchema
user_schema = UserSchema()

with app.app_context():
    db.drop_all()
    db.create_all()

    stephano, errors = user_schema.load({
        'username': 'stephano',
        'email': 'stephano@email.com',
        'password': 'password',
        'password_confirmation': 'password'
    })

    if errors:
        raise Exception(errors)

    db.session.add(stephano)

    sabo, errors = user_schema.load({
        'username': 'sabo',
        'email': 'sabo@email.com',
        'password': 'password',
        'password_confirmation': 'password'
    })

    if errors:
        raise Exception(errors)

    db.session.add(sabo)


    BTC = Coin(currency='BTC', full_name='Bitcoin', id='BTC', url='https://www.cryptocompare.com/media/19633/btc.png')
    ETH = Coin(currency='ETH', full_name='Ethereum', id='ETH', url='https://www.cryptocompare.com/media/20646/eth_logo.png')
    LTC = Coin(currency='LTC', full_name='Litecoin', id='LTC', url='https://www.cryptocompare.com/media/35309662/ltc.png')
    DASH = Coin(currency='DASH', full_name='Dash', id='DASH', url='https://www.cryptocompare.com/media/33842920/dash.png')
    XMR = Coin(currency='XMR', full_name='Monero', id='XMR', url='https://www.cryptocompare.com/media/19969/xmr.png')
    NXT = Coin(currency='NXT', full_name='Nxt', id='NXT', url='https://www.cryptocompare.com/media/20627/nxt.png')
    ETC = Coin(currency='ETC', full_name='Ethereum Classic', id='ETC', url='https://www.cryptocompare.com/media/33752295/etc_new.png')
    DOGE = Coin(currency='DOGE', full_name='Dogecoin', id='DOGE', url='https://www.cryptocompare.com/media/19684/doge.png')
    ZEC = Coin(currency='ZEC', full_name='ZCash', id='ZEC', url='https://www.cryptocompare.com/media/351360/zec.png')
    BTS = Coin(currency='BTS', full_name='Bitshares', id='BTS', url='https://www.cryptocompare.com/media/20705/bts.png')
    DGB = Coin(currency='DGB', full_name='DigiByte', id='DGB', url='https://www.cryptocompare.com/media/12318264/7638-nty_400x400.jpg')
    XRP = Coin(currency='XRP', full_name='XRP', id='XRP', url='https://www.cryptocompare.com/media/34477776/xrp.png')
    BTCD = Coin(currency='BTCD', full_name='BitcoinDark', id='BTCD', url='https://www.cryptocompare.com/media/19630/btcd_1.png')
    PPC = Coin(currency='PPC', full_name='PeerCoin', id='PPC', url='https://www.cryptocompare.com/media/19864/peercoin-logo.png')
    CRAIG = Coin(currency='CRAIG', full_name='CraigsCoin', id='CRAIG', url='https://www.cryptocompare.com/media/20022/craig.png')
    XBS = Coin(currency='XBS', full_name='Bitstake', id='XBS', url='https://www.cryptocompare.com/media/351060/xbs_1.png')
    XPY = Coin(currency='XPY', full_name='PayCoin', id='XPY', url='https://www.cryptocompare.com/media/20076/xpy_1.png')
    PRC = Coin(currency='PRC', full_name='ProsperCoin', id='PRC', url='https://www.cryptocompare.com/media/20393/prc.png')
    YBC = Coin(currency='YBC', full_name='YbCoin', id='YBC', url='https://www.cryptocompare.com/media/19975/ybc.png')
    DANK = Coin(currency='DANK', full_name='DarkKush', id='DANK', url='https://www.cryptocompare.com/media/20247/dank.png')
    GIVE = Coin(currency='GIVE', full_name='GiveCoin', id='GIVE', url='https://www.cryptocompare.com/media/20297/give.png')
    KOBO = Coin(currency='KOBO', full_name='KoboCoin', id='KOBO', url='https://www.cryptocompare.com/media/35521133/kobo.png')
    DT = Coin(currency='DT', full_name='DarkToken', id='DT', url='https://www.cryptocompare.com/media/20031/dt.png')
    CETI = Coin(currency='CETI', full_name='CETUS Coin', id='CETI', url='https://www.cryptocompare.com/media/20228/ceti.png')
    SUP = Coin(currency='SUP', full_name='Supcoin', id='SUP', url='https://www.cryptocompare.com/media/20442/sup.png')
    XPD = Coin(currency='XPD', full_name='PetroDollar', id='XPD', url='https://www.cryptocompare.com/media/20162/xpd.png')
    GEO = Coin(currency='GEO', full_name='GeoCoin', id='GEO', url='https://www.cryptocompare.com/media/35309716/geo.png')
    CHASH = Coin(currency='CHASH', full_name='CleverHash', id='CHASH', url='https://www.cryptocompare.com/media/20231/chash.png')
    SPR = Coin(currency='SPR', full_name='Spreadcoin', id='SPR', url='https://www.cryptocompare.com/media/20438/spr.png')
    NXTI = Coin(currency='NXTI', full_name='NXTI', id='NXTI', url='https://www.cryptocompare.com/media/20376/nxti.png')
    WOLF = Coin(currency='WOLF', full_name='Insanity Coin', id='WOLF', url='https://www.cryptocompare.com/media/20559/wolf.png')
    XDP = Coin(currency='XDP', full_name='DogeParty', id='XDP', url='https://www.cryptocompare.com/media/20560/xdp.png')
    AC = Coin(currency='AC', full_name='Asia Coin', id='AC', url='https://www.cryptocompare.com/media/19593/ac.png')
    ACOIN = Coin(currency='ACOIN', full_name='ACoin', id='ACOIN', url='https://www.cryptocompare.com/media/20079/acoin.png')
    AERO = Coin(currency='AERO', full_name='Aero Coin', id='AERO', url='https://www.cryptocompare.com/media/19594/aero.png')
    ALF = Coin(currency='ALF', full_name='AlphaCoin', id='ALF', url='https://www.cryptocompare.com/media/19600/alf.png')
    AGS = Coin(currency='AGS', full_name='Aegis', id='AGS', url='https://www.cryptocompare.com/media/19595/ags.png')
    AMC = Coin(currency='AMC', full_name='AmericanCoin', id='AMC', url='https://www.cryptocompare.com/media/19601/amc.png')
    ALN = Coin(currency='ALN', full_name='AlienCoin', id='ALN', url='https://www.cryptocompare.com/media/20080/aln.png')
    APEX = Coin(currency='APEX', full_name='ApexCoin', id='APEX', url='https://www.cryptocompare.com/media/19599/apex.png')
    ARCH = Coin(currency='ARCH', full_name='ArchCoin', id='ARCH', url='https://www.cryptocompare.com/media/20085/arch.png')
    ARG = Coin(currency='ARG', full_name='Argentum', id='ARG', url='https://www.cryptocompare.com/media/19602/arg.png')
    ARI = Coin(currency='ARI', full_name='AriCoin', id='ARI', url='https://www.cryptocompare.com/media/20082/ari.png')
    AUR = Coin(currency='AUR', full_name='Aurora Coin', id='AUR', url='https://www.cryptocompare.com/media/19608/aur.png')
    AXR = Coin(currency='AXR', full_name='AXRON', id='AXR', url='https://www.cryptocompare.com/media/20086/axr.png')
    BCX = Coin(currency='BCX', full_name='BattleCoin', id='BCX', url='https://www.cryptocompare.com/media/19620/bcx.png')
    BET = Coin(currency='BET', full_name='BetaCoin', id='BET', url='https://www.cryptocompare.com/media/19621/bet.png')
    BEAN = Coin(currency='BEAN', full_name='BeanCash', id='BEAN', url='https://www.cryptocompare.com/media/350879/bitb.png')
    BLU = Coin(currency='BLU', full_name='BlueCoin', id='BLU', url='https://www.cryptocompare.com/media/19624/blu.png')
    BLK = Coin(currency='BLK', full_name='BlackCoin', id='BLK', url='https://www.cryptocompare.com/media/351795/blk.png')
    BOST = Coin(currency='BOST', full_name='BoostCoin', id='BOST', url='https://www.cryptocompare.com/media/19626/bost.png')
    BQC = Coin(currency='BQC', full_name='BQCoin', id='BQC', url='https://www.cryptocompare.com/media/19631/bqc.png')
    XMY = Coin(currency='XMY', full_name='MyriadCoin', id='XMY', url='https://www.cryptocompare.com/media/19815/myr.png')
    MOON = Coin(currency='MOON', full_name='MoonCoin', id='MOON', url='https://www.cryptocompare.com/media/19802/moon.png')
    ZET = Coin(currency='ZET', full_name='ZetaCoin', id='ZET', url='https://www.cryptocompare.com/media/19993/zet.png')
    SXC = Coin(currency='SXC', full_name='SexCoin', id='SXC', url='https://www.cryptocompare.com/media/19924/sxc.png')
    QTL = Coin(currency='QTL', full_name='Quatloo', id='QTL', url='https://www.cryptocompare.com/media/19879/qtl.png')
    ENRG = Coin(currency='ENRG', full_name='EnergyCoin', id='ENRG', url='https://www.cryptocompare.com/media/19697/enrg.png')
    QRK = Coin(currency='QRK', full_name='QuarkCoin', id='QRK', url='https://www.cryptocompare.com/media/19882/qrk.png')
    RIC = Coin(currency='RIC', full_name='Riecoin', id='RIC', url='https://www.cryptocompare.com/media/19888/ric.jpg')
    DGC = Coin(currency='DGC', full_name='DigiCoin', id='DGC', url='https://www.cryptocompare.com/media/19676/dgc.png')
    LIMX = Coin(currency='LIMX', full_name='LimeCoinX', id='LIMX', url='https://www.cryptocompare.com/media/19769/limx.png')
    BTB = Coin(currency='BTB', full_name='BitBar', id='BTB', url='https://www.cryptocompare.com/media/20083/bitb.png')
    CAIX = Coin(currency='CAIX', full_name='CAIx', id='CAIX', url='https://www.cryptocompare.com/media/20226/caix.png')
    BTE = Coin(currency='BTE', full_name='ByteCoin', id='BTE', url='https://www.cryptocompare.com/media/19632/bte.png')
    BUK = Coin(currency='BUK', full_name='CryptoBuk', id='BUK', url='https://www.cryptocompare.com/media/19637/buk.png')
    CACH = Coin(currency='CACH', full_name='Cachecoin', id='CACH', url='https://www.cryptocompare.com/media/19642/cach.png')
    CANN = Coin(currency='CANN', full_name='CannabisCoin', id='CANN', url='https://www.cryptocompare.com/media/20015/cann.png')
    CAP = Coin(currency='CAP', full_name='BottleCaps', id='CAP', url='https://www.cryptocompare.com/media/20017/cap.png')
    CASH = Coin(currency='CASH', full_name='CashCoin', id='CASH', url='https://www.cryptocompare.com/media/20016/cash.png')
    CAT = Coin(currency='CAT', full_name='Catcoin', id='CAT', url='https://www.cryptocompare.com/media/35521144/cat.png')
    CBX = Coin(currency='CBX', full_name='CryptoBullion', id='CBX', url='https://www.cryptocompare.com/media/30001996/cbx.png')
    CCN = Coin(currency='CCN', full_name='CannaCoin', id='CCN', url='https://www.cryptocompare.com/media/19643/ccn.png')
    CIN = Coin(currency='CIN', full_name='CinderCoin', id='CIN', url='https://www.cryptocompare.com/media/20698/cinder.png')
    CINNI = Coin(currency='CINNI', full_name='CINNICOIN', id='CINNI', url='https://www.cryptocompare.com/media/19651/cinni.jpeg')
    CXC = Coin(currency='CXC', full_name='CheckCoin', id='CXC', url='https://www.cryptocompare.com/media/20246/cxc.png')
    CLAM = Coin(currency='CLAM', full_name='CLAMS', id='CLAM', url='https://www.cryptocompare.com/media/20020/clam.png')
    CLOAK = Coin(currency='CLOAK', full_name='CloakCoin', id='CLOAK', url='https://www.cryptocompare.com/media/19994/cloak.png')
    CLR = Coin(currency='CLR', full_name='CopperLark', id='CLR', url='https://www.cryptocompare.com/media/19657/clr.png')
    CMC = Coin(currency='CMC', full_name='CosmosCoin', id='CMC', url='https://www.cryptocompare.com/media/20019/cmc.png')
    CNC = Coin(currency='CNC', full_name='ChinaCoin', id='CNC', url='https://www.cryptocompare.com/media/20021/cnc.png')
    CNL = Coin(currency='CNL', full_name='ConcealCoin', id='CNL', url='https://www.cryptocompare.com/media/20024/cnl.png')
    COMM = Coin(currency='COMM', full_name='Community Coin', id='COMM', url='https://www.cryptocompare.com/media/19661/comm.png')
    COOL = Coin(currency='COOL', full_name='CoolCoin', id='COOL', url='https://www.cryptocompare.com/media/19658/cool.png')
    CRACK = Coin(currency='CRACK', full_name='CrackCoin', id='CRACK', url='https://www.cryptocompare.com/media/20023/crack.png')
    CRYPT = Coin(currency='CRYPT', full_name='CryptCoin', id='CRYPT', url='https://www.cryptocompare.com/media/19664/crypt.png')
    CSC = Coin(currency='CSC', full_name='CasinoCoin', id='CSC', url='https://www.cryptocompare.com/media/34478059/csc.png')
    DEM = Coin(currency='DEM', full_name='eMark', id='DEM', url='https://www.cryptocompare.com/media/20028/dem.png')
    DMD = Coin(currency='DMD', full_name='Diamond', id='DMD', url='https://www.cryptocompare.com/media/19680/dmd.png')
    XVG = Coin(currency='XVG', full_name='Verge', id='XVG', url='https://www.cryptocompare.com/media/12318032/xvg.png')
    DRKC = Coin(currency='DRKC', full_name='DarkCash', id='DRKC', url='https://www.cryptocompare.com/media/20027/drkc.png')
    DSB = Coin(currency='DSB', full_name='DarkShibe', id='DSB', url='https://www.cryptocompare.com/media/20034/dsb.png')
    DVC = Coin(currency='DVC', full_name='DevCoin', id='DVC', url='https://www.cryptocompare.com/media/20563/dvc.png')
    EAC = Coin(currency='EAC', full_name='EarthCoin', id='EAC', url='https://www.cryptocompare.com/media/19690/eac.png')
    EFL = Coin(currency='EFL', full_name='E-Gulden', id='EFL', url='https://www.cryptocompare.com/media/19692/efl.png')
    ELC = Coin(currency='ELC', full_name='Elacoin', id='ELC', url='https://www.cryptocompare.com/media/19694/elc.png')
    EMC2 = Coin(currency='EMC2', full_name='Einsteinium', id='EMC2', url='https://www.cryptocompare.com/media/20033/emc2.png')
    EMD = Coin(currency='EMD', full_name='Emerald', id='EMD', url='https://www.cryptocompare.com/media/35284304/emd.png')
    EXCL = Coin(currency='EXCL', full_name='Exclusive Coin', id='EXCL', url='https://www.cryptocompare.com/media/20035/excl.png')
    EXE = Coin(currency='EXE', full_name='ExeCoin', id='EXE', url='https://www.cryptocompare.com/media/19700/exe.png')
    EZC = Coin(currency='EZC', full_name='EZCoin', id='EZC', url='https://www.cryptocompare.com/media/19702/ezc.png')
    FLAP = Coin(currency='FLAP', full_name='Flappy Coin', id='FLAP', url='https://www.cryptocompare.com/media/20032/flap.png')
    FC2 = Coin(currency='FC2', full_name='Fuel2Coin', id='FC2', url='https://www.cryptocompare.com/media/19719/fuel.png')
    FFC = Coin(currency='FFC', full_name='FireflyCoin', id='FFC', url='https://www.cryptocompare.com/media/19706/ffc.png')
    FIBRE = Coin(currency='FIBRE', full_name='FIBRE', id='FIBRE', url='https://www.cryptocompare.com/media/20030/fibre.png')
    FRC = Coin(currency='FRC', full_name='FireRoosterCoin', id='FRC', url='https://www.cryptocompare.com/media/1382629/frc.png')
    FLT = Coin(currency='FLT', full_name='FlutterCoin', id='FLT', url='https://www.cryptocompare.com/media/19709/flt.png')
    FRK = Coin(currency='FRK', full_name='Franko', id='FRK', url='https://www.cryptocompare.com/media/19712/frk.png')
    FRAC = Coin(currency='FRAC', full_name='FractalCoin', id='FRAC', url='https://www.cryptocompare.com/media/19710/frac.png')
    FST = Coin(currency='FST', full_name='FastCoin', id='FST', url='https://www.cryptocompare.com/media/19720/fst.png')
    FTC = Coin(currency='FTC', full_name='FeatherCoin', id='FTC', url='https://www.cryptocompare.com/media/19718/ftc.png')
    GDC = Coin(currency='GDC', full_name='GrandCoin', id='GDC', url='https://www.cryptocompare.com/media/20054/gdc.png')
    GLC = Coin(currency='GLC', full_name='GlobalCoin', id='GLC', url='https://www.cryptocompare.com/media/19724/glc.png')
    GLD = Coin(currency='GLD', full_name='GoldCoin', id='GLD', url='https://www.cryptocompare.com/media/19723/gld.png')
    GLX = Coin(currency='GLX', full_name='GalaxyCoin', id='GLX', url='https://www.cryptocompare.com/media/19728/glx.png')
    GLYPH = Coin(currency='GLYPH', full_name='GlyphCoin', id='GLYPH', url='https://www.cryptocompare.com/media/19725/glyph.png')
    GML = Coin(currency='GML', full_name='GameLeagueCoin', id='GML', url='https://www.cryptocompare.com/media/19726/gml.png')
    GUE = Coin(currency='GUE', full_name='GuerillaCoin', id='GUE', url='https://www.cryptocompare.com/media/19732/gue.png')
    HAL = Coin(currency='HAL', full_name='Halcyon', id='HAL', url='https://www.cryptocompare.com/media/20036/hal.png')
    HBN = Coin(currency='HBN', full_name='HoboNickels', id='HBN', url='https://www.cryptocompare.com/media/19735/hbn.png')
    HUC = Coin(currency='HUC', full_name='HunterCoin', id='HUC', url='https://www.cryptocompare.com/media/20037/hun.png')
    HVC = Coin(currency='HVC', full_name='HeavyCoin', id='HVC', url='https://www.cryptocompare.com/media/19745/hvc.png')
    HYP = Coin(currency='HYP', full_name='Hyperstake', id='HYP', url='https://www.cryptocompare.com/media/20624/hyp.png')
    ICB = Coin(currency='ICB', full_name='IceBergCoin', id='ICB', url='https://www.cryptocompare.com/media/19747/icb.png')
    IFC = Coin(currency='IFC', full_name='Infinite Coin', id='IFC', url='https://www.cryptocompare.com/media/19754/ifc.png')
    IOC = Coin(currency='IOC', full_name='IOCoin', id='IOC', url='https://www.cryptocompare.com/media/20042/ioc.png')
    IXC = Coin(currency='IXC', full_name='IXcoin', id='IXC', url='https://www.cryptocompare.com/media/19761/ixc.png')
    JBS = Coin(currency='JBS', full_name='JumBucks Coin', id='JBS', url='https://www.cryptocompare.com/media/20044/jbs.png')
    JKC = Coin(currency='JKC', full_name='JunkCoin', id='JKC', url='https://www.cryptocompare.com/media/19757/jkc.png')
    JUDGE = Coin(currency='JUDGE', full_name='JudgeCoin', id='JUDGE', url='https://www.cryptocompare.com/media/20038/judge.png')
    KDC = Coin(currency='KDC', full_name='Klondike Coin', id='KDC', url='https://www.cryptocompare.com/media/19766/kdc.png')
    KGC = Coin(currency='KGC', full_name='KrugerCoin', id='KGC', url='https://www.cryptocompare.com/media/19763/kgc.png')
    LK7 = Coin(currency='LK7', full_name='Lucky7Coin', id='LK7', url='https://www.cryptocompare.com/media/19776/lk7.png')
    LKY = Coin(currency='LKY', full_name='LuckyCoin', id='LKY', url='https://www.cryptocompare.com/media/19774/lky.png')
    LSD = Coin(currency='LSD', full_name='LightSpeedCoin', id='LSD', url='https://www.cryptocompare.com/media/20041/lsd.png')
    LTB = Coin(currency='LTB', full_name='Litebar ', id='LTB', url='https://www.cryptocompare.com/media/20336/ltb.png')
    LTCD = Coin(currency='LTCD', full_name='LitecoinDark', id='LTCD', url='https://www.cryptocompare.com/media/20043/ltcd.png')
    LTCX = Coin(currency='LTCX', full_name='LitecoinX', id='LTCX', url='https://www.cryptocompare.com/media/19779/ltcx.png')
    LXC = Coin(currency='LXC', full_name='LibrexCoin', id='LXC', url='https://www.cryptocompare.com/media/20045/lxc.png')
    LYC = Coin(currency='LYC', full_name='LycanCoin', id='LYC', url='https://www.cryptocompare.com/media/19785/lyc.png')
    MAX = Coin(currency='MAX', full_name='MaxCoin', id='MAX', url='https://www.cryptocompare.com/media/19786/max.png')
    MEC = Coin(currency='MEC', full_name='MegaCoin', id='MEC', url='https://www.cryptocompare.com/media/19789/mec.png')
    MED = Coin(currency='MED', full_name='MediterraneanCoin', id='MED', url='https://www.cryptocompare.com/media/20046/med.png')
    MIN = Coin(currency='MIN', full_name='Minerals Coin', id='MIN', url='https://www.cryptocompare.com/media/19793/min.png')
    MN = Coin(currency='MN', full_name='Cryptsy Mining Contract', id='MN', url='https://www.cryptocompare.com/media/19796/mn1.png')
    MINC = Coin(currency='MINC', full_name='MinCoin', id='MINC', url='https://www.cryptocompare.com/media/19805/mincoin.png')
    MRY = Coin(currency='MRY', full_name='MurrayCoin', id='MRY', url='https://www.cryptocompare.com/media/19807/mry.jpg')
    MZC = Coin(currency='MZC', full_name='MazaCoin', id='MZC', url='https://www.cryptocompare.com/media/19816/mzc.png')
    NAN = Coin(currency='NAN', full_name='NanoToken', id='NAN', url='https://www.cryptocompare.com/media/19821/nan.png')
    NAUT = Coin(currency='NAUT', full_name='Nautilus Coin', id='NAUT', url='https://www.cryptocompare.com/media/19822/naut.png')
    NAV = Coin(currency='NAV', full_name='NavCoin', id='NAV', url='https://www.cryptocompare.com/media/351431/nav.png')
    NBL = Coin(currency='NBL', full_name='Nybble', id='NBL', url='https://www.cryptocompare.com/media/19825/nbl.png')
    NEC = Coin(currency='NEC', full_name='NeoCoin', id='NEC', url='https://www.cryptocompare.com/media/19824/nec.png')
    NET = Coin(currency='NET', full_name='NetCoin', id='NET', url='https://www.cryptocompare.com/media/19826/net.png')
    NMB = Coin(currency='NMB', full_name='Nimbus Coin', id='NMB', url='https://www.cryptocompare.com/media/20049/nmb.png')
    NRB = Coin(currency='NRB', full_name='NoirBits', id='NRB', url='https://www.cryptocompare.com/media/19839/nrb.png')
    NOBL = Coin(currency='NOBL', full_name='NobleCoin', id='NOBL', url='https://www.cryptocompare.com/media/19833/nobl.png')
    NRS = Coin(currency='NRS', full_name='NoirShares', id='NRS', url='https://www.cryptocompare.com/media/19834/nrs.png')
    NVC = Coin(currency='NVC', full_name='NovaCoin', id='NVC', url='https://www.cryptocompare.com/media/20713/nvc.png')
    NMC = Coin(currency='NMC', full_name='Namecoin', id='NMC', url='https://www.cryptocompare.com/media/19830/nmc.png')
    NYAN = Coin(currency='NYAN', full_name='NyanCoin', id='NYAN', url='https://www.cryptocompare.com/media/19842/nyan.png')
    OPAL = Coin(currency='OPAL', full_name='OpalCoin', id='OPAL', url='https://www.cryptocompare.com/media/20050/opal.png')
    ORB = Coin(currency='ORB', full_name='Orbitcoin', id='ORB', url='https://www.cryptocompare.com/media/19845/orb.png')
    OSC = Coin(currency='OSC', full_name='OpenSourceCoin', id='OSC', url='https://www.cryptocompare.com/media/19847/osc.png')
    PHS = Coin(currency='PHS', full_name='PhilosophersStone', id='PHS', url='https://www.cryptocompare.com/media/19857/phs.png')
    POINTS = Coin(currency='POINTS', full_name='Cryptsy Points', id='POINTS', url='https://www.cryptocompare.com/media/19863/points.png')
    POT = Coin(currency='POT', full_name='PotCoin', id='POT', url='https://www.cryptocompare.com/media/35309673/pot.png')
    PSEUD = Coin(currency='PSEUD', full_name='PseudoCash', id='PSEUD', url='https://www.cryptocompare.com/media/20052/pseud.png')
    PXC = Coin(currency='PXC', full_name='PhoenixCoin', id='PXC', url='https://www.cryptocompare.com/media/20058/pxc.png')
    PYC = Coin(currency='PYC', full_name='PayCoin', id='PYC', url='https://www.cryptocompare.com/media/19878/pyc.png')
    RDD = Coin(currency='RDD', full_name='Reddcoin', id='RDD', url='https://www.cryptocompare.com/media/19887/rdd.png')
    RIPO = Coin(currency='RIPO', full_name='RipOffCoin', id='RIPO', url='https://www.cryptocompare.com/media/20051/ripo.png')
    RPC = Coin(currency='RPC', full_name='RonPaulCoin', id='RPC', url='https://www.cryptocompare.com/media/19895/rpc-2.png')
    RT2 = Coin(currency='RT2', full_name='RotoCoin', id='RT2', url='https://www.cryptocompare.com/media/19896/rt2.png')
    RYC = Coin(currency='RYC', full_name='RoyalCoin', id='RYC', url='https://www.cryptocompare.com/media/19898/ryc.png')
    RZR = Coin(currency='RZR', full_name='RazorCoin', id='RZR', url='https://www.cryptocompare.com/media/20055/rzr.png')
    SAT2 = Coin(currency='SAT2', full_name='Saturn2Coin', id='SAT2', url='https://www.cryptocompare.com/media/19897/sat2.png')
    SBC = Coin(currency='SBC', full_name='StableCoin', id='SBC', url='https://www.cryptocompare.com/media/19900/sbc.png')
    SDC = Coin(currency='SDC', full_name='ShadowCash', id='SDC', url='https://www.cryptocompare.com/media/20419/sdc.png')
    SFR = Coin(currency='SFR', full_name='SaffronCoin', id='SFR', url='https://www.cryptocompare.com/media/19903/sfr.png')
    SHADE = Coin(currency='SHADE', full_name='ShadeCoin', id='SHADE', url='https://www.cryptocompare.com/media/20056/shade.png')
    SHLD = Coin(currency='SHLD', full_name='ShieldCoin', id='SHLD', url='https://www.cryptocompare.com/media/19904/shld.png')
    SILK = Coin(currency='SILK', full_name='SilkCoin', id='SILK', url='https://www.cryptocompare.com/media/20057/silk.png')
    SLG = Coin(currency='SLG', full_name='SterlingCoin', id='SLG', url='https://www.cryptocompare.com/media/20428/slg.png')
    SMC = Coin(currency='SMC', full_name='SmartCoin', id='SMC', url='https://www.cryptocompare.com/media/20059/smc.png')
    SOLE = Coin(currency='SOLE', full_name='SoleCoin', id='SOLE', url='https://www.cryptocompare.com/media/20431/sole.png')
    SPA = Coin(currency='SPA', full_name='SpainCoin', id='SPA', url='https://www.cryptocompare.com/media/19911/spa.png')
    SPT = Coin(currency='SPT', full_name='Spots', id='SPT', url='https://www.cryptocompare.com/media/19917/spt.png')
    SRC = Coin(currency='SRC', full_name='SecureCoin', id='SRC', url='https://www.cryptocompare.com/media/19918/src.png')
    SSV = Coin(currency='SSV', full_name='SSVCoin', id='SSV', url='https://www.cryptocompare.com/media/20060/ssv.png')
    SUPER = Coin(currency='SUPER', full_name='SuperCoin', id='SUPER', url='https://www.cryptocompare.com/media/20061/super.png')
    SWIFT = Coin(currency='SWIFT', full_name='BitSwift', id='SWIFT', url='https://www.cryptocompare.com/media/20446/swift.png')
    SYNC = Coin(currency='SYNC', full_name='SyncCoin', id='SYNC', url='https://www.cryptocompare.com/media/19922/sync.png')
    SYS = Coin(currency='SYS', full_name='SysCoin', id='SYS', url='https://www.cryptocompare.com/media/25792583/sys.png')
    TAG = Coin(currency='TAG', full_name='TagCoin', id='TAG', url='https://www.cryptocompare.com/media/19925/tag.png')
    TAK = Coin(currency='TAK', full_name='TakCoin', id='TAK', url='https://www.cryptocompare.com/media/19928/tak.png')
    TES = Coin(currency='TES', full_name='TeslaCoin', id='TES', url='https://www.cryptocompare.com/media/19927/tes.png')
    TGC = Coin(currency='TGC', full_name='TigerCoin', id='TGC', url='https://www.cryptocompare.com/media/19930/tgc.png')
    TIT = Coin(currency='TIT', full_name='TittieCoin', id='TIT', url='https://www.cryptocompare.com/media/20064/ttc.png')
    TOR = Coin(currency='TOR', full_name='TorCoin', id='TOR', url='https://www.cryptocompare.com/media/19934/tor.png')
    TRC = Coin(currency='TRC', full_name='TerraCoin', id='TRC', url='https://www.cryptocompare.com/media/19938/terracoin.png')
    ULTC = Coin(currency='ULTC', full_name='Umbrella', id='ULTC', url='https://www.cryptocompare.com/media/20063/ultc.png')
    UNB = Coin(currency='UNB', full_name='UnbreakableCoin', id='UNB', url='https://www.cryptocompare.com/media/19940/unb.png')
    UNO = Coin(currency='UNO', full_name='Unobtanium', id='UNO', url='https://www.cryptocompare.com/media/20065/uno.png')
    URO = Coin(currency='URO', full_name='UroCoin', id='URO', url='https://www.cryptocompare.com/media/19937/uro.png')
    USDE = Coin(currency='USDE', full_name='UnitaryStatus Dollar', id='USDE', url='https://www.cryptocompare.com/media/20465/usde.png')
    UTC = Coin(currency='UTC', full_name='UltraCoin', id='UTC', url='https://www.cryptocompare.com/media/35309631/utc.png')
    UTIL = Coin(currency='UTIL', full_name='Utility Coin', id='UTIL', url='https://www.cryptocompare.com/media/20067/util.png')
    VDO = Coin(currency='VDO', full_name='VidioCoin', id='VDO', url='https://www.cryptocompare.com/media/20066/vdo.png')
    VIA = Coin(currency='VIA', full_name='ViaCoin', id='VIA', url='https://www.cryptocompare.com/media/20070/via.png')
    VOOT = Coin(currency='VOOT', full_name='VootCoin', id='VOOT', url='https://www.cryptocompare.com/media/19946/voot.png')
    VRC = Coin(currency='VRC', full_name='VeriCoin', id='VRC', url='https://www.cryptocompare.com/media/20068/vrc.png')
    VTC = Coin(currency='VTC', full_name='Vertcoin', id='VTC', url='https://www.cryptocompare.com/media/19945/vtc.png')
    WC = Coin(currency='WC', full_name='WhiteCoin', id='WC', url='https://www.cryptocompare.com/media/19948/wc.png')
    WDC = Coin(currency='WDC', full_name='WorldCoin', id='WDC', url='https://www.cryptocompare.com/media/19949/wdc.png')
    XAI = Coin(currency='XAI', full_name='SapienceCoin', id='XAI', url='https://www.cryptocompare.com/media/20071/xai.png')
    XBOT = Coin(currency='XBOT', full_name='SocialXbotCoin', id='XBOT', url='https://www.cryptocompare.com/media/20073/xbot.png')
    XC = Coin(currency='XC', full_name='X11 Coin', id='XC', url='https://www.cryptocompare.com/media/19956/xc.png')
    XCSH = Coin(currency='XCSH', full_name='Xcash', id='XCSH', url='https://www.cryptocompare.com/media/20075/xcash.png')
    XCR = Coin(currency='XCR', full_name='Crypti', id='XCR', url='https://www.cryptocompare.com/media/19710/frac.png')
    XJO = Coin(currency='XJO', full_name='JouleCoin', id='XJO', url='https://www.cryptocompare.com/media/19962/xjo.png')
    XLB = Coin(currency='XLB', full_name='LibertyCoin', id='XLB', url='https://www.cryptocompare.com/media/19966/xlb.png')
    XPM = Coin(currency='XPM', full_name='PrimeCoin', id='XPM', url='https://www.cryptocompare.com/media/19970/xpm.png')
    XST = Coin(currency='XST', full_name='StealthCoin', id='XST', url='https://www.cryptocompare.com/media/20077/xst.png')
    XXX = Coin(currency='XXX', full_name='XXXCoin', id='XXX', url='https://www.cryptocompare.com/media/350617/xxx.png')
    YAC = Coin(currency='YAC', full_name='YAcCoin', id='YAC', url='https://www.cryptocompare.com/media/19976/yac.png')
    ZCC = Coin(currency='ZCC', full_name='ZCC Coin', id='ZCC', url='https://www.cryptocompare.com/media/19979/zcc.png')
    ZED = Coin(currency='ZED', full_name='ZedCoins', id='ZED', url='https://www.cryptocompare.com/media/19981/zed.png')
    BCN = Coin(currency='BCN', full_name='ByteCoin', id='BCN', url='https://www.cryptocompare.com/media/12318404/bcn.png')
    EKN = Coin(currency='EKN', full_name='Elektron', id='EKN', url='https://www.cryptocompare.com/media/20270/ekn.png')
    XAU = Coin(currency='XAU', full_name='XauCoin', id='XAU', url='https://www.cryptocompare.com/media/20479/xau.png')
    TMC = Coin(currency='TMC', full_name='TimesCoin', id='TMC', url='https://www.cryptocompare.com/media/20451/tmc.png')
    XEM = Coin(currency='XEM', full_name='NEM', id='XEM', url='https://www.cryptocompare.com/media/20490/xem.png')
    BURST = Coin(currency='BURST', full_name='BurstCoin', id='BURST', url='https://www.cryptocompare.com/media/16746623/burst.png')
    NBT = Coin(currency='NBT', full_name='NuBits', id='NBT', url='https://www.cryptocompare.com/media/20363/nbt.png')
    SJCX = Coin(currency='SJCX', full_name='StorjCoin', id='SJCX', url='https://www.cryptocompare.com/media/20422/sjcx.png')
    START = Coin(currency='START', full_name='StartCoin', id='START', url='https://www.cryptocompare.com/media/19916/start.png')
    HUGE = Coin(currency='HUGE', full_name='BigCoin', id='HUGE', url='https://www.cryptocompare.com/media/20318/huge.png')
    XCP = Coin(currency='XCP', full_name='CounterParty', id='XCP', url='https://www.cryptocompare.com/media/19960/xcp.png')
    MAID = Coin(currency='MAID', full_name='MaidSafe Coin', id='MAID', url='https://www.cryptocompare.com/media/352247/maid.png')
    NSR = Coin(currency='NSR', full_name='NuShares', id='NSR', url='https://www.cryptocompare.com/media/20378/nsr.png')
    MONA = Coin(currency='MONA', full_name='MonaCoin', id='MONA', url='https://www.cryptocompare.com/media/35309574/mona.png')
    CELL = Coin(currency='CELL', full_name='SolarFarm', id='CELL', url='https://www.cryptocompare.com/media/20227/cell.png')
    TEK = Coin(currency='TEK', full_name='TekCoin', id='TEK', url='https://www.cryptocompare.com/media/19929/tek.png')
    BAY = Coin(currency='BAY', full_name='BitBay', id='BAY', url='https://www.cryptocompare.com/media/1383137/bay1.png')
    NTRN = Coin(currency='NTRN', full_name='Neutron', id='NTRN', url='https://www.cryptocompare.com/media/12318281/ntrn.png')
    SLING = Coin(currency='SLING', full_name='Sling Coin', id='SLING', url='https://www.cryptocompare.com/media/20425/sling.png')
    XVC = Coin(currency='XVC', full_name='Vcash', id='XVC', url='https://www.cryptocompare.com/media/350813/xvc.png')
    CRAVE = Coin(currency='CRAVE', full_name='CraveCoin', id='CRAVE', url='https://www.cryptocompare.com/media/20242/crave.png')
    BLOCK = Coin(currency='BLOCK', full_name='BlockNet', id='BLOCK', url='https://www.cryptocompare.com/media/20204/block.png')
    XSI = Coin(currency='XSI', full_name='Stability Shares', id='XSI', url='https://www.cryptocompare.com/media/20165/xsi.png')
    BYC = Coin(currency='BYC', full_name='ByteCent', id='BYC', url='https://www.cryptocompare.com/media/20217/byc.png')
    GRC = Coin(currency='GRC', full_name='GridCoin', id='GRC', url='https://www.cryptocompare.com/media/20307/grc.png')
    GEMZ = Coin(currency='GEMZ', full_name='Gemz Social', id='GEMZ', url='https://www.cryptocompare.com/media/19710/frac.png')
    KTK = Coin(currency='KTK', full_name='KryptCoin', id='KTK', url='https://www.cryptocompare.com/media/19771/ktk.png')
    HZ = Coin(currency='HZ', full_name='Horizon', id='HZ', url='https://www.cryptocompare.com/media/20320/hz.png')
    FAIR = Coin(currency='FAIR', full_name='FairCoin', id='FAIR', url='https://www.cryptocompare.com/media/20287/fair.png')
    QORA = Coin(currency='QORA', full_name='QoraCoin', id='QORA', url='https://www.cryptocompare.com/media/19876/qora.png')
    NLG = Coin(currency='NLG', full_name='Gulden', id='NLG', url='https://www.cryptocompare.com/media/32655867/webpnet-resizeimage.png')
    RBY = Coin(currency='RBY', full_name='RubyCoin', id='RBY', url='https://www.cryptocompare.com/media/351279/rby.png')
    PTC = Coin(currency='PTC', full_name='PesetaCoin', id='PTC', url='https://www.cryptocompare.com/media/19868/ptc.png')
    KORE = Coin(currency='KORE', full_name='Kore', id='KORE', url='https://www.cryptocompare.com/media/14543972/kore.png')
    WBB = Coin(currency='WBB', full_name='Wild Beast Coin', id='WBB', url='https://www.cryptocompare.com/media/20477/wbb.png')
    SSD = Coin(currency='SSD', full_name='Sonic Screw Driver Coin', id='SSD', url='https://www.cryptocompare.com/media/20443/ssd.png')
    XTC = Coin(currency='XTC', full_name='TileCoin', id='XTC', url='https://www.cryptocompare.com/media/20167/xtc.png')
    NOTE = Coin(currency='NOTE', full_name='Dnotes', id='NOTE', url='https://www.cryptocompare.com/media/34478183/note.png')
    FLO = Coin(currency='FLO', full_name='Flo', id='FLO', url='https://www.cryptocompare.com/media/35309344/flo.png')
    MMXIV = Coin(currency='MMXIV', full_name='MaieutiCoin', id='MMXIV', url='https://www.cryptocompare.com/media/19798/mmxiv.png')
    STV = Coin(currency='STV', full_name='Sativa Coin', id='STV', url='https://www.cryptocompare.com/media/20444/stv.png')
    EBS = Coin(currency='EBS', full_name='EbolaShare', id='EBS', url='https://www.cryptocompare.com/media/20267/ebs.png')
    AM = Coin(currency='AM', full_name='AeroMe', id='AM', url='https://www.cryptocompare.com/media/20191/am.png')
    XMG = Coin(currency='XMG', full_name='Coin Magi', id='XMG', url='https://www.cryptocompare.com/media/20154/xmg.png')
    AMBER = Coin(currency='AMBER', full_name='AmberCoin', id='AMBER', url='https://www.cryptocompare.com/media/20187/amber.png')
    NKT = Coin(currency='NKT', full_name='NakomotoDark', id='NKT', url='https://www.cryptocompare.com/media/20371/nkt.png')
    J = Coin(currency='J', full_name='JoinCoin', id='J', url='https://www.cryptocompare.com/media/20350/j.png')
    GHC = Coin(currency='GHC', full_name='GhostCoin', id='GHC', url='https://www.cryptocompare.com/media/19721/ghc.png')
    ABY = Coin(currency='ABY', full_name='ArtByte', id='ABY', url='https://www.cryptocompare.com/media/1383379/aby.png')
    LDOGE = Coin(currency='LDOGE', full_name='LiteDoge', id='LDOGE', url='https://www.cryptocompare.com/media/20332/ldoge.png')
    MTR = Coin(currency='MTR', full_name='MasterTraderCoin', id='MTR', url='https://www.cryptocompare.com/media/19710/frac.png')
    TRI = Coin(currency='TRI', full_name='Triangles Coin', id='TRI', url='https://www.cryptocompare.com/media/350568/tri.png')
    SWARM = Coin(currency='SWARM', full_name='SwarmCoin', id='SWARM', url='https://www.cryptocompare.com/media/20445/swarm.png')
    BBR = Coin(currency='BBR', full_name='Boolberry', id='BBR', url='https://www.cryptocompare.com/media/19609/bbr.png')
    BTCRY = Coin(currency='BTCRY', full_name='BitCrystal', id='BTCRY', url='https://www.cryptocompare.com/media/20210/btcry.png')
    BCR = Coin(currency='BCR', full_name='BitCredit', id='BCR', url='https://www.cryptocompare.com/media/20198/bcr.png')
    XPB = Coin(currency='XPB', full_name='Pebble Coin', id='XPB', url='https://www.cryptocompare.com/media/20158/xpb.png')
    XDQ = Coin(currency='XDQ', full_name='Dirac Coin', id='XDQ', url='https://www.cryptocompare.com/media/19959/xdq.png')
    FLDC = Coin(currency='FLDC', full_name='Folding Coin', id='FLDC', url='https://www.cryptocompare.com/media/20284/fldc.png')
    SLR = Coin(currency='SLR', full_name='SolarCoin', id='SLR', url='https://www.cryptocompare.com/media/20699/slr.png')
    SMAC = Coin(currency='SMAC', full_name='Social Media Coin', id='SMAC', url='https://www.cryptocompare.com/media/20427/smac.png')
    TRK = Coin(currency='TRK', full_name='TruckCoin', id='TRK', url='https://www.cryptocompare.com/media/20460/trk.png')
    U = Coin(currency='U', full_name='Ucoin', id='U', url='https://www.cryptocompare.com/media/351629/u.jpg')
    UIS = Coin(currency='UIS', full_name='Unitus', id='UIS', url='https://www.cryptocompare.com/media/20455/uis.png')
    CYP = Coin(currency='CYP', full_name='CypherPunkCoin', id='CYP', url='https://www.cryptocompare.com/media/20248/cyp.png')
    UFO = Coin(currency='UFO', full_name='UFO Coin', id='UFO', url='https://www.cryptocompare.com/media/12318167/ufo1.png')
    ASN = Coin(currency='ASN', full_name='Ascension Coin', id='ASN', url='https://www.cryptocompare.com/media/20192/asn.png')
    OC = Coin(currency='OC', full_name='OrangeCoin', id='OC', url='https://www.cryptocompare.com/media/19843/oc.png')
    GSM = Coin(currency='GSM', full_name='GSM Coin', id='GSM', url='https://www.cryptocompare.com/media/20316/gsm.png')
    FSC = Coin(currency='FSC', full_name='FriendshipCoin', id='FSC', url='https://www.cryptocompare.com/media/30001859/fsc.jpg')
    NXTTY = Coin(currency='NXTTY', full_name='NXTTY', id='NXTTY', url='https://www.cryptocompare.com/media/20379/nxtty.png')
    QBK = Coin(currency='QBK', full_name='QuBuck Coin', id='QBK', url='https://www.cryptocompare.com/media/20400/qbk.png')
    BLC = Coin(currency='BLC', full_name='BlakeCoin', id='BLC', url='https://www.cryptocompare.com/media/35309218/blc.png')
    MARYJ = Coin(currency='MARYJ', full_name='MaryJane Coin', id='MARYJ', url='https://www.cryptocompare.com/media/20343/maryj.png')
    OMC = Coin(currency='OMC', full_name='OmniCron', id='OMC', url='https://www.cryptocompare.com/media/1381967/omc.png')
    GIG = Coin(currency='GIG', full_name='GigCoin', id='GIG', url='https://www.cryptocompare.com/media/20294/gig.png')
    CC = Coin(currency='CC', full_name='CyberCoin', id='CC', url='https://www.cryptocompare.com/media/20225/cc.png')
    BITS = Coin(currency='BITS', full_name='BitstarCoin', id='BITS', url='https://www.cryptocompare.com/media/19622/bits.png')
    LTBC = Coin(currency='LTBC', full_name='LTBCoin', id='LTBC', url='https://www.cryptocompare.com/media/20336/ltb.png')
    NEOS = Coin(currency='NEOS', full_name='NeosCoin', id='NEOS', url='https://www.cryptocompare.com/media/1382788/neos1.png')
    HYPER = Coin(currency='HYPER', full_name='HyperCoin', id='HYPER', url='https://www.cryptocompare.com/media/19744/hyper.png')
    VTR = Coin(currency='VTR', full_name='Vtorrent', id='VTR', url='https://www.cryptocompare.com/media/20471/vtr.png')
    METAL = Coin(currency='METAL', full_name='MetalCoin', id='METAL', url='https://www.cryptocompare.com/media/20359/metal.png')
    PINK = Coin(currency='PINK', full_name='PinkCoin', id='PINK', url='https://www.cryptocompare.com/media/350588/pinkcoin-logo.png')
    GRE = Coin(currency='GRE', full_name='GreenCoin', id='GRE', url='https://www.cryptocompare.com/media/1382396/grn.png')
    XG = Coin(currency='XG', full_name='XG Sports', id='XG', url='https://www.cryptocompare.com/media/20156/xg.png')
    CHILD = Coin(currency='CHILD', full_name='ChildCoin', id='CHILD', url='https://www.cryptocompare.com/media/20233/child.png')
    MINE = Coin(currency='MINE', full_name='Instamine Nuggets', id='MINE', url='https://www.cryptocompare.com/media/20356/mine.png')
    ROS = Coin(currency='ROS', full_name='ROS Coin', id='ROS', url='https://www.cryptocompare.comundefined')
    UNAT = Coin(currency='UNAT', full_name='Unattanium', id='UNAT', url='https://www.cryptocompare.com/media/20456/unat.png')
    SLM = Coin(currency='SLM', full_name='SlimCoin', id='SLM', url='https://www.cryptocompare.com/media/20426/slm.png')
    GAIA = Coin(currency='GAIA', full_name='GAIA Platform', id='GAIA', url='https://www.cryptocompare.com/media/20290/gaia.png')
    TRUST = Coin(currency='TRUST', full_name='TrustPlus', id='TRUST', url='https://www.cryptocompare.com/media/19935/trust.png')
    FCN = Coin(currency='FCN', full_name='FantomCoin ', id='FCN', url='https://www.cryptocompare.com/media/20282/fcn.png')
    XCN = Coin(currency='XCN', full_name='Cryptonite', id='XCN', url='https://www.cryptocompare.com/media/20483/xcn.png')
    CURE = Coin(currency='CURE', full_name='Curecoin', id='CURE', url='https://www.cryptocompare.com/media/1383812/cure.png')
    GMC = Coin(currency='GMC', full_name='Gridmaster', id='GMC', url='https://www.cryptocompare.com/media/20299/gmc.png')
    MMC = Coin(currency='MMC', full_name='MemoryCoin', id='MMC', url='https://www.cryptocompare.com/media/19795/mmc.png')
    XBC = Coin(currency='XBC', full_name='BitcoinPlus', id='XBC', url='https://www.cryptocompare.com/media/20488/xbc.png')
    CYC = Coin(currency='CYC', full_name='ConSpiracy Coin ', id='CYC', url='https://www.cryptocompare.com/media/19671/cyc.png')
    OCTO = Coin(currency='OCTO', full_name='OctoCoin', id='OCTO', url='https://www.cryptocompare.com/media/19983/888.png')
    MSC = Coin(currency='MSC', full_name='MasterCoin', id='MSC', url='https://www.cryptocompare.com/media/19814/mst.png')
    EGG = Coin(currency='EGG', full_name='EggCoin', id='EGG', url='https://www.cryptocompare.com/media/20269/egg.png')
    C2 = Coin(currency='C2', full_name='Coin.2', id='C2', url='https://www.cryptocompare.com/media/19640/c2.png')
    GSX = Coin(currency='GSX', full_name='GlowShares', id='GSX', url='https://www.cryptocompare.com/media/20314/gsxjpeg.png')
    CAM = Coin(currency='CAM', full_name='Camcoin', id='CAM', url='https://www.cryptocompare.com/media/20220/cam.png')
    RBR = Coin(currency='RBR', full_name='Ribbit Rewards', id='RBR', url='https://www.cryptocompare.com/media/20408/rbr.png')
    XQN = Coin(currency='XQN', full_name='Quotient', id='XQN', url='https://www.cryptocompare.com/media/12318067/xqn.png')
    ICASH = Coin(currency='ICASH', full_name='ICASH', id='ICASH', url='https://www.cryptocompare.com/media/20319/icash.png')
    NODE = Coin(currency='NODE', full_name='Node', id='NODE', url='https://www.cryptocompare.com/media/20373/node.png')
    SOON = Coin(currency='SOON', full_name='SoonCoin', id='SOON', url='https://www.cryptocompare.com/media/20436/soon.png')
    BTMI = Coin(currency='BTMI', full_name='BitMiles', id='BTMI', url='https://www.cryptocompare.com/media/20213/btmi.png')
    EVENT = Coin(currency='EVENT', full_name='Event Token', id='EVENT', url='https://www.cryptocompare.com/media/20277/event.png')
    VIOR = Coin(currency='VIOR', full_name='ViorCoin', id='VIOR', url='https://www.cryptocompare.com/media/20469/viorjpeg.png')
    XCO = Coin(currency='XCO', full_name='XCoin', id='XCO', url='https://www.cryptocompare.com/media/20486/xco.png')
    VMC = Coin(currency='VMC', full_name='VirtualMining Coin', id='VMC', url='https://www.cryptocompare.com/media/19943/vmc.png')
    MRS = Coin(currency='MRS', full_name='MarsCoin', id='MRS', url='https://www.cryptocompare.com/media/19808/mrs.png')
    VIRAL = Coin(currency='VIRAL', full_name='Viral Coin', id='VIRAL', url='https://www.cryptocompare.com/media/20472/viral.png')
    EQM = Coin(currency='EQM', full_name='Equilibrium Coin', id='EQM', url='https://www.cryptocompare.com/media/19808/mrs.png')
    ISL = Coin(currency='ISL', full_name='IslaCoin', id='ISL', url='https://www.cryptocompare.com/media/19808/mrs.png')
    QSLV = Coin(currency='QSLV', full_name='Quicksilver coin', id='QSLV', url='https://www.cryptocompare.com/media/20404/qslv.png')
    XWT = Coin(currency='XWT', full_name='World Trade Funds', id='XWT', url='https://www.cryptocompare.com/media/19808/mrs.png')
    XNA = Coin(currency='XNA', full_name='DeOxyRibose', id='XNA', url='https://www.cryptocompare.com/media/19808/mrs.png')
    RDN = Coin(currency='RDN', full_name='RadonPay', id='RDN', url='https://www.cryptocompare.com/media/19808/mrs.png')
    SKB = Coin(currency='SKB', full_name='SkullBuzz', id='SKB', url='https://www.cryptocompare.com/media/19808/mrs.png')
    BSTY = Coin(currency='BSTY', full_name='GlobalBoost', id='BSTY', url='https://www.cryptocompare.com/media/27010496/bsty.png')
    FCS = Coin(currency='FCS', full_name='CryptoFocus', id='FCS', url='https://www.cryptocompare.com/media/19808/mrs.png')
    GAM = Coin(currency='GAM', full_name='Gambit coin', id='GAM', url='https://www.cryptocompare.com/media/20293/gam.png')
    NXS = Coin(currency='NXS', full_name='Nexus', id='NXS', url='https://www.cryptocompare.com/media/1382387/nexus.jpg')
    CESC = Coin(currency='CESC', full_name='Crypto Escudo', id='CESC', url='https://www.cryptocompare.com/media/350786/cesc.png')
    TWLV = Coin(currency='TWLV', full_name='Twelve Coin', id='TWLV', url='https://www.cryptocompare.com/media/20472/viral.png')
    EAGS = Coin(currency='EAGS', full_name='EagsCoin', id='EAGS', url='https://www.cryptocompare.com/media/19808/mrs.png')
    MWC = Coin(currency='MWC', full_name='MultiWallet Coin', id='MWC', url='https://www.cryptocompare.com/media/19808/mrs.png')
    ADC = Coin(currency='ADC', full_name='AudioCoin', id='ADC', url='https://www.cryptocompare.com/media/350880/adc.png')
    MARS = Coin(currency='MARS', full_name='MarsCoin ', id='MARS', url='https://www.cryptocompare.com/media/19808/mrs.png')
    XMS = Coin(currency='XMS', full_name='Megastake', id='XMS', url='https://www.cryptocompare.com/media/19808/mrs.png')
    SPHR = Coin(currency='SPHR', full_name='Sphere Coin', id='SPHR', url='https://www.cryptocompare.com/media/19808/mrs.png')
    SIGU = Coin(currency='SIGU', full_name='Singular', id='SIGU', url='https://www.cryptocompare.com/media/19808/mrs.png')
    DCC = Coin(currency='DCC', full_name='DarkCrave', id='DCC', url='https://www.cryptocompare.com/media/19808/mrs.png')
    M1 = Coin(currency='M1', full_name='SupplyShock', id='M1', url='https://www.cryptocompare.com/media/19808/mrs.png')
    DB = Coin(currency='DB', full_name='DarkBit', id='DB', url='https://www.cryptocompare.com/media/19808/mrs.png')
    CTO = Coin(currency='CTO', full_name='Crypto', id='CTO', url='https://www.cryptocompare.com/media/19808/mrs.png')
    EDGE = Coin(currency='EDGE', full_name='EdgeCoin', id='EDGE', url='https://www.cryptocompare.com/media/20556/edge.png')
    FUTC = Coin(currency='FUTC', full_name='FutCoin', id='FUTC', url='https://www.cryptocompare.com/media/20558/futc.png')
    GLOBE = Coin(currency='GLOBE', full_name='Global', id='GLOBE', url='https://www.cryptocompare.com/media/20564/globe.png')
    TAM = Coin(currency='TAM', full_name='TamaGucci', id='TAM', url='https://www.cryptocompare.com/media/20565/tam.png')
    MRP = Coin(currency='MRP', full_name='MorpheusCoin', id='MRP', url='https://www.cryptocompare.com/media/20357/mrp.png')
    CREVA = Coin(currency='CREVA', full_name='Creva Coin', id='CREVA', url='https://www.cryptocompare.com/media/20571/creva.png')
    XFC = Coin(currency='XFC', full_name='Forever Coin', id='XFC', url='https://www.cryptocompare.com/media/20574/xfc.png')
    NANAS = Coin(currency='NANAS', full_name='BananaBits', id='NANAS', url='https://www.cryptocompare.com/media/20575/nanas.png')
    LOG = Coin(currency='LOG', full_name='Wood Coin', id='LOG', url='https://www.cryptocompare.com/media/20335/log.png')
    XCE = Coin(currency='XCE', full_name='Cerium', id='XCE', url='https://www.cryptocompare.com/media/20573/xce.png')
    ACP = Coin(currency='ACP', full_name='Anarchists Prime', id='ACP', url='https://www.cryptocompare.com/media/351019/acp.png')
    DRZ = Coin(currency='DRZ', full_name='Droidz', id='DRZ', url='https://www.cryptocompare.com/media/20605/drz.png')
    BSC = Coin(currency='BSC', full_name='BowsCoin', id='BSC', url='https://www.cryptocompare.com/media/20601/bsc.png')
    DRKT = Coin(currency='DRKT', full_name='DarkTron', id='DRKT', url='https://www.cryptocompare.com/media/20604/drkt.png')
    CIRC = Coin(currency='CIRC', full_name='CryptoCircuits', id='CIRC', url='https://www.cryptocompare.com/media/20603/circ.png')
    NKA = Coin(currency='NKA', full_name='IncaKoin', id='NKA', url='https://www.cryptocompare.com/media/20367/nka.png')
    VERSA = Coin(currency='VERSA', full_name='Versa Token', id='VERSA', url='https://www.cryptocompare.com/media/20629/versa.png')
    EPY = Coin(currency='EPY', full_name='Empyrean', id='EPY', url='https://www.cryptocompare.com/media/20628/epy.png')
    SQL = Coin(currency='SQL', full_name='Squall Coin', id='SQL', url='https://www.cryptocompare.com/media/20441/sql.png')
    PIGGY = Coin(currency='PIGGY', full_name='Piggy Coin', id='PIGGY', url='https://www.cryptocompare.com/media/19854/piggy.png')
    CHA = Coin(currency='CHA', full_name='Charity Coin', id='CHA', url='https://www.cryptocompare.com/media/19986/a3c.png')
    MIL = Coin(currency='MIL', full_name='Milllionaire Coin', id='MIL', url='https://www.cryptocompare.com/media/20354/mil.png')
    CRW = Coin(currency='CRW', full_name='Crown Coin', id='CRW', url='https://www.cryptocompare.com/media/1383378/crw1.png')
    GEN = Coin(currency='GEN', full_name='Genstake', id='GEN', url='https://www.cryptocompare.com/media/20640/gen.png')
    XPH = Coin(currency='XPH', full_name='PharmaCoin', id='XPH', url='https://www.cryptocompare.com/media/20641/xph.png')
    GRM = Coin(currency='GRM', full_name='GridMaster', id='GRM', url='https://www.cryptocompare.com/media/20642/grm.png')
    QTZ = Coin(currency='QTZ', full_name='Quartz', id='QTZ', url='https://www.cryptocompare.com/media/20643/qtz.png')
    ARB = Coin(currency='ARB', full_name='Arbit Coin', id='ARB', url='https://www.cryptocompare.com/media/20645/arb.png')
    LTS = Coin(currency='LTS', full_name='Litestar Coin', id='LTS', url='https://www.cryptocompare.com/media/20644/lts.png')
    SPC = Coin(currency='SPC', full_name='SpinCoin', id='SPC', url='https://www.cryptocompare.com/media/20655/spc.png')
    GP = Coin(currency='GP', full_name='GoldPieces', id='GP', url='https://www.cryptocompare.com/media/20656/gp.png')
    BITZ = Coin(currency='BITZ', full_name='Bitz Coin', id='BITZ', url='https://www.cryptocompare.com/media/20654/bitz.png')
    DUB = Coin(currency='DUB', full_name='DubCoin', id='DUB', url='https://www.cryptocompare.com/media/19986/a3c.png')
    GRAV = Coin(currency='GRAV', full_name='Graviton', id='GRAV', url='https://www.cryptocompare.com/media/20659/grav.png')
    MNV = Coin(currency='MNV', full_name='MonetaVerde', id='MNV', url='https://www.cryptocompare.com/media/20346/mcn.png')
    QCN = Coin(currency='QCN', full_name='Quazar Coin', id='QCN', url='https://www.cryptocompare.com/media/19877/qcn.png')
    HEDGE = Coin(currency='HEDGE', full_name='Hedgecoin', id='HEDGE', url='https://www.cryptocompare.com/media/20663/hedg.png')
    SONG = Coin(currency='SONG', full_name='Song Coin', id='SONG', url='https://www.cryptocompare.com/media/20432/song.png')
    XSEED = Coin(currency='XSEED', full_name='BitSeeds', id='XSEED', url='https://www.cryptocompare.com/media/20163/xseed.png')
    CRE = Coin(currency='CRE', full_name='Credits', id='CRE', url='https://www.cryptocompare.com/media/20683/cre.png')
    AXIOM = Coin(currency='AXIOM', full_name='Axiom Coin', id='AXIOM', url='https://www.cryptocompare.com/media/20686/axiom.png')
    SMLY = Coin(currency='SMLY', full_name='SmileyCoin', id='SMLY', url='https://www.cryptocompare.com/media/20429/smly.png')
    RBT = Coin(currency='RBT', full_name='Rimbit', id='RBT', url='https://www.cryptocompare.com/media/20407/rbt.png')
    CHIP = Coin(currency='CHIP', full_name='Chip', id='CHIP', url='https://www.cryptocompare.com/media/20685/chip.png')
    SPEC = Coin(currency='SPEC', full_name='SpecCoin', id='SPEC', url='https://www.cryptocompare.com/media/20689/spec.png')
    UNC = Coin(currency='UNC', full_name='UnCoin', id='UNC', url='https://www.cryptocompare.com/media/20693/unc.png')
    SPRTS = Coin(currency='SPRTS', full_name='Sprouts', id='SPRTS', url='https://www.cryptocompare.com/media/20692/sprts.png')
    ZNY = Coin(currency='ZNY', full_name='BitZeny', id='ZNY', url='https://www.cryptocompare.com/media/20691/zny.png')
    BTQ = Coin(currency='BTQ', full_name='BitQuark', id='BTQ', url='https://www.cryptocompare.com/media/19638/btq.png')
    PKB = Coin(currency='PKB', full_name='ParkByte', id='PKB', url='https://www.cryptocompare.com/media/20694/pkb.png')
    SNRG = Coin(currency='SNRG', full_name='Synergy', id='SNRG', url='https://www.cryptocompare.com/media/20700/snrg.png')
    GHOUL = Coin(currency='GHOUL', full_name='Ghoul Coin', id='GHOUL', url='https://www.cryptocompare.com/media/20701/ghoul.png')
    HNC = Coin(currency='HNC', full_name='Hellenic Coin', id='HNC', url='https://www.cryptocompare.com/media/20702/hnc.png')
    DIGS = Coin(currency='DIGS', full_name='Diggits', id='DIGS', url='https://www.cryptocompare.com/media/20706/digs.png')
    EXP = Coin(currency='EXP', full_name='Expanse', id='EXP', url='https://www.cryptocompare.com/media/20707/exp.png')
    GCR = Coin(currency='GCR', full_name='Global Currency Reserve', id='GCR', url='https://www.cryptocompare.com/media/20708/gcr.png')
    MAPC = Coin(currency='MAPC', full_name='MapCoin', id='MAPC', url='https://www.cryptocompare.com/media/20710/mapc.png')
    MI = Coin(currency='MI', full_name='XiaoMiCoin', id='MI', url='https://www.cryptocompare.com/media/20711/mi.png')
    CON = Coin(currency='CON', full_name='Paycon', id='CON', url='https://www.cryptocompare.com/media/20717/con_.png')
    TX = Coin(currency='TX', full_name='Transfer', id='TX', url='https://www.cryptocompare.com/media/35309732/tx.png')
    GRS = Coin(currency='GRS', full_name='Groestlcoin ', id='GRS', url='https://www.cryptocompare.com/media/20780736/grs.png')
    SC = Coin(currency='SC', full_name='Siacoin', id='SC', url='https://www.cryptocompare.com/media/20726/siacon-logo.png')
    CLV = Coin(currency='CLV', full_name='CleverCoin', id='CLV', url='https://www.cryptocompare.com/media/20727/clv.png')
    LYB = Coin(currency='LYB', full_name='LyraBar', id='LYB', url='https://www.cryptocompare.com/media/20339/lyb.png')
    BST = Coin(currency='BST', full_name='BitStone', id='BST', url='https://www.cryptocompare.com/media/350558/bst.png')
    PXI = Coin(currency='PXI', full_name='Prime-X1', id='PXI', url='https://www.cryptocompare.com/media/350559/pxi.png')
    CPC = Coin(currency='CPC', full_name='CapriCoin', id='CPC', url='https://www.cryptocompare.com/media/350560/cpc.png')
    AMS = Coin(currency='AMS', full_name='Amsterdam Coin', id='AMS', url='https://www.cryptocompare.com/media/350562/ams.png')
    OBITS = Coin(currency='OBITS', full_name='Obits Coin', id='OBITS', url='https://www.cryptocompare.com/media/350565/obits.png')
    CLUB = Coin(currency='CLUB', full_name=' ClubCoin', id='CLUB', url='https://www.cryptocompare.com/media/350609/club.png')
    RADS = Coin(currency='RADS', full_name='Radium', id='RADS', url='https://www.cryptocompare.com/media/350610/rads.png')
    EMC = Coin(currency='EMC', full_name='Emercoin', id='EMC', url='https://www.cryptocompare.com/media/350611/emc.png')
    EGC = Coin(currency='EGC', full_name='EverGreenCoin', id='EGC', url='https://www.cryptocompare.com/media/350614/egc.png')
    MND = Coin(currency='MND', full_name='MindCoin', id='MND', url='https://www.cryptocompare.com/media/350616/mnd.png')
    I0C = Coin(currency='I0C', full_name='I0coin', id='I0C', url='https://www.cryptocompare.com/media/350691/i0c.png')
    BTA = Coin(currency='BTA', full_name='Bata', id='BTA', url='https://www.cryptocompare.com/media/1383113/bta1.png')
    DCR = Coin(currency='DCR', full_name='Decred', id='DCR', url='https://www.cryptocompare.com/media/1382607/decred.png')
    NAS2 = Coin(currency='NAS2', full_name='Nas2Coin', id='NAS2', url='https://www.cryptocompare.com/media/350776/nas2.png')
    PAK = Coin(currency='PAK', full_name='Pakcoin', id='PAK', url='https://www.cryptocompare.com/media/350788/pak.png')
    CRB = Coin(currency='CRB', full_name='Creditbit ', id='CRB', url='https://www.cryptocompare.com/media/1382904/crbit1.png')
    DOGED = Coin(currency='DOGED', full_name='DogeCoinDark', id='DOGED', url='https://www.cryptocompare.com/media/20029/doged.png')
    REP = Coin(currency='REP', full_name='Augur', id='REP', url='https://www.cryptocompare.com/media/350815/augur-logo.png')
    OK = Coin(currency='OK', full_name='OKCash', id='OK', url='https://www.cryptocompare.com/media/350819/ok.png')
    RVR = Coin(currency='RVR', full_name='Revolution VR', id='RVR', url='https://www.cryptocompare.com/media/30002218/rvr.jpg')
    AMP = Coin(currency='AMP', full_name='Synereo', id='AMP', url='https://www.cryptocompare.com/media/350825/amp.png')
    HODL = Coin(currency='HODL', full_name='HOdlcoin', id='HODL', url='https://www.cryptocompare.com/media/350840/hodl.png')
    DGD = Coin(currency='DGD', full_name='Digix DAO', id='DGD', url='https://www.cryptocompare.com/media/350851/dgd.png')
    EDRC = Coin(currency='EDRC', full_name='EDRCoin', id='EDRC', url='https://www.cryptocompare.com/media/350858/edrc.jpg')
    LSK = Coin(currency='LSK', full_name='Lisk', id='LSK', url='https://www.cryptocompare.com/media/27011060/lsk.png')
    WAVES = Coin(currency='WAVES', full_name='Waves', id='WAVES', url='https://www.cryptocompare.com/media/27010639/waves2.png')
    HTC = Coin(currency='HTC', full_name='Hitcoin', id='HTC', url='https://www.cryptocompare.com/media/350888/htc.png')
    GAME = Coin(currency='GAME', full_name='Gamecredits', id='GAME', url='https://www.cryptocompare.com/media/350887/game.png')
    DSH = Coin(currency='DSH', full_name='Dashcoin', id='DSH', url='https://www.cryptocompare.com/media/20026/dash.png')
    DBIC = Coin(currency='DBIC', full_name='DubaiCoin', id='DBIC', url='https://www.cryptocompare.com/media/350891/dbic.png')
    XHI = Coin(currency='XHI', full_name='HiCoin', id='XHI', url='https://www.cryptocompare.com/media/350892/xhi.png')
    SPOTS = Coin(currency='SPOTS', full_name='Spots', id='SPOTS', url='https://www.cryptocompare.com/media/350893/spots.png')
    BIOS = Coin(currency='BIOS', full_name='BiosCrypto', id='BIOS', url='https://www.cryptocompare.com/media/350894/bios.png')
    CAB = Coin(currency='CAB', full_name='CabbageUnit', id='CAB', url='https://www.cryptocompare.com/media/350896/cab.png')
    DIEM = Coin(currency='DIEM', full_name='CarpeDiemCoin', id='DIEM', url='https://www.cryptocompare.com/media/20260/diem_1.png')
    GBT = Coin(currency='GBT', full_name='GameBetCoin', id='GBT', url='https://www.cryptocompare.com/media/350897/gbt.png')
    RCX = Coin(currency='RCX', full_name='RedCrowCoin', id='RCX', url='https://www.cryptocompare.com/media/350902/rcx.png')
    PWR = Coin(currency='PWR', full_name='PWR Coin', id='PWR', url='https://www.cryptocompare.com/media/30002119/pwr.png')
    TRUMP = Coin(currency='TRUMP', full_name='TrumpCoin', id='TRUMP', url='https://www.cryptocompare.com/media/350905/trump.png')
    PRM = Coin(currency='PRM', full_name='PrismChain', id='PRM', url='https://www.cryptocompare.com/media/350906/prm.png')
    BCY = Coin(currency='BCY', full_name='BitCrystals', id='BCY', url='https://www.cryptocompare.com/media/350903/bcy.png')
    RBIES = Coin(currency='RBIES', full_name='Rubies', id='RBIES', url='https://www.cryptocompare.com/media/350904/rbies.png')
    STEEM = Coin(currency='STEEM', full_name='Steem', id='STEEM', url='https://www.cryptocompare.com/media/350907/steem.png')
    BLRY = Coin(currency='BLRY', full_name='BillaryCoin', id='BLRY', url='https://www.cryptocompare.com/media/350908/blry.png')
    XWC = Coin(currency='XWC', full_name='WhiteCoin', id='XWC', url='https://www.cryptocompare.com/media/33957374/xwc.png')
    DOT = Coin(currency='DOT', full_name='Dotcoin', id='DOT', url='https://www.cryptocompare.com/media/350909/dot.png')
    SCOT = Coin(currency='SCOT', full_name='Scotcoin', id='SCOT', url='https://www.cryptocompare.com/media/20416/scot_1.png')
    DNET = Coin(currency='DNET', full_name='Darknet', id='DNET', url='https://www.cryptocompare.com/media/350912/dnet.png')
    BAC = Coin(currency='BAC', full_name='BitalphaCoin', id='BAC', url='https://www.cryptocompare.com/media/350913/bac.png')
    TCR = Coin(currency='TCR', full_name='Thecreed', id='TCR', url='https://www.cryptocompare.com/media/350918/tcr.png')
    POST = Coin(currency='POST', full_name='PostCoin', id='POST', url='https://www.cryptocompare.com/media/350917/post.png')
    INFX = Coin(currency='INFX', full_name='Influxcoin', id='INFX', url='https://www.cryptocompare.com/media/350919/infx.png')
    ETHS = Coin(currency='ETHS', full_name='EthereumScrypt', id='ETHS', url='https://www.cryptocompare.com/media/350910/eths.png')
    PXL = Coin(currency='PXL', full_name='Phalanx', id='PXL', url='https://www.cryptocompare.com/media/350930/pxl.png')
    NUM = Coin(currency='NUM', full_name='NumbersCoin', id='NUM', url='https://www.cryptocompare.com/media/350932/num.png')
    SOUL = Coin(currency='SOUL', full_name='SoulCoin', id='SOUL', url='https://www.cryptocompare.com/media/350930/pxl.png')
    ION = Coin(currency='ION', full_name='Ionomy', id='ION', url='https://www.cryptocompare.com/media/350933/ion.jpg')
    GROW = Coin(currency='GROW', full_name='GrownCoin', id='GROW', url='https://www.cryptocompare.com/media/350934/grow.png')
    UNITY = Coin(currency='UNITY', full_name='SuperNET', id='UNITY', url='https://www.cryptocompare.com/media/350935/unity_1.png')
    OLDSF = Coin(currency='OLDSF', full_name='OldSafeCoin', id='OLDSF', url='https://www.cryptocompare.com/media/350936/oldsf.png')
    SSTC = Coin(currency='SSTC', full_name='SunShotCoin', id='SSTC', url='https://www.cryptocompare.com/media/350937/ssc.png')
    NETC = Coin(currency='NETC', full_name='NetworkCoin', id='NETC', url='https://www.cryptocompare.com/media/350938/netc.png')
    GPU = Coin(currency='GPU', full_name='GPU Coin', id='GPU', url='https://www.cryptocompare.com/media/350939/gpu.png')
    TAGR = Coin(currency='TAGR', full_name='Think And Get Rich Coin', id='TAGR', url='https://www.cryptocompare.com/media/350940/tagr.png')
    HMP = Coin(currency='HMP', full_name='HempCoin', id='HMP', url='https://www.cryptocompare.com/media/350941/hmp.png')
    ADZ = Coin(currency='ADZ', full_name='Adzcoin', id='ADZ', url='https://www.cryptocompare.com/media/351424/adz1.jpg')
    GAP = Coin(currency='GAP', full_name='Gapcoin', id='GAP', url='https://www.cryptocompare.com/media/350943/gap.png')
    MYC = Coin(currency='MYC', full_name='MayaCoin', id='MYC', url='https://www.cryptocompare.com/media/350947/myc.png')
    IVZ = Coin(currency='IVZ', full_name='InvisibleCoin', id='IVZ', url='https://www.cryptocompare.com/media/350944/ivz.png')
    VTA = Coin(currency='VTA', full_name='VirtaCoin', id='VTA', url='https://www.cryptocompare.com/media/350945/vta.png')
    SLS = Coin(currency='SLS', full_name='SaluS', id='SLS', url='https://www.cryptocompare.com/media/350946/sls.png')
    SOIL = Coin(currency='SOIL', full_name='SoilCoin', id='SOIL', url='https://www.cryptocompare.com/media/350949/soil.png')
    CUBE = Coin(currency='CUBE', full_name='DigiCube', id='CUBE', url='https://www.cryptocompare.com/media/350948/cube.png')
    YOC = Coin(currency='YOC', full_name='YoCoin', id='YOC', url='https://www.cryptocompare.com/media/350957/yoc.png')
    VPRC = Coin(currency='VPRC', full_name='VapersCoin', id='VPRC', url='https://www.cryptocompare.com/media/350951/vpc.png')
    APC = Coin(currency='APC', full_name='AlpaCoin', id='APC', url='https://www.cryptocompare.com/media/350956/apc.png')
    STEPS = Coin(currency='STEPS', full_name='Steps', id='STEPS', url='https://www.cryptocompare.com/media/350952/steps.png')
    DBTC = Coin(currency='DBTC', full_name='DebitCoin', id='DBTC', url='https://www.cryptocompare.com/media/350953/dbtc.png')
    UNIT = Coin(currency='UNIT', full_name='Universal Currency', id='UNIT', url='https://www.cryptocompare.com/media/35309731/unit.png')
    AEON = Coin(currency='AEON', full_name='AEON', id='AEON', url='https://www.cryptocompare.com/media/350955/aeon.png')
    MOIN = Coin(currency='MOIN', full_name='MoinCoin', id='MOIN', url='https://www.cryptocompare.com/media/350959/moin.png')
    SIB = Coin(currency='SIB', full_name='SibCoin', id='SIB', url='https://www.cryptocompare.com/media/350958/sib.png')
    ERC = Coin(currency='ERC', full_name='EuropeCoin', id='ERC', url='https://www.cryptocompare.com/media/350960/erc.png')
    AIB = Coin(currency='AIB', full_name='AdvancedInternetBlock', id='AIB', url='https://www.cryptocompare.com/media/350971/aib.png')
    PRIME = Coin(currency='PRIME', full_name='PrimeChain', id='PRIME', url='https://www.cryptocompare.com/media/350979/prime.png')
    BERN = Coin(currency='BERN', full_name='BERNcash', id='BERN', url='https://www.cryptocompare.com/media/350973/bern.png')
    BIGUP = Coin(currency='BIGUP', full_name='BigUp', id='BIGUP', url='https://www.cryptocompare.com/media/350980/bigup.png')
    KR = Coin(currency='KR', full_name='Krypton', id='KR', url='https://www.cryptocompare.com/media/350974/kr.png')
    XRE = Coin(currency='XRE', full_name='RevolverCoin', id='XRE', url='https://www.cryptocompare.com/media/33187859/xre.png')
    MEME = Coin(currency='MEME', full_name='Pepe', id='MEME', url='https://www.cryptocompare.com/media/35309722/meme.png')
    XDB = Coin(currency='XDB', full_name='DragonSphere', id='XDB', url='https://www.cryptocompare.com/media/350977/xdb.png')
    ANTI = Coin(currency='ANTI', full_name='Anti Bitcoin', id='ANTI', url='https://www.cryptocompare.com/media/350972/anti.png')
    BRK = Coin(currency='BRK', full_name='BreakoutCoin', id='BRK', url='https://www.cryptocompare.com/media/350981/brk.png')
    COLX = Coin(currency='COLX', full_name='ColossusCoinXT', id='COLX', url='https://www.cryptocompare.com/media/12318297/colx.png')
    MNM = Coin(currency='MNM', full_name='Mineum', id='MNM', url='https://www.cryptocompare.com/media/350982/mnm.png')
    ADCN = Coin(currency='ADCN', full_name='Asiadigicoin', id='ADCN', url='https://www.cryptocompare.com/media/350983/adcn.png')
    ZEIT = Coin(currency='ZEIT', full_name='ZeitCoin', id='ZEIT', url='https://www.cryptocompare.com/media/350984/zeit.png')
    CGA = Coin(currency='CGA', full_name='Cryptographic Anomaly', id='CGA', url='https://www.cryptocompare.com/media/350988/cga.png')
    SWING = Coin(currency='SWING', full_name='SwingCoin', id='SWING', url='https://www.cryptocompare.com/media/350987/swing.png')
    SAFEX = Coin(currency='SAFEX', full_name='SafeExchangeCoin', id='SAFEX', url='https://www.cryptocompare.com/media/1383986/safex.png')
    NEBU = Coin(currency='NEBU', full_name='Nebuchadnezzar', id='NEBU', url='https://www.cryptocompare.com/media/350990/nebu.png')
    AEC = Coin(currency='AEC', full_name='AcesCoin', id='AEC', url='https://www.cryptocompare.com/media/350991/aec.png')
    FRN = Coin(currency='FRN', full_name='Francs', id='FRN', url='https://www.cryptocompare.com/media/350992/frn.png')
    ADN = Coin(currency='ADN', full_name='Aiden', id='ADN', url='https://www.cryptocompare.com/media/350993/adn.png')
    PULSE = Coin(currency='PULSE', full_name='Pulse', id='PULSE', url='https://www.cryptocompare.com/media/350994/pulse.jpg')
    N7 = Coin(currency='N7', full_name='Number7', id='N7', url='https://www.cryptocompare.com/media/350995/n7.jpg')
    CYG = Coin(currency='CYG', full_name='Cygnus', id='CYG', url='https://www.cryptocompare.com/media/350997/cygnus.png')
    LGBTQ = Coin(currency='LGBTQ', full_name='LGBTQoin', id='LGBTQ', url='https://www.cryptocompare.com/media/350996/lgbtq.png')
    UTH = Coin(currency='UTH', full_name='Uther', id='UTH', url='https://www.cryptocompare.com/media/350998/uth.png')
    MPRO = Coin(currency='MPRO', full_name='MediumProject', id='MPRO', url='https://www.cryptocompare.com/media/350999/mpro.jpg')
    KAT = Coin(currency='KAT', full_name='KATZcoin', id='KAT', url='https://www.cryptocompare.com/media/351028/katz.png')
    SPM = Coin(currency='SPM', full_name='Supreme', id='SPM', url='https://www.cryptocompare.com/media/351002/sup.png')
    MOJO = Coin(currency='MOJO', full_name='Mojocoin', id='MOJO', url='https://www.cryptocompare.com/media/35309727/mojo.png')
    BELA = Coin(currency='BELA', full_name='Bela', id='BELA', url='https://www.cryptocompare.com/media/34478099/bela.png')
    FLX = Coin(currency='FLX', full_name='Flash', id='FLX', url='https://www.cryptocompare.com/media/351007/flx.png')
    BOLI = Coin(currency='BOLI', full_name='BolivarCoin', id='BOLI', url='https://www.cryptocompare.com/media/34478039/boli.png')
    CLUD = Coin(currency='CLUD', full_name='CludCoin', id='CLUD', url='https://www.cryptocompare.com/media/351027/clud.png')
    DIME = Coin(currency='DIME', full_name='DimeCoin', id='DIME', url='https://www.cryptocompare.com/media/25792612/dime.png')
    FLY = Coin(currency='FLY', full_name='FlyCoin', id='FLY', url='https://www.cryptocompare.com/media/351013/fly.png')
    HVCO = Coin(currency='HVCO', full_name='High Voltage Coin', id='HVCO', url='https://www.cryptocompare.com/media/351014/hvco.png')
    GIZ = Coin(currency='GIZ', full_name='GIZMOcoin', id='GIZ', url='https://www.cryptocompare.com/media/351015/giz.png')
    GREXIT = Coin(currency='GREXIT', full_name='GrexitCoin', id='GREXIT', url='https://www.cryptocompare.com/media/351016/grexit.png')
    CARBON = Coin(currency='CARBON', full_name='Carboncoin', id='CARBON', url='https://www.cryptocompare.com/media/351017/carbon.png')
    DEUR = Coin(currency='DEUR', full_name='DigiEuro', id='DEUR', url='https://www.cryptocompare.com/media/351018/deur.png')
    TUR = Coin(currency='TUR', full_name='Turron', id='TUR', url='https://www.cryptocompare.com/media/351020/tur.png')
    LEMON = Coin(currency='LEMON', full_name='LemonCoin', id='LEMON', url='https://www.cryptocompare.com/media/351021/lemon.png')
    STS = Coin(currency='STS', full_name='STRESScoin', id='STS', url='https://www.cryptocompare.com/media/351022/sts.png')
    DISK = Coin(currency='DISK', full_name='Dark Lisk', id='DISK', url='https://www.cryptocompare.com/media/351023/disk.png')
    NEVA = Coin(currency='NEVA', full_name='NevaCoin', id='NEVA', url='https://www.cryptocompare.com/media/351026/neva.png')
    CYT = Coin(currency='CYT', full_name='Cryptokenz', id='CYT', url='https://www.cryptocompare.com/media/351024/cyt.png')
    FUZZ = Coin(currency='FUZZ', full_name='Fuzzballs', id='FUZZ', url='https://www.cryptocompare.com/media/351025/fuzz.png')
    NKC = Coin(currency='NKC', full_name='Nukecoinz', id='NKC', url='https://www.cryptocompare.com/media/351041/nkc.png')
    SCRT = Coin(currency='SCRT', full_name='SecretCoin', id='SCRT', url='https://www.cryptocompare.com/media/351031/scrt.png')
    XRA = Coin(currency='XRA', full_name='Ratecoin', id='XRA', url='https://www.cryptocompare.com/media/351032/xra.png')
    XNX = Coin(currency='XNX', full_name='XanaxCoin', id='XNX', url='https://www.cryptocompare.com/media/351033/xnx.jpg')
    STHR = Coin(currency='STHR', full_name='Stakerush', id='STHR', url='https://www.cryptocompare.com/media/351042/sthr.png')
    DBG = Coin(currency='DBG', full_name='Digital Bullion Gold', id='DBG', url='https://www.cryptocompare.com/media/351047/dbg.png')
    BON = Coin(currency='BON', full_name='BonesCoin', id='BON', url='https://www.cryptocompare.com/media/351045/bon_1.png')
    WMC = Coin(currency='WMC', full_name='WMCoin', id='WMC', url='https://www.cryptocompare.com/media/351044/wmc.png')
    GOTX = Coin(currency='GOTX', full_name='GothicCoin', id='GOTX', url='https://www.cryptocompare.com/media/351071/gotx.png')
    FLVR = Coin(currency='FLVR', full_name='FlavorCoin', id='FLVR', url='https://www.cryptocompare.com/media/351046/2flav.png')
    SHREK = Coin(currency='SHREK', full_name='ShrekCoin', id='SHREK', url='https://www.cryptocompare.com/media/351048/shrek.png')
    RISE = Coin(currency='RISE', full_name='Rise', id='RISE', url='https://www.cryptocompare.com/media/351059/rise.png')
    REV = Coin(currency='REV', full_name='Revenu', id='REV', url='https://www.cryptocompare.com/media/351061/rev.png')
    PBC = Coin(currency='PBC', full_name='PabyosiCoin', id='PBC', url='https://www.cryptocompare.com/media/351062/pbc.png')
    OBS = Coin(currency='OBS', full_name='Obscurebay', id='OBS', url='https://www.cryptocompare.com/media/351064/obs.png')
    EXIT = Coin(currency='EXIT', full_name='ExitCoin', id='EXIT', url='https://www.cryptocompare.com/media/351065/exit.png')
    CLINT = Coin(currency='CLINT', full_name='Clinton', id='CLINT', url='https://www.cryptocompare.com/media/351067/clint.png')
    CKC = Coin(currency='CKC', full_name='Clockcoin', id='CKC', url='https://www.cryptocompare.com/media/351068/ckc.png')
    VIP = Coin(currency='VIP', full_name='VIP Tokens', id='VIP', url='https://www.cryptocompare.com/media/351069/vip.png')
    NXE = Coin(currency='NXE', full_name='NXEcoin', id='NXE', url='https://www.cryptocompare.com/media/351070/nxe.png')
    ZOOM = Coin(currency='ZOOM', full_name='ZoomCoin', id='ZOOM', url='https://www.cryptocompare.com/media/351081/zoom.png')
    DRACO = Coin(currency='DRACO', full_name='DT Token', id='DRACO', url='https://www.cryptocompare.com/media/351390/dt-token.png')
    YOVI = Coin(currency='YOVI', full_name='YobitVirtualCoin', id='YOVI', url='https://www.cryptocompare.com/media/351073/yovi.png')
    ORLY = Coin(currency='ORLY', full_name='OrlyCoin', id='ORLY', url='https://www.cryptocompare.com/media/351076/orly.png')
    KUBOS = Coin(currency='KUBOS', full_name='KubosCoin', id='KUBOS', url='https://www.cryptocompare.com/media/351077/kubo.png')
    INCP = Coin(currency='INCP', full_name='InceptionCoin', id='INCP', url='https://www.cryptocompare.com/media/351078/incp.png')
    SAK = Coin(currency='SAK', full_name='SharkCoin', id='SAK', url='https://www.cryptocompare.com/media/351079/sak.png')
    EVIL = Coin(currency='EVIL', full_name='EvilCoin', id='EVIL', url='https://www.cryptocompare.com/media/351080/evil.png')
    OMA = Coin(currency='OMA', full_name='OmegaCoin', id='OMA', url='https://www.cryptocompare.com/media/20386/oma.png')
    MUE = Coin(currency='MUE', full_name='MonetaryUnit', id='MUE', url='https://www.cryptocompare.com/media/351084/mue.png')
    COX = Coin(currency='COX', full_name='CobraCoin', id='COX', url='https://www.cryptocompare.com/media/351083/cox.png')
    BNT = Coin(currency='BNT', full_name='Bancor Network Token', id='BNT', url='https://www.cryptocompare.com/media/1383549/bnt.jpg')
    BSD = Coin(currency='BSD', full_name='BitSend', id='BSD', url='https://www.cryptocompare.com/media/351086/bsd.png')
    DES = Coin(currency='DES', full_name='Destiny', id='DES', url='https://www.cryptocompare.com/media/351087/des.png')
    BIT16 = Coin(currency='BIT16', full_name='16BitCoin', id='BIT16', url='https://www.cryptocompare.com/media/20181/16bit.png')
    PDC = Coin(currency='PDC', full_name='Project Decorum', id='PDC', url='https://www.cryptocompare.com/media/351088/pdc.png')
    CMTC = Coin(currency='CMTC', full_name='CometCoin', id='CMTC', url='https://www.cryptocompare.com/media/34835904/cmtc.png')
    CHESS = Coin(currency='CHESS', full_name='ChessCoin', id='CHESS', url='https://www.cryptocompare.com/media/351094/chess.jpg')
    SPACE = Coin(currency='SPACE', full_name='SpaceCoin', id='SPACE', url='https://www.cryptocompare.com/media/351095/space.png')
    REE = Coin(currency='REE', full_name='ReeCoin', id='REE', url='https://www.cryptocompare.com/media/351096/ree.png')
    LQD = Coin(currency='LQD', full_name='Liquid', id='LQD', url='https://www.cryptocompare.com/media/351097/lqd.png')
    MARV = Coin(currency='MARV', full_name='Marvelous', id='MARV', url='https://www.cryptocompare.com/media/351099/marv.png')
    XDE2 = Coin(currency='XDE2', full_name='XDE II', id='XDE2', url='https://www.cryptocompare.com/media/351100/xde2.png')
    VEC2 = Coin(currency='VEC2', full_name='VectorCoin 2.0 ', id='VEC2', url='https://www.cryptocompare.com/media/351101/vec2.png')
    OMNI = Coin(currency='OMNI', full_name='Omni', id='OMNI', url='https://www.cryptocompare.com/media/351102/omni.png')
    GSY = Coin(currency='GSY', full_name='GenesysCoin', id='GSY', url='https://www.cryptocompare.com/media/351103/gsy.png')
    LIR = Coin(currency='LIR', full_name='Let it Ride', id='LIR', url='https://www.cryptocompare.com/media/351208/lir.png')
    MMNXT = Coin(currency='MMNXT', full_name='MMNXT ', id='MMNXT', url='https://www.cryptocompare.com/media/351209/nxtasset.png')
    SCRPT = Coin(currency='SCRPT', full_name='ScryptCoin', id='SCRPT', url='https://www.cryptocompare.com/media/351210/scrpt.png')
    LBC = Coin(currency='LBC', full_name='LBRY Credits', id='LBC', url='https://www.cryptocompare.com/media/351211/lbc.png')
    SPX = Coin(currency='SPX', full_name='Specie', id='SPX', url='https://www.cryptocompare.com/media/351212/spx.png')
    CJ = Coin(currency='CJ', full_name='CryptoJacks', id='CJ', url='https://www.cryptocompare.com/media/351234/cj.png')
    PUT = Coin(currency='PUT', full_name='PutinCoin', id='PUT', url='https://www.cryptocompare.com/media/1383668/put1.png')
    KRAK = Coin(currency='KRAK', full_name='Kraken', id='KRAK', url='https://www.cryptocompare.com/media/351236/krak.png')
    DLISK = Coin(currency='DLISK', full_name='Dlisk', id='DLISK', url='https://www.cryptocompare.com/media/351237/dlisk.png')
    IBANK = Coin(currency='IBANK', full_name='iBankCoin', id='IBANK', url='https://www.cryptocompare.com/media/351238/ibank.png')
    STRAT = Coin(currency='STRAT', full_name='Stratis', id='STRAT', url='https://www.cryptocompare.com/media/351303/stratis-logo.png')
    VOYA = Coin(currency='VOYA', full_name='Voyacoin', id='VOYA', url='https://www.cryptocompare.com/media/351304/voya.png')
    ENTER = Coin(currency='ENTER', full_name='EnterCoin (ENTER)', id='ENTER', url='https://www.cryptocompare.com/media/351305/enter.png')
    WGC = Coin(currency='WGC', full_name='World Gold Coin', id='WGC', url='https://www.cryptocompare.com/media/351310/wgc.png')
    BM = Coin(currency='BM', full_name='BitMoon', id='BM', url='https://www.cryptocompare.com/media/351311/bm.png')
    FRWC = Coin(currency='FRWC', full_name='Frankywillcoin', id='FRWC', url='https://www.cryptocompare.com/media/351361/frwc.png')
    PSY = Coin(currency='PSY', full_name='Psilocybin', id='PSY', url='https://www.cryptocompare.com/media/351362/psy.png')
    XT = Coin(currency='XT', full_name='ExtremeCoin', id='XT', url='https://www.cryptocompare.com/media/351364/xt.png')
    RUST = Coin(currency='RUST', full_name='RustCoin', id='RUST', url='https://www.cryptocompare.com/media/351365/rust.png')
    NZC = Coin(currency='NZC', full_name='NewZealandCoin', id='NZC', url='https://www.cryptocompare.com/media/351366/nzc.png')
    SNGLS = Coin(currency='SNGLS', full_name='SingularDTV', id='SNGLS', url='https://www.cryptocompare.com/media/351368/sngls.png')
    XAUR = Coin(currency='XAUR', full_name='Xaurum', id='XAUR', url='https://www.cryptocompare.com/media/351382/xaur.png')
    BFX = Coin(currency='BFX', full_name='BitFinex Tokens', id='BFX', url='https://www.cryptocompare.com/media/19554/bitfinex.png')
    UNIQ = Coin(currency='UNIQ', full_name='Uniqredit', id='UNIQ', url='https://www.cryptocompare.com/media/351387/uniq.png')
    CRX = Coin(currency='CRX', full_name='ChronosCoin', id='CRX', url='https://www.cryptocompare.com/media/351388/crx.png')
    DCT = Coin(currency='DCT', full_name='Decent', id='DCT', url='https://www.cryptocompare.com/media/351389/dct.png')
    XPOKE = Coin(currency='XPOKE', full_name='PokeChain', id='XPOKE', url='https://www.cryptocompare.com/media/351393/xpoke.png')
    MUDRA = Coin(currency='MUDRA', full_name='MudraCoin', id='MUDRA', url='https://www.cryptocompare.com/media/351394/mudra.png')
    WARP = Coin(currency='WARP', full_name='WarpCoin', id='WARP', url='https://www.cryptocompare.com/media/351395/warp.png')
    CNMT = Coin(currency='CNMT', full_name='Coinomat', id='CNMT', url='https://www.cryptocompare.com/media/351396/cnmt.png')
    PIZZA = Coin(currency='PIZZA', full_name='PizzaCoin', id='PIZZA', url='https://www.cryptocompare.com/media/351397/pizza.png')
    LC = Coin(currency='LC', full_name='Lutetium Coin', id='LC', url='https://www.cryptocompare.com/media/351398/lc.png')
    HEAT = Coin(currency='HEAT', full_name='Heat Ledger', id='HEAT', url='https://www.cryptocompare.com/media/351399/heat.png')
    ICN = Coin(currency='ICN', full_name='Iconomi', id='ICN', url='https://www.cryptocompare.com/media/351400/icn.png')
    EXB = Coin(currency='EXB', full_name='ExaByte (EXB)', id='EXB', url='https://www.cryptocompare.com/media/351401/exb.png')
    WINGS = Coin(currency='WINGS', full_name='Wings DAO', id='WINGS', url='https://www.cryptocompare.com/media/1382758/1wings.png')
    RBIT = Coin(currency='RBIT', full_name='ReturnBit', id='RBIT', url='https://www.cryptocompare.com/media/351405/rbit.png')
    KMD = Coin(currency='KMD', full_name='Komodo', id='KMD', url='https://www.cryptocompare.com/media/351408/kmd.png')
    GB = Coin(currency='GB', full_name='GoldBlocks', id='GB', url='https://www.cryptocompare.com/media/351411/db.png')
    NEO = Coin(currency='NEO', full_name='NEO', id='NEO', url='https://www.cryptocompare.com/media/1383858/neo.jpg')
    ANC = Coin(currency='ANC', full_name='Anoncoin', id='ANC', url='https://www.cryptocompare.com/media/19598/anc.png')
    SYNX = Coin(currency='SYNX', full_name='Syndicate', id='SYNX', url='https://www.cryptocompare.com/media/15887426/synx.png')
    MC = Coin(currency='MC', full_name='Mass Coin', id='MC', url='https://www.cryptocompare.com/media/351428/mc.png')
    JWL = Coin(currency='JWL', full_name='Jewels', id='JWL', url='https://www.cryptocompare.com/media/351432/jwl.png')
    WAY = Coin(currency='WAY', full_name='WayCoin', id='WAY', url='https://www.cryptocompare.com/media/351433/way.png')
    TAB = Coin(currency='TAB', full_name='MollyCoin', id='TAB', url='https://www.cryptocompare.com/media/351488/tab.png')
    TRIG = Coin(currency='TRIG', full_name='Trigger', id='TRIG', url='https://www.cryptocompare.com/media/351489/trg.png')
    BITCNY = Coin(currency='BITCNY', full_name='bitCNY', id='BITCNY', url='https://www.cryptocompare.com/media/351490/bitcny.png')
    BITUSD = Coin(currency='BITUSD', full_name='bitUSD', id='BITUSD', url='https://www.cryptocompare.com/media/351491/bitusd.png')
    STO = Coin(currency='STO', full_name='Save The Ocean', id='STO', url='https://www.cryptocompare.com/media/351493/sto.png')
    SNS = Coin(currency='SNS', full_name='Sense', id='SNS', url='https://www.cryptocompare.com/media/351494/sns.png')
    CTC = Coin(currency='CTC', full_name='CarterCoin', id='CTC', url='https://www.cryptocompare.com/media/351496/ctc.png')
    TOT = Coin(currency='TOT', full_name='TotCoin', id='TOT', url='https://www.cryptocompare.com/media/351497/tot.png')
    BTD = Coin(currency='BTD', full_name='Bitcloud', id='BTD', url='https://www.cryptocompare.com/media/351498/btd.png')
    BOTS = Coin(currency='BOTS', full_name='ArkDAO', id='BOTS', url='https://www.cryptocompare.com/media/351499/bot.png')
    MDC = Coin(currency='MDC', full_name='MedicCoin', id='MDC', url='https://www.cryptocompare.com/media/351500/mdc.png')
    FTP = Coin(currency='FTP', full_name='FuturePoints', id='FTP', url='https://www.cryptocompare.com/media/351501/ftp.png')
    ZET2 = Coin(currency='ZET2', full_name='Zeta2Coin', id='ZET2', url='https://www.cryptocompare.com/media/351502/zet2.png')
    KRB = Coin(currency='KRB', full_name='Karbo', id='KRB', url='https://www.cryptocompare.com/media/25792684/krb.png')
    TELL = Coin(currency='TELL', full_name='Tellurion', id='TELL', url='https://www.cryptocompare.com/media/351505/tell.png')
    ENE = Coin(currency='ENE', full_name='EneCoin', id='ENE', url='https://www.cryptocompare.com/media/351506/ene.png')
    TDFB = Coin(currency='TDFB', full_name='TDFB', id='TDFB', url='https://www.cryptocompare.com/media/351507/tdfb.png')
    BLOCKPAY = Coin(currency='BLOCKPAY', full_name='BlockPay', id='BLOCKPAY', url='https://www.cryptocompare.com/media/351508/blockpay.png')
    BXT = Coin(currency='BXT', full_name='BitTokens', id='BXT', url='https://www.cryptocompare.com/media/351509/bxt.png')
    ZYD = Coin(currency='ZYD', full_name='ZayedCoin', id='ZYD', url='https://www.cryptocompare.com/media/351510/zyd.png')
    MST = Coin(currency='MST', full_name='MustangCoin', id='MST', url='https://www.cryptocompare.com/media/351529/mst1.png')
    GOON = Coin(currency='GOON', full_name='Goonies', id='GOON', url='https://www.cryptocompare.com/media/351512/goon.png')
    VLT = Coin(currency='VLT', full_name='Veltor', id='VLT', url='https://www.cryptocompare.com/media/351514/vlt.png')
    ZNE = Coin(currency='ZNE', full_name='ZoneCoin', id='ZNE', url='https://www.cryptocompare.com/media/351515/zne.jpg')
    DCK = Coin(currency='DCK', full_name='DickCoin', id='DCK', url='https://www.cryptocompare.com/media/351516/dck.png')
    COVAL = Coin(currency='COVAL', full_name='Circuits of Value', id='COVAL', url='https://www.cryptocompare.com/media/351519/coval.png')
    DGDC = Coin(currency='DGDC', full_name='DarkGold', id='DGDC', url='https://www.cryptocompare.com/media/351520/dgd.png')
    TODAY = Coin(currency='TODAY', full_name='TodayCoin', id='TODAY', url='https://www.cryptocompare.com/media/351521/today.png')
    VRM = Coin(currency='VRM', full_name='Verium', id='VRM', url='https://www.cryptocompare.com/media/351522/vrm.png')
    ROOT = Coin(currency='ROOT', full_name='RootCoin', id='ROOT', url='https://www.cryptocompare.com/media/351523/root.png')
    GPL = Coin(currency='GPL', full_name='Gold Pressed Latinum', id='GPL', url='https://www.cryptocompare.com/media/351525/gpl.png')
    DOPE = Coin(currency='DOPE', full_name='DopeCoin', id='DOPE', url='https://www.cryptocompare.com/media/351526/dope.png')
    FX = Coin(currency='FX', full_name='FCoin', id='FX', url='https://www.cryptocompare.com/media/351527/fx.png')
    PIO = Coin(currency='PIO', full_name='Pioneershares', id='PIO', url='https://www.cryptocompare.com/media/351528/pio.png')
    PROUD = Coin(currency='PROUD', full_name='PROUD Money', id='PROUD', url='https://www.cryptocompare.com/media/32655932/proud.png')
    SMSR = Coin(currency='SMSR', full_name='Samsara Coin', id='SMSR', url='https://www.cryptocompare.com/media/351543/smsr.png')
    UBIQ = Coin(currency='UBIQ', full_name='Ubiqoin', id='UBIQ', url='https://www.cryptocompare.com/media/351544/ubiq.png')
    ARM = Coin(currency='ARM', full_name='Armory Coin', id='ARM', url='https://www.cryptocompare.com/media/351545/arm.png')
    RING = Coin(currency='RING', full_name='RingCoin', id='RING', url='https://www.cryptocompare.com/media/351546/ring.png')
    ERB = Coin(currency='ERB', full_name='ERBCoin', id='ERB', url='https://www.cryptocompare.com/media/351550/erb.png')
    LAZ = Coin(currency='LAZ', full_name='Lazarus', id='LAZ', url='https://www.cryptocompare.com/media/351552/laz.png')
    FONZ = Coin(currency='FONZ', full_name='FonzieCoin', id='FONZ', url='https://www.cryptocompare.com/media/351553/fonz.png')
    BTCR = Coin(currency='BTCR', full_name='BitCurrency', id='BTCR', url='https://www.cryptocompare.com/media/351554/btr.png')
    SANDG = Coin(currency='SANDG', full_name='Save and Gain', id='SANDG', url='https://www.cryptocompare.com/media/351556/sandt.png')
    PNK = Coin(currency='PNK', full_name='SteamPunk', id='PNK', url='https://www.cryptocompare.com/media/351557/pnk.png')
    MOOND = Coin(currency='MOOND', full_name='Dark Moon', id='MOOND', url='https://www.cryptocompare.com/media/351558/moond.png')
    DLC = Coin(currency='DLC', full_name='DollarCoin', id='DLC', url='https://www.cryptocompare.com/media/351559/dlc.png')
    SEN = Coin(currency='SEN', full_name='Sentaro', id='SEN', url='https://www.cryptocompare.com/media/351560/sen.png')
    SCN = Coin(currency='SCN', full_name='Swiscoin', id='SCN', url='https://www.cryptocompare.com/media/351563/scn.png')
    WEX = Coin(currency='WEX', full_name='Wexcoin', id='WEX', url='https://www.cryptocompare.com/media/351564/wex.jpg')
    LTH = Coin(currency='LTH', full_name='Lathaan', id='LTH', url='https://www.cryptocompare.com/media/351565/lth.png')
    BRONZ = Coin(currency='BRONZ', full_name='BitBronze', id='BRONZ', url='https://www.cryptocompare.com/media/33957382/bronz.png')
    SH = Coin(currency='SH', full_name='Shilling', id='SH', url='https://www.cryptocompare.com/media/351567/sh.png')
    BUZZ = Coin(currency='BUZZ', full_name='BuzzCoin', id='BUZZ', url='https://www.cryptocompare.com/media/15887419/buzz.png')
    MG = Coin(currency='MG', full_name='Mind Gene', id='MG', url='https://www.cryptocompare.com/media/351588/mg.png')
    PSI = Coin(currency='PSI', full_name='PSIcoin', id='PSI', url='https://www.cryptocompare.com/media/351589/psi.png')
    XPO = Coin(currency='XPO', full_name='Opair', id='XPO', url='https://www.cryptocompare.com/media/351590/xpo.png')
    NLC = Coin(currency='NLC', full_name='NoLimitCoin', id='NLC', url='https://www.cryptocompare.com/media/351591/nlc.png')
    PSB = Coin(currency='PSB', full_name='PesoBit', id='PSB', url='https://www.cryptocompare.com/media/351594/psb.jpg')
    XBTS = Coin(currency='XBTS', full_name='Beats', id='XBTS', url='https://www.cryptocompare.com/media/351617/beats.png')
    FIT = Coin(currency='FIT', full_name='Fitcoin', id='FIT', url='https://www.cryptocompare.com/media/351618/fit.png')
    PINKX = Coin(currency='PINKX', full_name='PantherCoin', id='PINKX', url='https://www.cryptocompare.com/media/351624/pinkx.png')
    FIRE = Coin(currency='FIRE', full_name='FireCoin', id='FIRE', url='https://www.cryptocompare.com/media/351625/fire.png')
    UNF = Coin(currency='UNF', full_name='Unfed Coin', id='UNF', url='https://www.cryptocompare.com/media/351626/unf.png')
    SPORT = Coin(currency='SPORT', full_name='SportsCoin', id='SPORT', url='https://www.cryptocompare.com/media/351627/sports.png')
    PPY = Coin(currency='PPY', full_name='Peerplays', id='PPY', url='https://www.cryptocompare.com/media/351630/peerplays.png')
    NTC = Coin(currency='NTC', full_name='NineElevenTruthCoin', id='NTC', url='https://www.cryptocompare.com/media/351631/ntc.png')
    EGO = Coin(currency='EGO', full_name='EGOcoin', id='EGO', url='https://www.cryptocompare.com/media/351632/ego.png')
    X2 = Coin(currency='X2', full_name='X2Coin', id='X2', url='https://www.cryptocompare.com/media/351635/x2.png')
    MT = Coin(currency='MT', full_name='Mycelium Token', id='MT', url='https://www.cryptocompare.com/media/19453/mycelium.png')
    TIA = Coin(currency='TIA', full_name='Tianhe', id='TIA', url='https://www.cryptocompare.com/media/351636/tia.png')
    GBRC = Coin(currency='GBRC', full_name='GBR Coin', id='GBRC', url='https://www.cryptocompare.com/media/351637/gbrc.png')
    XUP = Coin(currency='XUP', full_name='UPcoin', id='XUP', url='https://www.cryptocompare.com/media/351638/xup.png')
    HALLO = Coin(currency='HALLO', full_name='Halloween Coin', id='HALLO', url='https://www.cryptocompare.com/media/351657/hallo.png')
    BBCC = Coin(currency='BBCC', full_name='BaseballCardCoin', id='BBCC', url='https://www.cryptocompare.com/media/351658/bbcc.png')
    EMIGR = Coin(currency='EMIGR', full_name='EmiratesGoldCoin', id='EMIGR', url='https://www.cryptocompare.com/media/351659/emirg.png')
    BHC = Coin(currency='BHC', full_name='BighanCoin', id='BHC', url='https://www.cryptocompare.com/media/351660/bhc.png')
    CRAFT = Coin(currency='CRAFT', full_name='Craftcoin', id='CRAFT', url='https://www.cryptocompare.com/media/351681/craft.png')
    INV = Coin(currency='INV', full_name='Invictus', id='INV', url='https://www.cryptocompare.com/media/351682/inv.png')
    OLYMP = Coin(currency='OLYMP', full_name='OlympCoin', id='OLYMP', url='https://www.cryptocompare.com/media/351683/olymp.png')
    DPAY = Coin(currency='DPAY', full_name='DelightPay', id='DPAY', url='https://www.cryptocompare.com/media/351684/dpay.png')
    ATOM = Coin(currency='ATOM', full_name='Atomic Coin', id='ATOM', url='https://www.cryptocompare.com/media/351685/atom.png')
    HKG = Coin(currency='HKG', full_name='Hacker Gold', id='HKG', url='https://www.cryptocompare.com/media/351689/hkg.jpg')
    ANTC = Coin(currency='ANTC', full_name='AntiLitecoin', id='ANTC', url='https://www.cryptocompare.com/media/351690/antc.png')
    JOBS = Coin(currency='JOBS', full_name='JobsCoin', id='JOBS', url='https://www.cryptocompare.com/media/351691/jobs.png')
    DGORE = Coin(currency='DGORE', full_name='DogeGoreCoin', id='DGORE', url='https://www.cryptocompare.com/media/351697/dgore.png')
    THC = Coin(currency='THC', full_name='The Hempcoin', id='THC', url='https://www.cryptocompare.com/media/351699/thc.png')
    TRA = Coin(currency='TRA', full_name='Tetra', id='TRA', url='https://www.cryptocompare.com/media/351700/tra.png')
    RMS = Coin(currency='RMS', full_name='Resumeo Shares', id='RMS', url='https://www.cryptocompare.com/media/351701/rms.png')
    FJC = Coin(currency='FJC', full_name='FujiCoin', id='FJC', url='https://www.cryptocompare.com/media/27010498/fjc.png')
    VAPOR = Coin(currency='VAPOR', full_name='Vaporcoin', id='VAPOR', url='https://www.cryptocompare.com/media/351708/vapor.png')
    SDP = Coin(currency='SDP', full_name='SydPakCoin', id='SDP', url='https://www.cryptocompare.com/media/351709/sdp.jpg')
    RRT = Coin(currency='RRT', full_name='Recovery Right Tokens', id='RRT', url='https://www.cryptocompare.com/media/19554/bitfinex.png')
    XZC = Coin(currency='XZC', full_name='ZCoin', id='XZC', url='https://www.cryptocompare.com/media/1382780/xzc1.png')
    PRE = Coin(currency='PRE', full_name='Premium', id='PRE', url='https://www.cryptocompare.com/media/351711/pre.png')
    CALC = Coin(currency='CALC', full_name='CaliphCoin', id='CALC', url='https://www.cryptocompare.com/media/351712/calc.png')
    LEA = Coin(currency='LEA', full_name='LeaCoin', id='LEA', url='https://www.cryptocompare.com/media/351729/lea.png')
    CF = Coin(currency='CF', full_name='Californium', id='CF', url='https://www.cryptocompare.com/media/351730/cf.png')
    CRNK = Coin(currency='CRNK', full_name='CrankCoin', id='CRNK', url='https://www.cryptocompare.com/media/351731/crnk.png')
    CFC = Coin(currency='CFC', full_name='CoffeeCoin', id='CFC', url='https://www.cryptocompare.com/media/351732/cfc.png')
    VTY = Coin(currency='VTY', full_name='Victoriouscoin', id='VTY', url='https://www.cryptocompare.com/media/351733/vty.png')
    ARDR = Coin(currency='ARDR', full_name='Ardor', id='ARDR', url='https://www.cryptocompare.com/media/351736/ardr.png')
    BS = Coin(currency='BS', full_name='BlackShadowCoin', id='BS', url='https://www.cryptocompare.com/media/351737/bs.png')
    JIF = Coin(currency='JIF', full_name='JiffyCoin', id='JIF', url='https://www.cryptocompare.com/media/351738/jif.png')
    CRAB = Coin(currency='CRAB', full_name='CrabCoin', id='CRAB', url='https://www.cryptocompare.com/media/351739/crab.png')
    HILL = Coin(currency='HILL', full_name='President Clinton', id='HILL', url='https://www.cryptocompare.com/media/351747/hill.png')
    MONETA = Coin(currency='MONETA', full_name='Moneta', id='MONETA', url='https://www.cryptocompare.com/media/351749/moneta.png')
    EC = Coin(currency='EC', full_name='Eclipse', id='EC', url='https://www.cryptocompare.com/media/351750/ec.jpg')
    RUBIT = Coin(currency='RUBIT', full_name='Rublebit', id='RUBIT', url='https://www.cryptocompare.com/media/351751/rubit.png')
    HCC = Coin(currency='HCC', full_name='HappyCreatorCoin ', id='HCC', url='https://www.cryptocompare.com/media/351752/hcc.png')
    BRAIN = Coin(currency='BRAIN', full_name='BrainCoin', id='BRAIN', url='https://www.cryptocompare.com/media/351753/brain.png')
    VTX = Coin(currency='VTX', full_name='Vertex', id='VTX', url='https://www.cryptocompare.com/media/351754/vertex.png')
    KRC = Coin(currency='KRC', full_name='KRCoin', id='KRC', url='https://www.cryptocompare.com/media/351755/krc.png')
    ROYAL = Coin(currency='ROYAL', full_name='RoyalCoin', id='ROYAL', url='https://www.cryptocompare.com/media/351756/royal.png')
    LFC = Coin(currency='LFC', full_name='BigLifeCoin', id='LFC', url='https://www.cryptocompare.com/media/351757/lfc.png')
    ZUR = Coin(currency='ZUR', full_name='Zurcoin', id='ZUR', url='https://www.cryptocompare.com/media/35280521/zur.png')
    NUBIS = Coin(currency='NUBIS', full_name='NubisCoin', id='NUBIS', url='https://www.cryptocompare.com/media/351759/nubis.png')
    TENNET = Coin(currency='TENNET', full_name='Tennet', id='TENNET', url='https://www.cryptocompare.com/media/351760/tennet.png')
    PEC = Coin(currency='PEC', full_name='PeaceCoin', id='PEC', url='https://www.cryptocompare.com/media/351761/pec.png')
    GMX = Coin(currency='GMX', full_name='Goldmaxcoin', id='GMX', url='https://www.cryptocompare.com/media/351762/gmx.jpg')
    GNJ = Coin(currency='GNJ', full_name='GanjaCoin V2', id='GNJ', url='https://www.cryptocompare.com/media/351789/gnj.png')
    TEAM = Coin(currency='TEAM', full_name='TeamUP', id='TEAM', url='https://www.cryptocompare.com/media/351790/team.png')
    SCT = Coin(currency='SCT', full_name='ScryptToken', id='SCT', url='https://www.cryptocompare.com/media/351791/sct.png')
    LANA = Coin(currency='LANA', full_name='LanaCoin', id='LANA', url='https://www.cryptocompare.com/media/351792/lana.png')
    ELE = Coin(currency='ELE', full_name='Elementrem', id='ELE', url='https://www.cryptocompare.com/media/351793/ele.png')
    GCC = Coin(currency='GCC', full_name='GuccioneCoin', id='GCC', url='https://www.cryptocompare.com/media/351796/gcc.jpg')
    AND = Coin(currency='AND', full_name='AndromedaCoin', id='AND', url='https://www.cryptocompare.com/media/351797/and.png')
    EQUAL = Coin(currency='EQUAL', full_name='EqualCoin', id='EQUAL', url='https://www.cryptocompare.com/media/351867/equal.png')
    SWEET = Coin(currency='SWEET', full_name='SweetStake', id='SWEET', url='https://www.cryptocompare.com/media/351868/sweet.png')
    DKC = Coin(currency='DKC', full_name='DarkKnightCoin', id='DKC', url='https://www.cryptocompare.com/media/351870/dkc.png')
    COC = Coin(currency='COC', full_name='Community Coin', id='COC', url='https://www.cryptocompare.com/media/351872/coc.png')
    CHOOF = Coin(currency='CHOOF', full_name='ChoofCoin', id='CHOOF', url='https://www.cryptocompare.com/media/351876/choof.png')
    CSH = Coin(currency='CSH', full_name='CashOut', id='CSH', url='https://www.cryptocompare.com/media/351877/csh.png')
    ZCL = Coin(currency='ZCL', full_name='ZClassic', id='ZCL', url='https://www.cryptocompare.com/media/351926/zcl.png')
    RYCN = Coin(currency='RYCN', full_name='RoyalCoin 2.0', id='RYCN', url='https://www.cryptocompare.com/media/351756/royal.png')
    PCS = Coin(currency='PCS', full_name='Pabyosi Coin', id='PCS', url='https://www.cryptocompare.com/media/351927/pabyosi.png')
    NBIT = Coin(currency='NBIT', full_name='NetBit', id='NBIT', url='https://www.cryptocompare.com/media/351928/nbit.png')
    WINE = Coin(currency='WINE', full_name='WineCoin', id='WINE', url='https://www.cryptocompare.com/media/351929/wine.png')
    DAR = Coin(currency='DAR', full_name='Darcrus', id='DAR', url='https://www.cryptocompare.com/media/351930/dar.png')
    ARK = Coin(currency='ARK', full_name='ARK', id='ARK', url='https://www.cryptocompare.com/media/351931/ark.png')
    IFLT = Coin(currency='IFLT', full_name='InflationCoin', id='IFLT', url='https://www.cryptocompare.com/media/35309724/iflt.png')
    ZECD = Coin(currency='ZECD', full_name='ZCashDarkCoin', id='ZECD', url='https://www.cryptocompare.com/media/351935/zecd.png')
    ZXT = Coin(currency='ZXT', full_name='Zcrypt', id='ZXT', url='https://www.cryptocompare.com/media/351936/zxt.png')
    WASH = Coin(currency='WASH', full_name='WashingtonCoin', id='WASH', url='https://www.cryptocompare.com/media/351944/wash.png')
    TESLA = Coin(currency='TESLA', full_name='TeslaCoilCoin', id='TESLA', url='https://www.cryptocompare.com/media/351945/tesla.png')
    LUCKY = Coin(currency='LUCKY', full_name='LuckyBlocks', id='LUCKY', url='https://www.cryptocompare.com/media/351946/lucky.png')
    VSL = Coin(currency='VSL', full_name='vSlice', id='VSL', url='https://www.cryptocompare.com/media/352113/d5a4e4f0366d3ae8cdbc45ad097f664c2557a55f0c237c1710-pimgpsh_fullsize_distr.jpg')
    TPG = Coin(currency='TPG', full_name='Troll Payment', id='TPG', url='https://www.cryptocompare.com/media/351948/tpg.png')
    LEO = Coin(currency='LEO', full_name='LEOcoin', id='LEO', url='https://www.cryptocompare.com/media/351988/leo.png')
    MDT = Coin(currency='MDT', full_name='Midnight', id='MDT', url='https://www.cryptocompare.com/media/351989/mdt.png')
    CBD = Coin(currency='CBD', full_name='CBD Crystals', id='CBD', url='https://www.cryptocompare.com/media/351990/cbd.png')
    PEX = Coin(currency='PEX', full_name='PosEx', id='PEX', url='https://www.cryptocompare.com/media/351992/pex.png')
    INSANE = Coin(currency='INSANE', full_name='InsaneCoin', id='INSANE', url='https://www.cryptocompare.com/media/351993/insane.png')
    GNT = Coin(currency='GNT', full_name='Golem Network Token', id='GNT', url='https://www.cryptocompare.com/media/351995/golem_logo.png')
    BASH = Coin(currency='BASH', full_name='LuckChain', id='BASH', url='https://www.cryptocompare.com/media/352004/bash.png')
    FAME = Coin(currency='FAME', full_name='FameCoin', id='FAME', url='https://www.cryptocompare.com/media/352006/fame.png')
    LIV = Coin(currency='LIV', full_name='LiviaCoin', id='LIV', url='https://www.cryptocompare.com/media/352007/liv.png')
    SP = Coin(currency='SP', full_name='Sex Pistols', id='SP', url='https://www.cryptocompare.com/media/352018/sp.png')
    MEGA = Coin(currency='MEGA', full_name='MegaFlash', id='MEGA', url='https://www.cryptocompare.com/media/352020/mega.png')
    VRS = Coin(currency='VRS', full_name='Veros', id='VRS', url='https://www.cryptocompare.com/media/35284407/veros.png')
    ALC = Coin(currency='ALC', full_name='Arab League Coin', id='ALC', url='https://www.cryptocompare.com/media/352022/alc.png')
    DOGETH = Coin(currency='DOGETH', full_name='EtherDoge', id='DOGETH', url='https://www.cryptocompare.com/media/352023/dogeth-2.png')
    KLC = Coin(currency='KLC', full_name='KiloCoin', id='KLC', url='https://www.cryptocompare.com/media/352024/klc.png')
    HUSH = Coin(currency='HUSH', full_name='Hush', id='HUSH', url='https://www.cryptocompare.com/media/1383138/thehush_300x300.png')
    BTLC = Coin(currency='BTLC', full_name='BitLuckCoin', id='BTLC', url='https://www.cryptocompare.com/media/352054/btlc.png')
    DRM8 = Coin(currency='DRM8', full_name='Dream8Coin', id='DRM8', url='https://www.cryptocompare.com/media/352055/drm8.png')
    FIST = Coin(currency='FIST', full_name='FistBump', id='FIST', url='https://www.cryptocompare.com/media/352056/fist.png')
    EBZ = Coin(currency='EBZ', full_name='Ebitz', id='EBZ', url='https://www.cryptocompare.com/media/352069/ebz.png')
    DRS = Coin(currency='DRS', full_name='Digital Rupees', id='DRS', url='https://www.cryptocompare.com/media/352072/drs.png')
    FGZ = Coin(currency='FGZ', full_name='Free Game Zone', id='FGZ', url='https://www.cryptocompare.com/media/352082/fgz.png')
    BOSON = Coin(currency='BOSON', full_name='BosonCoin', id='BOSON', url='https://www.cryptocompare.com/media/352083/boson.png')
    ATX = Coin(currency='ATX', full_name='ArtexCoin', id='ATX', url='https://www.cryptocompare.com/media/352084/atx.png')
    PNC = Coin(currency='PNC', full_name='PlatiniumCoin', id='PNC', url='https://www.cryptocompare.com/media/352085/pnc.png')
    BRDD = Coin(currency='BRDD', full_name='BeardDollars', id='BRDD', url='https://www.cryptocompare.com/media/352086/brdd.png')
    TIME = Coin(currency='TIME', full_name='Time', id='TIME', url='https://www.cryptocompare.com/media/352105/time.png')
    BIPC = Coin(currency='BIPC', full_name='BipCoin', id='BIPC', url='https://www.cryptocompare.com/media/352108/bip.png')
    XNC = Coin(currency='XNC', full_name='XenCoin', id='XNC', url='https://www.cryptocompare.com/media/352109/xnc.png')
    EMB = Coin(currency='EMB', full_name='EmberCoin', id='EMB', url='https://www.cryptocompare.com/media/352110/emb.png')
    BTTF = Coin(currency='BTTF', full_name='Coin to the Future', id='BTTF', url='https://www.cryptocompare.com/media/352111/bttf.png')
    DLR = Coin(currency='DLR', full_name='DollarOnline', id='DLR', url='https://www.cryptocompare.com/media/352114/dollarcoin.png')
    CSMIC = Coin(currency='CSMIC', full_name='Cosmic', id='CSMIC', url='https://www.cryptocompare.com/media/352115/csmic.png')
    FIRST = Coin(currency='FIRST', full_name='FirstCoin', id='FIRST', url='https://www.cryptocompare.com/media/352116/first.png')
    SCASH = Coin(currency='SCASH', full_name='SpaceCash', id='SCASH', url='https://www.cryptocompare.com/media/352117/scash.png')
    JIO = Coin(currency='JIO', full_name='JIO Token', id='JIO', url='https://www.cryptocompare.com/media/352120/jio.png')
    IW = Coin(currency='IW', full_name='iWallet', id='IW', url='https://www.cryptocompare.com/media/352121/iw.png')
    JNS = Coin(currency='JNS', full_name='Janus', id='JNS', url='https://www.cryptocompare.com/media/352126/jns.png')
    TRICK = Coin(currency='TRICK', full_name='TrickyCoin', id='TRICK', url='https://www.cryptocompare.com/media/352127/trick.png')
    DCRE = Coin(currency='DCRE', full_name='DeltaCredits', id='DCRE', url='https://www.cryptocompare.com/media/352128/dcre.png')
    FRE = Coin(currency='FRE', full_name='FreeCoin', id='FRE', url='https://www.cryptocompare.com/media/352129/fre.png')
    NPC = Coin(currency='NPC', full_name='NPCcoin', id='NPC', url='https://www.cryptocompare.com/media/352130/npc.png')
    PLNC = Coin(currency='PLNC', full_name='PLNCoin', id='PLNC', url='https://www.cryptocompare.com/media/352131/plnc.png')
    DGMS = Coin(currency='DGMS', full_name='Digigems', id='DGMS', url='https://www.cryptocompare.com/media/352132/dgms.png')
    ICOB = Coin(currency='ICOB', full_name='Icobid', id='ICOB', url='https://www.cryptocompare.com/media/352133/icb.png')
    ARCO = Coin(currency='ARCO', full_name='AquariusCoin', id='ARCO', url='https://www.cryptocompare.com/media/352134/arco.png')
    KURT = Coin(currency='KURT', full_name='Kurrent', id='KURT', url='https://www.cryptocompare.com/media/352155/kurt.png')
    XCRE = Coin(currency='XCRE', full_name='Creatio', id='XCRE', url='https://www.cryptocompare.com/media/352156/xcre.png')
    ENT = Coin(currency='ENT', full_name='Eternity', id='ENT', url='https://www.cryptocompare.com/media/352157/ent.jpg')
    UR = Coin(currency='UR', full_name='UR', id='UR', url='https://www.cryptocompare.com/media/352182/ur.jpg')
    MTLM3 = Coin(currency='MTLM3', full_name='Metal Music v3', id='MTLM3', url='https://www.cryptocompare.com/media/352183/mtmc3.png')
    ODNT = Coin(currency='ODNT', full_name='Old Dogs New Tricks', id='ODNT', url='https://www.cryptocompare.com/media/352186/odnt.png')
    EUC = Coin(currency='EUC', full_name='Eurocoin', id='EUC', url='https://www.cryptocompare.com/media/1382471/euc.png')
    CCX = Coin(currency='CCX', full_name='CoolDarkCoin', id='CCX', url='https://www.cryptocompare.com/media/352188/ccx.png')
    BCF = Coin(currency='BCF', full_name='BitcoinFast', id='BCF', url='https://www.cryptocompare.com/media/352189/btf.png')
    SEEDS = Coin(currency='SEEDS', full_name='SeedShares', id='SEEDS', url='https://www.cryptocompare.com/media/352190/seeds.png')
    XSN = Coin(currency='XSN', full_name='Stakenet', id='XSN', url='https://www.cryptocompare.com/media/34478393/stakenet.png')
    TKS = Coin(currency='TKS', full_name='Tokes', id='TKS', url='https://www.cryptocompare.com/media/35309097/tks.png')
    BCCOIN = Coin(currency='BCCOIN', full_name='BitConnect Coin', id='BCCOIN', url='https://www.cryptocompare.com/media/9350709/bccoin1.png')
    SHORTY = Coin(currency='SHORTY', full_name='ShortyCoin', id='SHORTY', url='https://www.cryptocompare.com/media/352222/shorty.png')
    PCM = Coin(currency='PCM', full_name='Procom', id='PCM', url='https://www.cryptocompare.com/media/352223/pcm.png')
    KC = Coin(currency='KC', full_name='Kernalcoin', id='KC', url='https://www.cryptocompare.com/media/352224/kc.png')
    CORAL = Coin(currency='CORAL', full_name='CoralPay', id='CORAL', url='https://www.cryptocompare.com/media/352225/coral.png')
    BamitCoin = Coin(currency='BamitCoin', full_name='BAM', id='BamitCoin', url='https://www.cryptocompare.com/media/352236/bam.png')
    NXC = Coin(currency='NXC', full_name='Nexium', id='NXC', url='https://www.cryptocompare.com/media/352248/nxc.png')
    MONEY = Coin(currency='MONEY', full_name='MoneyCoin', id='MONEY', url='https://www.cryptocompare.com/media/352249/money.png')
    BSTAR = Coin(currency='BSTAR', full_name='Blackstar', id='BSTAR', url='https://www.cryptocompare.com/media/352250/bstar.png')
    HSP = Coin(currency='HSP', full_name='Horse Power', id='HSP', url='https://www.cryptocompare.com/media/352251/hsp.png')
    HZT = Coin(currency='HZT', full_name='HazMatCoin', id='HZT', url='https://www.cryptocompare.com/media/352291/hzt.png')
    CS = Coin(currency='CS', full_name='CryptoSpots', id='CS', url='https://www.cryptocompare.com/media/352292/cs.png')
    XSP = Coin(currency='XSP', full_name='PoolStamp', id='XSP', url='https://www.cryptocompare.com/media/352293/xsp.png')
    CCRB = Coin(currency='CCRB', full_name='CryptoCarbon', id='CCRB', url='https://www.cryptocompare.com/media/27011026/ccrb.png')
    BULLS = Coin(currency='BULLS', full_name='BullshitCoin', id='BULLS', url='https://www.cryptocompare.com/media/352295/bulls.png')
    INCNT = Coin(currency='INCNT', full_name='Incent', id='INCNT', url='https://www.cryptocompare.com/media/352296/incnt.png')
    ICON = Coin(currency='ICON', full_name='Iconic', id='ICON', url='https://www.cryptocompare.com/media/352297/icon.png')
    NIC = Coin(currency='NIC', full_name='NewInvestCoin', id='NIC', url='https://www.cryptocompare.com/media/352309/nic.png')
    ACN = Coin(currency='ACN', full_name='AvonCoin', id='ACN', url='https://www.cryptocompare.com/media/352310/acn.png')
    XNG = Coin(currency='XNG', full_name='Enigma', id='XNG', url='https://www.cryptocompare.com/media/352311/xng.png')
    XCI = Coin(currency='XCI', full_name='Cannabis Industry Coin', id='XCI', url='https://www.cryptocompare.com/media/352312/xci.png')
    LOOK = Coin(currency='LOOK', full_name='LookCoin', id='LOOK', url='https://www.cryptocompare.com/media/1381970/look.png')
    LOC = Coin(currency='LOC', full_name='Loco', id='LOC', url='https://www.cryptocompare.com/media/1381971/loc.png')
    MMXVI = Coin(currency='MMXVI', full_name='MMXVI', id='MMXVI', url='https://www.cryptocompare.com/media/1381972/mmxvi.png')
    TRST = Coin(currency='TRST', full_name='TrustCoin', id='TRST', url='https://www.cryptocompare.com/media/1381975/trst.png')
    MIS = Coin(currency='MIS', full_name='MIScoin', id='MIS', url='https://www.cryptocompare.com/media/1381981/mis.png')
    WOP = Coin(currency='WOP', full_name='WorldPay', id='WOP', url='https://www.cryptocompare.com/media/1381982/wop.png')
    CQST = Coin(currency='CQST', full_name='ConquestCoin', id='CQST', url='https://www.cryptocompare.com/media/1381983/cqst.png')
    IMPS = Coin(currency='IMPS', full_name='Impulse Coin', id='IMPS', url='https://www.cryptocompare.com/media/1381984/imps.jpg')
    IN = Coin(currency='IN', full_name='InCoin', id='IN', url='https://www.cryptocompare.com/media/1381987/in.png')
    CHIEF = Coin(currency='CHIEF', full_name='TheChiefCoin', id='CHIEF', url='https://www.cryptocompare.com/media/1381988/chief.png')
    GOAT = Coin(currency='GOAT', full_name='Goat', id='GOAT', url='https://www.cryptocompare.com/media/1381990/goat.png')
    ANAL = Coin(currency='ANAL', full_name='AnalCoin', id='ANAL', url='https://www.cryptocompare.com/media/1381991/anal.jpg')
    RC = Coin(currency='RC', full_name='Russiacoin', id='RC', url='https://www.cryptocompare.com/media/1381992/rc.png')
    PND = Coin(currency='PND', full_name='PandaCoin', id='PND', url='https://www.cryptocompare.com/media/12318184/pnd.png')
    PX = Coin(currency='PX', full_name='PXcoin', id='PX', url='https://www.cryptocompare.com/media/1381994/px.png')
    OPTION = Coin(currency='OPTION', full_name='OptionCoin', id='OPTION', url='https://www.cryptocompare.com/media/1381998/option.png')
    AV = Coin(currency='AV', full_name='Avatar Coin', id='AV', url='https://www.cryptocompare.com/media/1382048/av.png')
    LTD = Coin(currency='LTD', full_name='Limited Coin', id='LTD', url='https://www.cryptocompare.com/media/1382049/ltd.png')
    UNITS = Coin(currency='UNITS', full_name='GameUnits', id='UNITS', url='https://www.cryptocompare.com/media/1382050/units.png')
    HEEL = Coin(currency='HEEL', full_name='HeelCoin', id='HEEL', url='https://www.cryptocompare.com/media/1382051/heel.png')
    GAKH = Coin(currency='GAKH', full_name='GAKHcoin', id='GAKH', url='https://www.cryptocompare.com/media/1382090/gakh.png')
    GAIN = Coin(currency='GAIN', full_name='Gainfy', id='GAIN', url='https://www.cryptocompare.com/media/35521188/gain.png')
    SHIFT = Coin(currency='SHIFT', full_name='Shift', id='SHIFT', url='https://www.cryptocompare.com/media/1382125/shift.png')
    S8C = Coin(currency='S8C', full_name='S88 Coin', id='S8C', url='https://www.cryptocompare.com/media/1382093/s8c.png')
    LVG = Coin(currency='LVG', full_name='Leverage Coin', id='LVG', url='https://www.cryptocompare.com/media/1382094/lvg.png')
    DRA = Coin(currency='DRA', full_name='DraculaCoin', id='DRA', url='https://www.cryptocompare.com/media/1382095/dra.png')
    ASAFE2 = Coin(currency='ASAFE2', full_name='Allsafe', id='ASAFE2', url='https://www.cryptocompare.com/media/35309626/safe.png')
    LTCR = Coin(currency='LTCR', full_name='LiteCreed', id='LTCR', url='https://www.cryptocompare.com/media/1382097/ltcr.png')
    QBC = Coin(currency='QBC', full_name='Quebecoin', id='QBC', url='https://www.cryptocompare.com/media/19874/qbc.png')
    XPRO = Coin(currency='XPRO', full_name='ProCoin', id='XPRO', url='https://www.cryptocompare.com/media/1382098/xpro.png')
    GIFT = Coin(currency='GIFT', full_name='GiftNet', id='GIFT', url='https://www.cryptocompare.com/media/1382171/gift.png')
    VIDZ = Coin(currency='VIDZ', full_name='PureVidz', id='VIDZ', url='https://www.cryptocompare.com/media/1382172/vidz.png')
    INC = Coin(currency='INC', full_name='Incrementum', id='INC', url='https://www.cryptocompare.com/media/1382173/inc.png')
    PTA = Coin(currency='PTA', full_name='PentaCoin', id='PTA', url='https://www.cryptocompare.com/media/1382236/pta.png')
    ACID = Coin(currency='ACID', full_name='AcidCoin', id='ACID', url='https://www.cryptocompare.com/media/1382237/acid.png')
    ZLQ = Coin(currency='ZLQ', full_name='ZLiteQubit', id='ZLQ', url='https://www.cryptocompare.com/media/1382238/zlq.png')
    RADI = Coin(currency='RADI', full_name='RadicalCoin', id='RADI', url='https://www.cryptocompare.com/media/1382239/rad.png')
    RNC = Coin(currency='RNC', full_name='ReturnCoin', id='RNC', url='https://www.cryptocompare.com/media/1382240/rnc.png')
    GOLOS = Coin(currency='GOLOS', full_name='Golos', id='GOLOS', url='https://www.cryptocompare.com/media/1382246/golos.png')
    PASC = Coin(currency='PASC', full_name='Pascal Coin', id='PASC', url='https://www.cryptocompare.com/media/1382247/pasc.png')
    TWIST = Coin(currency='TWIST', full_name='TwisterCoin', id='TWIST', url='https://www.cryptocompare.com/media/1382250/twist1.png')
    PAYP = Coin(currency='PAYP', full_name='PayPeer', id='PAYP', url='https://www.cryptocompare.com/media/1382251/payp.png')
    DETH = Coin(currency='DETH', full_name='DarkEther', id='DETH', url='https://www.cryptocompare.com/media/1382252/deth.png')
    YAY = Coin(currency='YAY', full_name='YAYcoin', id='YAY', url='https://www.cryptocompare.com/media/1382253/yay.png')
    YES = Coin(currency='YES', full_name='YesCoin', id='YES', url='https://www.cryptocompare.com/media/1382269/yes.png')
    LENIN = Coin(currency='LENIN', full_name='LeninCoin', id='LENIN', url='https://www.cryptocompare.com/media/1382270/lenin.png')
    MRSA = Coin(currency='MRSA', full_name='MrsaCoin', id='MRSA', url='https://www.cryptocompare.com/media/1382287/msra.png')
    OS76 = Coin(currency='OS76', full_name='OsmiumCoin', id='OS76', url='https://www.cryptocompare.com/media/1382288/os76.png')
    BOSS = Coin(currency='BOSS', full_name='BitBoss', id='BOSS', url='https://www.cryptocompare.com/media/1382289/boss.png')
    MKR = Coin(currency='MKR', full_name='Maker', id='MKR', url='https://www.cryptocompare.com/media/1382296/mkr.png')
    BIC = Coin(currency='BIC', full_name='Bikercoins', id='BIC', url='https://www.cryptocompare.com/media/1382337/bic.png')
    CRPS = Coin(currency='CRPS', full_name='CryptoPennies', id='CRPS', url='https://www.cryptocompare.com/media/1382338/crps.png')
    MOTO = Coin(currency='MOTO', full_name='Motocoin', id='MOTO', url='https://www.cryptocompare.com/media/1382339/moto.png')
    NTCC = Coin(currency='NTCC', full_name='NeptuneClassic', id='NTCC', url='https://www.cryptocompare.com/media/1382346/ntcc.png')
    HXX = Coin(currency='HXX', full_name='HexxCoin', id='HXX', url='https://www.cryptocompare.com/media/1382348/hexx.jpg')
    SPKTR = Coin(currency='SPKTR', full_name='Ghost Coin', id='SPKTR', url='https://www.cryptocompare.com/media/1382349/spkr.png')
    MAC = Coin(currency='MAC', full_name='MachineCoin', id='MAC', url='https://www.cryptocompare.com/media/1382368/mac.png')
    SEL = Coin(currency='SEL', full_name='SelenCoin', id='SEL', url='https://www.cryptocompare.com/media/1382369/sel.png')
    NOO = Coin(currency='NOO', full_name='Noocoin', id='NOO', url='https://www.cryptocompare.com/media/1382370/noo.png')
    CHAO = Coin(currency='CHAO', full_name='23 Skidoo', id='CHAO', url='https://www.cryptocompare.com/media/1382371/chao.png')
    XGB = Coin(currency='XGB', full_name='GoldenBird', id='XGB', url='https://www.cryptocompare.com/media/1382372/xgb.png')
    YMC = Coin(currency='YMC', full_name='YamahaCoin', id='YMC', url='https://www.cryptocompare.com/media/1382380/ymc.png')
    JOK = Coin(currency='JOK', full_name='JokerCoin', id='JOK', url='https://www.cryptocompare.com/media/1382381/jok.png')
    GBIT = Coin(currency='GBIT', full_name='GravityBit', id='GBIT', url='https://www.cryptocompare.com/media/1382382/gbit.jpg')
    TEC = Coin(currency='TEC', full_name='TeCoin', id='TEC', url='https://www.cryptocompare.com/media/1382383/tecoin.png')
    BOMB = Coin(currency='BOMB', full_name='BombCoin', id='BOMB', url='https://www.cryptocompare.com/media/1382384/bomb.png')
    RIDE = Coin(currency='RIDE', full_name='Ride My Car', id='RIDE', url='https://www.cryptocompare.com/media/1382388/ride.png')
    PIVX = Coin(currency='PIVX', full_name='Private Instant Verified Transaction', id='PIVX', url='https://www.cryptocompare.com/media/1382389/pivx.png')
    KED = Coin(currency='KED', full_name='Klingon Empire Darsek', id='KED', url='https://www.cryptocompare.com/media/1382390/ked.png')
    CNO = Coin(currency='CNO', full_name='Coino', id='CNO', url='https://www.cryptocompare.com/media/1382391/coino.png')
    WEALTH = Coin(currency='WEALTH', full_name='WealthCoin', id='WEALTH', url='https://www.cryptocompare.com/media/1382392/wealth.png')
    IOP = Coin(currency='IOP', full_name='Internet of People', id='IOP', url='https://www.cryptocompare.com/media/12318262/iop.png')
    XSPEC = Coin(currency='XSPEC', full_name='Spectre', id='XSPEC', url='https://www.cryptocompare.com/media/1382395/xspec.png')
    PEPECASH = Coin(currency='PEPECASH', full_name='Pepe Cash', id='PEPECASH', url='https://www.cryptocompare.com/media/1382397/pepecash.png')
    CLICK = Coin(currency='CLICK', full_name='Clickcoin', id='CLICK', url='https://www.cryptocompare.com/media/1382399/click.png')
    ELS = Coin(currency='ELS', full_name='Elysium', id='ELS', url='https://www.cryptocompare.com/media/1382400/els.png')
    KUSH = Coin(currency='KUSH', full_name='KushCoin', id='KUSH', url='https://www.cryptocompare.com/media/1382401/kush.png')
    ERY = Coin(currency='ERY', full_name='Eryllium', id='ERY', url='https://www.cryptocompare.com/media/1382403/ely2.png')
    PLU = Coin(currency='PLU', full_name='Pluton', id='PLU', url='https://www.cryptocompare.com/media/1382431/plu.png')
    PRES = Coin(currency='PRES', full_name='President Trump', id='PRES', url='https://www.cryptocompare.com/media/1382432/pres.png')
    BTZ = Coin(currency='BTZ', full_name='BitzCoin', id='BTZ', url='https://www.cryptocompare.com/media/1382433/btz.png')
    OPES = Coin(currency='OPES', full_name='Opes', id='OPES', url='https://www.cryptocompare.com/media/1382434/opes.png')
    WCT = Coin(currency='WCT', full_name='Waves Community Token', id='WCT', url='https://www.cryptocompare.com/media/350884/waves_1.png')
    UBQ = Coin(currency='UBQ', full_name='Ubiq', id='UBQ', url='https://www.cryptocompare.com/media/1382441/ubq.png')
    RATIO = Coin(currency='RATIO', full_name='Ratio', id='RATIO', url='https://www.cryptocompare.com/media/1382442/ratio.png')
    BAN = Coin(currency='BAN', full_name='Babes and Nerds', id='BAN', url='https://www.cryptocompare.com/media/1382466/ban.png')
    NICE = Coin(currency='NICE', full_name='NiceCoin', id='NICE', url='https://www.cryptocompare.com/media/1382467/nice.png')
    SMF = Coin(currency='SMF', full_name='SmurfCoin', id='SMF', url='https://www.cryptocompare.com/media/1382468/xmf.png')
    CWXT = Coin(currency='CWXT', full_name='CryptoWorldXToken', id='CWXT', url='https://www.cryptocompare.com/media/1382470/cwxt.png')
    TECH = Coin(currency='TECH', full_name='TechCoin', id='TECH', url='https://www.cryptocompare.com/media/1382505/tech.png')
    CIR = Coin(currency='CIR', full_name='CircuitCoin', id='CIR', url='https://www.cryptocompare.com/media/1382506/cir.png')
    LEPEN = Coin(currency='LEPEN', full_name='LePenCoin', id='LEPEN', url='https://www.cryptocompare.com/media/1382507/lepen.png')
    ROUND = Coin(currency='ROUND', full_name='RoundCoin', id='ROUND', url='https://www.cryptocompare.com/media/1382508/round.png')
    MAR = Coin(currency='MAR', full_name='MarijuanaCoin', id='MAR', url='https://www.cryptocompare.com/media/1382577/mar.png')
    MARX = Coin(currency='MARX', full_name='MarxCoin', id='MARX', url='https://www.cryptocompare.com/media/1382578/marx.png')
    TAT = Coin(currency='TAT', full_name='Tatiana Coin', id='TAT', url='https://www.cryptocompare.com/media/1382594/tat.png')
    HAZE = Coin(currency='HAZE', full_name='HazeCoin', id='HAZE', url='https://www.cryptocompare.com/media/1382595/haze.png')
    PRX = Coin(currency='PRX', full_name='Printerium', id='PRX', url='https://www.cryptocompare.com/media/1382603/prx.png')
    NRC = Coin(currency='NRC', full_name='Neurocoin', id='NRC', url='https://www.cryptocompare.com/media/1382604/nrc.png')
    PAC = Coin(currency='PAC', full_name='PacCoin', id='PAC', url='https://www.cryptocompare.com/media/30002082/pac.png')
    IMPCH = Coin(currency='IMPCH', full_name='Impeach', id='IMPCH', url='https://www.cryptocompare.com/media/1382606/impch.png')
    ERR = Coin(currency='ERR', full_name='ErrorCoin', id='ERR', url='https://www.cryptocompare.com/media/1382624/err.png')
    TIC = Coin(currency='TIC', full_name='TrueInvestmentCoin', id='TIC', url='https://www.cryptocompare.com/media/1382625/tic.png')
    NUKE = Coin(currency='NUKE', full_name='NukeCoin', id='NUKE', url='https://www.cryptocompare.com/media/1382626/nuke.png')
    EOC = Coin(currency='EOC', full_name='EveryonesCoin', id='EOC', url='https://www.cryptocompare.com/media/1382628/eoc.png')
    SFC = Coin(currency='SFC', full_name='Solarflarecoin', id='SFC', url='https://www.cryptocompare.com/media/1382639/sfc.png')
    JANE = Coin(currency='JANE', full_name='JaneCoin', id='JANE', url='https://www.cryptocompare.com/media/1382640/jane.png')
    PARA = Coin(currency='PARA', full_name='ParanoiaCoin', id='PARA', url='https://www.cryptocompare.com/media/1382641/para.png')
    MM = Coin(currency='MM', full_name='MasterMint', id='MM', url='https://www.cryptocompare.com/media/1382642/mm.jpg')
    CTL = Coin(currency='CTL', full_name='Citadel', id='CTL', url='https://www.cryptocompare.com/media/33842977/ctl.jpg')
    NDOGE = Coin(currency='NDOGE', full_name='NinjaDoge', id='NDOGE', url='https://www.cryptocompare.com/media/1382650/ndoge.png')
    ZBC = Coin(currency='ZBC', full_name='Zilbercoin', id='ZBC', url='https://www.cryptocompare.com/media/35284309/zbc.png')
    MLN = Coin(currency='MLN', full_name='Melon', id='MLN', url='https://www.cryptocompare.com/media/1382653/mln.png')
    FRST = Coin(currency='FRST', full_name='FirstCoin', id='FRST', url='https://www.cryptocompare.com/media/1382654/first.png')
    PAY = Coin(currency='PAY', full_name='TenX', id='PAY', url='https://www.cryptocompare.com/media/1383687/pay.png')
    ORO = Coin(currency='ORO', full_name='OroCoin', id='ORO', url='https://www.cryptocompare.com/media/1382656/oro.png')
    ALEX = Coin(currency='ALEX', full_name='Alexandrite', id='ALEX', url='https://www.cryptocompare.com/media/1382657/alex.png')
    TBCX = Coin(currency='TBCX', full_name='TrashBurn', id='TBCX', url='https://www.cryptocompare.com/media/1382658/tbcx.png')
    MCAR = Coin(currency='MCAR', full_name='MasterCar', id='MCAR', url='https://www.cryptocompare.com/media/1382659/mcar.png')
    THS = Coin(currency='THS', full_name='TechShares', id='THS', url='https://www.cryptocompare.com/media/1382660/ths.png')
    ACES = Coin(currency='ACES', full_name='AcesCoin', id='ACES', url='https://www.cryptocompare.com/media/1382661/aces.png')
    UAEC = Coin(currency='UAEC', full_name='United Arab Emirates Coin', id='UAEC', url='https://www.cryptocompare.com/media/1382684/uaec.png')
    EA = Coin(currency='EA', full_name='EagleCoin', id='EA', url='https://www.cryptocompare.com/media/1382685/ea.png')
    PIE = Coin(currency='PIE', full_name='Persistent Information Exchange', id='PIE', url='https://www.cryptocompare.com/media/1382686/pie.png')
    CREA = Coin(currency='CREA', full_name='CreativeChain', id='CREA', url='https://www.cryptocompare.com/media/1382709/crea.png')
    WISC = Coin(currency='WISC', full_name='WisdomCoin', id='WISC', url='https://www.cryptocompare.com/media/1382710/wisc.jpg')
    BVC = Coin(currency='BVC', full_name='BeaverCoin', id='BVC', url='https://www.cryptocompare.com/media/1382711/bvc.png')
    FIND = Coin(currency='FIND', full_name='FindCoin', id='FIND', url='https://www.cryptocompare.com/media/1382713/find.png')
    MLITE = Coin(currency='MLITE', full_name='MeLite', id='MLITE', url='https://www.cryptocompare.com/media/1382725/mlite.png')
    STALIN = Coin(currency='STALIN', full_name='StalinCoin', id='STALIN', url='https://www.cryptocompare.com/media/1382726/stalin.png')
    TSE = Coin(currency='TSE', full_name='TattooCoin', id='TSE', url='https://www.cryptocompare.com/media/1382790/tato1.png')
    VLTC = Coin(currency='VLTC', full_name='VaultCoin', id='VLTC', url='https://www.cryptocompare.com/media/1382738/vltc.png')
    BIOB = Coin(currency='BIOB', full_name='BioBar', id='BIOB', url='https://www.cryptocompare.com/media/1382739/biob.png')
    SWT = Coin(currency='SWT', full_name='Swarm City Token', id='SWT', url='https://www.cryptocompare.com/media/1382740/swt.jpg')
    PASL = Coin(currency='PASL', full_name='Pascal Lite', id='PASL', url='https://www.cryptocompare.com/media/1382741/pasl.png')
    ZER = Coin(currency='ZER', full_name='Zero', id='ZER', url='https://www.cryptocompare.com/media/34155612/zer.png')
    CHAT = Coin(currency='CHAT', full_name='OpenChat', id='CHAT', url='https://www.cryptocompare.com/media/34478301/logo_132_132_chat.png')
    CDN = Coin(currency='CDN', full_name='Canada eCoin', id='CDN', url='https://www.cryptocompare.com/media/1382763/cdn.png')
    NETKO = Coin(currency='NETKO', full_name='Netko', id='NETKO', url='https://www.cryptocompare.com/media/1382771/netko.png')
    ZOI = Coin(currency='ZOI', full_name='Zoin', id='ZOI', url='https://www.cryptocompare.com/media/27011018/zoi.png')
    HONEY = Coin(currency='HONEY', full_name='Honey', id='HONEY', url='https://www.cryptocompare.com/media/1382937/honey1.png')
    MXT = Coin(currency='MXT', full_name='MartexCoin', id='MXT', url='https://www.cryptocompare.com/media/1382782/mxt.jpg')
    MUSIC = Coin(currency='MUSIC', full_name='Musicoin', id='MUSIC', url='https://www.cryptocompare.com/media/1382783/music.png')
    DTB = Coin(currency='DTB', full_name='Databits', id='DTB', url='https://www.cryptocompare.com/media/1382791/dtb.png')
    VEG = Coin(currency='VEG', full_name='BitVegan', id='VEG', url='https://www.cryptocompare.com/media/1382792/veg.png')
    MBIT = Coin(currency='MBIT', full_name='Mbitbooks', id='MBIT', url='https://www.cryptocompare.com/media/1382793/mbit.png')
    VOLT = Coin(currency='VOLT', full_name='BitVolt', id='VOLT', url='https://www.cryptocompare.com/media/1382794/volt.png')
    EDG = Coin(currency='EDG', full_name='Edgeless', id='EDG', url='https://www.cryptocompare.com/media/1382799/edg.jpg')
    BEST = Coin(currency='BEST', full_name='BestChain', id='BEST', url='https://www.cryptocompare.com/media/1382805/best.jpg')
    CHC = Coin(currency='CHC', full_name='ChainCoin', id='CHC', url='https://www.cryptocompare.com/media/33842945/chc.jpg')
    ZENI = Coin(currency='ZENI', full_name='Zennies', id='ZENI', url='https://www.cryptocompare.com/media/1382807/zen.png')
    PLANET = Coin(currency='PLANET', full_name='PlanetCoin', id='PLANET', url='https://www.cryptocompare.com/media/1382851/planet.png')
    DUCK = Coin(currency='DUCK', full_name='DuckDuckCoin', id='DUCK', url='https://www.cryptocompare.com/media/1382852/duckduckcoin.png')
    BNX = Coin(currency='BNX', full_name='BnrtxCoin', id='BNX', url='https://www.cryptocompare.com/media/1382853/bnx.png')
    BSTK = Coin(currency='BSTK', full_name='BattleStake', id='BSTK', url='https://www.cryptocompare.com/media/1382858/bstk.png')
    RNS = Coin(currency='RNS', full_name='RenosCoin', id='RNS', url='https://www.cryptocompare.com/media/35309730/rns.png')
    DBIX = Coin(currency='DBIX', full_name='DubaiCoin', id='DBIX', url='https://www.cryptocompare.com/media/1382860/dbix.png')
    AMIS = Coin(currency='AMIS', full_name='AMIS', id='AMIS', url='https://www.cryptocompare.com/media/1382862/amis.png')
    KAYI = Coin(currency='KAYI', full_name='Kayı', id='KAYI', url='https://www.cryptocompare.com/media/1382863/kayi.png')
    XVP = Coin(currency='XVP', full_name='VirtacoinPlus', id='XVP', url='https://www.cryptocompare.com/media/1382865/xvp.png')
    BOAT = Coin(currency='BOAT', full_name='Doubloon', id='BOAT', url='https://www.cryptocompare.com/media/1382866/boat.png')
    TAJ = Coin(currency='TAJ', full_name='TajCoin', id='TAJ', url='https://www.cryptocompare.com/media/1382867/taj.png')
    IMX = Coin(currency='IMX', full_name='Impact', id='IMX', url='https://www.cryptocompare.com/media/35309728/imx.png')
    CJC = Coin(currency='CJC', full_name='CryptoJournal', id='CJC', url='https://www.cryptocompare.com/media/1382887/cjc.png')
    AMY = Coin(currency='AMY', full_name='Amygws', id='AMY', url='https://www.cryptocompare.com/media/1382935/amy.jpg')
    QBT = Coin(currency='QBT', full_name='Cubits', id='QBT', url='https://www.cryptocompare.com/media/1382936/qbt.png')
    EB3 = Coin(currency='EB3', full_name='EB3coin', id='EB3', url='https://www.cryptocompare.com/media/1382938/eb3.png')
    XVE = Coin(currency='XVE', full_name='The Vegan Initiative', id='XVE', url='https://www.cryptocompare.com/media/1382937/xve.png')
    FAZZ = Coin(currency='FAZZ', full_name='FazzCoin', id='FAZZ', url='https://www.cryptocompare.com/media/1382944/fazz.png')
    APT = Coin(currency='APT', full_name='Aptcoin', id='APT', url='https://www.cryptocompare.com/media/1382945/apt.png')
    BLAZR = Coin(currency='BLAZR', full_name='BlazerCoin', id='BLAZR', url='https://www.cryptocompare.com/media/1382946/blazr.png')
    ARPA = Coin(currency='ARPA', full_name='ArpaCoin', id='ARPA', url='https://www.cryptocompare.com/media/1382966/arpa.png')
    UNI = Coin(currency='UNI', full_name='Universe', id='UNI', url='https://www.cryptocompare.com/media/1382968/uni.png')
    ECO = Coin(currency='ECO', full_name='ECOcoin', id='ECO', url='https://www.cryptocompare.com/media/1382993/eco.png')
    XLR = Coin(currency='XLR', full_name='Solaris', id='XLR', url='https://www.cryptocompare.com/media/1382994/xlr.png')
    DARK = Coin(currency='DARK', full_name='Dark', id='DARK', url='https://www.cryptocompare.com/media/1382995/dark.png')
    DON = Coin(currency='DON', full_name='DonationCoin', id='DON', url='https://www.cryptocompare.com/media/1382995/don.png')
    MER = Coin(currency='MER', full_name='Mercury', id='MER', url='https://www.cryptocompare.com/media/14913628/mer.png')
    WGO = Coin(currency='WGO', full_name='WavesGO', id='WGO', url='https://www.cryptocompare.com/media/1382998/wgo.png')
    RLC = Coin(currency='RLC', full_name='iEx.ec', id='RLC', url='https://www.cryptocompare.com/media/12318418/rlc.png')
    ATMOS = Coin(currency='ATMOS', full_name='Atmos', id='ATMOS', url='https://www.cryptocompare.com/media/30002333/atmos.jpg')
    ETT = Coin(currency='ETT', full_name='EncryptoTel', id='ETT', url='https://www.cryptocompare.com/media/1383046/ett.png')
    VISIO = Coin(currency='VISIO', full_name='Visio', id='VISIO', url='https://www.cryptocompare.com/media/1383047/visio.png')
    HPC = Coin(currency='HPC', full_name='HappyCoin', id='HPC', url='https://www.cryptocompare.com/media/1383046/hpc.png')
    GOT = Coin(currency='GOT', full_name='Giotto Coin', id='GOT', url='https://www.cryptocompare.com/media/1383079/got.png')
    CXT = Coin(currency='CXT', full_name='Coinonat', id='CXT', url='https://www.cryptocompare.com/media/1383080/cxt.png')
    EMPC = Coin(currency='EMPC', full_name='EmporiumCoin', id='EMPC', url='https://www.cryptocompare.com/media/1383081/empc.png')
    GNO = Coin(currency='GNO', full_name='Gnosis', id='GNO', url='https://www.cryptocompare.com/media/1383083/gnosis-logo.png')
    LGD = Coin(currency='LGD', full_name='Legends Cryptocurrency', id='LGD', url='https://www.cryptocompare.com/media/1383085/lgd.png')
    TAAS = Coin(currency='TAAS', full_name='Token as a Service', id='TAAS', url='https://www.cryptocompare.com/media/1383085/taas.png')
    BUCKS = Coin(currency='BUCKS', full_name='SwagBucks', id='BUCKS', url='https://www.cryptocompare.com/media/1383089/bucks.png')
    XBY = Coin(currency='XBY', full_name='XTRABYTES', id='XBY', url='https://www.cryptocompare.com/media/35284408/extrabytes.png')
    GUP = Coin(currency='GUP', full_name='Guppy', id='GUP', url='https://www.cryptocompare.com/media/1383107/gup.png')
    MCRN = Coin(currency='MCRN', full_name='MacronCoin', id='MCRN', url='https://www.cryptocompare.com/media/1383111/mcrn.png')
    LUN = Coin(currency='LUN', full_name='Lunyr', id='LUN', url='https://www.cryptocompare.com/media/1383112/lunyr-logo.png')
    RAIN = Coin(currency='RAIN', full_name='Condensate', id='RAIN', url='https://www.cryptocompare.com/media/1383114/rain.png')
    WSX = Coin(currency='WSX', full_name='WeAreSatoshi', id='WSX', url='https://www.cryptocompare.com/media/1383144/wsx.png')
    IEC = Coin(currency='IEC', full_name='IvugeoEvolutionCoin', id='IEC', url='https://www.cryptocompare.com/media/1383144/wsx.png')
    IMS = Coin(currency='IMS', full_name='Independent Money System', id='IMS', url='https://www.cryptocompare.com/media/1383145/ims.png')
    ARGUS = Coin(currency='ARGUS', full_name='ArgusCoin', id='ARGUS', url='https://www.cryptocompare.com/media/1383149/argus.png')
    CNT = Coin(currency='CNT', full_name='Centurion', id='CNT', url='https://www.cryptocompare.com/media/1383150/cnt.png')
    LMC = Coin(currency='LMC', full_name='LomoCoin', id='LMC', url='https://www.cryptocompare.com/media/1383139/lmc.png')
    TKN = Coin(currency='TKN', full_name='TokenCard  ', id='TKN', url='https://www.cryptocompare.com/media/1383157/tkn.png')
    BTCS = Coin(currency='BTCS', full_name='Bitcoin Scrypt', id='BTCS', url='https://www.cryptocompare.com/media/1383158/btcs.png')
    PROC = Coin(currency='PROC', full_name='ProCurrency', id='PROC', url='https://www.cryptocompare.com/media/1383159/proc.png')
    XGR = Coin(currency='XGR', full_name='GoldReserve', id='XGR', url='https://www.cryptocompare.com/media/1383161/xgr.png')
    BENJI = Coin(currency='BENJI', full_name='BenjiRolls', id='BENJI', url='https://www.cryptocompare.com/media/1383163/benji.png')
    HMQ = Coin(currency='HMQ', full_name='Humaniq', id='HMQ', url='https://www.cryptocompare.com/media/1383174/hmq.png')
    BCAP = Coin(currency='BCAP', full_name='Blockchain Capital', id='BCAP', url='https://www.cryptocompare.com/media/1383948/bcap1.png')
    DUO = Coin(currency='DUO', full_name='ParallelCoin', id='DUO', url='https://www.cryptocompare.com/media/1383196/duo.png')
    RBX = Coin(currency='RBX', full_name='RiptoBuX', id='RBX', url='https://www.cryptocompare.com/media/1383197/rbx.png')
    GRW = Coin(currency='GRW', full_name='GrowthCoin', id='GRW', url='https://www.cryptocompare.com/media/1383234/grw.png')
    APX = Coin(currency='APX', full_name='Apx', id='APX', url='https://www.cryptocompare.com/media/1383235/apx.png')
    MILO = Coin(currency='MILO', full_name='MiloCoin', id='MILO', url='https://www.cryptocompare.com/media/1383236/milo.png')
    OLV = Coin(currency='OLV', full_name='OldV', id='OLV', url='https://www.cryptocompare.com/media/1383239/xvs.png')
    ILC = Coin(currency='ILC', full_name='ILCoin', id='ILC', url='https://www.cryptocompare.com/media/1383238/ilc.png')
    MRT = Coin(currency='MRT', full_name='MinersReward', id='MRT', url='https://www.cryptocompare.com/media/350884/waves_1.png')
    IOU = Coin(currency='IOU', full_name='IOU1', id='IOU', url='https://www.cryptocompare.com/media/1383241/iou1.png')
    PZM = Coin(currency='PZM', full_name='Prizm', id='PZM', url='https://www.cryptocompare.com/media/1383242/pzm.jpg')
    PHR = Coin(currency='PHR', full_name='Phreak', id='PHR', url='https://www.cryptocompare.com/media/1383243/phr.jpg')
    ANT = Coin(currency='ANT', full_name='Aragon', id='ANT', url='https://www.cryptocompare.com/media/1383244/ant.png')
    PUPA = Coin(currency='PUPA', full_name='PupaCoin', id='PUPA', url='https://www.cryptocompare.com/media/1383245/pupa.png')
    RICE = Coin(currency='RICE', full_name='RiceCoin', id='RICE', url='https://www.cryptocompare.com/media/1383245/rice.png')
    XCT = Coin(currency='XCT', full_name='C-Bits', id='XCT', url='https://www.cryptocompare.com/media/1383246/xct.png')
    DEA = Coin(currency='DEA', full_name='Degas Coin', id='DEA', url='https://www.cryptocompare.com/media/1383264/dea.png')
    RED = Coin(currency='RED', full_name='Redcoin', id='RED', url='https://www.cryptocompare.com/media/1383265/red.png')
    ZSE = Coin(currency='ZSE', full_name='ZSEcoin', id='ZSE', url='https://www.cryptocompare.com/media/1383266/zse.png')
    CTIC = Coin(currency='CTIC', full_name='Coinmatic', id='CTIC', url='https://www.cryptocompare.com/media/1383267/ctic.png')
    TAP = Coin(currency='TAP', full_name='TappingCoin', id='TAP', url='https://www.cryptocompare.com/media/1383283/tap.png')
    BITOK = Coin(currency='BITOK', full_name='BitOKX', id='BITOK', url='https://www.cryptocompare.com/media/1383282/bitok.jpg')
    PBT = Coin(currency='PBT', full_name='Primalbase', id='PBT', url='https://www.cryptocompare.com/media/1383324/pbt.png')
    MUU = Coin(currency='MUU', full_name='MilkCoin', id='MUU', url='https://www.cryptocompare.com/media/1383325/muu.png')
    INF8 = Coin(currency='INF8', full_name='Infinium-8', id='INF8', url='https://www.cryptocompare.com/media/1383326/inf8.png')
    HTML5 = Coin(currency='HTML5', full_name='HTML5 Coin', id='HTML5', url='https://www.cryptocompare.com/media/1383327/html5.png')
    MNE = Coin(currency='MNE', full_name='Minereum', id='MNE', url='https://www.cryptocompare.com/media/1383328/mne.png')
    DICE = Coin(currency='DICE', full_name='Etheroll', id='DICE', url='https://www.cryptocompare.com/media/1383361/dice.png')
    USC = Coin(currency='USC', full_name='Ultimate Secure Cash', id='USC', url='https://www.cryptocompare.com/media/1383363/usc.png')
    DUX = Coin(currency='DUX', full_name='DuxCoin', id='DUX', url='https://www.cryptocompare.com/media/1383364/dux.png')
    XPS = Coin(currency='XPS', full_name='PoisonIvyCoin', id='XPS', url='https://www.cryptocompare.com/media/1383365/xps.png')
    EQT = Coin(currency='EQT', full_name='EquiTrader', id='EQT', url='https://www.cryptocompare.com/media/1383366/eqt.png')
    INSN = Coin(currency='INSN', full_name='Insane Coin', id='INSN', url='https://www.cryptocompare.com/media/1383366/insn.png')
    BAT = Coin(currency='BAT', full_name='Basic Attention Token', id='BAT', url='https://www.cryptocompare.com/media/1383370/bat.png')
    F16 = Coin(currency='F16', full_name='F16Coin', id='F16', url='https://www.cryptocompare.com/media/1383372/f16.png')
    HAMS = Coin(currency='HAMS', full_name='HamsterCoin', id='HAMS', url='https://www.cryptocompare.com/media/1383381/hams.png')
    QTUM = Coin(currency='QTUM', full_name='QTUM', id='QTUM', url='https://www.cryptocompare.com/media/1383382/qtum.png')
    NEF = Coin(currency='NEF', full_name='NefariousCoin', id='NEF', url='https://www.cryptocompare.com/media/1383383/nef.png')
    BOS = Coin(currency='BOS', full_name='BOScoin', id='BOS', url='https://www.cryptocompare.com/media/1383521/bos.png')
    QWARK = Coin(currency='QWARK', full_name='Qwark', id='QWARK', url='https://www.cryptocompare.com/media/1383522/qwark.png')
    IOT = Coin(currency='IOT', full_name='IOTA', id='IOT', url='https://www.cryptocompare.com/media/1383540/iota_logo.png')
    QRL = Coin(currency='QRL', full_name='Quantum Resistant Ledger', id='QRL', url='https://www.cryptocompare.com/media/34478071/qrl.png')
    ADL = Coin(currency='ADL', full_name='Adelphoi', id='ADL', url='https://www.cryptocompare.com/media/1383544/adl.png')
    PTOY = Coin(currency='PTOY', full_name='Patientory', id='PTOY', url='https://www.cryptocompare.com/media/1383547/ptoy.png')
    ZRC = Coin(currency='ZRC', full_name='ZrCoin', id='ZRC', url='https://www.cryptocompare.com/media/1383548/xzc.png')
    LKK = Coin(currency='LKK', full_name='Lykke', id='LKK', url='https://www.cryptocompare.com/media/1383553/lkk.png')
    ESP = Coin(currency='ESP', full_name='Espers', id='ESP', url='https://www.cryptocompare.com/media/14761907/esp.png')
    DYN = Coin(currency='DYN', full_name='Dynamic', id='DYN', url='https://www.cryptocompare.com/media/35521029/dyn.png')
    SEQ = Coin(currency='SEQ', full_name='Sequence', id='SEQ', url='https://www.cryptocompare.com/media/35521030/seq.png')
    MCAP = Coin(currency='MCAP', full_name='MCAP', id='MCAP', url='https://www.cryptocompare.com/media/1383559/mcap.png')
    MYST = Coin(currency='MYST', full_name='Mysterium', id='MYST', url='https://www.cryptocompare.com/media/1383561/myst.png')
    VERI = Coin(currency='VERI', full_name='Veritaseum', id='VERI', url='https://www.cryptocompare.com/media/1383562/veri.png')
    SNM = Coin(currency='SNM', full_name='SONM', id='SNM', url='https://www.cryptocompare.com/media/1383564/snm.png')
    SKY = Coin(currency='SKY', full_name='Skycoin', id='SKY', url='https://www.cryptocompare.com/media/30001806/sky.png')
    CFI = Coin(currency='CFI', full_name='Cofound.it', id='CFI', url='https://www.cryptocompare.com/media/1383567/cfi.png')
    SNT = Coin(currency='SNT', full_name='Status Network Token', id='SNT', url='https://www.cryptocompare.com/media/1383568/snt.png')
    AVT = Coin(currency='AVT', full_name='AventCoin', id='AVT', url='https://www.cryptocompare.com/media/1383599/avt.png')
    CVC = Coin(currency='CVC', full_name='Civic', id='CVC', url='https://www.cryptocompare.com/media/1383611/cvc.png')
    IXT = Coin(currency='IXT', full_name='iXledger', id='IXT', url='https://www.cryptocompare.com/media/1383612/ixt.png')
    DENT = Coin(currency='DENT', full_name='Dent', id='DENT', url='https://www.cryptocompare.com/media/1383613/dent.png')
    ETHOS = Coin(currency='ETHOS', full_name='Ethos', id='ETHOS', url='https://www.cryptocompare.com/media/16404851/ethos.png')
    STA = Coin(currency='STA', full_name='Starta', id='STA', url='https://www.cryptocompare.com/media/1383620/crs.png')
    TFL = Coin(currency='TFL', full_name='True Flip Lottery', id='TFL', url='https://www.cryptocompare.com/media/1383621/tfl.png')
    EFYT = Coin(currency='EFYT', full_name='Ergo', id='EFYT', url='https://www.cryptocompare.com/media/1383646/efyt.png')
    EOS = Coin(currency='EOS', full_name='EOS', id='EOS', url='https://www.cryptocompare.com/media/1383652/eos_1.png')
    MCO = Coin(currency='MCO', full_name='Crypto.com', id='MCO', url='https://www.cryptocompare.com/media/34478435/mco.png')
    NMR = Coin(currency='NMR', full_name='Numeraire', id='NMR', url='https://www.cryptocompare.com/media/1383655/nmr.png')
    ADX = Coin(currency='ADX', full_name='AdEx', id='ADX', url='https://www.cryptocompare.com/media/1383667/adx1.png')
    QAU = Coin(currency='QAU', full_name='Quantum', id='QAU', url='https://www.cryptocompare.com/media/1383669/qau.png')
    ECOB = Coin(currency='ECOB', full_name='EcoBit', id='ECOB', url='https://www.cryptocompare.com/media/1383670/ecob.png')
    PLBT = Coin(currency='PLBT', full_name='Polybius', id='PLBT', url='https://www.cryptocompare.com/media/1383671/polybius.png')
    USDT = Coin(currency='USDT', full_name='Tether', id='USDT', url='https://www.cryptocompare.com/media/1383672/usdt.png')
    NANO = Coin(currency='NANO', full_name='Nano', id='NANO', url='https://www.cryptocompare.com/media/30001997/untitled-1.png')
    AHT = Coin(currency='AHT', full_name='Ahoolee', id='AHT', url='https://www.cryptocompare.com/media/1383688/ahc.png')
    ATB = Coin(currency='ATB', full_name='ATB coin', id='ATB', url='https://www.cryptocompare.com/media/1383689/atb.png')
    TIX = Coin(currency='TIX', full_name='Blocktix', id='TIX', url='https://www.cryptocompare.com/media/1383690/tix.png')
    CHAN = Coin(currency='CHAN', full_name='ChanCoin', id='CHAN', url='https://www.cryptocompare.com/media/1383831/chan2.png')
    CMP = Coin(currency='CMP', full_name='Compcoin', id='CMP', url='https://www.cryptocompare.com/media/1383692/compcoin.png')
    RVT = Coin(currency='RVT', full_name='Rivetz', id='RVT', url='https://www.cryptocompare.com/media/1383694/rvt.png')
    HRB = Coin(currency='HRB', full_name='Harbour DAO', id='HRB', url='https://www.cryptocompare.com/media/1383695/hrb.png')
    NIM = Coin(currency='NIM', full_name='Nimiq ', id='NIM', url='https://www.cryptocompare.com/media/1383697/net1.png')
    CDT = Coin(currency='CDT', full_name='Blox', id='CDT', url='https://www.cryptocompare.com/media/1383699/cdt.png')
    ACT = Coin(currency='ACT', full_name='ACT', id='ACT', url='https://www.cryptocompare.com/media/1383700/act.png')
    DNT = Coin(currency='DNT', full_name='district0x', id='DNT', url='https://www.cryptocompare.com/media/1383701/dnt.png')
    SUR = Coin(currency='SUR', full_name='Suretly', id='SUR', url='https://www.cryptocompare.com/media/1383696/sur.png')
    PING = Coin(currency='PING', full_name='CryptoPing', id='PING', url='https://www.cryptocompare.com/media/1383706/ping1.png')
    MIV = Coin(currency='MIV', full_name='MakeItViral', id='MIV', url='https://www.cryptocompare.com/media/1383728/miv.png')
    SAN = Coin(currency='SAN', full_name='Santiment', id='SAN', url='https://www.cryptocompare.com/media/1383730/san.png')
    KIN = Coin(currency='KIN', full_name='Kin', id='KIN', url='https://www.cryptocompare.com/media/1383731/kin.png')
    WGR = Coin(currency='WGR', full_name='Wagerr', id='WGR', url='https://www.cryptocompare.com/media/1383736/wgr.png')
    XEL = Coin(currency='XEL', full_name='Elastic', id='XEL', url='https://www.cryptocompare.com/media/1383737/xel.png')
    NVST = Coin(currency='NVST', full_name='NVO', id='NVST', url='https://www.cryptocompare.com/media/1383732/nvst.png')
    FUN = Coin(currency='FUN', full_name='FunFair', id='FUN', url='https://www.cryptocompare.com/media/1383738/fun.png')
    FUNC = Coin(currency='FUNC', full_name='FunCoin', id='FUNC', url='https://www.cryptocompare.com/media/1383739/func.png')
    PQT = Coin(currency='PQT', full_name='PAquarium', id='PQT', url='https://www.cryptocompare.com/media/1383741/pqt.png')
    WTT = Coin(currency='WTT', full_name='Giga Watt', id='WTT', url='https://www.cryptocompare.com/media/1383742/wtt.png')
    MTL = Coin(currency='MTL', full_name='Metal', id='MTL', url='https://www.cryptocompare.com/media/1383743/mtl.png')
    HVN = Coin(currency='HVN', full_name='Hiveterminal Token', id='HVN', url='https://www.cryptocompare.com/media/1383745/hvt.png')
    MYB = Coin(currency='MYB', full_name='MyBit', id='MYB', url='https://www.cryptocompare.com/media/35308849/mybit.png')
    PPT = Coin(currency='PPT', full_name='Populous', id='PPT', url='https://www.cryptocompare.com/media/1383747/ppt.png')
    SNC = Coin(currency='SNC', full_name='SunContract', id='SNC', url='https://www.cryptocompare.com/media/1383748/snc.png')
    STAR = Coin(currency='STAR', full_name='Starbase', id='STAR', url='https://www.cryptocompare.com/media/1383750/star1.png')
    COR = Coin(currency='COR', full_name='Corion', id='COR', url='https://www.cryptocompare.com/media/1383753/cor.png')
    XRL = Coin(currency='XRL', full_name='Rialto.AI', id='XRL', url='https://www.cryptocompare.com/media/1383754/xrl.png')
    OROC = Coin(currency='OROC', full_name='Orocrypt', id='OROC', url='https://www.cryptocompare.com/media/1383755/oroc.png')
    OAX = Coin(currency='OAX', full_name='OpenANX', id='OAX', url='https://www.cryptocompare.com/media/1383756/oax.png')
    MBI = Coin(currency='MBI', full_name='Monster Byte Inc', id='MBI', url='https://www.cryptocompare.com/media/1383759/mbi.png')
    DDF = Coin(currency='DDF', full_name='Digital Developers Fund', id='DDF', url='https://www.cryptocompare.com/media/1383760/ddf.png')
    DIM = Coin(currency='DIM', full_name='DIMCOIN', id='DIM', url='https://www.cryptocompare.com/media/1383761/dim.png')
    GGS = Coin(currency='GGS', full_name='Gilgam', id='GGS', url='https://www.cryptocompare.com/media/1383762/ggs.png')
    DNA = Coin(currency='DNA', full_name='EncrypGen', id='DNA', url='https://www.cryptocompare.com/media/34155600/encrypgen-exchange-icon-300.png')
    FYN = Coin(currency='FYN', full_name='FundYourselfNow', id='FYN', url='https://www.cryptocompare.com/media/1383764/fyn.png')
    FND = Coin(currency='FND', full_name='FundRequest', id='FND', url='https://www.cryptocompare.com/media/1383765/fnd.png')
    DCY = Coin(currency='DCY', full_name='Dinastycoin', id='DCY', url='https://www.cryptocompare.com/media/1383767/dcy.png')
    CFT = Coin(currency='CFT', full_name='CryptoForecast', id='CFT', url='https://www.cryptocompare.com/media/1383769/cft.png')
    DNR = Coin(currency='DNR', full_name='Denarius', id='DNR', url='https://www.cryptocompare.com/media/1383770/dnr.png')
    DP = Coin(currency='DP', full_name='DigitalPrice', id='DP', url='https://www.cryptocompare.com/media/1383772/dp.png')
    VUC = Coin(currency='VUC', full_name='Virta Unique Coin', id='VUC', url='https://www.cryptocompare.com/media/1383773/vuc.png')
    BTPL = Coin(currency='BTPL', full_name='Bitcoin Planet', id='BTPL', url='https://www.cryptocompare.com/media/1383774/btpl.png')
    UNIFY = Coin(currency='UNIFY', full_name='Unify', id='UNIFY', url='https://www.cryptocompare.com/media/1383775/unify.png')
    IPC = Coin(currency='IPC', full_name='ImperialCoin', id='IPC', url='https://www.cryptocompare.com/media/1383776/ipc.png')
    BRIT = Coin(currency='BRIT', full_name='BritCoin', id='BRIT', url='https://www.cryptocompare.com/media/1383777/brit.png')
    AMMO = Coin(currency='AMMO', full_name='Ammo Rewards', id='AMMO', url='https://www.cryptocompare.com/media/1383778/ammo.png')
    SOCC = Coin(currency='SOCC', full_name='SocialCoin', id='SOCC', url='https://www.cryptocompare.com/media/1383779/socc.png')
    MASS = Coin(currency='MASS', full_name='Mass.Cloud', id='MASS', url='https://www.cryptocompare.com/media/1383781/mass.png')
    LA = Coin(currency='LA', full_name='LATOKEN', id='LA', url='https://www.cryptocompare.com/media/27010681/latoken.png')
    IML = Coin(currency='IML', full_name='IMMLA', id='IML', url='https://www.cryptocompare.com/media/1383783/iml.png')
    XUC = Coin(currency='XUC', full_name='Exchange Union', id='XUC', url='https://www.cryptocompare.com/media/1383784/xuc.png')
    STU = Coin(currency='STU', full_name='BitJob', id='STU', url='https://www.cryptocompare.com/media/1383785/stu.png')
    PLR = Coin(currency='PLR', full_name='Pillar', id='PLR', url='https://www.cryptocompare.com/media/27010510/plr.png')
    GUNS = Coin(currency='GUNS', full_name='GeoFunders', id='GUNS', url='https://www.cryptocompare.com/media/1383789/guns.png')
    IFT = Coin(currency='IFT', full_name='InvestFeed', id='IFT', url='https://www.cryptocompare.com/media/12318127/ift.png')
    PRO = Coin(currency='PRO', full_name='Propy', id='PRO', url='https://www.cryptocompare.com/media/1383792/pro.png')
    SYC = Coin(currency='SYC', full_name='SynchroCoin', id='SYC', url='https://www.cryptocompare.com/media/1383793/syc.png')
    IND = Coin(currency='IND', full_name='Indorse', id='IND', url='https://www.cryptocompare.com/media/1383794/ind.png')
    TRIBE = Coin(currency='TRIBE', full_name='TribeToken', id='TRIBE', url='https://www.cryptocompare.com/media/1383797/tribe.jpg')
    ZRX = Coin(currency='ZRX', full_name='0x', id='ZRX', url='https://www.cryptocompare.com/media/1383799/zrx.png')
    TNT = Coin(currency='TNT', full_name='Tierion', id='TNT', url='https://www.cryptocompare.com/media/1383800/tnt.png')
    COSS = Coin(currency='COSS', full_name='COSS', id='COSS', url='https://www.cryptocompare.com/media/1383802/coss.png')
    STORM = Coin(currency='STORM', full_name='Storm', id='STORM', url='https://www.cryptocompare.com/media/1383803/storm.jpg')
    NPX = Coin(currency='NPX', full_name='Napoleon X', id='NPX', url='https://www.cryptocompare.com/media/12318066/npx.png')
    STORJ = Coin(currency='STORJ', full_name='Storj', id='STORJ', url='https://www.cryptocompare.com/media/20422/sjcx.png')
    SCORE = Coin(currency='SCORE', full_name='Scorecoin', id='SCORE', url='https://www.cryptocompare.com/media/1383813/score.png')
    OMG = Coin(currency='OMG', full_name='OmiseGo', id='OMG', url='https://www.cryptocompare.com/media/1383814/omisego.png')
    OTX = Coin(currency='OTX', full_name='Octanox', id='OTX', url='https://www.cryptocompare.com/media/1383817/1qrfuod6_400x400.jpg')
    EQB = Coin(currency='EQB', full_name='Equibit', id='EQB', url='https://www.cryptocompare.com/media/1383816/eqb.png')
    VOISE = Coin(currency='VOISE', full_name='Voise', id='VOISE', url='https://www.cryptocompare.com/media/12318263/voise.png')
    ETBS = Coin(currency='ETBS', full_name='EthBits', id='ETBS', url='https://www.cryptocompare.com/media/12318348/etbs.png')
    CVCOIN = Coin(currency='CVCOIN', full_name='Crypviser', id='CVCOIN', url='https://www.cryptocompare.com/media/1383821/cvcoin.png')
    DRP = Coin(currency='DRP', full_name='DCORP', id='DRP', url='https://www.cryptocompare.com/media/1383822/drp.png')
    ARC = Coin(currency='ARC', full_name='ArcticCoin', id='ARC', url='https://www.cryptocompare.com/media/1383824/arc.png')
    BOG = Coin(currency='BOG', full_name='Bogcoin', id='BOG', url='https://www.cryptocompare.com/media/1383826/bog.png')
    NDC = Coin(currency='NDC', full_name='NeverDie', id='NDC', url='https://www.cryptocompare.com/media/1383827/ndc.png')
    POE = Coin(currency='POE', full_name='Po.et', id='POE', url='https://www.cryptocompare.com/media/1383828/poe.png')
    ADT = Coin(currency='ADT', full_name='AdToken', id='ADT', url='https://www.cryptocompare.com/media/1383829/adt.png')
    AE = Coin(currency='AE', full_name='Aeternity', id='AE', url='https://www.cryptocompare.com/media/1383836/ae.png')
    UET = Coin(currency='UET', full_name='Useless Ethereum Token', id='UET', url='https://www.cryptocompare.com/media/1383837/uet.png')
    AGRS = Coin(currency='AGRS', full_name='Agoras Token', id='AGRS', url='https://www.cryptocompare.com/media/1383839/agrs.png')
    SAND = Coin(currency='SAND', full_name='BeachCoin', id='SAND', url='https://www.cryptocompare.com/media/1383825/beach.png')
    DMT = Coin(currency='DMT', full_name='DMarket', id='DMT', url='https://www.cryptocompare.com/media/1383841/dmarket.png')
    DAS = Coin(currency='DAS', full_name='DAS', id='DAS', url='https://www.cryptocompare.com/media/14543970/das.png')
    ADST = Coin(currency='ADST', full_name='Adshares', id='ADST', url='https://www.cryptocompare.com/media/1383846/adst.png')
    BCAT = Coin(currency='BCAT', full_name='BlockCAT', id='BCAT', url='https://www.cryptocompare.com/media/1383848/bcat1.png')
    XCJ = Coin(currency='XCJ', full_name='CoinJob', id='XCJ', url='https://www.cryptocompare.com/media/1383849/xcj.png')
    RKC = Coin(currency='RKC', full_name='Royal Kingdom Coin', id='RKC', url='https://www.cryptocompare.com/media/1383852/rkc.png')
    NLC2 = Coin(currency='NLC2', full_name='NoLimitCoin', id='NLC2', url='https://www.cryptocompare.com/media/16746543/nlc2.png')
    LINDA = Coin(currency='LINDA', full_name='Linda', id='LINDA', url='https://www.cryptocompare.com/media/1383860/linda.png')
    KING = Coin(currency='KING', full_name='King93', id='KING', url='https://www.cryptocompare.com/media/1383862/king.png')
    ANCP = Coin(currency='ANCP', full_name='Anacrypt', id='ANCP', url='https://www.cryptocompare.com/media/1383863/ancp.png')
    RCC = Coin(currency='RCC', full_name='Reality Clash', id='RCC', url='https://www.cryptocompare.com/media/1383864/rcc.png')
    ROOTS = Coin(currency='ROOTS', full_name='RootProject', id='ROOTS', url='https://www.cryptocompare.com/media/1383851/roots.png')
    SNK = Coin(currency='SNK', full_name='Sosnovkino', id='SNK', url='https://www.cryptocompare.com/media/1383865/snk.png')
    CABS = Coin(currency='CABS', full_name='CryptoABS', id='CABS', url='https://www.cryptocompare.com/media/1383869/cabs.png')
    OPT = Coin(currency='OPT', full_name='Opus', id='OPT', url='https://www.cryptocompare.com/media/1383873/opt.png')
    ZNT = Coin(currency='ZNT', full_name='OpenZen', id='ZNT', url='https://www.cryptocompare.com/media/1383875/znt.png')
    BITSD = Coin(currency='BITSD', full_name='Bits Digit', id='BITSD', url='https://www.cryptocompare.com/media/1383878/bitsd.png')
    XLC = Coin(currency='XLC', full_name='LeviarCoin', id='XLC', url='https://www.cryptocompare.com/media/34333433/xlc.png')
    SKIN = Coin(currency='SKIN', full_name='Skincoin', id='SKIN', url='https://www.cryptocompare.com/media/1383880/dsb_amky_400x400.jpg')
    MSP = Coin(currency='MSP', full_name='Mothership', id='MSP', url='https://www.cryptocompare.com/media/1383881/c9fobrlr_400x400.jpg')
    HIRE = Coin(currency='HIRE', full_name='HireMatch', id='HIRE', url='https://www.cryptocompare.com/media/1383882/hite.png')
    REAL = Coin(currency='REAL', full_name='REAL', id='REAL', url='https://www.cryptocompare.com/media/1383884/rise.png')
    DFBT = Coin(currency='DFBT', full_name='DentalFix', id='DFBT', url='https://www.cryptocompare.com/media/1383890/dfbt.png')
    EQ = Coin(currency='EQ', full_name='EQUI', id='EQ', url='https://www.cryptocompare.com/media/1383891/eq.png')
    WLK = Coin(currency='WLK', full_name='Wolk', id='WLK', url='https://www.cryptocompare.com/media/1383892/wolk.png')
    VIB = Coin(currency='VIB', full_name='Viberate', id='VIB', url='https://www.cryptocompare.com/media/1383893/vib.png')
    ONION = Coin(currency='ONION', full_name='DeepOnion', id='ONION', url='https://www.cryptocompare.com/media/35521000/onion.png')
    BTX = Coin(currency='BTX', full_name='Bitcore', id='BTX', url='https://www.cryptocompare.com/media/1383895/btx.png')
    ICE = Coin(currency='ICE', full_name='iDice', id='ICE', url='https://www.cryptocompare.com/media/1383896/46b-uaba_400x400.jpg')
    XID = Coin(currency='XID', full_name='Sphre AIR', id='XID', url='https://www.cryptocompare.com/media/1383898/xid.jpg')
    GCN = Coin(currency='GCN', full_name='gCn Coin', id='GCN', url='https://www.cryptocompare.com/media/1383899/gcn.png')
    MANA = Coin(currency='MANA', full_name='Decentraland', id='MANA', url='https://www.cryptocompare.com/media/1383903/mana.png')
    ICOO = Coin(currency='ICOO', full_name='ICO OpenLedger', id='ICOO', url='https://www.cryptocompare.com/media/1383904/icoo.jpg')
    TME = Coin(currency='TME', full_name='Timereum', id='TME', url='https://www.cryptocompare.com/media/1383905/tme.png')
    SMART = Coin(currency='SMART', full_name='SmartCash', id='SMART', url='https://www.cryptocompare.com/media/34477887/smart2.png')
    SIGT = Coin(currency='SIGT', full_name='Signatum', id='SIGT', url='https://www.cryptocompare.com/media/9350710/sigt.png')
    ONX = Coin(currency='ONX', full_name='Onix', id='ONX', url='https://www.cryptocompare.com/media/1383910/onx.png')
    COE = Coin(currency='COE', full_name='CoEval', id='COE', url='https://www.cryptocompare.com/media/1383911/coe.png')
    ARENA = Coin(currency='ARENA', full_name='Arena', id='ARENA', url='https://www.cryptocompare.com/media/34478444/arena.png')
    WINK = Coin(currency='WINK', full_name='Wink', id='WINK', url='https://www.cryptocompare.com/media/1383913/wink.png')
    CRM = Coin(currency='CRM', full_name='Cream', id='CRM', url='https://www.cryptocompare.com/media/1383915/cream.png')
    DGPT = Coin(currency='DGPT', full_name='DigiPulse', id='DGPT', url='https://www.cryptocompare.com/media/1383920/dgt.png')
    MOBI = Coin(currency='MOBI', full_name='Mobius', id='MOBI', url='https://www.cryptocompare.com/media/1383921/mobi.png')
    CSNO = Coin(currency='CSNO', full_name='BitDice', id='CSNO', url='https://www.cryptocompare.com/media/1383922/csno.png')
    KICK = Coin(currency='KICK', full_name='KickCoin', id='KICK', url='https://www.cryptocompare.com/media/1383929/kick.png')
    SDAO = Coin(currency='SDAO', full_name='Solar DAO', id='SDAO', url='https://www.cryptocompare.com/media/1383933/sdao.png')
    STX = Coin(currency='STX', full_name='Stox', id='STX', url='https://www.cryptocompare.com/media/1383946/stx.png')
    BNB = Coin(currency='BNB', full_name='Binance Coin', id='BNB', url='https://www.cryptocompare.com/media/1383947/bnb.png')
    CORE = Coin(currency='CORE', full_name='Core Group Asset', id='CORE', url='https://www.cryptocompare.com/media/1383950/core.png')
    KEN = Coin(currency='KEN', full_name='Kencoin', id='KEN', url='https://www.cryptocompare.com/media/1383953/kencoin.png')
    QVT = Coin(currency='QVT', full_name='Qvolta', id='QVT', url='https://www.cryptocompare.com/media/1383954/qvt.png')
    TIE = Coin(currency='TIE', full_name='Ties Network', id='TIE', url='https://www.cryptocompare.com/media/1383955/tie.png')
    AUT = Coin(currency='AUT', full_name='Autoria', id='AUT', url='https://www.cryptocompare.com/media/1383956/aut.png')
    CTT = Coin(currency='CTT', full_name='CodeTract', id='CTT', url='https://www.cryptocompare.com/media/1383957/ctt.png')
    GRWI = Coin(currency='GRWI', full_name='Growers International', id='GRWI', url='https://www.cryptocompare.com/media/1383971/grwi.png')
    MNY = Coin(currency='MNY', full_name='Monkey', id='MNY', url='https://www.cryptocompare.com/media/1383973/mny.png')
    MTH = Coin(currency='MTH', full_name='Monetha', id='MTH', url='https://www.cryptocompare.com/media/1383976/mth.png')
    CCC = Coin(currency='CCC', full_name='CCCoin', id='CCC', url='https://www.cryptocompare.com/media/1383980/ccc.png')
    UMC = Coin(currency='UMC', full_name='Umbrella Coin', id='UMC', url='https://www.cryptocompare.com/media/1383983/umb.png')
    BMXT = Coin(currency='BMXT', full_name='Bitmxittz', id='BMXT', url='https://www.cryptocompare.com/media/1383984/bmxt.png')
    GAS = Coin(currency='GAS', full_name='Gas', id='GAS', url='https://www.cryptocompare.com/media/1383858/neo.jpg')
    FIL = Coin(currency='FIL', full_name='FileCoin', id='FIL', url='https://www.cryptocompare.com/media/1383987/fil.png')
    OCL = Coin(currency='OCL', full_name='Oceanlab', id='OCL', url='https://www.cryptocompare.com/media/1383989/ocl.png')
    BNC = Coin(currency='BNC', full_name='Benjacoin', id='BNC', url='https://www.cryptocompare.com/media/1383991/bnc.png')
    TOM = Coin(currency='TOM', full_name='Tomahawkcoin', id='TOM', url='https://www.cryptocompare.com/media/1383992/tom.png')
    XAS = Coin(currency='XAS', full_name='Asch', id='XAS', url='https://www.cryptocompare.com/media/1383997/xas.png')
    SMNX = Coin(currency='SMNX', full_name='SMNX', id='SMNX', url='https://www.cryptocompare.com/media/1383998/sx.png')
    DCN = Coin(currency='DCN', full_name='Dentacoin', id='DCN', url='https://www.cryptocompare.com/media/1383999/dcn.png')
    DLT = Coin(currency='DLT', full_name='Agrello Delta', id='DLT', url='https://www.cryptocompare.com/media/1384001/delta.png')
    MRV = Coin(currency='MRV', full_name='Macroverse', id='MRV', url='https://www.cryptocompare.com/media/1384009/mrv.png')
    MBRS = Coin(currency='MBRS', full_name='Embers', id='MBRS', url='https://www.cryptocompare.com/media/1384010/mbrs.png')
    SUB = Coin(currency='SUB', full_name='Substratum Network', id='SUB', url='https://www.cryptocompare.com/media/1384011/sub1.png')
    MET = Coin(currency='MET', full_name='Memessenger', id='MET', url='https://www.cryptocompare.com/media/1384013/met1.png')
    NEBL = Coin(currency='NEBL', full_name='Neblio', id='NEBL', url='https://www.cryptocompare.com/media/1384016/nebl.png')
    PGL = Coin(currency='PGL', full_name='Prospectors', id='PGL', url='https://www.cryptocompare.com/media/1384018/pgl.png')
    XMCC = Coin(currency='XMCC', full_name='Monoeci', id='XMCC', url='https://www.cryptocompare.com/media/27010930/xmcc.jpg')
    AUN = Coin(currency='AUN', full_name='Authoreon', id='AUN', url='https://www.cryptocompare.com/media/1384019/auth.png')
    CMPCO = Coin(currency='CMPCO', full_name='CampusCoin', id='CMPCO', url='https://www.cryptocompare.com/media/1384036/cmpo.png')
    DTCT = Coin(currency='DTCT', full_name='DetectorToken', id='DTCT', url='https://www.cryptocompare.com/media/1384025/dtct.png')
    CTR = Coin(currency='CTR', full_name='Centra', id='CTR', url='https://www.cryptocompare.com/media/1384029/ctr.png')
    WNET = Coin(currency='WNET', full_name='Wavesnode.net', id='WNET', url='https://www.cryptocompare.com/media/1383982/wnet1.png')
    PRG = Coin(currency='PRG', full_name='Paragon', id='PRG', url='https://www.cryptocompare.com/media/1384033/prg.png')
    THNX = Coin(currency='THNX', full_name='ThankYou', id='THNX', url='https://www.cryptocompare.com/media/1384039/thnx.jpg')
    WORM = Coin(currency='WORM', full_name='HealthyWorm', id='WORM', url='https://www.cryptocompare.com/media/1384040/worm.png')
    FUCK = Coin(currency='FUCK', full_name='Fuck Token', id='FUCK', url='https://www.cryptocompare.com/media/1384043/fuck.png')
    VNT = Coin(currency='VNT', full_name='Veredictum', id='VNT', url='https://www.cryptocompare.com/media/1384015/vent.png')
    SIFT = Coin(currency='SIFT', full_name='Smart Investment Fund Token', id='SIFT', url='https://www.cryptocompare.com/media/1384045/sift.jpg')
    IGNIS = Coin(currency='IGNIS', full_name='Ignis', id='IGNIS', url='https://www.cryptocompare.com/media/1384046/ignis.png')
    IWT = Coin(currency='IWT', full_name='IwToken', id='IWT', url='https://www.cryptocompare.com/media/1384048/iwt.png')
    JDC = Coin(currency='JDC', full_name='JustDatingSite', id='JDC', url='https://www.cryptocompare.com/media/1384049/jdc.png')
    ITT = Coin(currency='ITT', full_name='Intelligent Trading', id='ITT', url='https://www.cryptocompare.com/media/33957371/itt_new.jpg')
    LNC = Coin(currency='LNC', full_name='BlockLancer', id='LNC', url='https://www.cryptocompare.com/media/20780792/lnc.png')
    AIX = Coin(currency='AIX', full_name='Aigang', id='AIX', url='https://www.cryptocompare.com/media/1383807/aig.png')
    EVX = Coin(currency='EVX', full_name='Everex', id='EVX', url='https://www.cryptocompare.com/media/1383850/evx.png')
    XEC = Coin(currency='XEC', full_name='Eternal Coin', id='XEC', url='https://www.cryptocompare.com/media/30001868/xec.png')
    ENTRP = Coin(currency='ENTRP', full_name='Entropy Token', id='ENTRP', url='https://www.cryptocompare.com/media/1383969/ent.png')
    ICOS = Coin(currency='ICOS', full_name='ICOBox', id='ICOS', url='https://www.cryptocompare.com/media/1383968/icos1.png')
    PIX = Coin(currency='PIX', full_name='Lampix', id='PIX', url='https://www.cryptocompare.com/media/1384024/pix.png')
    MEDI = Coin(currency='MEDI', full_name='MediBond', id='MEDI', url='https://www.cryptocompare.com/media/1384051/medi.png')
    HGT = Coin(currency='HGT', full_name='Hello Gold', id='HGT', url='https://www.cryptocompare.com/media/9350692/hgt.jpg')
    LTA = Coin(currency='LTA', full_name='Litra', id='LTA', url='https://www.cryptocompare.com/media/9350693/lta.png')
    NIMFA = Coin(currency='NIMFA', full_name='Nimfamoney', id='NIMFA', url='https://www.cryptocompare.com/media/9350694/nimfa.jpg')
    SCOR = Coin(currency='SCOR', full_name='Scorista', id='SCOR', url='https://www.cryptocompare.com/media/9350695/scor.jpg')
    MLS = Coin(currency='MLS', full_name='CPROP', id='MLS', url='https://www.cryptocompare.com/media/9350696/mls.png')
    KEX = Coin(currency='KEX', full_name='KexCoin', id='KEX', url='https://www.cryptocompare.com/media/9350699/kex.png')
    COB = Coin(currency='COB', full_name='Cobinhood', id='COB', url='https://www.cryptocompare.com/media/9350700/cobin.png')
    BRO = Coin(currency='BRO', full_name='Bitradio', id='BRO', url='https://www.cryptocompare.com/media/9350701/bro.png')
    MINEX = Coin(currency='MINEX', full_name='Minex', id='MINEX', url='https://www.cryptocompare.com/media/9350702/minex.png')
    ATL = Coin(currency='ATL', full_name='ATLANT', id='ATL', url='https://www.cryptocompare.com/media/9350703/atlant.png')
    DFT = Coin(currency='DFT', full_name='Draftcoin', id='DFT', url='https://www.cryptocompare.com/media/9350712/dft.png')
    VET = Coin(currency='VET', full_name='Vechain', id='VET', url='https://www.cryptocompare.com/media/12318129/ven.png')
    UTK = Coin(currency='UTK', full_name='Utrust', id='UTK', url='https://www.cryptocompare.com/media/9350717/utrust.png')
    LAT = Coin(currency='LAT', full_name='Latium', id='LAT', url='https://www.cryptocompare.com/media/9350724/lat.png')
    SOJ = Coin(currency='SOJ', full_name='Sojourn Coin', id='SOJ', url='https://www.cryptocompare.com/media/9350725/soj.png')
    HDG = Coin(currency='HDG', full_name='Hedge Token', id='HDG', url='https://www.cryptocompare.com/media/9350726/hdg.png')
    STCN = Coin(currency='STCN', full_name='Stakecoin', id='STCN', url='https://www.cryptocompare.com/media/9350727/stcn.png')
    SQP = Coin(currency='SQP', full_name='SqPay', id='SQP', url='https://www.cryptocompare.com/media/9350728/sqp.png')
    RIYA = Coin(currency='RIYA', full_name='Etheriya', id='RIYA', url='https://www.cryptocompare.com/media/9350737/riya.png')
    LNK = Coin(currency='LNK', full_name='Ethereum.Link', id='LNK', url='https://www.cryptocompare.com/media/9350738/lnk.png')
    AMB = Coin(currency='AMB', full_name='Ambrosus', id='AMB', url='https://www.cryptocompare.com/media/9350739/amb.png')
    MNTP = Coin(currency='MNTP', full_name='GoldMint', id='MNTP', url='https://www.cryptocompare.com/media/9350745/mntp.png')
    ALTOCAR = Coin(currency='ALTOCAR', full_name='AltoCar', id='ALTOCAR', url='https://www.cryptocompare.com/media/9350746/altc.png')
    BLX = Coin(currency='BLX', full_name='Blockchain Index', id='BLX', url='https://www.cryptocompare.com/media/9350748/blx.png')
    BKX = Coin(currency='BKX', full_name='BANKEX', id='BKX', url='https://www.cryptocompare.com/media/14913571/bkx.png')
    BOU = Coin(currency='BOU', full_name='Boulle', id='BOU', url='https://www.cryptocompare.com/media/9350750/bou.jpg')
    OXY = Coin(currency='OXY', full_name='Oxycoin', id='OXY', url='https://www.cryptocompare.com/media/9350753/oxy.png')
    AMT = Coin(currency='AMT', full_name='Acumen', id='AMT', url='https://www.cryptocompare.com/media/9350756/amt.jpg')
    GIM = Coin(currency='GIM', full_name='Gimli', id='GIM', url='https://www.cryptocompare.com/media/27010507/gim.png')
    NYC = Coin(currency='NYC', full_name='NewYorkCoin', id='NYC', url='https://www.cryptocompare.com/media/30001653/nyc.png')
    LBTC = Coin(currency='LBTC', full_name='LiteBitcoin', id='LBTC', url='https://www.cryptocompare.com/media/9350763/lbtc.png')
    FRAZ = Coin(currency='FRAZ', full_name='FrazCoin', id='FRAZ', url='https://www.cryptocompare.com/media/9350764/fraz.png')
    EMT = Coin(currency='EMT', full_name='EasyMine', id='EMT', url='https://www.cryptocompare.com/media/9350765/emt.png')
    GXC = Coin(currency='GXC', full_name='Gx Coin', id='GXC', url='https://www.cryptocompare.com/media/9350766/gxc.png')
    HBT = Coin(currency='HBT', full_name='Hubii Network', id='HBT', url='https://www.cryptocompare.com/media/9350768/hbt.png')
    KRONE = Coin(currency='KRONE', full_name='Kronecoin', id='KRONE', url='https://www.cryptocompare.com/media/9350770/krone.png')
    SRT = Coin(currency='SRT', full_name='Scrypto', id='SRT', url='https://www.cryptocompare.com/media/9350771/srt.png')
    AVA = Coin(currency='AVA', full_name='Avalon', id='AVA', url='https://www.cryptocompare.com/media/9350772/ava.png')
    BT = Coin(currency='BT', full_name='BuildTeam', id='BT', url='https://www.cryptocompare.com/media/9350775/bt.png')
    ACC = Coin(currency='ACC', full_name='AdCoin', id='ACC', url='https://www.cryptocompare.com/media/9350776/acc.jpg')
    Z2 = Coin(currency='Z2', full_name='Z2 Coin', id='Z2', url='https://www.cryptocompare.com/media/9350780/z2.png')
    LINX = Coin(currency='LINX', full_name='Linx', id='LINX', url='https://www.cryptocompare.com/media/9350783/linx.png')
    XCXT = Coin(currency='XCXT', full_name='CoinonatX', id='XCXT', url='https://www.cryptocompare.com/media/9350784/xcxt.png')
    BLAS = Coin(currency='BLAS', full_name='BlakeStar', id='BLAS', url='https://www.cryptocompare.com/media/25792611/blas.png')
    GOOD = Coin(currency='GOOD', full_name='GoodCoin', id='GOOD', url='https://www.cryptocompare.com/media/9350786/good.png')
    SCL = Coin(currency='SCL', full_name='Sociall', id='SCL', url='https://www.cryptocompare.com/media/27010947/untitled-1.png')
    TRV = Coin(currency='TRV', full_name='Travel Coin', id='TRV', url='https://www.cryptocompare.com/media/9350789/trv.png')
    CRTM = Coin(currency='CRTM', full_name='Cryptum', id='CRTM', url='https://www.cryptocompare.com/media/9350790/crtm.jpg')
    EON = Coin(currency='EON', full_name='Exscudo', id='EON', url='https://www.cryptocompare.com/media/9350791/eon.jpg')
    PST = Coin(currency='PST', full_name='Primas', id='PST', url='https://www.cryptocompare.com/media/9350792/pst.jpg')
    MTX = Coin(currency='MTX', full_name='Matryx', id='MTX', url='https://www.cryptocompare.com/media/9350793/mtx.png')
    PRIX = Coin(currency='PRIX', full_name='Privatix', id='PRIX', url='https://www.cryptocompare.com/media/33842954/300x300_logo_blue.png')
    CTX = Coin(currency='CTX', full_name='CarTaxi', id='CTX', url='https://www.cryptocompare.com/media/12318075/ctx1.png')
    ENJ = Coin(currency='ENJ', full_name='Enjin Coin', id='ENJ', url='https://www.cryptocompare.com/media/11417639/enjt.png')
    CNX = Coin(currency='CNX', full_name='Cryptonex', id='CNX', url='https://www.cryptocompare.com/media/11417632/cnx.png')
    DRC = Coin(currency='DRC', full_name='Dropcoin', id='DRC', url='https://www.cryptocompare.com/media/11417638/drp.png')
    FUEL = Coin(currency='FUEL', full_name='Etherparty', id='FUEL', url='https://www.cryptocompare.com/media/11999072/fuel.png')
    ACE = Coin(currency='ACE', full_name='TokenStars', id='ACE', url='https://www.cryptocompare.com/media/11999076/ace.png')
    WRC = Coin(currency='WRC', full_name='Worldcore', id='WRC', url='https://www.cryptocompare.com/media/11999078/wrc.png')
    WTC = Coin(currency='WTC', full_name='Waltonchain', id='WTC', url='https://www.cryptocompare.com/media/12317959/wtc.png')
    BRX = Coin(currency='BRX', full_name='Breakout Stake', id='BRX', url='https://www.cryptocompare.com/media/12317960/brx.png')
    UCASH = Coin(currency='UCASH', full_name='U.CASH', id='UCASH', url='https://www.cryptocompare.com/media/12317962/xuc.png')
    WRT = Coin(currency='WRT', full_name='WRTcoin', id='WRT', url='https://www.cryptocompare.com/media/12317963/wrt.png')
    ORME = Coin(currency='ORME', full_name='Ormeus Coin', id='ORME', url='https://www.cryptocompare.com/media/12317975/omes.png')
    DEEP = Coin(currency='DEEP', full_name='Deep Gold', id='DEEP', url='https://www.cryptocompare.com/media/12317976/deep.png')
    CCT = Coin(currency='CCT', full_name='Crystal Clear Token ', id='CCT', url='https://www.cryptocompare.com/media/12317979/cct1.png')
    WSH = Coin(currency='WSH', full_name='Wish Finance', id='WSH', url='https://www.cryptocompare.com/media/12317980/wish.png')
    ABC = Coin(currency='ABC', full_name='AB-Chain', id='ABC', url='https://www.cryptocompare.com/media/12318006/bac.png')
    PRP = Coin(currency='PRP', full_name='Papyrus', id='PRP', url='https://www.cryptocompare.com/media/12318007/prp.png')
    BMC = Coin(currency='BMC', full_name='Blackmoon Crypto', id='BMC', url='https://www.cryptocompare.com/media/12318008/bmc.png')
    PYN = Coin(currency='PYN', full_name='Paycentos', id='PYN', url='https://www.cryptocompare.com/media/12318033/pyn.png')
    KAPU = Coin(currency='KAPU', full_name='Kapu', id='KAPU', url='https://www.cryptocompare.com/media/12318035/logo_500x500.png')
    SENSE = Coin(currency='SENSE', full_name='Sense Token', id='SENSE', url='https://www.cryptocompare.com/media/12318034/sense.png')
    CAPP = Coin(currency='CAPP', full_name='Cappasity', id='CAPP', url='https://www.cryptocompare.com/media/35284311/capp.png')
    VEE = Coin(currency='VEE', full_name='BLOCKv', id='VEE', url='https://www.cryptocompare.com/media/12318044/vee.png')
    FC = Coin(currency='FC', full_name='Facecoin', id='FC', url='https://www.cryptocompare.com/media/12318045/fc.png')
    RCN = Coin(currency='RCN', full_name='Ripio', id='RCN', url='https://www.cryptocompare.com/media/12318046/rnc.png')
    NRN = Coin(currency='NRN', full_name='Doc.ai Neuron', id='NRN', url='https://www.cryptocompare.com/media/12318047/nrn.png')
    EVC = Coin(currency='EVC', full_name='Eventchain', id='EVC', url='https://www.cryptocompare.com/media/12318064/evc.png')
    LINK = Coin(currency='LINK', full_name='ChainLink', id='LINK', url='https://www.cryptocompare.com/media/35309382/link.png')
    WIZ = Coin(currency='WIZ', full_name='Crowdwiz', id='WIZ', url='https://www.cryptocompare.com/media/12318081/wiz.png')
    ATKN = Coin(currency='ATKN', full_name='A-Token', id='ATKN', url='https://www.cryptocompare.com/media/12318083/atkn.png')
    KNC = Coin(currency='KNC', full_name='Kyber Network', id='KNC', url='https://www.cryptocompare.com/media/12318084/knc.png')
    RUSTBITS = Coin(currency='RUSTBITS', full_name='Rustbits', id='RUSTBITS', url='https://www.cryptocompare.com/media/12318085/rustbits.png')
    REX = Coin(currency='REX', full_name='Imbrex', id='REX', url='https://www.cryptocompare.com/media/12318086/rex.png')
    ETHD = Coin(currency='ETHD', full_name='Ethereum Dark', id='ETHD', url='https://www.cryptocompare.com/media/12318087/ethd.png')
    SUMO = Coin(currency='SUMO', full_name='Sumokoin', id='SUMO', url='https://www.cryptocompare.com/media/27010696/sumo.png')
    TRX = Coin(currency='TRX', full_name='TRON', id='TRX', url='https://www.cryptocompare.com/media/34477805/trx.jpg')
    H2O = Coin(currency='H2O', full_name='Hydrominer', id='H2O', url='https://www.cryptocompare.com/media/12318092/h2o.png')
    TKT = Coin(currency='TKT', full_name='Crypto Tickets', id='TKT', url='https://www.cryptocompare.com/media/12318093/tkt.png')
    RHEA = Coin(currency='RHEA', full_name='Rhea', id='RHEA', url='https://www.cryptocompare.com/media/12318096/rhea.png')
    ART = Coin(currency='ART', full_name='Maecenas', id='ART', url='https://www.cryptocompare.com/media/12318097/art.png')
    DRT = Coin(currency='DRT', full_name='DomRaider', id='DRT', url='https://www.cryptocompare.com/media/12318099/drt.png')
    SNOV = Coin(currency='SNOV', full_name='Snovio', id='SNOV', url='https://www.cryptocompare.com/media/12318100/snov.png')
    DREAM = Coin(currency='DREAM', full_name='DreamTeam Token', id='DREAM', url='https://www.cryptocompare.com/media/12318109/dtt.png')
    MTN = Coin(currency='MTN', full_name='TrackNetToken', id='MTN', url='https://www.cryptocompare.com/media/12318118/mtn.png')
    STOCKBET = Coin(currency='STOCKBET', full_name='StockBet', id='STOCKBET', url='https://www.cryptocompare.com/media/12318119/stockbet.png')
    PLM = Coin(currency='PLM', full_name='Algo.Land', id='PLM', url='https://www.cryptocompare.com/media/12318124/plm.jpg')
    SALT = Coin(currency='SALT', full_name='Salt Lending', id='SALT', url='https://www.cryptocompare.com/media/9350744/salt.jpg')
    SND = Coin(currency='SND', full_name='Sandcoin', id='SND', url='https://www.cryptocompare.com/media/12318128/snd.png')
    XP = Coin(currency='XP', full_name='Experience Points', id='XP', url='https://www.cryptocompare.com/media/12318134/xp.png')
    LRC = Coin(currency='LRC', full_name='Loopring', id='LRC', url='https://www.cryptocompare.com/media/12318135/lrc.png')
    HSR = Coin(currency='HSR', full_name='Hshare', id='HSR', url='https://www.cryptocompare.com/media/12318137/hsr.png')
    GLA = Coin(currency='GLA', full_name='Gladius', id='GLA', url='https://www.cryptocompare.com/media/12318141/gla.png')
    ZNA = Coin(currency='ZNA', full_name='Zenome', id='ZNA', url='https://www.cryptocompare.com/media/12318142/zna.png')
    EZM = Coin(currency='EZM', full_name='EZMarket', id='EZM', url='https://www.cryptocompare.com/media/12318143/ezm.png')
    ODN = Coin(currency='ODN', full_name='Obsidian', id='ODN', url='https://www.cryptocompare.com/media/12318145/odn.png')
    POLL = Coin(currency='POLL', full_name='ClearPoll', id='POLL', url='https://www.cryptocompare.com/media/12318144/poll.png')
    MTK = Coin(currency='MTK', full_name='Moya Token', id='MTK', url='https://www.cryptocompare.com/media/12318149/mtk.png')
    CAS = Coin(currency='CAS', full_name='Cashaa', id='CAS', url='https://www.cryptocompare.com/media/12318148/cas.png')
    MAT = Coin(currency='MAT', full_name='MiniApps', id='MAT', url='https://www.cryptocompare.com/media/12318162/mat.png')
    GJC = Coin(currency='GJC', full_name='Global Jobcoin', id='GJC', url='https://www.cryptocompare.com/media/12318166/gjc.png')
    WIC = Coin(currency='WIC', full_name='Wi Coin', id='WIC', url='https://www.cryptocompare.com/media/12318168/ocfkmb0t_400x400.jpg')
    WEB = Coin(currency='WEB', full_name='Webcoin', id='WEB', url='https://www.cryptocompare.com/media/12318169/web.png')
    WAND = Coin(currency='WAND', full_name='WandX', id='WAND', url='https://www.cryptocompare.com/media/12318182/wandxlogo_new1.png')
    ELIX = Coin(currency='ELIX', full_name='Elixir', id='ELIX', url='https://www.cryptocompare.com/media/12318172/elix.png')
    EBTC = Coin(currency='EBTC', full_name='eBitcoin', id='EBTC', url='https://www.cryptocompare.com/media/12318175/ebtc.png')
    HAC = Coin(currency='HAC', full_name='Hackspace Capital', id='HAC', url='https://www.cryptocompare.com/media/12318176/hac.jpg')
    ADA = Coin(currency='ADA', full_name='Cardano', id='ADA', url='https://www.cryptocompare.com/media/12318177/ada.png')
    YOYOW = Coin(currency='YOYOW', full_name='Yoyow', id='YOYOW', url='https://www.cryptocompare.com/media/12318178/yoyow.png')
    REC = Coin(currency='REC', full_name='Regalcoin', id='REC', url='https://www.cryptocompare.com/media/12318179/rec.png')
    BIS = Coin(currency='BIS', full_name='Bismuth', id='BIS', url='https://www.cryptocompare.com/media/35309411/bis.png')
    OPP = Coin(currency='OPP', full_name='Opporty', id='OPP', url='https://www.cryptocompare.com/media/12318188/opp.png')
    ROCK2 = Coin(currency='ROCK2', full_name='Ice Rock Mining', id='ROCK2', url='https://www.cryptocompare.com/media/12318189/rock.png')
    EARTH = Coin(currency='EARTH', full_name='Earth Token', id='EARTH', url='https://www.cryptocompare.com/media/12318190/earth.png')
    ICX = Coin(currency='ICX', full_name='ICON Project', id='ICX', url='https://www.cryptocompare.com/media/12318192/icx.png')
    VSX = Coin(currency='VSX', full_name='Vsync', id='VSX', url='https://www.cryptocompare.com/media/12318194/vsx.png')
    FLASH = Coin(currency='FLASH', full_name='FLASH coin', id='FLASH', url='https://www.cryptocompare.com/media/35521172/flash.png')
    GRFT = Coin(currency='GRFT', full_name='Graft Blockchain', id='GRFT', url='https://www.cryptocompare.com/media/12318208/grf.png')
    BTCZ = Coin(currency='BTCZ', full_name='BitcoinZ', id='BTCZ', url='https://www.cryptocompare.com/media/12318408/btcz.png')
    CZC = Coin(currency='CZC', full_name='Crazy Coin', id='CZC', url='https://www.cryptocompare.com/media/12318215/czc.png')
    PPP = Coin(currency='PPP', full_name='PayPie', id='PPP', url='https://www.cryptocompare.com/media/12318216/ppp.png')
    GUESS = Coin(currency='GUESS', full_name='Peerguess', id='GUESS', url='https://www.cryptocompare.com/media/12318217/guess.png')
    CAN = Coin(currency='CAN', full_name='CanYaCoin', id='CAN', url='https://www.cryptocompare.com/media/12318218/canya.png')
    ETP = Coin(currency='ETP', full_name='Metaverse', id='ETP', url='https://www.cryptocompare.com/media/12318223/etp.png')
    CIX = Coin(currency='CIX', full_name='Cryptonetix', id='CIX', url='https://www.cryptocompare.com/media/12318222/cnxasterisco.png')
    ERT = Coin(currency='ERT', full_name='Esports.com', id='ERT', url='https://www.cryptocompare.com/media/12318226/ert.png')
    FLIK = Coin(currency='FLIK', full_name='FLiK', id='FLIK', url='https://www.cryptocompare.com/media/12318230/flik.png')
    TRIP = Coin(currency='TRIP', full_name='Trippki', id='TRIP', url='https://www.cryptocompare.com/media/12318231/trip.png')
    MBT = Coin(currency='MBT', full_name='Multibot', id='MBT', url='https://www.cryptocompare.com/media/12318238/mbt.png')
    ALIS = Coin(currency='ALIS', full_name='ALISmedia', id='ALIS', url='https://www.cryptocompare.com/media/12318247/alis.png')
    LEV = Coin(currency='LEV', full_name='Leverj', id='LEV', url='https://www.cryptocompare.com/media/12318249/lev.png')
    ARBI = Coin(currency='ARBI', full_name='Arbi', id='ARBI', url='https://www.cryptocompare.com/media/12318258/arbi.png')
    REQ = Coin(currency='REQ', full_name='Request Network', id='REQ', url='https://www.cryptocompare.com/media/12318260/req.png')
    ARN = Coin(currency='ARN', full_name='Aeron', id='ARN', url='https://www.cryptocompare.com/media/12318261/arn.png')
    DAT = Coin(currency='DAT', full_name='Datum', id='DAT', url='https://www.cryptocompare.com/media/12318265/dat.png')
    VIBE = Coin(currency='VIBE', full_name='VIBEHub', id='VIBE', url='https://www.cryptocompare.com/media/12318267/vibe.png')
    ROK = Coin(currency='ROK', full_name='Rockchain', id='ROK', url='https://www.cryptocompare.com/media/12318268/rok.png')
    XRED = Coin(currency='XRED', full_name='X Real Estate Development', id='XRED', url='https://www.cryptocompare.com/media/12318269/xred.png')
    DAY = Coin(currency='DAY', full_name='Chronologic', id='DAY', url='https://www.cryptocompare.com/media/12318271/day.png')
    AST = Coin(currency='AST', full_name='AirSwap', id='AST', url='https://www.cryptocompare.com/media/35309639/ast.png')
    FLP = Coin(currency='FLP', full_name='Gameflip', id='FLP', url='https://www.cryptocompare.com/media/12318280/flip.png')
    HXT = Coin(currency='HXT', full_name='HextraCoin', id='HXT', url='https://www.cryptocompare.com/media/12318282/hxt.png')
    CND = Coin(currency='CND', full_name='Cindicator', id='CND', url='https://www.cryptocompare.com/media/35309768/cnd.png')
    NTM = Coin(currency='NTM', full_name='NetM', id='NTM', url='https://www.cryptocompare.com/media/12318286/ntm.png')
    TZC = Coin(currency='TZC', full_name='TrezarCoin', id='TZC', url='https://www.cryptocompare.com/media/12318285/tzc.png')
    ENG = Coin(currency='ENG', full_name='Enigma', id='ENG', url='https://www.cryptocompare.com/media/12318287/eng.png')
    MCI = Coin(currency='MCI', full_name='Musiconomi', id='MCI', url='https://www.cryptocompare.com/media/12318289/mci.png')
    COV = Coin(currency='COV', full_name='Covesting', id='COV', url='https://www.cryptocompare.com/media/12318288/cov.png')
    WAX = Coin(currency='WAX', full_name='Worldwide Asset eXchange', id='WAX', url='https://www.cryptocompare.com/media/12318290/wax.png')
    AIR = Coin(currency='AIR', full_name='AirToken', id='AIR', url='https://www.cryptocompare.com/media/12318291/air.png')
    NTO = Coin(currency='NTO', full_name='Fujinto', id='NTO', url='https://www.cryptocompare.com/media/12318293/nto.png')
    ATCC = Coin(currency='ATCC', full_name='ATC Coin', id='ATCC', url='https://www.cryptocompare.com/media/12318294/atcc.png')
    KOLION = Coin(currency='KOLION', full_name='Kolion', id='KOLION', url='https://www.cryptocompare.com/media/12318295/kolion.png')
    WILD = Coin(currency='WILD', full_name='Wild Crypto', id='WILD', url='https://www.cryptocompare.com/media/12318298/wild.png')
    ELTC2 = Coin(currency='ELTC2', full_name='eLTC', id='ELTC2', url='https://www.cryptocompare.com/media/12318300/eltc2.png')
    ILCT = Coin(currency='ILCT', full_name='ILCoin Token', id='ILCT', url='https://www.cryptocompare.com/media/12318299/ilct.png')
    POWR = Coin(currency='POWR', full_name='Power Ledger', id='POWR', url='https://www.cryptocompare.com/media/12318301/powr.png')
    C20 = Coin(currency='C20', full_name='Crypto20', id='C20', url='https://www.cryptocompare.com/media/12318302/c20.png')
    RYZ = Coin(currency='RYZ', full_name='Anryze', id='RYZ', url='https://www.cryptocompare.com/media/12318305/ryz.png')
    ELM = Coin(currency='ELM', full_name='Elements', id='ELM', url='https://www.cryptocompare.com/media/12318308/elm.png')
    TER = Coin(currency='TER', full_name='TerraNovaCoin', id='TER', url='https://www.cryptocompare.com/media/12318324/ter.png')
    XCS = Coin(currency='XCS', full_name='CybCSec Coin', id='XCS', url='https://www.cryptocompare.com/media/12318323/xcs.png')
    BQ = Coin(currency='BQ', full_name='Bitqy', id='BQ', url='https://www.cryptocompare.com/media/12318325/bq.png')
    CAV = Coin(currency='CAV', full_name='Caviar', id='CAV', url='https://www.cryptocompare.com/media/12318328/cav.png')
    CLOUT = Coin(currency='CLOUT', full_name='Clout', id='CLOUT', url='https://www.cryptocompare.com/media/12318329/clout.png')
    WABI = Coin(currency='WABI', full_name='WaBi', id='WABI', url='https://www.cryptocompare.com/media/12318331/wabi.png')
    EVR = Coin(currency='EVR', full_name='Everus', id='EVR', url='https://www.cryptocompare.com/media/12318332/evr.png')
    TOA = Coin(currency='TOA', full_name='TOA Coin', id='TOA', url='https://www.cryptocompare.com/media/12318334/toacoin.png')
    MNZ = Coin(currency='MNZ', full_name='Monaize', id='MNZ', url='https://www.cryptocompare.com/media/12318336/mnz.png')
    VIVO = Coin(currency='VIVO', full_name='VIVO Coin', id='VIVO', url='https://www.cryptocompare.com/media/12318337/vivo.png')
    PHX = Coin(currency='PHX', full_name='Red Pulse Phoenix', id='PHX', url='https://www.cryptocompare.com/media/34478203/phx.png')
    MDA = Coin(currency='MDA', full_name='Moeda', id='MDA', url='https://www.cryptocompare.com/media/12318340/mda.png')
    ZSC = Coin(currency='ZSC', full_name='Zeusshield', id='ZSC', url='https://www.cryptocompare.com/media/12318341/zsc.png')
    AURS = Coin(currency='AURS', full_name='Aureus', id='AURS', url='https://www.cryptocompare.com/media/12318345/aurs.png')
    CAG = Coin(currency='CAG', full_name='Change', id='CAG', url='https://www.cryptocompare.com/media/25792623/cag1.png')
    PKT = Coin(currency='PKT', full_name='Playkey', id='PKT', url='https://www.cryptocompare.com/media/12318349/playkey.png')
    ECHT = Coin(currency='ECHT', full_name='e-Chat', id='ECHT', url='https://www.cryptocompare.com/media/12318352/echt.png')
    INXT = Coin(currency='INXT', full_name='Internxt', id='INXT', url='https://www.cryptocompare.com/media/12318355/inxt.png')
    ATS = Coin(currency='ATS', full_name='Authorship', id='ATS', url='https://www.cryptocompare.com/media/12318356/ats.png')
    RGC = Coin(currency='RGC', full_name='RG Coin', id='RGC', url='https://www.cryptocompare.com/media/12318357/rgc.png')
    EBET = Coin(currency='EBET', full_name='EthBet', id='EBET', url='https://www.cryptocompare.com/media/12318358/ebet.png')
    R = Coin(currency='R', full_name='Revain', id='R', url='https://www.cryptocompare.com/media/12318360/r.png')
    MOD = Coin(currency='MOD', full_name='Modum', id='MOD', url='https://www.cryptocompare.com/media/12318362/mod.png')
    CPAY = Coin(currency='CPAY', full_name='CryptoPay', id='CPAY', url='https://www.cryptocompare.com/media/12318303/cpay.png')
    RUP = Coin(currency='RUP', full_name='Rupee', id='RUP', url='https://www.cryptocompare.com/media/30001935/rup.png')
    APPC = Coin(currency='APPC', full_name='AppCoins', id='APPC', url='https://www.cryptocompare.com/media/12318370/app.png')
    WHL = Coin(currency='WHL', full_name='WhaleCoin', id='WHL', url='https://www.cryptocompare.com/media/12318372/whl.png')
    UP = Coin(currency='UP', full_name='UpToken', id='UP', url='https://www.cryptocompare.com/media/12318374/up.png')
    ETG = Coin(currency='ETG', full_name='Ethereum Gold', id='ETG', url='https://www.cryptocompare.com/media/12318378/etg.png')
    WOMEN = Coin(currency='WOMEN', full_name='WomenCoin', id='WOMEN', url='https://www.cryptocompare.com/media/12318379/women.png')
    MAY = Coin(currency='MAY', full_name='Theresa May Coin', id='MAY', url='https://www.cryptocompare.com/media/12318380/may.png')
    RNDR = Coin(currency='RNDR', full_name='Render Token', id='RNDR', url='https://www.cryptocompare.com/media/12318381/rndr.png')
    EDDIE = Coin(currency='EDDIE', full_name='Eddie coin', id='EDDIE', url='https://www.cryptocompare.com/media/12318382/eddie.png')
    NAMO = Coin(currency='NAMO', full_name='NamoCoin', id='NAMO', url='https://www.cryptocompare.com/media/12318384/namo.png')
    KCS = Coin(currency='KCS', full_name='Kucoin', id='KCS', url='https://www.cryptocompare.com/media/12318389/kcs.png')
    GAT = Coin(currency='GAT', full_name='GATCOIN', id='GAT', url='https://www.cryptocompare.com/media/12318390/gat.png')
    BLUE = Coin(currency='BLUE', full_name='Ethereum Blue', id='BLUE', url='https://www.cryptocompare.com/media/12318407/blue.png')
    FLLW = Coin(currency='FLLW', full_name='Follow Coin', id='FLLW', url='https://www.cryptocompare.com/media/12318412/fllw.png')
    WYR = Coin(currency='WYR', full_name='Wyrify', id='WYR', url='https://www.cryptocompare.com/media/12318413/wyr.png')
    VZT = Coin(currency='VZT', full_name='Vezt', id='VZT', url='https://www.cryptocompare.com/media/12318414/vzt.png')
    INDI = Coin(currency='INDI', full_name='IndiCoin', id='INDI', url='https://www.cryptocompare.com/media/12318419/indi.png')
    LUX = Coin(currency='LUX', full_name='LUXCoin', id='LUX', url='https://www.cryptocompare.com/media/12318422/lux.png')
    BAR = Coin(currency='BAR', full_name='TBIS token', id='BAR', url='https://www.cryptocompare.com/media/14543951/bar.png')
    PIRL = Coin(currency='PIRL', full_name='Pirl', id='PIRL', url='https://www.cryptocompare.com/media/34155614/pirl.png')
    ECASH = Coin(currency='ECASH', full_name='Ethereum Cash', id='ECASH', url='https://www.cryptocompare.com/media/14543971/ecash.png')
    WPR = Coin(currency='WPR', full_name='WePower', id='WPR', url='https://www.cryptocompare.com/media/14543969/wpr.png')
    DRGN = Coin(currency='DRGN', full_name='Dragonchain', id='DRGN', url='https://www.cryptocompare.com/media/16746490/drgn.png')
    ODMC = Coin(currency='ODMC', full_name='ODMCoin', id='ODMC', url='https://www.cryptocompare.com/media/14761889/odmcoin.png')
    BRAT = Coin(currency='BRAT', full_name='BROTHER', id='BRAT', url='https://www.cryptocompare.com/media/25792621/brat.png')
    DTR = Coin(currency='DTR', full_name='Dynamic Trading Rights', id='DTR', url='https://www.cryptocompare.com/media/14761903/dtr.png')
    TKR = Coin(currency='TKR', full_name='CryptoInsight', id='TKR', url='https://www.cryptocompare.com/media/14761909/tkr.png')
    KEY = Coin(currency='KEY', full_name='SelfKey', id='KEY', url='https://www.cryptocompare.com/media/14761912/key.png')
    ELITE = Coin(currency='ELITE', full_name='EthereumLite', id='ELITE', url='https://www.cryptocompare.com/media/14761914/elite.png')
    XIOS = Coin(currency='XIOS', full_name='Xios', id='XIOS', url='https://www.cryptocompare.com/media/14761915/xios.png')
    DOV = Coin(currency='DOV', full_name='DOVU', id='DOV', url='https://www.cryptocompare.com/media/14761916/dovu.png')
    ETN = Coin(currency='ETN', full_name='Electroneum', id='ETN', url='https://www.cryptocompare.com/media/14761932/electroneum.png')
    REA = Coin(currency='REA', full_name='Realisto', id='REA', url='https://www.cryptocompare.com/media/14761934/rea.png')
    AVE = Coin(currency='AVE', full_name='Avesta', id='AVE', url='https://www.cryptocompare.com/media/14761937/ave.png')
    XNN = Coin(currency='XNN', full_name='Xenon', id='XNN', url='https://www.cryptocompare.com/media/14761938/xnn.png')
    BTDX = Coin(currency='BTDX', full_name='Bitcloud 2.0', id='BTDX', url='https://www.cryptocompare.com/media/14761939/btdx.png')
    ZAB = Coin(currency='ZAB', full_name='ZABERcoin', id='ZAB', url='https://www.cryptocompare.com/media/14761946/zab.png')
    BT1 = Coin(currency='BT1', full_name='Bitfinex Bitcoin Future', id='BT1', url='https://www.cryptocompare.com/media/19633/btc.png')
    BT2 = Coin(currency='BT2', full_name='Bitcoin SegWit2X', id='BT2', url='https://www.cryptocompare.com/media/19633/btc.png')
    JCR = Coin(currency='JCR', full_name='Jincor', id='JCR', url='https://www.cryptocompare.com/media/14761952/jcr.png')
    XSB = Coin(currency='XSB', full_name='Extreme Sportsbook', id='XSB', url='https://www.cryptocompare.com/media/14761953/xbs.png')
    ATM = Coin(currency='ATM', full_name='ATMChain', id='ATM', url='https://www.cryptocompare.com/media/14913430/atm.png')
    EBST = Coin(currency='EBST', full_name='eBoost', id='EBST', url='https://www.cryptocompare.com/media/14913431/ebst.png')
    KEK = Coin(currency='KEK', full_name='KekCoin', id='KEK', url='https://www.cryptocompare.com/media/14913432/kek.png')
    AID = Coin(currency='AID', full_name='AidCoin', id='AID', url='https://www.cryptocompare.com/media/14913433/aidcoin.png')
    ALTCOM = Coin(currency='ALTCOM', full_name='AltCommunity Coin', id='ALTCOM', url='https://www.cryptocompare.com/media/14913436/altcom.png')
    OST = Coin(currency='OST', full_name='Simple Token', id='OST', url='https://www.cryptocompare.com/media/14913437/st.png')
    DATA = Coin(currency='DATA', full_name='Streamr DATAcoin', id='DATA', url='https://www.cryptocompare.com/media/30002338/data.png')
    UGC = Coin(currency='UGC', full_name='ugChain', id='UGC', url='https://www.cryptocompare.com/media/14913439/ugt.png')
    DTC = Coin(currency='DTC', full_name='Datacoin', id='DTC', url='https://www.cryptocompare.com/media/14913440/dtc.png')
    PLAY = Coin(currency='PLAY', full_name='HEROcoin', id='PLAY', url='https://www.cryptocompare.com/media/14913441/play.png')
    PURE = Coin(currency='PURE', full_name='Pure', id='PURE', url='https://www.cryptocompare.com/media/14913451/pure.png')
    CLD = Coin(currency='CLD', full_name='Cloud', id='CLD', url='https://www.cryptocompare.com/media/14913452/cld.png')
    OTN = Coin(currency='OTN', full_name='Open Trading Network', id='OTN', url='https://www.cryptocompare.com/media/14913453/otn.png')
    POS = Coin(currency='POS', full_name='PoSToken', id='POS', url='https://www.cryptocompare.com/media/14913455/pos.png')
    REBL = Coin(currency='REBL', full_name='REBL', id='REBL', url='https://www.cryptocompare.com/media/30001864/rebl1.jpg')
    NEOG = Coin(currency='NEOG', full_name='NEO Gold', id='NEOG', url='https://www.cryptocompare.com/media/14913457/neog.png')
    EXN = Coin(currency='EXN', full_name='ExchangeN', id='EXN', url='https://www.cryptocompare.com/media/14913459/exn.png')
    INS = Coin(currency='INS', full_name='Insolar', id='INS', url='https://www.cryptocompare.com/media/35264177/ins.jpg')
    TRCT = Coin(currency='TRCT', full_name='Tracto', id='TRCT', url='https://www.cryptocompare.com/media/14913462/trct.png')
    UKG = Coin(currency='UKG', full_name='UnikoinGold', id='UKG', url='https://www.cryptocompare.com/media/14913456/ukg.png')
    BTCRED = Coin(currency='BTCRED', full_name='Bitcoin Red', id='BTCRED', url='https://www.cryptocompare.com/media/14913463/btcred.png')
    CPEX = Coin(currency='CPEX', full_name='CoinPulseToken', id='CPEX', url='https://www.cryptocompare.com/media/34478354/cpex.png')
    JTX = Coin(currency='JTX', full_name='Project J', id='JTX', url='https://www.cryptocompare.com/media/14913466/jpc.png')
    AXT = Coin(currency='AXT', full_name='AIX', id='AXT', url='https://www.cryptocompare.com/media/14913467/axt.png')
    NEU = Coin(currency='NEU', full_name='Neumark', id='NEU', url='https://www.cryptocompare.com/media/14913483/neu.png')
    RUPX = Coin(currency='RUPX', full_name='Rupaya', id='RUPX', url='https://www.cryptocompare.com/media/34835666/rupaya.png')
    BDR = Coin(currency='BDR', full_name='BlueDragon', id='BDR', url='https://www.cryptocompare.com/media/14913485/bdr.png')
    XIN = Coin(currency='XIN', full_name='Infinity Economics', id='XIN', url='https://www.cryptocompare.com/media/30002029/xin.png')
    DUTCH = Coin(currency='DUTCH', full_name='Dutch Coin', id='DUTCH', url='https://www.cryptocompare.com/media/14913487/dutch.png')
    TIO = Coin(currency='TIO', full_name='Trade.io', id='TIO', url='https://www.cryptocompare.com/media/14913488/tio.png')
    PURA = Coin(currency='PURA', full_name='Pura', id='PURA', url='https://www.cryptocompare.com/media/14913533/pura.png')
    INN = Coin(currency='INN', full_name='Innova', id='INN', url='https://www.cryptocompare.com/media/14913536/inn.png')
    HST = Coin(currency='HST', full_name='Decision Token', id='HST', url='https://www.cryptocompare.com/media/34155557/horizonstate-logo_preview.png')
    BCPT = Coin(currency='BCPT', full_name='BlockMason Credit Protocol', id='BCPT', url='https://www.cryptocompare.com/media/16746476/bcpt.png')
    BDL = Coin(currency='BDL', full_name='Bitdeal', id='BDL', url='https://www.cryptocompare.com/media/14913539/bdl.png')
    CMS = Coin(currency='CMS', full_name='COMSA', id='CMS', url='https://www.cryptocompare.com/media/14913540/comsa.png')
    XBL = Coin(currency='XBL', full_name='Billionaire Token', id='XBL', url='https://www.cryptocompare.com/media/14913541/xbl.png')
    ZEPH = Coin(currency='ZEPH', full_name='ZEPHYR', id='ZEPH', url='https://www.cryptocompare.com/media/35309172/zphyr.png')
    ATFS = Coin(currency='ATFS', full_name='ATFS Project', id='ATFS', url='https://www.cryptocompare.com/media/14913545/atfs.png')
    GES = Coin(currency='GES', full_name='Galaxy eSolutions', id='GES', url='https://www.cryptocompare.com/media/14913547/ges.png')
    NULS = Coin(currency='NULS', full_name='Nuls', id='NULS', url='https://www.cryptocompare.com/media/14913548/nuls.png')
    LCASH = Coin(currency='LCASH', full_name='LitecoinCash', id='LCASH', url='https://www.cryptocompare.com/media/14913550/lcash.png')
    CFD = Coin(currency='CFD', full_name='Confido', id='CFD', url='https://www.cryptocompare.com/media/14913552/cfd.png')
    SPHTX = Coin(currency='SPHTX', full_name='SophiaTX', id='SPHTX', url='https://www.cryptocompare.com/media/14913551/sphtx.png')
    PLC = Coin(currency='PLC', full_name='PlusCoin', id='PLC', url='https://www.cryptocompare.com/media/14913555/plus.png')
    SRN = Coin(currency='SRN', full_name='SirinLabs', id='SRN', url='https://www.cryptocompare.com/media/14913556/srn.png')
    WSC = Coin(currency='WSC', full_name='WiserCoin', id='WSC', url='https://www.cryptocompare.com/media/14913560/wsc.png')
    DBET = Coin(currency='DBET', full_name='Decent.bet', id='DBET', url='https://www.cryptocompare.com/media/14913561/dbet.png')
    XGOX = Coin(currency='XGOX', full_name='Go!', id='XGOX', url='https://www.cryptocompare.com/media/14913685/xgox.png')
    NEWB = Coin(currency='NEWB', full_name='Newbium', id='NEWB', url='https://www.cryptocompare.com/media/14913564/newb.png')
    LIFE = Coin(currency='LIFE', full_name='LIFE', id='LIFE', url='https://www.cryptocompare.com/media/14913568/life.png')
    RMC = Coin(currency='RMC', full_name='Russian Mining Coin', id='RMC', url='https://www.cryptocompare.com/media/14913570/rmc.png')
    CREDO = Coin(currency='CREDO', full_name='Credo', id='CREDO', url='https://www.cryptocompare.com/media/14913573/credo-1.png')
    MSR = Coin(currency='MSR', full_name='Masari', id='MSR', url='https://www.cryptocompare.com/media/14913574/msr.png')
    CJT = Coin(currency='CJT', full_name='ConnectJob Token', id='CJT', url='https://www.cryptocompare.com/media/14913575/cjt.png')
    EVN = Coin(currency='EVN', full_name='Envion', id='EVN', url='https://www.cryptocompare.com/media/14913587/env.png')
    BNK = Coin(currency='BNK', full_name='Bankera', id='BNK', url='https://www.cryptocompare.com/media/14913602/bnk.png')
    ELLA = Coin(currency='ELLA', full_name='Ellaism', id='ELLA', url='https://www.cryptocompare.com/media/14913603/ella.png')
    BPL = Coin(currency='BPL', full_name='BlockPool', id='BPL', url='https://www.cryptocompare.com/media/14913604/bpl.png')
    COIN = Coin(currency='COIN', full_name='Coinvest', id='COIN', url='https://www.cryptocompare.com/media/14913606/coin.png')
    DRXNE = Coin(currency='DRXNE', full_name='Droxne', id='DRXNE', url='https://www.cryptocompare.com/media/14913608/drxne.png')
    SKR = Coin(currency='SKR', full_name='Sakuracoin', id='SKR', url='https://www.cryptocompare.com/media/14913631/skr.png')
    GRID = Coin(currency='GRID', full_name='Grid+', id='GRID', url='https://www.cryptocompare.com/media/14913632/grid.png')
    XPTX = Coin(currency='XPTX', full_name='PlatinumBAR', id='XPTX', url='https://www.cryptocompare.com/media/14913633/xptx.png')
    GVT = Coin(currency='GVT', full_name='Genesis Vision', id='GVT', url='https://www.cryptocompare.com/media/14913634/gvt.png')
    ETK = Coin(currency='ETK', full_name='Energi Token', id='ETK', url='https://www.cryptocompare.com/media/14913635/etk.png')
    ASTRO = Coin(currency='ASTRO', full_name='Astronaut', id='ASTRO', url='https://www.cryptocompare.com/media/14913641/astro.png')
    GMT = Coin(currency='GMT', full_name='Mercury Protocol', id='GMT', url='https://www.cryptocompare.com/media/14913642/gmt.png')
    SOAR = Coin(currency='SOAR', full_name='Soarcoin', id='SOAR', url='https://www.cryptocompare.com/media/14913644/soar.png')
    EXY = Coin(currency='EXY', full_name='Experty', id='EXY', url='https://www.cryptocompare.com/media/14913645/exy.png')
    ISH = Coin(currency='ISH', full_name='Interstellar Holdings', id='ISH', url='https://www.cryptocompare.com/media/14913647/hold.png')
    MNX = Coin(currency='MNX', full_name='MinexCoin', id='MNX', url='https://www.cryptocompare.com/media/14913648/mnx.png')
    CRDS = Coin(currency='CRDS', full_name='Credits', id='CRDS', url='https://www.cryptocompare.com/media/14913675/crds.png')
    VIU = Coin(currency='VIU', full_name='Viuly', id='VIU', url='https://www.cryptocompare.com/media/14913680/viu.png')
    DBR = Coin(currency='DBR', full_name='Düber', id='DBR', url='https://www.cryptocompare.com/media/14913687/dbr.png')
    GFT = Coin(currency='GFT', full_name='Giftcoin', id='GFT', url='https://www.cryptocompare.com/media/14913686/gft.jpg')
    STAC = Coin(currency='STAC', full_name='STAC', id='STAC', url='https://www.cryptocompare.com/media/27010495/stac1.png')
    QSP = Coin(currency='QSP', full_name='Quantstamp', id='QSP', url='https://www.cryptocompare.com/media/15887408/qsp.png')
    RIPT = Coin(currency='RIPT', full_name='RiptideCoin', id='RIPT', url='https://www.cryptocompare.com/media/15887409/ript.png')
    BBT = Coin(currency='BBT', full_name='BitBoost', id='BBT', url='https://www.cryptocompare.com/media/15887410/bbt.png')
    GBX = Coin(currency='GBX', full_name='GoByte', id='GBX', url='https://www.cryptocompare.com/media/15887411/gbx.png')
    CSTL = Coin(currency='CSTL', full_name='Castle', id='CSTL', url='https://www.cryptocompare.com/media/15887421/cstl.png')
    ICC = Coin(currency='ICC', full_name='Insta Cash Coin', id='ICC', url='https://www.cryptocompare.com/media/15887424/icc.png')
    JNT = Coin(currency='JNT', full_name='Jibrel Network Token', id='JNT', url='https://www.cryptocompare.com/media/34155550/jnt.png')
    QASH = Coin(currency='QASH', full_name='Quoine Liquid', id='QASH', url='https://www.cryptocompare.com/media/15887431/qash.png')
    ALQO = Coin(currency='ALQO', full_name='Alqo', id='ALQO', url='https://www.cryptocompare.com/media/16404849/alqo.png')
    TRIA = Coin(currency='TRIA', full_name='Triaconta', id='TRIA', url='https://www.cryptocompare.com/media/16404852/tria.png')
    PBL = Coin(currency='PBL', full_name='Pebbles', id='PBL', url='https://www.cryptocompare.com/media/16404866/pbl.png')
    MAG = Coin(currency='MAG', full_name='Magnet', id='MAG', url='https://www.cryptocompare.com/media/16404853/mag.png')
    STEX = Coin(currency='STEX', full_name='STEX', id='STEX', url='https://www.cryptocompare.com/media/34478506/stex.png')
    UFR = Coin(currency='UFR', full_name='Upfiring', id='UFR', url='https://www.cryptocompare.com/media/16404855/ufr.png')
    LOCI = Coin(currency='LOCI', full_name='LociCoin', id='LOCI', url='https://www.cryptocompare.com/media/16404856/loci.png')
    TAU = Coin(currency='TAU', full_name='Lamden Tau', id='TAU', url='https://www.cryptocompare.com/media/16404857/lamden.png')
    LAB = Coin(currency='LAB', full_name='Labrys', id='LAB', url='https://www.cryptocompare.com/media/16404858/lab.png')
    DEB = Coin(currency='DEB', full_name='Debitum Token', id='DEB', url='https://www.cryptocompare.com/media/16404861/deb.png')
    FLIXX = Coin(currency='FLIXX', full_name='Flixxo', id='FLIXX', url='https://www.cryptocompare.com/media/16404862/flixx.png')
    FRD = Coin(currency='FRD', full_name='Farad', id='FRD', url='https://www.cryptocompare.com/media/16404865/frd.png')
    PFR = Coin(currency='PFR', full_name='PayFair', id='PFR', url='https://www.cryptocompare.com/media/30001682/pfr.png')
    ECA = Coin(currency='ECA', full_name='Electra', id='ECA', url='https://www.cryptocompare.com/media/16404869/eca.png')
    LDM = Coin(currency='LDM', full_name='Ludum token', id='LDM', url='https://www.cryptocompare.com/media/16404870/ldm.png')
    LTG = Coin(currency='LTG', full_name='LiteCoin Gold', id='LTG', url='https://www.cryptocompare.com/media/16404871/ltg.png')
    STP = Coin(currency='STP', full_name='StashPay', id='STP', url='https://www.cryptocompare.com/media/16404874/stp.png')
    SPANK = Coin(currency='SPANK', full_name='SpankChain', id='SPANK', url='https://www.cryptocompare.com/media/16404890/spank.png')
    WISH = Coin(currency='WISH', full_name='MyWish', id='WISH', url='https://www.cryptocompare.com/media/16404892/wish.png')
    AERM = Coin(currency='AERM', full_name='Aerium', id='AERM', url='https://www.cryptocompare.com/media/16404893/aerm.png')
    PLX = Coin(currency='PLX', full_name='PlexCoin', id='PLX', url='https://www.cryptocompare.com/media/16404895/plx.png')
    ETHB = Coin(currency='ETHB', full_name='EtherBTC', id='ETHB', url='https://www.cryptocompare.com/media/16746424/ethb.png')
    CDX = Coin(currency='CDX', full_name='CDX Network ', id='CDX', url='https://www.cryptocompare.com/media/16746425/cdx.png')
    FOOD = Coin(currency='FOOD', full_name='FoodCoin', id='FOOD', url='https://www.cryptocompare.com/media/16746427/food.png')
    DEC = Coin(currency='DEC', full_name='Darico', id='DEC', url='https://www.cryptocompare.com/media/34835776/dec.png')
    VOT = Coin(currency='VOT', full_name='Votecoin', id='VOT', url='https://www.cryptocompare.com/media/16746442/vot.png')
    UQC = Coin(currency='UQC', full_name='Uquid Coin', id='UQC', url='https://www.cryptocompare.com/media/16746443/uqc.png')
    LEND = Coin(currency='LEND', full_name='EthLend', id='LEND', url='https://www.cryptocompare.com/media/16746444/lend.png')
    SETH = Coin(currency='SETH', full_name='Sether', id='SETH', url='https://www.cryptocompare.com/media/16746447/seth.png')
    ABYSS = Coin(currency='ABYSS', full_name='The Abyss', id='ABYSS', url='https://www.cryptocompare.com/media/30002251/abyss1.png')
    XSH = Coin(currency='XSH', full_name='SHIELD', id='XSH', url='https://www.cryptocompare.com/media/16746453/xsh.png')
    GEA = Coin(currency='GEA', full_name='Goldea', id='GEA', url='https://www.cryptocompare.com/media/16746475/gea.png')
    DSR = Coin(currency='DSR', full_name='Desire', id='DSR', url='https://www.cryptocompare.com/media/16746481/dsr.png')
    BDG = Coin(currency='BDG', full_name='BitDegree', id='BDG', url='https://www.cryptocompare.com/media/16746482/bdg.png')
    ONG = Coin(currency='ONG', full_name='SoMee.Social', id='ONG', url='https://www.cryptocompare.com/media/34478253/ong.png')
    BTCM = Coin(currency='BTCM', full_name='BTCMoon', id='BTCM', url='https://www.cryptocompare.com/media/16746489/btcm.png')
    ETBT = Coin(currency='ETBT', full_name='Ethereum Black', id='ETBT', url='https://www.cryptocompare.com/media/16746535/etbt.png')
    ZCG = Coin(currency='ZCG', full_name='ZCashGOLD', id='ZCG', url='https://www.cryptocompare.com/media/16746536/zcg.png')
    MUT = Coin(currency='MUT', full_name='Mutual Coin', id='MUT', url='https://www.cryptocompare.com/media/16746537/mut.png')
    MEOW = Coin(currency='MEOW', full_name='Kittehcoin', id='MEOW', url='https://www.cryptocompare.com/media/16746539/meow.png')
    DIVX = Coin(currency='DIVX', full_name='Divi Exchange Token', id='DIVX', url='https://www.cryptocompare.com/media/34835716/divx.png')
    CNBC = Coin(currency='CNBC', full_name='Cash & Back Coin', id='CNBC', url='https://www.cryptocompare.com/media/16746541/cnbc.png')
    RHOC = Coin(currency='RHOC', full_name='RChain', id='RHOC', url='https://www.cryptocompare.com/media/16746544/rhoc.png')
    XUN = Coin(currency='XUN', full_name='UltraNote', id='XUN', url='https://www.cryptocompare.com/media/16746548/xun.png')
    RFL = Coin(currency='RFL', full_name='RAFL', id='RFL', url='https://www.cryptocompare.com/media/16746549/rfl.png')
    COFI = Coin(currency='COFI', full_name='CoinFi', id='COFI', url='https://www.cryptocompare.com/media/16746551/cofi.png')
    ELTCOIN = Coin(currency='ELTCOIN', full_name='ELTCOIN', id='ELTCOIN', url='https://www.cryptocompare.com/media/16746556/eltcoin.png')
    GRX = Coin(currency='GRX', full_name='Gold Reward Token', id='GRX', url='https://www.cryptocompare.com/media/16746557/grx.png')
    NTK = Coin(currency='NTK', full_name='Neurotoken', id='NTK', url='https://www.cryptocompare.com/media/16746560/ntk.png')
    ERO = Coin(currency='ERO', full_name='Eroscoin', id='ERO', url='https://www.cryptocompare.com/media/16746561/ero.png')
    CMT = Coin(currency='CMT', full_name='CyberMiles', id='CMT', url='https://www.cryptocompare.com/media/30002257/cmt.png')
    RLX = Coin(currency='RLX', full_name='Relex', id='RLX', url='https://www.cryptocompare.com/media/34155508/rlx.png')
    MAN = Coin(currency='MAN', full_name='People', id='MAN', url='https://www.cryptocompare.com/media/16746574/man.png')
    CWV = Coin(currency='CWV', full_name='CryptoWave', id='CWV', url='https://www.cryptocompare.com/media/16746575/cwv.png')
    NRO = Coin(currency='NRO', full_name='Neuro', id='NRO', url='https://www.cryptocompare.com/media/16746592/nro.png')
    SEND = Coin(currency='SEND', full_name='Social Send', id='SEND', url='https://www.cryptocompare.com/media/16746577/send.png')
    GLT = Coin(currency='GLT', full_name='GlobalToken', id='GLT', url='https://www.cryptocompare.com/media/16746578/glt.png')
    X8X = Coin(currency='X8X', full_name='X8Currency', id='X8X', url='https://www.cryptocompare.com/media/16746588/x8x.png')
    COAL = Coin(currency='COAL', full_name='BitCoal', id='COAL', url='https://www.cryptocompare.com/media/16746586/coal.png')
    DAXX = Coin(currency='DAXX', full_name='DaxxCoin', id='DAXX', url='https://www.cryptocompare.com/media/16746587/daxx.png')
    BWK = Coin(currency='BWK', full_name='Bulwark', id='BWK', url='https://www.cryptocompare.com/media/35284325/bwk.png')
    FNTB = Coin(currency='FNTB', full_name='FinTab', id='FNTB', url='https://www.cryptocompare.com/media/16746591/fnt.png')
    XMRG = Coin(currency='XMRG', full_name='Monero Gold', id='XMRG', url='https://www.cryptocompare.com/media/16746651/xmrg.png')
    BTCE = Coin(currency='BTCE', full_name='EthereumBitcoin', id='BTCE', url='https://www.cryptocompare.com/media/16746600/btce.png')
    FYP = Coin(currency='FYP', full_name='FlypMe', id='FYP', url='https://www.cryptocompare.com/media/16746604/fyp.png')
    BOXY = Coin(currency='BOXY', full_name='BoxyCoin', id='BOXY', url='https://www.cryptocompare.com/media/16746605/boxy.png')
    NGC = Coin(currency='NGC', full_name='NagaCoin', id='NGC', url='https://www.cryptocompare.com/media/16746609/ngc.png')
    UTNP = Coin(currency='UTNP', full_name='Universa', id='UTNP', url='https://www.cryptocompare.com/media/16746611/utn.png')
    EGAS = Coin(currency='EGAS', full_name='ETHGAS', id='EGAS', url='https://www.cryptocompare.com/media/16746616/egas.png')
    DPP = Coin(currency='DPP', full_name='Digital Assets Power Play', id='DPP', url='https://www.cryptocompare.com/media/35308836/dpp.png')
    ADB = Coin(currency='ADB', full_name='Adbank', id='ADB', url='https://www.cryptocompare.com/media/16746619/adb.png')
    TGT = Coin(currency='TGT', full_name='TargetCoin', id='TGT', url='https://www.cryptocompare.com/media/16746629/tgt.png')
    XDCE = Coin(currency='XDCE', full_name='XinFin Coin', id='XDCE', url='https://www.cryptocompare.com/media/16746634/xdc.png')
    BMT = Coin(currency='BMT', full_name='BMChain', id='BMT', url='https://www.cryptocompare.com/media/16746638/bmt.png')
    BIO = Coin(currency='BIO', full_name='Biocoin', id='BIO', url='https://www.cryptocompare.com/media/16746639/bio.png')
    MTRC = Coin(currency='MTRC', full_name='ModulTrade', id='MTRC', url='https://www.cryptocompare.com/media/16746642/mtrc.png')
    BTCL = Coin(currency='BTCL', full_name='BTC Lite', id='BTCL', url='https://www.cryptocompare.com/media/16746647/btcl.png')
    PCN = Coin(currency='PCN', full_name='PeepCoin', id='PCN', url='https://www.cryptocompare.com/media/16746648/pcn.png')
    PYP = Coin(currency='PYP', full_name='PayPro', id='PYP', url='https://www.cryptocompare.com/media/16746650/pyp.png')
    CRED = Coin(currency='CRED', full_name='Verify', id='CRED', url='https://www.cryptocompare.com/media/16746661/cred.png')
    SBTC = Coin(currency='SBTC', full_name='Super Bitcoin', id='SBTC', url='https://www.cryptocompare.com/media/16746666/sbtc.png')
    KLKS = Coin(currency='KLKS', full_name='Kalkulus', id='KLKS', url='https://www.cryptocompare.com/media/16746667/klk.png')
    AC3 = Coin(currency='AC3', full_name='AC3', id='AC3', url='https://www.cryptocompare.com/media/16746668/ac3.png')
    GTO = Coin(currency='GTO', full_name='GIFTO', id='GTO', url='https://www.cryptocompare.com/media/16746671/gto.png')
    TNB = Coin(currency='TNB', full_name='Time New Bank', id='TNB', url='https://www.cryptocompare.com/media/16746672/tnb.png')
    HKN = Coin(currency='HKN', full_name='Hacken', id='HKN', url='https://www.cryptocompare.com/media/16746674/hkn.png')
    B2B = Coin(currency='B2B', full_name='B2BX', id='B2B', url='https://www.cryptocompare.com/media/12318185/b2bx.png')
    LTHN = Coin(currency='LTHN', full_name='Lethean', id='LTHN', url='https://www.cryptocompare.com/media/35309393/lthn.png')
    GER = Coin(currency='GER', full_name='GermanCoin', id='GER', url='https://www.cryptocompare.com/media/16746741/ger.png')
    LTCU = Coin(currency='LTCU', full_name='LiteCoin Ultra', id='LTCU', url='https://www.cryptocompare.com/media/16746704/ltcu.png')
    MGO = Coin(currency='MGO', full_name='MobileGo', id='MGO', url='https://www.cryptocompare.com/media/1382798/mgo.png')
    BTCA = Coin(currency='BTCA', full_name='Bitair', id='BTCA', url='https://www.cryptocompare.com/media/16746705/btca.png')
    HQX = Coin(currency='HQX', full_name='HOQU', id='HQX', url='https://www.cryptocompare.com/media/16746735/hqx.png')
    ETF = Coin(currency='ETF', full_name='EthereumFog', id='ETF', url='https://www.cryptocompare.com/media/16746737/etf.png')
    STAK = Coin(currency='STAK', full_name='Straks', id='STAK', url='https://www.cryptocompare.com/media/16746740/stak.png')
    BCOIN = Coin(currency='BCOIN', full_name='BannerCoin', id='BCOIN', url='https://www.cryptocompare.com/media/16746742/bcoin.png')
    CCOS = Coin(currency='CCOS', full_name='CrowdCoinage', id='CCOS', url='https://www.cryptocompare.com/media/16746767/ccos.png')
    BNTY = Coin(currency='BNTY', full_name='Bounty0x', id='BNTY', url='https://www.cryptocompare.com/media/20780588/bnty.png')
    BRD = Coin(currency='BRD', full_name='Bread token', id='BRD', url='https://www.cryptocompare.com/media/20780589/brd.png')
    HAT = Coin(currency='HAT', full_name='Hawala.Exchange', id='HAT', url='https://www.cryptocompare.com/media/34478229/hat.png')
    ELF = Coin(currency='ELF', full_name='aelf', id='ELF', url='https://www.cryptocompare.com/media/20780600/elf.png')
    VLR = Coin(currency='VLR', full_name='Valorem', id='VLR', url='https://www.cryptocompare.com/media/20780606/vlr.png')
    CWX = Coin(currency='CWX', full_name='Crypto-X', id='CWX', url='https://www.cryptocompare.com/media/20780607/cwx.png')
    DBC = Coin(currency='DBC', full_name='DeepBrain Chain', id='DBC', url='https://www.cryptocompare.com/media/20780608/dbc.png')
    ZP = Coin(currency='ZP', full_name='Zen Protocol', id='ZP', url='https://www.cryptocompare.com/media/20780609/zen.png')
    POP = Coin(currency='POP', full_name='PopularCoin', id='POP', url='https://www.cryptocompare.com/media/20780610/pop.png')
    PNX = Coin(currency='PNX', full_name='PhantomX', id='PNX', url='https://www.cryptocompare.com/media/20780612/pnx.png')
    BAS = Coin(currency='BAS', full_name='BitAsean', id='BAS', url='https://www.cryptocompare.com/media/20780613/bas.png')
    UTT = Coin(currency='UTT', full_name='United Traders Token', id='UTT', url='https://www.cryptocompare.com/media/20780614/utt.png')
    HBC = Coin(currency='HBC', full_name='HomeBlockCoin', id='HBC', url='https://www.cryptocompare.com/media/20780615/hbc.png')
    AMM = Coin(currency='AMM', full_name='MicroMoney', id='AMM', url='https://www.cryptocompare.com/media/20780616/amm.png')
    DAV = Coin(currency='DAV', full_name='DavorCoin', id='DAV', url='https://www.cryptocompare.com/media/20780624/dav.png')
    XCPO = Coin(currency='XCPO', full_name='Copico', id='XCPO', url='https://www.cryptocompare.com/media/20780625/xcpo.png')
    GET = Coin(currency='GET', full_name='Guaranteed Entrance Token', id='GET', url='https://www.cryptocompare.com/media/20780626/get.png')
    ERC20 = Coin(currency='ERC20', full_name='Index ERC20', id='ERC20', url='https://www.cryptocompare.com/media/34836091/erc20.png')
    ITC = Coin(currency='ITC', full_name='IoT Chain', id='ITC', url='https://www.cryptocompare.com/media/20780628/itc.png')
    HTML = Coin(currency='HTML', full_name='HTML Coin', id='HTML', url='https://www.cryptocompare.com/media/34477916/html_newer.png')
    GENE = Coin(currency='GENE', full_name='PARKGENE', id='GENE', url='https://www.cryptocompare.com/media/20780630/gene.png')
    NMS = Coin(currency='NMS', full_name='Numus', id='NMS', url='https://www.cryptocompare.com/media/35309720/nms.png')
    PHO = Coin(currency='PHO', full_name='Photon', id='PHO', url='https://www.cryptocompare.com/media/35309219/pho.png')
    XTRA = Coin(currency='XTRA', full_name='ExtraCredit', id='XTRA', url='https://www.cryptocompare.com/media/20780641/extra-logo-white.png')
    NTWK = Coin(currency='NTWK', full_name='Network Token', id='NTWK', url='https://www.cryptocompare.com/media/20780649/ntwk.png')
    SUCR = Coin(currency='SUCR', full_name='Sucre', id='SUCR', url='https://www.cryptocompare.com/media/20780650/sucr.png')
    GNX = Coin(currency='GNX', full_name='Genaro Network', id='GNX', url='https://www.cryptocompare.com/media/20780652/gnx.png')
    NAS = Coin(currency='NAS', full_name='Nebulas', id='NAS', url='https://www.cryptocompare.com/media/20780653/nas.png')
    ACCO = Coin(currency='ACCO', full_name='Accolade', id='ACCO', url='https://www.cryptocompare.com/media/20780654/acco.png')
    BYTHER = Coin(currency='BYTHER', full_name='Bytether ', id='BYTHER', url='https://www.cryptocompare.com/media/20780656/bth.png')
    REM = Coin(currency='REM', full_name='REMME', id='REM', url='https://www.cryptocompare.com/media/20780658/rem.png')
    TOK = Coin(currency='TOK', full_name='TokugawaCoin', id='TOK', url='https://www.cryptocompare.com/media/20780659/tok.png')
    EREAL = Coin(currency='EREAL', full_name='eREAL', id='EREAL', url='https://www.cryptocompare.com/media/20780660/ereal.png')
    CPN = Coin(currency='CPN', full_name='CompuCoin', id='CPN', url='https://www.cryptocompare.com/media/20780661/cpn.png')
    XFT = Coin(currency='XFT', full_name='Fantasy Cash', id='XFT', url='https://www.cryptocompare.com/media/30002339/xft.jpg')
    QLC = Coin(currency='QLC', full_name='QLC Chain', id='QLC', url='https://www.cryptocompare.com/media/20780665/qlc.png')
    BTSE = Coin(currency='BTSE', full_name='BitSerial', id='BTSE', url='https://www.cryptocompare.com/media/20780666/bte.png')
    OMGC = Coin(currency='OMGC', full_name='OmiseGO Classic', id='OMGC', url='https://www.cryptocompare.com/media/20780667/omgc.png')
    Q2C = Coin(currency='Q2C', full_name='QubitCoin', id='Q2C', url='https://www.cryptocompare.com/media/19872/q2c.jpg')
    BLT = Coin(currency='BLT', full_name='Bloom Token', id='BLT', url='https://www.cryptocompare.com/media/20780668/blt.png')
    SPF = Coin(currency='SPF', full_name='SportyCo', id='SPF', url='https://www.cryptocompare.com/media/20780669/spf.png')
    TDS = Coin(currency='TDS', full_name='TokenDesk', id='TDS', url='https://www.cryptocompare.com/media/20780673/tds.png')
    ORE = Coin(currency='ORE', full_name='Galactrum', id='ORE', url='https://www.cryptocompare.com/media/20780695/ore.png')
    SPK = Coin(currency='SPK', full_name='SparksPay', id='SPK', url='https://www.cryptocompare.com/media/35309655/spk.png')
    GOA = Coin(currency='GOA', full_name='GoaCoin', id='GOA', url='https://www.cryptocompare.com/media/20780698/goa.png')
    FLS = Coin(currency='FLS', full_name='Fuloos Coin', id='FLS', url='https://www.cryptocompare.com/media/20780701/fuloos.png')
    WAGE = Coin(currency='WAGE', full_name='Digiwage', id='WAGE', url='https://www.cryptocompare.com/media/30002011/digiwage.jpg')
    GUN = Coin(currency='GUN', full_name='GunCoin', id='GUN', url='https://www.cryptocompare.com/media/20780703/gun.png')
    DFS = Coin(currency='DFS', full_name='Digital Fantasy Sports', id='DFS', url='https://www.cryptocompare.com/media/35309074/dfs.png')
    POLIS = Coin(currency='POLIS', full_name='PolisPay', id='POLIS', url='https://www.cryptocompare.com/media/20780731/polis.png')
    WELL = Coin(currency='WELL', full_name='Well', id='WELL', url='https://www.cryptocompare.com/media/20780732/well.png')
    FLOT = Coin(currency='FLOT', full_name='FireLotto', id='FLOT', url='https://www.cryptocompare.com/media/20780733/flot.png')
    CL = Coin(currency='CL', full_name='CoinLancer', id='CL', url='https://www.cryptocompare.com/media/20780740/cl.png')
    SHND = Coin(currency='SHND', full_name='StrongHands', id='SHND', url='https://www.cryptocompare.com/media/20780741/shnd.png')
    AUA = Coin(currency='AUA', full_name='ArubaCoin', id='AUA', url='https://www.cryptocompare.com/media/20780743/aua.png')
    DNN = Coin(currency='DNN', full_name='DNN Token', id='DNN', url='https://www.cryptocompare.com/media/20780744/dnn.png')
    SAGA = Coin(currency='SAGA', full_name='SagaCoin', id='SAGA', url='https://www.cryptocompare.com/media/20780745/saga.png')
    GXS = Coin(currency='GXS', full_name='GXChain', id='GXS', url='https://www.cryptocompare.com/media/20780746/gxs.png')
    TSL = Coin(currency='TSL', full_name='Energo', id='TSL', url='https://www.cryptocompare.com/media/20780749/tsl.png')
    IRL = Coin(currency='IRL', full_name='IrishCoin', id='IRL', url='https://www.cryptocompare.com/media/20780751/irl.png')
    BOT = Coin(currency='BOT', full_name='Bodhi', id='BOT', url='https://www.cryptocompare.com/media/20780753/bot.png')
    PMA = Coin(currency='PMA', full_name='PumaPay', id='PMA', url='https://www.cryptocompare.com/media/20780758/pma.png')
    TROLL = Coin(currency='TROLL', full_name='Trollcoin', id='TROLL', url='https://www.cryptocompare.com/media/20780762/troll.png')
    FOR = Coin(currency='FOR', full_name='Force Coin', id='FOR', url='https://www.cryptocompare.com/media/20780764/for.png')
    SGR = Coin(currency='SGR', full_name='Sugar Exchange', id='SGR', url='https://www.cryptocompare.com/media/20780766/sgr.png')
    JET = Coin(currency='JET', full_name='Jetcoin', id='JET', url='https://www.cryptocompare.com/media/20780772/jet.png')
    MDS = Coin(currency='MDS', full_name='MediShares', id='MDS', url='https://www.cryptocompare.com/media/20780773/ipnvhhke_400x400.jpg')
    LCP = Coin(currency='LCP', full_name='Litecoin Plus', id='LCP', url='https://www.cryptocompare.com/media/20780774/lcp.png')
    GTC = Coin(currency='GTC', full_name='Game', id='GTC', url='https://www.cryptocompare.com/media/20780776/gtc.png')
    IETH = Coin(currency='IETH', full_name='iEthereum', id='IETH', url='https://www.cryptocompare.com/media/20780777/ieth.png')
    SDRN = Coin(currency='SDRN', full_name='Senderon', id='SDRN', url='https://www.cryptocompare.com/media/20780780/sdrn.png')
    INK = Coin(currency='INK', full_name='Ink', id='INK', url='https://www.cryptocompare.com/media/20780781/ink.png')
    KBR = Coin(currency='KBR', full_name='Kubera Coin', id='KBR', url='https://www.cryptocompare.com/media/20780782/kbr.png')
    HPB = Coin(currency='HPB', full_name='High Performance Blockchain', id='HPB', url='https://www.cryptocompare.com/media/20780783/hpb.png')
    MONK = Coin(currency='MONK', full_name='Monkey Project', id='MONK', url='https://www.cryptocompare.com/media/35284366/monkey.png')
    JINN = Coin(currency='JINN', full_name='Jinn', id='JINN', url='https://www.cryptocompare.com/media/20780786/jinn.png')
    MGN = Coin(currency='MGN', full_name='MagnaCoin', id='MGN', url='https://www.cryptocompare.com/media/20780788/mgn.png')
    KZC = Coin(currency='KZC', full_name='KZCash', id='KZC', url='https://www.cryptocompare.com/media/20780789/kz.png')
    GNR = Coin(currency='GNR', full_name='Gainer', id='GNR', url='https://www.cryptocompare.com/media/20780791/gnr.png')
    LWF = Coin(currency='LWF', full_name='Local World Forwarders', id='LWF', url='https://www.cryptocompare.com/media/20780794/lwf.png')
    BRC = Coin(currency='BRC', full_name='BrightCoin', id='BRC', url='https://www.cryptocompare.com/media/20780798/brc.png')
    WCG = Coin(currency='WCG', full_name='World Crypto Gold', id='WCG', url='https://www.cryptocompare.com/media/20780799/wcg.png')
    HIVE = Coin(currency='HIVE', full_name='Hive', id='HIVE', url='https://www.cryptocompare.com/media/20780800/flat.png')
    LCK = Coin(currency='LCK', full_name='Luckbox', id='LCK', url='https://www.cryptocompare.com/media/20780805/luck.png')
    MFG = Coin(currency='MFG', full_name='SyncFab', id='MFG', url='https://www.cryptocompare.com/media/25792563/mfg.png')
    ETL = Coin(currency='ETL', full_name='EtherLite', id='ETL', url='https://www.cryptocompare.com/media/25792566/etl.png')
    TEL = Coin(currency='TEL', full_name='Telcoin', id='TEL', url='https://www.cryptocompare.com/media/25792569/tel.png')
    ONL = Coin(currency='ONL', full_name='On.Live', id='ONL', url='https://www.cryptocompare.com/media/25792573/onl.png')
    ZAP = Coin(currency='ZAP', full_name='Zap', id='ZAP', url='https://www.cryptocompare.com/media/25792575/zap.png')
    AIDOC = Coin(currency='AIDOC', full_name='AI Doctor', id='AIDOC', url='https://www.cryptocompare.com/media/25792577/aidoc.png')
    ECC = Coin(currency='ECC', full_name='ECC', id='ECC', url='https://www.cryptocompare.com/media/25792579/ecc.png')
    ET4 = Coin(currency='ET4', full_name='Eticket4', id='ET4', url='https://www.cryptocompare.com/media/25792581/et4.png')
    LCT = Coin(currency='LCT', full_name='LendConnect', id='LCT', url='https://www.cryptocompare.com/media/25792592/lct.png')
    EBC = Coin(currency='EBC', full_name='EBCoin', id='EBC', url='https://www.cryptocompare.com/media/25792622/ebc.png')
    VST = Coin(currency='VST', full_name='Vestarin', id='VST', url='https://www.cryptocompare.com/media/25792598/vst.png')
    INT = Coin(currency='INT', full_name='Internet Node Token', id='INT', url='https://www.cryptocompare.com/media/25792603/int.png')
    CPY = Coin(currency='CPY', full_name='COPYTRACK', id='CPY', url='https://www.cryptocompare.com/media/25792602/cpy.png')
    STN = Coin(currency='STN', full_name='Steneum Coin', id='STN', url='https://www.cryptocompare.com/media/25792600/stn.png')
    SFU = Coin(currency='SFU', full_name='Saifu', id='SFU', url='https://www.cryptocompare.com/media/25792604/sfu.png')
    PCOIN = Coin(currency='PCOIN', full_name='Pioneer Coin', id='PCOIN', url='https://www.cryptocompare.com/media/25792606/pcoin.png')
    LUC = Coin(currency='LUC', full_name='Play 2 Live', id='LUC', url='https://www.cryptocompare.com/media/25792608/luc.png')
    EDT = Coin(currency='EDT', full_name='EtherDelta', id='EDT', url='https://www.cryptocompare.com/media/25792615/edt.png')
    CYDER = Coin(currency='CYDER', full_name='Cyder Coin', id='CYDER', url='https://www.cryptocompare.com/media/25792617/cyder.png')
    SRNT = Coin(currency='SRNT', full_name='Serenity', id='SRNT', url='https://www.cryptocompare.com/media/25792618/srnt.png')
    MLT = Coin(currency='MLT', full_name='MultiGames', id='MLT', url='https://www.cryptocompare.com/media/25792620/mlt.png')
    EKO = Coin(currency='EKO', full_name='EchoLink', id='EKO', url='https://www.cryptocompare.com/media/25792625/eko.png')
    UBTC = Coin(currency='UBTC', full_name='UnitedBitcoin', id='UBTC', url='https://www.cryptocompare.com/media/33187879/rsz_rc6d5pq9_400x400.jpg')
    BTO = Coin(currency='BTO', full_name='Bottos', id='BTO', url='https://www.cryptocompare.com/media/25792636/bot.png')
    DOC = Coin(currency='DOC', full_name='Doc Coin', id='DOC', url='https://www.cryptocompare.com/media/25792637/doc.png')
    ARCT = Coin(currency='ARCT', full_name='ArbitrageCT', id='ARCT', url='https://www.cryptocompare.com/media/25792638/arct.png')
    IMVR = Coin(currency='IMVR', full_name='ImmVRse', id='IMVR', url='https://www.cryptocompare.com/media/25792642/imv.png')
    AURA = Coin(currency='AURA', full_name='Aurora', id='AURA', url='https://www.cryptocompare.com/media/25792643/aura.png')
    IDH = Coin(currency='IDH', full_name='IndaHash', id='IDH', url='https://www.cryptocompare.com/media/25792644/idh.png')
    CBT = Coin(currency='CBT', full_name='CommerceBlock Token', id='CBT', url='https://www.cryptocompare.com/media/35521161/cbt.png')
    ITZ = Coin(currency='ITZ', full_name='Interzone', id='ITZ', url='https://www.cryptocompare.com/media/25792662/itz.png')
    XBP = Coin(currency='XBP', full_name='Black Pearl Coin', id='XBP', url='https://www.cryptocompare.com/media/25792650/xbp.png')
    EXRN = Coin(currency='EXRN', full_name='EXRNchain', id='EXRN', url='https://www.cryptocompare.com/media/20780642/exrn.png')
    AGI = Coin(currency='AGI', full_name='SingularityNET', id='AGI', url='https://www.cryptocompare.com/media/25792653/agi.png')
    BFT = Coin(currency='BFT', full_name='BF Token', id='BFT', url='https://www.cryptocompare.com/media/25792654/bft.png')
    LGO = Coin(currency='LGO', full_name='Legolas Exchange', id='LGO', url='https://www.cryptocompare.com/media/25792655/lgo.png')
    CRPT = Coin(currency='CRPT', full_name='Crypterium', id='CRPT', url='https://www.cryptocompare.com/media/25792665/crpt.png')
    SGL = Coin(currency='SGL', full_name='Sigil', id='SGL', url='https://www.cryptocompare.com/media/25792671/sgl.png')
    TNC = Coin(currency='TNC', full_name='Trinity Network Credit', id='TNC', url='https://www.cryptocompare.com/media/25792672/tnc.png')
    FSBT = Coin(currency='FSBT', full_name='Forty Seven Bank', id='FSBT', url='https://www.cryptocompare.com/media/25792673/fsbt.png')
    CFTY = Coin(currency='CFTY', full_name='Crafty', id='CFTY', url='https://www.cryptocompare.com/media/25792674/cfty.png')
    DTA = Coin(currency='DTA', full_name='Data', id='DTA', url='https://www.cryptocompare.com/media/25792680/dta.png')
    CV = Coin(currency='CV', full_name='CarVertical', id='CV', url='https://www.cryptocompare.com/media/27010446/cv.png')
    DTX = Coin(currency='DTX', full_name='DataBroker DAO', id='DTX', url='https://www.cryptocompare.com/media/25792685/dtx.png')
    MCU = Coin(currency='MCU', full_name='MediChain', id='MCU', url='https://www.cryptocompare.com/media/27010445/mcu.png')
    OCN = Coin(currency='OCN', full_name='Odyssey', id='OCN', url='https://www.cryptocompare.com/media/27010448/ocn.png')
    THETA = Coin(currency='THETA', full_name='Theta', id='THETA', url='https://www.cryptocompare.com/media/27010450/theta.png')
    PRPS = Coin(currency='PRPS', full_name='Purpose', id='PRPS', url='https://www.cryptocompare.com/media/27010452/prps.png')
    DUBI = Coin(currency='DUBI', full_name='Decentralized Universal Basic Income', id='DUBI', url='https://www.cryptocompare.com/media/27010453/dubi.png')
    BPT = Coin(currency='BPT', full_name='Blockport', id='BPT', url='https://www.cryptocompare.com/media/27010454/bpt.png')
    SGN = Coin(currency='SGN', full_name='Signals Network', id='SGN', url='https://www.cryptocompare.com/media/27010455/sgn.png')
    IOST = Coin(currency='IOST', full_name='IOS token', id='IOST', url='https://www.cryptocompare.com/media/27010459/iost.png')
    TCT = Coin(currency='TCT', full_name='TokenClub ', id='TCT', url='https://www.cryptocompare.com/media/27010460/tct.png')
    TRAC = Coin(currency='TRAC', full_name='OriginTrail', id='TRAC', url='https://www.cryptocompare.com/media/27010463/trac.png')
    MOT = Coin(currency='MOT', full_name='Olympus Labs', id='MOT', url='https://www.cryptocompare.com/media/27010462/mot.png')
    ZIL = Coin(currency='ZIL', full_name='Zilliqa', id='ZIL', url='https://www.cryptocompare.com/media/27010464/zil.png')
    HORSE = Coin(currency='HORSE', full_name='Ethorse ', id='HORSE', url='https://www.cryptocompare.com/media/27010465/horse.png')
    QUN = Coin(currency='QUN', full_name='QunQun', id='QUN', url='https://www.cryptocompare.com/media/27010466/qun.png')
    SWFTC = Coin(currency='SWFTC', full_name='SwftCoin', id='SWFTC', url='https://www.cryptocompare.com/media/27010472/swftc.png')
    SENT = Coin(currency='SENT', full_name='Sentinel', id='SENT', url='https://www.cryptocompare.com/media/27010471/sent.png')
    IPL = Coin(currency='IPL', full_name='InsurePal', id='IPL', url='https://www.cryptocompare.com/media/27010470/ipl.png')
    OPC = Coin(currency='OPC', full_name='OP Coin', id='OPC', url='https://www.cryptocompare.com/media/27010474/opc.png')
    SAF = Coin(currency='SAF', full_name='Safinus', id='SAF', url='https://www.cryptocompare.com/media/27010473/sfu.png')
    SHA = Coin(currency='SHA', full_name='Shacoin', id='SHA', url='https://www.cryptocompare.com/media/27010477/sha.png')
    PYLNT = Coin(currency='PYLNT', full_name='Pylon Network', id='PYLNT', url='https://www.cryptocompare.com/media/27010479/pylnt.png')
    GRLC = Coin(currency='GRLC', full_name='Garlicoin', id='GRLC', url='https://www.cryptocompare.com/media/27010480/garlic.png')
    EVE = Coin(currency='EVE', full_name='Devery', id='EVE', url='https://www.cryptocompare.com/media/27010481/eve.png')
    YEE = Coin(currency='YEE', full_name='Yee', id='YEE', url='https://www.cryptocompare.com/media/27010483/yee.png')
    REPUX = Coin(currency='REPUX', full_name='Repux', id='REPUX', url='https://www.cryptocompare.com/media/27010482/repux.png')
    JOYT = Coin(currency='JOYT', full_name='JoyToken', id='JOYT', url='https://www.cryptocompare.com/media/27010484/joy.png')
    XCD = Coin(currency='XCD', full_name='Capdax', id='XCD', url='https://www.cryptocompare.com/media/27010488/xcd.png')
    BTW = Coin(currency='BTW', full_name='BitWhite', id='BTW', url='https://www.cryptocompare.com/media/27010490/btw.png')
    AXPR = Coin(currency='AXPR', full_name='aXpire', id='AXPR', url='https://www.cryptocompare.com/media/27010491/axp.png')
    FOTA = Coin(currency='FOTA', full_name='Fortuna', id='FOTA', url='https://www.cryptocompare.com/media/27010497/fota.png')
    DDD = Coin(currency='DDD', full_name='Scry.info', id='DDD', url='https://www.cryptocompare.com/media/27010499/ddd.png')
    SPEND = Coin(currency='SPEND', full_name='Spend', id='SPEND', url='https://www.cryptocompare.com/media/27010502/spend.png')
    NPXS = Coin(currency='NPXS', full_name='Pundi X', id='NPXS', url='https://www.cryptocompare.com/media/27010505/pxs.png')
    ZPT = Coin(currency='ZPT', full_name='Zeepin', id='ZPT', url='https://www.cryptocompare.com/media/27010506/zpt.png')
    CROAT = Coin(currency='CROAT', full_name='Croat', id='CROAT', url='https://www.cryptocompare.com/media/27010508/croat.png')
    REF = Coin(currency='REF', full_name='RefToken', id='REF', url='https://www.cryptocompare.com/media/27010509/ref.png')
    SXDT = Coin(currency='SXDT', full_name='SPECTRE Dividend Token', id='SXDT', url='https://www.cryptocompare.com/media/27010511/sxdt.png')
    SXUT = Coin(currency='SXUT', full_name='SPECTRE Utility Token', id='SXUT', url='https://www.cryptocompare.com/media/27010511/sxdt.png')
    LDC = Coin(currency='LDC', full_name='LeadCoin', id='LDC', url='https://www.cryptocompare.com/media/27010513/ldc.png')
    VAL = Coin(currency='VAL', full_name='Valorbit', id='VAL', url='https://www.cryptocompare.com/media/27010515/val.png')
    BCDN = Coin(currency='BCDN', full_name='BlockCDN ', id='BCDN', url='https://www.cryptocompare.com/media/27010517/1.png')
    STK = Coin(currency='STK', full_name='STK Token', id='STK', url='https://www.cryptocompare.com/media/27010524/stk.png')
    MZX = Coin(currency='MZX', full_name='Mosaic Network', id='MZX', url='https://www.cryptocompare.com/media/27010540/mzx.png')
    SPICE = Coin(currency='SPICE', full_name='SPiCE Venture Capital ', id='SPICE', url='https://www.cryptocompare.com/media/27010560/vc.png')
    Q1S = Coin(currency='Q1S', full_name='Quantum1Net', id='Q1S', url='https://www.cryptocompare.com/media/27010561/q1s.png')
    XTO = Coin(currency='XTO', full_name='Tao', id='XTO', url='https://www.cryptocompare.com/media/27010572/xto.png')
    RUFF = Coin(currency='RUFF', full_name='Ruff', id='RUFF', url='https://www.cryptocompare.com/media/27010573/fqqzfp9_400x400.png')
    ELA = Coin(currency='ELA', full_name='Elastos', id='ELA', url='https://www.cryptocompare.com/media/27010574/ela.png')
    CXO = Coin(currency='CXO', full_name='CargoX', id='CXO', url='https://www.cryptocompare.com/media/27010577/cxo.png')
    WT = Coin(currency='WT', full_name='WeToken', id='WT', url='https://www.cryptocompare.com/media/27010582/wt.png')
    HGS = Coin(currency='HGS', full_name='HashGains', id='HGS', url='https://www.cryptocompare.com/media/27010583/hgs.png')
    SISA = Coin(currency='SISA', full_name='Strategic Investments in Significant Areas', id='SISA', url='https://www.cryptocompare.com/media/27010587/sisa.png')
    EBIT = Coin(currency='EBIT', full_name='eBit', id='EBIT', url='https://www.cryptocompare.com/media/27010588/ebit-logo.png')
    RCT = Coin(currency='RCT', full_name='RealChain', id='RCT', url='https://www.cryptocompare.com/media/27010590/rct.png')
    CUZ = Coin(currency='CUZ', full_name='Cool Cousin', id='CUZ', url='https://www.cryptocompare.com/media/27010593/cuz.png')
    HLC = Coin(currency='HLC', full_name='Halal-Chain', id='HLC', url='https://www.cryptocompare.com/media/27010592/hlc_logo.png')
    BETR = Coin(currency='BETR', full_name='BetterBetting', id='BETR', url='https://www.cryptocompare.com/media/33842944/betr_new.png')
    GMR = Coin(currency='GMR', full_name='Gimmer', id='GMR', url='https://www.cryptocompare.com/media/27010596/gmr.png')
    ING = Coin(currency='ING', full_name='Iungo', id='ING', url='https://www.cryptocompare.com/media/27010597/ing_logo.png')
    LHC = Coin(currency='LHC', full_name='LHCoin', id='LHC', url='https://www.cryptocompare.com/media/27010598/lhc.png')
    BLZ = Coin(currency='BLZ', full_name='Bluzelle', id='BLZ', url='https://www.cryptocompare.com/media/27010607/1.png')
    CHSB = Coin(currency='CHSB', full_name='SwissBorg', id='CHSB', url='https://www.cryptocompare.com/media/27010612/chsb_logo.png')
    EQUI = Coin(currency='EQUI', full_name='EQUI Token', id='EQUI', url='https://www.cryptocompare.com/media/27010614/equi.png')
    MCT = Coin(currency='MCT', full_name='1717 Masonic Commemorative Token', id='MCT', url='https://www.cryptocompare.com/media/27010616/1717mct_logo.png')
    HHEM = Coin(currency='HHEM', full_name='Healthureum', id='HHEM', url='https://www.cryptocompare.com/media/27010617/hhem.png')
    CWIS = Coin(currency='CWIS', full_name='Crypto Wisdom Coin', id='CWIS', url='https://www.cryptocompare.com/media/27010619/cwis_logo.png')
    MBC = Coin(currency='MBC', full_name='My Big Coin', id='MBC', url='https://www.cryptocompare.com/media/27010620/mbc_logo.png')
    GRO = Coin(currency='GRO', full_name='Gron Digital', id='GRO', url='https://www.cryptocompare.com/media/27010628/gro.png')
    SWM = Coin(currency='SWM', full_name='Swarm Fund', id='SWM', url='https://www.cryptocompare.com/media/27010630/swm_logo.png')
    WOBTC = Coin(currency='WOBTC', full_name='WorldBTC', id='WOBTC', url='https://www.cryptocompare.com/media/27010633/wbtc.png')
    DNO = Coin(currency='DNO', full_name='Denaro', id='DNO', url='https://www.cryptocompare.com/media/27010637/dno.png')
    eFIC = Coin(currency='eFIC', full_name='FIC Network', id='eFIC', url='https://www.cryptocompare.com/media/30001623/efic.png')
    TKY = Coin(currency='TKY', full_name='THEKEY Token', id='TKY', url='https://www.cryptocompare.com/media/27010658/tky.png')
    BANCA = Coin(currency='BANCA', full_name='BANCA', id='BANCA', url='https://www.cryptocompare.com/media/27010659/banca.png')
    TRTL = Coin(currency='TRTL', full_name='TurtleCoin', id='TRTL', url='https://www.cryptocompare.com/media/27010966/untitled-1.png')
    BIX = Coin(currency='BIX', full_name='BiboxCoin', id='BIX', url='https://www.cryptocompare.com/media/27010664/bix.png')
    ABT = Coin(currency='ABT', full_name='ArcBlock', id='ABT', url='https://www.cryptocompare.com/media/27010666/abt2.png')
    HBZ = Coin(currency='HBZ', full_name='HBZ Coin', id='HBZ', url='https://www.cryptocompare.com/media/27010671/hbz.png')
    DRPU = Coin(currency='DRPU', full_name='DRP Utility', id='DRPU', url='https://www.cryptocompare.com/media/34077417/drup.png')
    DOR = Coin(currency='DOR', full_name='Dorado', id='DOR', url='https://www.cryptocompare.com/media/27010676/dor.png')
    PRFT = Coin(currency='PRFT', full_name='Proof Suite Token', id='PRFT', url='https://www.cryptocompare.com/media/27010677/prft.png')
    PARETO = Coin(currency='PARETO', full_name='Pareto Network Token', id='PARETO', url='https://www.cryptocompare.com/media/27010679/pareto.png')
    DTRC = Coin(currency='DTRC', full_name='Datarius', id='DTRC', url='https://www.cryptocompare.com/media/27010691/dtr.png')
    IQB = Coin(currency='IQB', full_name='Intelligence Quotient Benefit', id='IQB', url='https://www.cryptocompare.com/media/27010692/iqb.png')
    BEE = Coin(currency='BEE', full_name='Bee Token', id='BEE', url='https://www.cryptocompare.com/media/27010700/bee.png')
    MUN = Coin(currency='MUN', full_name='MUNcoin', id='MUN', url='https://www.cryptocompare.com/media/27010701/mun.png')
    TIG = Coin(currency='TIG', full_name='Tigereum', id='TIG', url='https://www.cryptocompare.com/media/27010719/tig.png')
    LYK = Coin(currency='LYK', full_name='Loyakk Vega', id='LYK', url='https://www.cryptocompare.com/media/30002217/lykk.jpg')
    NYX = Coin(currency='NYX', full_name='NYXCOIN', id='NYX', url='https://www.cryptocompare.com/media/27010735/nyx.png')
    DXT = Coin(currency='DXT', full_name='DataWallet', id='DXT', url='https://www.cryptocompare.com/media/27010739/dxt.png')
    SAT = Coin(currency='SAT', full_name='Satisfaction Token', id='SAT', url='https://www.cryptocompare.com/media/27010744/sat.png')
    CRL = Coin(currency='CRL', full_name='Cryptelo Coin', id='CRL', url='https://www.cryptocompare.com/media/27010747/crl.png')
    ORI = Coin(currency='ORI', full_name='Origami', id='ORI', url='https://www.cryptocompare.com/media/27010748/ori.png')
    USX = Coin(currency='USX', full_name='Unified Society USDEX', id='USX', url='https://www.cryptocompare.com/media/27010758/usx.png')
    LGR = Coin(currency='LGR', full_name='Logarithm', id='LGR', url='https://www.cryptocompare.com/media/27010759/lgr.jpg')
    BCA = Coin(currency='BCA', full_name='Bitcoin Atom', id='BCA', url='https://www.cryptocompare.com/media/27010760/bca-2.jpg')
    B2X = Coin(currency='B2X', full_name='SegWit2x', id='B2X', url='https://www.cryptocompare.com/media/27010761/b2x.jpg')
    EXMR = Coin(currency='EXMR', full_name='EXMR', id='EXMR', url='https://www.cryptocompare.com/media/34836030/exmr.png')
    FSN = Coin(currency='FSN', full_name='Fusion', id='FSN', url='https://www.cryptocompare.com/media/27010765/fsn.png')
    UETL = Coin(currency='UETL', full_name='Useless Eth Token Lite', id='UETL', url='https://www.cryptocompare.com/media/27010771/uetl.jpg')
    NBR = Coin(currency='NBR', full_name='Niobio Cash', id='NBR', url='https://www.cryptocompare.com/media/27010775/nbr.jpg')
    ARY = Coin(currency='ARY', full_name='Block Array', id='ARY', url='https://www.cryptocompare.com/media/27010774/ary.png')
    RAVE = Coin(currency='RAVE', full_name='Ravelous', id='RAVE', url='https://www.cryptocompare.com/media/27010776/rave.jpg')
    ILT = Coin(currency='ILT', full_name='iOlite', id='ILT', url='https://www.cryptocompare.com/media/27010772/iqt.png')
    SCOOBY = Coin(currency='SCOOBY', full_name='Scooby coin', id='SCOOBY', url='https://www.cryptocompare.com/media/27010777/scooby.jpg')
    CEFS = Coin(currency='CEFS', full_name='CryptopiaFeeShares', id='CEFS', url='https://www.cryptocompare.com/media/27010779/cefs.png')
    BUN = Coin(currency='BUN', full_name='BunnyCoin', id='BUN', url='https://www.cryptocompare.com/media/27010781/bun.png')
    BSR = Coin(currency='BSR', full_name='BitSoar Coin', id='BSR', url='https://www.cryptocompare.com/media/27010783/bsr.png')
    SKULL = Coin(currency='SKULL', full_name='Pirate Blocks', id='SKULL', url='https://www.cryptocompare.com/media/27010785/skull.jpg')
    TRDT = Coin(currency='TRDT', full_name='Trident', id='TRDT', url='https://www.cryptocompare.com/media/27010784/trdt.png')
    XBTY = Coin(currency='XBTY', full_name='Bounty', id='XBTY', url='https://www.cryptocompare.com/media/27010787/xbty.jpg')
    JC = Coin(currency='JC', full_name='JesusCoin', id='JC', url='https://www.cryptocompare.com/media/27010790/jc.png')
    BTCP = Coin(currency='BTCP', full_name='Bitcoin Private', id='BTCP', url='https://www.cryptocompare.com/media/27010791/btcpjpg.png')
    SKC = Coin(currency='SKC', full_name='Skeincoin', id='SKC', url='https://www.cryptocompare.com/media/27010793/skc.jpg')
    MWAT = Coin(currency='MWAT', full_name='RED MegaWatt', id='MWAT', url='https://www.cryptocompare.com/media/27010794/mwat.jpg')
    JEW = Coin(currency='JEW', full_name='Shekel', id='JEW', url='https://www.cryptocompare.com/media/27010795/untitled-1.png')
    KRM = Coin(currency='KRM', full_name='Karma', id='KRM', url='https://www.cryptocompare.com/media/27010812/krm.png')
    HT = Coin(currency='HT', full_name='Huobi Token', id='HT', url='https://www.cryptocompare.com/media/27010813/ht.png')
    CDY = Coin(currency='CDY', full_name='Bitcoin Candy', id='CDY', url='https://www.cryptocompare.com/media/27010814/bcy.jpg')
    SSS = Coin(currency='SSS', full_name='ShareChain', id='SSS', url='https://www.cryptocompare.com/media/27010815/sss.png')
    CRDNC = Coin(currency='CRDNC', full_name='Credence Coin', id='CRDNC', url='https://www.cryptocompare.com/media/27010816/crdnc.png')
    BIFI = Coin(currency='BIFI', full_name='BitcoinFile', id='BIFI', url='https://www.cryptocompare.com/media/27010817/bifi.png')
    BTF = Coin(currency='BTF', full_name='Blockchain Traded Fund', id='BTF', url='https://www.cryptocompare.com/media/27010823/btf.jpg')
    SHOW = Coin(currency='SHOW', full_name='ShowCoin', id='SHOW', url='https://www.cryptocompare.com/media/27010825/show.jpg')
    STC = Coin(currency='STC', full_name='StarChain', id='STC', url='https://www.cryptocompare.com/media/27010826/stc.jpg')
    AIT = Coin(currency='AIT', full_name='AIChain Token', id='AIT', url='https://www.cryptocompare.com/media/27010829/ait.jpg')
    STQ = Coin(currency='STQ', full_name='Storiqa Token', id='STQ', url='https://www.cryptocompare.com/media/27010830/stq.jpg')
    ALT = Coin(currency='ALT', full_name='ALTcoin', id='ALT', url='https://www.cryptocompare.com/media/27010831/alt.jpg')
    TRF = Coin(currency='TRF', full_name='Travelflex', id='TRF', url='https://www.cryptocompare.com/media/27010832/trf.png')
    KB3 = Coin(currency='KB3', full_name='B3Coin', id='KB3', url='https://www.cryptocompare.com/media/27010833/kb3.jpg')
    FDX = Coin(currency='FDX', full_name='fidentiaX', id='FDX', url='https://www.cryptocompare.com/media/27010834/fdx.jpg')
    KREDS = Coin(currency='KREDS', full_name='KREDS', id='KREDS', url='https://www.cryptocompare.com/media/27010837/kreds.png')
    EQL = Coin(currency='EQL', full_name='EQUAL', id='EQL', url='https://www.cryptocompare.com/media/27010838/eql.jpg')
    GAI = Coin(currency='GAI', full_name='GraphGrail AI', id='GAI', url='https://www.cryptocompare.com/media/27010839/gai.png')
    VULC = Coin(currency='VULC', full_name='Vulcano', id='VULC', url='https://www.cryptocompare.com/media/35309111/vulc.png')
    DADI = Coin(currency='DADI', full_name='DADI', id='DADI', url='https://www.cryptocompare.com/media/27010852/dadi.png')
    UNRC = Coin(currency='UNRC', full_name='UniversalRoyalCoin', id='UNRC', url='https://www.cryptocompare.com/media/27010854/unrc.png')
    BBP = Coin(currency='BBP', full_name='BiblePay', id='BBP', url='https://www.cryptocompare.com/media/27010855/bbp.png')
    NOX = Coin(currency='NOX', full_name='NITRO', id='NOX', url='https://www.cryptocompare.com/media/27010857/nox.jpg')
    HYS = Coin(currency='HYS', full_name='Heiss Shares', id='HYS', url='https://www.cryptocompare.com/media/27010859/hys.jpg')
    LCWP = Coin(currency='LCWP', full_name='LiteCoinW Plus', id='LCWP', url='https://www.cryptocompare.com/media/27010860/lcwp.jpg')
    NAVI = Coin(currency='NAVI', full_name='NaviAddress', id='NAVI', url='https://www.cryptocompare.com/media/27010863/navi.png')
    ADI = Coin(currency='ADI', full_name='Aditus', id='ADI', url='https://www.cryptocompare.com/media/27010865/adi.jpg')
    TEN = Coin(currency='TEN', full_name='Tokenomy', id='TEN', url='https://www.cryptocompare.com/media/27010864/ten.png')
    VVI = Coin(currency='VVI', full_name='VV Coin', id='VVI', url='https://www.cryptocompare.com/media/27010869/vvi.png')
    ANK = Coin(currency='ANK', full_name='Ankorus Token', id='ANK', url='https://www.cryptocompare.com/media/27010873/ank.jpg')
    IVC = Coin(currency='IVC', full_name='Investy Coin', id='IVC', url='https://www.cryptocompare.com/media/27010876/ivc.jpg')
    HLP = Coin(currency='HLP', full_name='Purpose Coin', id='HLP', url='https://www.cryptocompare.com/media/27010877/hlp.png')
    VIN = Coin(currency='VIN', full_name='VinChain', id='VIN', url='https://www.cryptocompare.com/media/27010882/vin.jpg')
    SHPING = Coin(currency='SHPING', full_name='Shping Coin', id='SHPING', url='https://www.cryptocompare.com/media/27010884/shping.png')
    PTR = Coin(currency='PTR', full_name='Petro', id='PTR', url='https://www.cryptocompare.com/media/27010888/ptr.png')
    LCC = Coin(currency='LCC', full_name='LitecoinCash', id='LCC', url='https://www.cryptocompare.com/media/34478345/lcc.png')
    VANY = Coin(currency='VANY', full_name='Vanywhere', id='VANY', url='https://www.cryptocompare.com/media/27010900/vany.png')
    TFD = Coin(currency='TFD', full_name='TE-FOOD', id='TFD', url='https://www.cryptocompare.com/media/27010902/tfood.jpg')
    NBX = Coin(currency='NBX', full_name='Noxbox', id='NBX', url='https://www.cryptocompare.com/media/27010901/nbx.png')
    BAX = Coin(currency='BAX', full_name='BABB', id='BAX', url='https://www.cryptocompare.com/media/27010904/bax.jpg')
    BERRY = Coin(currency='BERRY', full_name='Rentberry', id='BERRY', url='https://www.cryptocompare.com/media/27010907/berry.jpg')
    FLIP = Coin(currency='FLIP', full_name='BitFlip', id='FLIP', url='https://www.cryptocompare.com/media/27010910/flip.png')
    CLIN = Coin(currency='CLIN', full_name='Clinicoin', id='CLIN', url='https://www.cryptocompare.com/media/27010911/clin.png')
    DHT = Coin(currency='DHT', full_name='DeHedge Token', id='DHT', url='https://www.cryptocompare.com/media/27010912/dht.png')
    ENK = Coin(currency='ENK', full_name='Enkidu', id='ENK', url='https://www.cryptocompare.com/media/27010914/enk.png')
    ALX = Coin(currency='ALX', full_name='ALAX', id='ALX', url='https://www.cryptocompare.com/media/27010915/alx.jpg')
    REN = Coin(currency='REN', full_name='Republic Token', id='REN', url='https://www.cryptocompare.com/media/27010916/ren.jpg')
    DTH = Coin(currency='DTH', full_name='Dether', id='DTH', url='https://www.cryptocompare.com/media/27010917/dth.jpg')
    SOC = Coin(currency='SOC', full_name='All Sports Coin', id='SOC', url='https://www.cryptocompare.com/media/27010918/soc.png')
    TDX = Coin(currency='TDX', full_name='Tidex Token', id='TDX', url='https://www.cryptocompare.com/media/27010919/tdx.png')
    LOT = Coin(currency='LOT', full_name='LottoCoin', id='LOT', url='https://www.cryptocompare.com/media/27010925/lot.png')
    FUNK = Coin(currency='FUNK', full_name='Cypherfunks Coin', id='FUNK', url='https://www.cryptocompare.com/media/27010926/funk.png')
    LEAF = Coin(currency='LEAF', full_name='LeafCoin', id='LEAF', url='https://www.cryptocompare.com/media/27010927/leaf.jpg')
    COMP = Coin(currency='COMP', full_name='Compound Coin', id='COMP', url='https://www.cryptocompare.com/media/27010929/comp.jpg')
    BITCAR = Coin(currency='BITCAR', full_name='BitCar', id='BITCAR', url='https://www.cryptocompare.com/media/27010931/bitcar.png')
    CLN = Coin(currency='CLN', full_name='Colu Local Network', id='CLN', url='https://www.cryptocompare.com/media/27010933/cln.png')
    NIHL = Coin(currency='NIHL', full_name='Nihilo Coin', id='NIHL', url='https://www.cryptocompare.com/media/27010943/nihl.png')
    BASHC = Coin(currency='BASHC', full_name='BashCoin', id='BASHC', url='https://www.cryptocompare.com/media/27010941/bashc.png')
    DIGIF = Coin(currency='DIGIF', full_name='DigiFel', id='DIGIF', url='https://www.cryptocompare.com/media/27010942/digif.png')
    DGM = Coin(currency='DGM', full_name='DigiMoney', id='DGM', url='https://www.cryptocompare.com/media/27010944/dgm.png')
    CBS = Coin(currency='CBS', full_name='Cerberus', id='CBS', url='https://www.cryptocompare.com/media/27010945/cbs.png')
    TERN = Coin(currency='TERN', full_name='Ternio', id='TERN', url='https://www.cryptocompare.com/media/27010948/tern.jpg')
    SVD = Coin(currency='SVD', full_name='savedroid', id='SVD', url='https://www.cryptocompare.com/media/35309230/svd.png')
    PROOF = Coin(currency='PROOF', full_name='PROVER', id='PROOF', url='https://www.cryptocompare.com/media/27010950/untitled-1.png')
    BTCH = Coin(currency='BTCH', full_name='Bitcoin Hush', id='BTCH', url='https://www.cryptocompare.com/media/27010951/btch.jpg')
    redBUX = Coin(currency='redBUX', full_name='redBUX', id='redBUX', url='https://www.cryptocompare.com/media/30001743/redbux.png')
    AUC = Coin(currency='AUC', full_name='Auctus', id='AUC', url='https://www.cryptocompare.com/media/27010954/untitled-1.png')
    LIZ = Coin(currency='LIZ', full_name='Lizus Payment', id='LIZ', url='https://www.cryptocompare.com/media/27010957/liz.png')
    CIF = Coin(currency='CIF', full_name='Crypto Improvement Fund', id='CIF', url='https://www.cryptocompare.com/media/27010958/cif.png')
    NCASH = Coin(currency='NCASH', full_name='Nucleus Vision', id='NCASH', url='https://www.cryptocompare.com/media/27010960/untitled-1.png')
    SPD = Coin(currency='SPD', full_name='Stipend', id='SPD', url='https://www.cryptocompare.com/media/27010967/spd.png')
    CMCT = Coin(currency='CMCT', full_name='Crowd Machine', id='CMCT', url='https://www.cryptocompare.com/media/27010977/cmct.png')
    FILL = Coin(currency='FILL', full_name='Fillit', id='FILL', url='https://www.cryptocompare.com/media/27011029/fil1.png')
    POA = Coin(currency='POA', full_name='Poa Network', id='POA', url='https://www.cryptocompare.com/media/35280537/poa.png')
    RVN = Coin(currency='RVN', full_name='Ravencoin', id='RVN', url='https://www.cryptocompare.com/media/27011010/rvn.jpg')
    XNK = Coin(currency='XNK', full_name='Ink Protocol', id='XNK', url='https://www.cryptocompare.com/media/27011011/xnk.jpg')
    XYO = Coin(currency='XYO', full_name='XY Oracle', id='XYO', url='https://www.cryptocompare.com/media/27011014/untitled-1.png')
    RFR = Coin(currency='RFR', full_name='Refereum', id='RFR', url='https://www.cryptocompare.com/media/27011023/rfr.png')
    PROPS = Coin(currency='PROPS', full_name='Props', id='PROPS', url='https://www.cryptocompare.com/media/27011028/props.jpg')
    CEDEX = Coin(currency='CEDEX', full_name='CEDEX Coin', id='CEDEX', url='https://www.cryptocompare.com/media/34478425/cedex.png')
    FUND = Coin(currency='FUND', full_name='Fund Platform', id='FUND', url='https://www.cryptocompare.com/media/27011031/fund.png')
    CEL = Coin(currency='CEL', full_name='Celsius Network', id='CEL', url='https://www.cryptocompare.com/media/27011043/cel.png')
    PUSHI = Coin(currency='PUSHI', full_name='Pushi', id='PUSHI', url='https://www.cryptocompare.com/media/27011046/pushi.png')
    BINS = Coin(currency='BINS', full_name='Bitsense', id='BINS', url='https://www.cryptocompare.com/media/27011047/bins.jpg')
    POKER = Coin(currency='POKER', full_name='PokerCoin', id='POKER', url='https://www.cryptocompare.com/media/27011048/poker.jpg')
    AXYS = Coin(currency='AXYS', full_name='Axys', id='AXYS', url='https://www.cryptocompare.com/media/27011049/axys.jpg')
    BOLD = Coin(currency='BOLD', full_name='Bold', id='BOLD', url='https://www.cryptocompare.com/media/27011051/bold.jpg')
    EXTN = Coin(currency='EXTN', full_name='Extensive Coin', id='EXTN', url='https://www.cryptocompare.com/media/27011052/extn.jpg')
    DIG = Coin(currency='DIG', full_name='Dignity', id='DIG', url='https://www.cryptocompare.com/media/30001609/dig.png')
    ETS = Coin(currency='ETS', full_name='ETH Share', id='ETS', url='https://www.cryptocompare.com/media/27011054/ets.jpg')
    LIPC = Coin(currency='LIPC', full_name='LIpcoin', id='LIPC', url='https://www.cryptocompare.com/media/27011055/lipc.jpg')
    HELL = Coin(currency='HELL', full_name='HELL COIN', id='HELL', url='https://www.cryptocompare.com/media/30001610/hell.jpg')
    ELP = Coin(currency='ELP', full_name='Ellerium', id='ELP', url='https://www.cryptocompare.com/media/30001611/elp.png')
    ACAT = Coin(currency='ACAT', full_name='Alphacat', id='ACAT', url='https://www.cryptocompare.com/media/30001613/acat.jpg')
    RKT = Coin(currency='RKT', full_name='Rock Token', id='RKT', url='https://www.cryptocompare.com/media/30001617/rkt.jpg')
    ELI = Coin(currency='ELI', full_name='Eligma', id='ELI', url='https://www.cryptocompare.com/media/30001620/rpqn1zqi_400x400.jpg')
    CO2 = Coin(currency='CO2', full_name='CO2 Token', id='CO2', url='https://www.cryptocompare.com/media/30001624/co2.png')
    INVOX = Coin(currency='INVOX', full_name='Invox Finance', id='INVOX', url='https://www.cryptocompare.com/media/30001639/untitled-1.png')
    VLX = Coin(currency='VLX', full_name='Velox', id='VLX', url='https://www.cryptocompare.com/media/30001652/vlx.png')
    ACTN = Coin(currency='ACTN', full_name='Action Coin', id='ACTN', url='https://www.cryptocompare.com/media/30001655/actn.jpg')
    LTCH = Coin(currency='LTCH', full_name='Litecoin Cash', id='LTCH', url='https://www.cryptocompare.com/media/30001658/ltch.png')
    ZUP = Coin(currency='ZUP', full_name='Zupply Token', id='ZUP', url='https://www.cryptocompare.com/media/30001659/zup.png')
    HMT = Coin(currency='HMT', full_name='Hamster Marketplace Token', id='HMT', url='https://www.cryptocompare.com/media/30001660/hmt.jpg')
    ONT = Coin(currency='ONT', full_name='Ontology', id='ONT', url='https://www.cryptocompare.com/media/30001663/ont.jpg')
    USCOIN = Coin(currency='USCOIN', full_name='USCoin', id='USCOIN', url='https://www.cryptocompare.com/media/30001666/untitled-1.png')
    KIND = Coin(currency='KIND', full_name='Kind Ads', id='KIND', url='https://www.cryptocompare.com/media/30001674/untitled-1.png')
    BCT = Coin(currency='BCT', full_name='Blockchain Terminal', id='BCT', url='https://www.cryptocompare.com/media/30001675/bct.png')
    CLO = Coin(currency='CLO', full_name='Callisto Network', id='CLO', url='https://www.cryptocompare.com/media/30001680/clo.png')
    CRU = Coin(currency='CRU', full_name='Curium', id='CRU', url='https://www.cryptocompare.com/media/30001681/cru.png')
    MOAT = Coin(currency='MOAT', full_name='Mother Of All Tokens', id='MOAT', url='https://www.cryptocompare.com/media/30001685/moat.jpg')
    BBI = Coin(currency='BBI', full_name='BelugaPay', id='BBI', url='https://www.cryptocompare.com/media/30001684/bbi.png')
    BEZ = Coin(currency='BEZ', full_name='Bezop', id='BEZ', url='https://www.cryptocompare.com/media/30001686/bez.jpg')
    ENTRC = Coin(currency='ENTRC', full_name='ENTER COIN', id='ENTRC', url='https://www.cryptocompare.com/media/30001688/entrc.jpg')
    BTCGO = Coin(currency='BTCGO', full_name='BitcoinGo', id='BTCGO', url='https://www.cryptocompare.com/media/30001689/btcgo.jpg')
    XTROPTIONS = Coin(currency='XTROPTIONS', full_name='TROPTIONS', id='XTROPTIONS', url='https://www.cryptocompare.com/media/30001691/xtroptions.jpg')
    KNW = Coin(currency='KNW', full_name='Knowledge ', id='KNW', url='https://www.cryptocompare.com/media/30001710/knowledge-icon-stroke-3.png')
    PGC = Coin(currency='PGC', full_name='Pegascoin', id='PGC', url='https://www.cryptocompare.com/media/30001697/pgc.jpg')
    BIT = Coin(currency='BIT', full_name='BitRewards', id='BIT', url='https://www.cryptocompare.com/media/30001705/bit.png')
    DATX = Coin(currency='DATX', full_name='DATx', id='DATX', url='https://www.cryptocompare.com/media/30001711/datx.jpg')
    PKC = Coin(currency='PKC', full_name='Pikciochain', id='PKC', url='https://www.cryptocompare.com/media/30001714/untitled-1.png')
    SQOIN = Coin(currency='SQOIN', full_name='StasyQ', id='SQOIN', url='https://www.cryptocompare.com/media/30001720/sqoin.jpg')
    TBAR = Coin(currency='TBAR', full_name='Titanium BAR', id='TBAR', url='https://www.cryptocompare.com/media/30001724/tbar.png')
    CPL = Coin(currency='CPL', full_name='CoinPlace Token', id='CPL', url='https://www.cryptocompare.com/media/30001726/cpl.png')
    TUBE = Coin(currency='TUBE', full_name='BitTube', id='TUBE', url='https://www.cryptocompare.com/media/33842919/tube.png')
    AUTO = Coin(currency='AUTO', full_name='Cube', id='AUTO', url='https://www.cryptocompare.com/media/30001729/untitled-1.png')
    OMX = Coin(currency='OMX', full_name='Project Shivom', id='OMX', url='https://www.cryptocompare.com/media/30001732/omx.jpg')
    TRCK = Coin(currency='TRCK', full_name='Truckcoin', id='TRCK', url='https://www.cryptocompare.com/media/30001735/trck.jpg')
    SNX = Coin(currency='SNX', full_name='Synthetix', id='SNX', url='https://www.cryptocompare.com/media/35309690/hav.png')
    TOMO = Coin(currency='TOMO', full_name='TomoChain', id='TOMO', url='https://www.cryptocompare.com/media/30001748/tomo.jpg')
    CHI = Coin(currency='CHI', full_name='XAYA', id='CHI', url='https://www.cryptocompare.com/media/34478236/chi.png')
    W3C = Coin(currency='W3C', full_name='W3Coin', id='W3C', url='https://www.cryptocompare.com/media/30001759/untitled-1.png')
    DIN = Coin(currency='DIN', full_name='Dinero', id='DIN', url='https://www.cryptocompare.com/media/30001760/din.jpg')
    INSTAR = Coin(currency='INSTAR', full_name='Insights Network', id='INSTAR', url='https://www.cryptocompare.com/media/30001761/instar.png')
    CHP = Coin(currency='CHP', full_name='CoinPoker Token', id='CHP', url='https://www.cryptocompare.com/media/30001762/chp.jpg')
    PSD = Coin(currency='PSD', full_name='Poseidon', id='PSD', url='https://www.cryptocompare.com/media/30001764/psd.png')
    J8T = Coin(currency='J8T', full_name='JET8', id='J8T', url='https://www.cryptocompare.com/media/30001765/jt8.png')
    LELE = Coin(currency='LELE', full_name='Lelecoin', id='LELE', url='https://www.cryptocompare.com/media/30001766/lele.png')
    DROP = Coin(currency='DROP', full_name='Dropil', id='DROP', url='https://www.cryptocompare.com/media/30001849/drop.jpg')
    AKA = Coin(currency='AKA', full_name='Akroma', id='AKA', url='https://www.cryptocompare.com/media/30001848/aka.jpg')
    SHIP = Coin(currency='SHIP', full_name='ShipChain', id='SHIP', url='https://www.cryptocompare.com/media/30001824/untitled-1.png')
    IHT = Coin(currency='IHT', full_name='I-House Token', id='IHT', url='https://www.cryptocompare.com/media/30001831/iht.jpg')
    LCS = Coin(currency='LCS', full_name='LocalCoinSwap', id='LCS', url='https://www.cryptocompare.com/media/35309764/lcs.jpg')
    LALA = Coin(currency='LALA', full_name='LaLa World', id='LALA', url='https://www.cryptocompare.com/media/30001833/lala.jpg')
    LEDU = Coin(currency='LEDU', full_name='Education Ecosystem', id='LEDU', url='https://www.cryptocompare.com/media/30001836/ledu.png')
    FOXT = Coin(currency='FOXT', full_name='Fox Trading', id='FOXT', url='https://www.cryptocompare.com/media/30001842/foxt.jpg')
    ETKN = Coin(currency='ETKN', full_name='EasyToken', id='ETKN', url='https://www.cryptocompare.com/media/30001841/etnk.png')
    ROX = Coin(currency='ROX', full_name='Robotina', id='ROX', url='https://www.cryptocompare.com/media/30001850/untitled-1.png')
    ADM = Coin(currency='ADM', full_name='Adamant', id='ADM', url='https://www.cryptocompare.com/media/30001860/adm.png')
    AMBT = Coin(currency='AMBT', full_name='AMBT Token', id='AMBT', url='https://www.cryptocompare.com/media/30001865/ambt.png')
    MEE = Coin(currency='MEE', full_name='CoinMeet', id='MEE', url='https://www.cryptocompare.com/media/30001874/mee.jpg')
    BTRM = Coin(currency='BTRM', full_name='Betrium Token', id='BTRM', url='https://www.cryptocompare.com/media/30001875/btrm.png')
    MANNA = Coin(currency='MANNA', full_name='Manna', id='MANNA', url='https://www.cryptocompare.com/media/30001876/manna.jpg')
    PROD = Coin(currency='PROD', full_name='Darenta', id='PROD', url='https://www.cryptocompare.com/media/30001878/prod.jpg')
    ePRX = Coin(currency='ePRX', full_name='eProxy', id='ePRX', url='https://www.cryptocompare.com/media/30001877/eprx.jpg')
    HMC = Coin(currency='HMC', full_name='Hi Mutual Society', id='HMC', url='https://www.cryptocompare.com/media/30001881/hmc.jpg')
    ZIX = Coin(currency='ZIX', full_name='ZIX Token', id='ZIX', url='https://www.cryptocompare.com/media/30001884/zix.png')
    ELEC = Coin(currency='ELEC', full_name='Electrify.Asia', id='ELEC', url='https://www.cryptocompare.com/media/30001886/elec.jpg')
    ORGT = Coin(currency='ORGT', full_name='Organic Token', id='ORGT', url='https://www.cryptocompare.com/media/30001887/e.png')
    LOOM = Coin(currency='LOOM', full_name='Loom Network', id='LOOM', url='https://www.cryptocompare.com/media/30001890/untitled-1.png')
    PAN = Coin(currency='PAN', full_name='Pantos', id='PAN', url='https://www.cryptocompare.com/media/30001898/untitled-1.png')
    BOTC = Coin(currency='BOTC', full_name='BotChain', id='BOTC', url='https://www.cryptocompare.com/media/30001908/untitled-1.png')
    GO = Coin(currency='GO', full_name='GoChain', id='GO', url='https://www.cryptocompare.com/media/30001914/goc.png')
    VIEW = Coin(currency='VIEW', full_name='Viewly', id='VIEW', url='https://www.cryptocompare.com/media/30001915/untitled-1.png')
    OKOIN = Coin(currency='OKOIN', full_name='OKOIN', id='OKOIN', url='https://www.cryptocompare.com/media/30001925/okoin.png')
    ADK = Coin(currency='ADK', full_name='Aidos Kuneen', id='ADK', url='https://www.cryptocompare.com/media/30001930/adk.jpg')
    GRAM = Coin(currency='GRAM', full_name='Telegram Open Network', id='GRAM', url='https://www.cryptocompare.com/media/30001931/gram.png')
    ESS = Coin(currency='ESS', full_name='Essentia', id='ESS', url='https://www.cryptocompare.com/media/30001932/ess.png')
    VIT = Coin(currency='VIT', full_name='Vice Industry Token', id='VIT', url='https://www.cryptocompare.com/media/30001936/untitled-1.png')
    SERA = Coin(currency='SERA', full_name='Seraph', id='SERA', url='https://www.cryptocompare.com/media/30001937/untitled-1.png')
    AET = Coin(currency='AET', full_name='AfterEther', id='AET', url='https://www.cryptocompare.com/media/30001955/aet.jpg')
    CMOS = Coin(currency='CMOS', full_name='Cosmo', id='CMOS', url='https://www.cryptocompare.com/media/30001956/cmos.jpg')
    PGN = Coin(currency='PGN', full_name='Pigeoncoin', id='PGN', url='https://www.cryptocompare.com/media/30001959/pgn.png')
    BMH = Coin(currency='BMH', full_name='BlockMesh', id='BMH', url='https://www.cryptocompare.com/media/30001961/mesh.jpg')
    TT = Coin(currency='TT', full_name='TravelChain', id='TT', url='https://www.cryptocompare.com/media/30001962/tt.jpg')
    REDN = Coin(currency='REDN', full_name='Reden', id='REDN', url='https://www.cryptocompare.com/media/33187870/redn.png')
    TLP = Coin(currency='TLP', full_name='TulipCoin', id='TLP', url='https://www.cryptocompare.com/media/30001964/tlp.jpg')
    BSX = Coin(currency='BSX', full_name='Bitspace', id='BSX', url='https://www.cryptocompare.com/media/30001965/bsx.jpg')
    BBN = Coin(currency='BBN', full_name='BBNCOIN', id='BBN', url='https://www.cryptocompare.com/media/30001968/bbn.jpg')
    TDZ = Coin(currency='TDZ', full_name='Tradelize', id='TDZ', url='https://www.cryptocompare.com/media/30001966/tdz.png')
    PAVO = Coin(currency='PAVO', full_name='Pavocoin', id='PAVO', url='https://www.cryptocompare.com/media/30001969/photo_2018-04-04_18-01-12.jpg')
    TUSD = Coin(currency='TUSD', full_name='True USD', id='TUSD', url='https://www.cryptocompare.com/media/30001972/tusd.png')
    LDN = Coin(currency='LDN', full_name='Lydiancoin', id='LDN', url='https://www.cryptocompare.com/media/30001976/ldn.jpg')
    BUBO = Coin(currency='BUBO', full_name='Budbo', id='BUBO', url='https://www.cryptocompare.com/media/30001978/bubo.jpg')
    USOAMIC = Coin(currency='USOAMIC', full_name='USOAMIC', id='USOAMIC', url='https://www.cryptocompare.com/media/30001984/usoamic.jpg')
    FLUZ = Coin(currency='FLUZ', full_name='FluzFluz', id='FLUZ', url='https://www.cryptocompare.com/media/30001985/fluz.jpg')
    IPSX = Coin(currency='IPSX', full_name='IP Exchange', id='IPSX', url='https://www.cryptocompare.com/media/30001989/ipsx.png')
    MIO = Coin(currency='MIO', full_name='Miner One token', id='MIO', url='https://www.cryptocompare.com/media/30001998/mio.png')
    AIC = Coin(currency='AIC', full_name='AI Crypto', id='AIC', url='https://www.cryptocompare.com/media/32655843/aic.png')
    MITH = Coin(currency='MITH', full_name='Mithril', id='MITH', url='https://www.cryptocompare.com/media/30002012/mith.jpg')
    FNO = Coin(currency='FNO', full_name='Fonero', id='FNO', url='https://www.cryptocompare.com/media/30002174/fno.png')
    PAS = Coin(currency='PAS', full_name='Passive Coin', id='PAS', url='https://www.cryptocompare.com/media/30002018/pas.jpg')
    XSG = Coin(currency='XSG', full_name='Snowgem', id='XSG', url='https://www.cryptocompare.com/media/30002019/sng.jpg')
    CVTC = Coin(currency='CVTC', full_name='CavatCoin', id='CVTC', url='https://www.cryptocompare.com/media/30002020/cvtc.jpg')
    PLMT = Coin(currency='PLMT', full_name='Pallium', id='PLMT', url='https://www.cryptocompare.com/media/30002021/plmt.png')
    FARM = Coin(currency='FARM', full_name='FARM Coin', id='FARM', url='https://www.cryptocompare.com/media/30002023/faarm.jpg')
    NEXT = Coin(currency='NEXT', full_name='Next.exchange Token', id='NEXT', url='https://www.cryptocompare.com/media/30002030/next.jpg')
    RNTB = Coin(currency='RNTB', full_name='BitRent', id='RNTB', url='https://www.cryptocompare.com/media/30002046/rntb.jpg')
    XCLR = Coin(currency='XCLR', full_name='ClearCoin', id='XCLR', url='https://www.cryptocompare.com/media/30002047/clr.png')
    SWTH = Coin(currency='SWTH', full_name='Switcheo', id='SWTH', url='https://www.cryptocompare.com/media/30002053/swh.jpg')
    FDZ = Coin(currency='FDZ', full_name='Friendz', id='FDZ', url='https://www.cryptocompare.com/media/30002054/fdz.jpg')
    VTN = Coin(currency='VTN', full_name='Voltroon', id='VTN', url='https://www.cryptocompare.com/media/30002055/vtn.jpg')
    LION = Coin(currency='LION', full_name='CoinLion', id='LION', url='https://www.cryptocompare.com/media/30002060/lion.png')
    MASP = Coin(currency='MASP', full_name='Market.space', id='MASP', url='https://www.cryptocompare.com/media/30002079/masp.png')
    XTL = Coin(currency='XTL', full_name='Stellite', id='XTL', url='https://www.cryptocompare.com/media/30002080/xtl.jpg')
    UCN = Coin(currency='UCN', full_name='UC Coin', id='UCN', url='https://www.cryptocompare.com/media/30002081/ucn.jpg')
    HUR = Coin(currency='HUR', full_name='Hurify', id='HUR', url='https://www.cryptocompare.com/media/30002083/hur.png')
    BRIA = Coin(currency='BRIA', full_name='Briacoin', id='BRIA', url='https://www.cryptocompare.com/media/30002084/bria.jpg')
    IC = Coin(currency='IC', full_name='Ignition', id='IC', url='https://www.cryptocompare.com/media/30002085/ic.png')
    LATX = Coin(currency='LATX', full_name='LatiumX', id='LATX', url='https://www.cryptocompare.com/media/30002086/latx.jpg')
    ROI = Coin(currency='ROI', full_name='ROIcoin', id='ROI', url='https://www.cryptocompare.com/media/30002087/roi.jpg')
    ETHPR = Coin(currency='ETHPR', full_name='Ethereum Premium', id='ETHPR', url='https://www.cryptocompare.com/media/30002088/ethpr.jpg')
    MNB = Coin(currency='MNB', full_name='MoneyBag', id='MNB', url='https://www.cryptocompare.com/media/30002097/mnb.jpg')
    BTL = Coin(currency='BTL', full_name='Bitrolium', id='BTL', url='https://www.cryptocompare.com/media/30002099/btl.jpg')
    GOAL = Coin(currency='GOAL', full_name='Goal Bonanza', id='GOAL', url='https://www.cryptocompare.com/media/30002100/goal.jpg')
    RAC = Coin(currency='RAC', full_name='RAcoin', id='RAC', url='https://www.cryptocompare.com/media/30002101/rac.jpg')
    BEX = Coin(currency='BEX', full_name='BEX token', id='BEX', url='https://www.cryptocompare.com/media/30002102/bex.png')
    HOLD = Coin(currency='HOLD', full_name='HOLD', id='HOLD', url='https://www.cryptocompare.com/media/30002104/hold.png')
    EZT = Coin(currency='EZT', full_name='EZToken', id='EZT', url='https://www.cryptocompare.com/media/30002107/ezt.jpg')
    SOL = Coin(currency='SOL', full_name='Sola', id='SOL', url='https://www.cryptocompare.com/media/30002110/sol.jpg')
    VIC = Coin(currency='VIC', full_name='Victorium', id='VIC', url='https://www.cryptocompare.com/media/30002111/vic.jpg')
    XCM = Coin(currency='XCM', full_name='CoinMetro', id='XCM', url='https://www.cryptocompare.com/media/30002112/xcm1.jpg')
    NFN = Coin(currency='NFN', full_name='Nafen', id='NFN', url='https://www.cryptocompare.com/media/30002113/nfn.jpg')
    CEEK = Coin(currency='CEEK', full_name='CEEK Smart VR Token', id='CEEK', url='https://www.cryptocompare.com/media/30002124/ceek.png')
    WIIX = Coin(currency='WIIX', full_name='Wiix', id='WIIX', url='https://www.cryptocompare.com/media/30002135/wiix.jpg')
    EOSDAC = Coin(currency='EOSDAC', full_name='eosDAC', id='EOSDAC', url='https://www.cryptocompare.com/media/30002139/eosdac.png')
    BCI = Coin(currency='BCI', full_name='Bitcoin Interest', id='BCI', url='https://www.cryptocompare.com/media/30002141/bci.jpg')
    MEDIC = Coin(currency='MEDIC', full_name='MedicCoin', id='MEDIC', url='https://www.cryptocompare.com/media/30002146/medic.jpg')
    BBC = Coin(currency='BBC', full_name='TraDove B2BCoin', id='BBC', url='https://www.cryptocompare.com/media/35521019/bbc.png')
    KWH = Coin(currency='KWH', full_name='KWHCoin', id='KWH', url='https://www.cryptocompare.com/media/30002147/kwh.jpg')
    CTXC = Coin(currency='CTXC', full_name='Cortex', id='CTXC', url='https://www.cryptocompare.com/media/30002149/ctxc.png')
    VLD = Coin(currency='VLD', full_name='Valid', id='VLD', url='https://www.cryptocompare.com/media/30002154/vld.jpg')
    FTX = Coin(currency='FTX', full_name='FintruX', id='FTX', url='https://www.cryptocompare.com/media/30002155/ftx.jpg')
    GSI = Coin(currency='GSI', full_name='Globex SCI', id='GSI', url='https://www.cryptocompare.com/media/30002166/gsi.png')
    BDP = Coin(currency='BDP', full_name='Bidipass', id='BDP', url='https://www.cryptocompare.com/media/34478179/bdp.png')
    FLM = Coin(currency='FLM', full_name='FOLM coin', id='FLM', url='https://www.cryptocompare.com/media/30002171/flm.jpg')
    ALPS = Coin(currency='ALPS', full_name='Alpenschillling', id='ALPS', url='https://www.cryptocompare.com/media/30002172/alps.jpg')
    ZEL = Coin(currency='ZEL', full_name='Zelcash', id='ZEL', url='https://www.cryptocompare.com/media/30002173/zel.jpg')
    BKC = Coin(currency='BKC', full_name='Balkancoin', id='BKC', url='https://www.cryptocompare.com/media/30002175/bkc.jpg')
    BITG = Coin(currency='BITG', full_name='Bitcoin Green', id='BITG', url='https://www.cryptocompare.com/media/30002176/bitg.jpg')
    DEV = Coin(currency='DEV', full_name='Deviant Coin', id='DEV', url='https://www.cryptocompare.com/media/30002202/dev.jpg')
    CHT = Coin(currency='CHT', full_name='Countinghouse Fund', id='CHT', url='https://www.cryptocompare.com/media/30002203/cht.png')
    GEX = Coin(currency='GEX', full_name='GreenX', id='GEX', url='https://www.cryptocompare.com/media/30002206/gex.jpg')
    ABJ = Coin(currency='ABJ', full_name='Abjcoin', id='ABJ', url='https://www.cryptocompare.com/media/30002209/abj.png')
    FTW = Coin(currency='FTW', full_name='FutureWorks', id='FTW', url='https://www.cryptocompare.com/media/30002211/ftw.jpg')
    RAP = Coin(currency='RAP', full_name='Rapture', id='RAP', url='https://www.cryptocompare.com/media/30002214/rap.jpg')
    ARTE = Coin(currency='ARTE', full_name='Artemine', id='ARTE', url='https://www.cryptocompare.com/media/30002216/arte.jpg')
    ANI = Coin(currency='ANI', full_name='Animecoin', id='ANI', url='https://www.cryptocompare.com/media/30002219/ani.png')
    PHC = Coin(currency='PHC', full_name='Profit Hunters Coin', id='PHC', url='https://www.cryptocompare.com/media/30002220/phc.jpg')
    ETHM = Coin(currency='ETHM', full_name='Ethereum Meta', id='ETHM', url='https://www.cryptocompare.com/media/30002221/ethm.jpg')
    UBC = Coin(currency='UBC', full_name='Ubcoin', id='UBC', url='https://www.cryptocompare.com/media/30002222/ubc.jpg')
    SENC = Coin(currency='SENC', full_name='Sentinel Chain', id='SENC', url='https://www.cryptocompare.com/media/30002228/senc.jpg')
    PAT = Coin(currency='PAT', full_name='PATRON', id='PAT', url='https://www.cryptocompare.com/media/30002231/pat.png')
    LIGER = Coin(currency='LIGER', full_name='Ligercoin', id='LIGER', url='https://www.cryptocompare.com/media/30002232/liger.jpg')
    CHFN = Coin(currency='CHFN', full_name='NOKU CHF', id='CHFN', url='https://www.cryptocompare.com/media/30002224/noku.jpg')
    EURN = Coin(currency='EURN', full_name='NOKU EUR', id='EURN', url='https://www.cryptocompare.com/media/34478368/eurn.png')
    LEU = Coin(currency='LEU', full_name='CryptoLEU', id='LEU', url='https://www.cryptocompare.com/media/30002242/leu.jpg')
    SWC = Coin(currency='SWC', full_name='Scanetchain Token', id='SWC', url='https://www.cryptocompare.com/media/30002243/swc.png')
    SEM = Coin(currency='SEM', full_name='Semux', id='SEM', url='https://www.cryptocompare.com/media/30002248/sem.jpg')
    DARX = Coin(currency='DARX', full_name='Bitdaric', id='DARX', url='https://www.cryptocompare.com/media/30002249/darx.png')
    BBK = Coin(currency='BBK', full_name='BitBlocks', id='BBK', url='https://www.cryptocompare.com/media/30002250/bbk.jpg')
    NCT = Coin(currency='NCT', full_name='PolySwarm', id='NCT', url='https://www.cryptocompare.com/media/30002262/nct.png')
    UWC = Coin(currency='UWC', full_name='Uwezocoin', id='UWC', url='https://www.cryptocompare.com/media/30002269/uwc.jpg')
    UUU = Coin(currency='UUU', full_name='U Network', id='UUU', url='https://www.cryptocompare.com/media/30002272/uuu.png')
    XHV = Coin(currency='XHV', full_name='Haven Protocol', id='XHV', url='https://www.cryptocompare.com/media/30002273/xhv.png')
    CPX = Coin(currency='CPX', full_name='Apex Token', id='CPX', url='https://www.cryptocompare.com/media/30002271/cpx.jpg')
    DOCK = Coin(currency='DOCK', full_name='Dock.io', id='DOCK', url='https://www.cryptocompare.com/media/30002275/dock.png')
    EQC = Coin(currency='EQC', full_name='Ethereum Qchain Token', id='EQC', url='https://www.cryptocompare.com/media/30002277/eqcxqc.jpg')
    ADH = Coin(currency='ADH', full_name='Adhive', id='ADH', url='https://www.cryptocompare.com/media/30002279/adh.jpg')
    ZLA = Coin(currency='ZLA', full_name='Zilla', id='ZLA', url='https://www.cryptocompare.com/media/30002280/zla.jpg')
    LIF = Coin(currency='LIF', full_name='Winding Tree', id='LIF', url='https://www.cryptocompare.com/media/30002281/lif.jpg')
    EFX = Coin(currency='EFX', full_name='The EFFECT Network', id='EFX', url='https://www.cryptocompare.com/media/30002284/efx.jpg')
    LND = Coin(currency='LND', full_name='Lendingblock', id='LND', url='https://www.cryptocompare.com/media/30002285/lnd.jpg')
    FTO = Coin(currency='FTO', full_name='FuturoCoin', id='FTO', url='https://www.cryptocompare.com/media/30002288/fto.png')
    HPAY = Coin(currency='HPAY', full_name='HadePay', id='HPAY', url='https://www.cryptocompare.com/media/34478006/hpay.png')
    SIG = Coin(currency='SIG', full_name='Signal', id='SIG', url='https://www.cryptocompare.com/media/30002295/sig.jpg')
    CARE = Coin(currency='CARE', full_name='Carebit', id='CARE', url='https://www.cryptocompare.com/media/30002297/care.jpg')
    NZL = Coin(currency='NZL', full_name='Zealium', id='NZL', url='https://www.cryptocompare.com/media/30002301/nzl.jpg')
    TBT = Coin(currency='TBT', full_name='T-BOT', id='TBT', url='https://www.cryptocompare.com/media/30002303/tbt.jpg')
    XMC = Coin(currency='XMC', full_name='Monero Classic', id='XMC', url='https://www.cryptocompare.com/media/30002308/xmc.jpg')
    OAK = Coin(currency='OAK', full_name='Acorn Collective', id='OAK', url='https://www.cryptocompare.com/media/30002320/oak.png')
    DML = Coin(currency='DML', full_name='Decentralized Machine Learning', id='DML', url='https://www.cryptocompare.com/media/30002332/dml.jpg')
    GEM = Coin(currency='GEM', full_name='Gems', id='GEM', url='https://www.cryptocompare.com/media/30002334/gem.jpg')
    TIPS = Coin(currency='TIPS', full_name='FedoraCoin', id='TIPS', url='https://www.cryptocompare.com/media/30002340/tips.jpg')
    MOS = Coin(currency='MOS', full_name='MOS Coin', id='MOS', url='https://www.cryptocompare.com/media/32655838/mos.jpg')
    TBX = Coin(currency='TBX', full_name='Tokenbox', id='TBX', url='https://www.cryptocompare.com/media/32655844/tbx.jpg')
    PNT = Coin(currency='PNT', full_name='Penta', id='PNT', url='https://www.cryptocompare.com/media/32655845/pnt.jpg')
    WIN = Coin(currency='WIN', full_name='WCoin', id='WIN', url='https://www.cryptocompare.com/media/32655846/win.jpg')
    CHARM = Coin(currency='CHARM', full_name='Charm Coin', id='CHARM', url='https://www.cryptocompare.com/media/32655849/charm.jpg')
    PROTON = Coin(currency='PROTON', full_name='Proton', id='PROTON', url='https://www.cryptocompare.com/media/32655850/proton.jpg')
    CRS = Coin(currency='CRS', full_name='Cryptoreal', id='CRS', url='https://www.cryptocompare.com/media/32655853/crs.jpg')
    DERO = Coin(currency='DERO', full_name='Dero', id='DERO', url='https://www.cryptocompare.com/media/32655854/dero.jpg')
    DEAL = Coin(currency='DEAL', full_name='iDealCash', id='DEAL', url='https://www.cryptocompare.com/media/32655855/deal.jpg')
    JUMP = Coin(currency='JUMP', full_name='Jumpcoin', id='JUMP', url='https://www.cryptocompare.com/media/32655856/jump.jpg')
    ZCO = Coin(currency='ZCO', full_name='Zebi Coin', id='ZCO', url='https://www.cryptocompare.com/media/32655858/zco.jpg')
    KRL = Coin(currency='KRL', full_name='Kryll', id='KRL', url='https://www.cryptocompare.com/media/32655864/krl.jpg')
    NEXO = Coin(currency='NEXO', full_name='NEXO', id='NEXO', url='https://www.cryptocompare.com/media/32655865/nexo.jpg')
    CHX = Coin(currency='CHX', full_name='Chainium', id='CHX', url='https://www.cryptocompare.com/media/32655866/chx.jpg')
    SS = Coin(currency='SS', full_name='Sharder', id='SS', url='https://www.cryptocompare.com/media/32655869/ss.png')
    IFX = Coin(currency='IFX', full_name='Infinex', id='IFX', url='https://www.cryptocompare.com/media/32655870/ifx.png')
    XMO = Coin(currency='XMO', full_name='Monero Original', id='XMO', url='https://www.cryptocompare.com/media/32655873/xmo.jpg')
    EDU = Coin(currency='EDU', full_name='EduCoin', id='EDU', url='https://www.cryptocompare.com/media/34478255/edu.png')
    PCL = Coin(currency='PCL', full_name='Peculium', id='PCL', url='https://www.cryptocompare.com/media/32655889/pcl.jpg')
    MITX = Coin(currency='MITX', full_name='Morpheus Infrastructure Token', id='MITX', url='https://www.cryptocompare.com/media/32655903/mitx.jpg')
    APH = Coin(currency='APH', full_name='Aphelion', id='APH', url='https://www.cryptocompare.com/media/32655904/aph.jpg')
    NBAI = Coin(currency='NBAI', full_name='Nebula AI', id='NBAI', url='https://www.cryptocompare.com/media/32655907/nbai.jpg')
    CVT = Coin(currency='CVT', full_name='CyberVein', id='CVT', url='https://www.cryptocompare.com/media/32655908/cvt.jpg')
    TUT = Coin(currency='TUT', full_name='Tutellus', id='TUT', url='https://www.cryptocompare.com/media/32655909/tut.png')
    BETT = Coin(currency='BETT', full_name='Bettium', id='BETT', url='https://www.cryptocompare.com/media/32655922/bett.jpg')
    NOAH = Coin(currency='NOAH', full_name='NOAHCOIN', id='NOAH', url='https://www.cryptocompare.com/media/32655930/noah.jpg')
    PAL = Coin(currency='PAL', full_name='PolicyPal Network', id='PAL', url='https://www.cryptocompare.com/media/32655935/pal.png')
    ENU = Coin(currency='ENU', full_name='Enumivo', id='ENU', url='https://www.cryptocompare.com/media/32655936/enu.jpg')
    BFDT = Coin(currency='BFDT', full_name='Befund', id='BFDT', url='https://www.cryptocompare.com/media/32655938/bfdt.jpg')
    KEP = Coin(currency='KEP', full_name='Kepler', id='KEP', url='https://www.cryptocompare.com/media/32655941/kep.png')
    RUBY = Coin(currency='RUBY', full_name='Rubius', id='RUBY', url='https://www.cryptocompare.com/media/32655942/ruby.png')
    CTKN = Coin(currency='CTKN', full_name='Curaizon', id='CTKN', url='https://www.cryptocompare.com/media/32655945/ctkn.jpg')
    YUM = Coin(currency='YUM', full_name='Yumerium', id='YUM', url='https://www.cryptocompare.com/media/32655952/yum.png')
    GSC = Coin(currency='GSC', full_name='Global Social Chain', id='GSC', url='https://www.cryptocompare.com/media/33187819/gsc.png')
    DESI = Coin(currency='DESI', full_name='Desico', id='DESI', url='https://www.cryptocompare.com/media/33187822/desi.png')
    FNP = Coin(currency='FNP', full_name='FlipNpik', id='FNP', url='https://www.cryptocompare.com/media/33187823/fnp.jpg')
    VLUX = Coin(currency='VLUX', full_name='VLUX', id='VLUX', url='https://www.cryptocompare.com/media/33187827/vlux.png')
    MTC = Coin(currency='MTC', full_name='DOCADEMIC', id='MTC', url='https://www.cryptocompare.com/media/33187828/mtc.png')
    SSH = Coin(currency='SSH', full_name='StreamSpace', id='SSH', url='https://www.cryptocompare.com/media/33187832/ssh.png')
    XBI = Coin(currency='XBI', full_name='Bitcoin Incognito', id='XBI', url='https://www.cryptocompare.com/media/33187835/btci.jpg')
    TRUE = Coin(currency='TRUE', full_name='True Chain', id='TRUE', url='https://www.cryptocompare.com/media/33187843/true.jpg')
    MRK = Coin(currency='MRK', full_name='MARK.SPACE', id='MRK', url='https://www.cryptocompare.com/media/33187844/mrk.jpg')
    FRV = Coin(currency='FRV', full_name='Fitrova', id='FRV', url='https://www.cryptocompare.com/media/33187842/bcdw9qea_400x400.jpg')
    WINS = Coin(currency='WINS', full_name='WinStars', id='WINS', url='https://www.cryptocompare.com/media/33187846/wins.png')
    XES = Coin(currency='XES', full_name='Proxeus', id='XES', url='https://www.cryptocompare.com/media/33187847/rsz_fengcry6_400x400.jpg')
    RTB = Coin(currency='RTB', full_name='AB-CHAIN', id='RTB', url='https://www.cryptocompare.com/media/33187848/rsz_j0jj1fgb_400x400.jpg')
    FXT = Coin(currency='FXT', full_name='FuzeX', id='FXT', url='https://www.cryptocompare.com/media/33187853/bhbg2_sa_400x400.jpg')
    HYDRO = Coin(currency='HYDRO', full_name='Hydrogen', id='HYDRO', url='https://www.cryptocompare.com/media/33187856/rsz_prd5wxkj_400x400-1.jpg')
    DXC = Coin(currency='DXC', full_name='DixiCoin', id='DXC', url='https://www.cryptocompare.com/media/33187858/rsz_po0xsyaa_400x400.jpg')
    CHBR = Coin(currency='CHBR', full_name='CryptoHub', id='CHBR', url='https://www.cryptocompare.com/media/33187861/chbr.png')
    OWD = Coin(currency='OWD', full_name='Owlstand', id='OWD', url='https://www.cryptocompare.com/media/33187865/owd.png')
    ELLI = Coin(currency='ELLI', full_name='ElliotCoin', id='ELLI', url='https://www.cryptocompare.com/media/33187868/elli.jpg')
    AXS = Coin(currency='AXS', full_name='AXS', id='AXS', url='https://www.cryptocompare.com/media/33187869/axs.jpg')
    DAN = Coin(currency='DAN', full_name='Daneel', id='DAN', url='https://www.cryptocompare.com/media/33187871/dan.jpg')
    UBT = Coin(currency='UBT', full_name='UniBright', id='UBT', url='https://www.cryptocompare.com/media/33187875/rsz_6fqeq4zg_400x400-1.jpg')
    AMO = Coin(currency='AMO', full_name='AMO Coin', id='AMO', url='https://www.cryptocompare.com/media/35309355/amo.png')
    LBA = Coin(currency='LBA', full_name='Libra Credit', id='LBA', url='https://www.cryptocompare.com/media/33187882/rsz_b5olgqs7_400x400.jpg')
    LIVE = Coin(currency='LIVE', full_name='Live Stars', id='LIVE', url='https://www.cryptocompare.com/media/33187883/live.png')
    GBG = Coin(currency='GBG', full_name='Golos Gold', id='GBG', url='https://www.cryptocompare.com/media/1382246/golos.png')
    CNN = Coin(currency='CNN', full_name='Content Neutrality Network', id='CNN', url='https://www.cryptocompare.com/media/33187884/cnn.png')
    SHL = Coin(currency='SHL', full_name='Oyster Shell', id='SHL', url='https://www.cryptocompare.com/media/33187885/rsz_mhq4rzia_400x400.jpg')
    ETZ = Coin(currency='ETZ', full_name='EtherZero', id='ETZ', url='https://www.cryptocompare.com/media/33187887/rsz_obc3pjkr_400x400.jpg')
    SKM = Coin(currency='SKM', full_name='Skrumble Network', id='SKM', url='https://www.cryptocompare.com/media/33187888/skm.jpg')
    SHR = Coin(currency='SHR', full_name='ShareRing', id='SHR', url='https://www.cryptocompare.com/media/33187889/shr.png')
    UBEX = Coin(currency='UBEX', full_name='Ubex', id='UBEX', url='https://www.cryptocompare.com/media/33187892/ubex.png')
    IVY = Coin(currency='IVY', full_name='IvyKoin', id='IVY', url='https://www.cryptocompare.com/media/33187893/rsz_udyc4sjg_400x400.jpg')
    KEC = Coin(currency='KEC', full_name='KEYCO', id='KEC', url='https://www.cryptocompare.com/media/33187895/rsz_x8rkuu1o_400x400-1.png')
    ODE = Coin(currency='ODE', full_name='ODEM ', id='ODE', url='https://www.cryptocompare.com/media/33187894/rsz_rliunpu-_400x400.jpg')
    HOT = Coin(currency='HOT', full_name='Hydro Protocol', id='HOT', url='https://www.cryptocompare.com/media/33187896/hot.png')
    AMN = Coin(currency='AMN', full_name='Amon', id='AMN', url='https://www.cryptocompare.com/media/33187898/rsz_m8svzqju_400x400.jpg')
    SABR = Coin(currency='SABR', full_name='SABR Coin', id='SABR', url='https://www.cryptocompare.com/media/33187902/download.png')
    HWC = Coin(currency='HWC', full_name='HollyWoodCoin', id='HWC', url='https://www.cryptocompare.com/media/33187903/rsz_ti9rvys2_400x400.jpg')
    BITGOLD = Coin(currency='BITGOLD', full_name='bitGold', id='BITGOLD', url='https://www.cryptocompare.com/media/33187928/bitgold.png')
    BITSILVER = Coin(currency='BITSILVER', full_name='bitSilver', id='BITSILVER', url='https://www.cryptocompare.com/media/33187928/bitgold.png')
    GIN = Coin(currency='GIN', full_name='GINcoin', id='GIN', url='https://www.cryptocompare.com/media/33187910/0suib6bl_400x400.jpg')
    OPEN = Coin(currency='OPEN', full_name='Open Platform', id='OPEN', url='https://www.cryptocompare.com/media/33187913/ec78plgb_400x400.jpg')
    NLX = Coin(currency='NLX', full_name='Nullex', id='NLX', url='https://www.cryptocompare.com/media/33187915/rsz_k6egfcvp_400x400.jpg')
    FACE = Coin(currency='FACE', full_name='Faceter ', id='FACE', url='https://www.cryptocompare.com/media/33187920/rsz_xey-vj3j_400x400.jpg')
    MRPH = Coin(currency='MRPH', full_name='Morpheus Network', id='MRPH', url='https://www.cryptocompare.com/media/33187921/rsz_aqwlc_on_400x400.jpg')
    IOTX = Coin(currency='IOTX', full_name='IoTeX Network', id='IOTX', url='https://www.cryptocompare.com/media/33187927/rsz_njsdvvpv_400x400.jpg')
    STM = Coin(currency='STM', full_name='Streamity', id='STM', url='https://www.cryptocompare.com/media/33434194/rsz_tu_ozspz_400x400.jpg')
    ITL = Coin(currency='ITL', full_name='Italian Lira', id='ITL', url='https://www.cryptocompare.com/media/33434198/rsz_n6efwomu_400x400.jpg')
    AITT = Coin(currency='AITT', full_name='AITrading', id='AITT', url='https://www.cryptocompare.com/media/33434201/aitt.png')
    ITM = Coin(currency='ITM', full_name='intimate.io', id='ITM', url='https://www.cryptocompare.com/media/33434202/itm.jpg')
    VID = Coin(currency='VID', full_name='VideoCoin', id='VID', url='https://www.cryptocompare.com/media/33434208/vid.jpg')
    UCT = Coin(currency='UCT', full_name='UCOT', id='UCT', url='https://www.cryptocompare.com/media/33434210/uct.png')
    SNTR = Coin(currency='SNTR', full_name='Silent Notary', id='SNTR', url='https://www.cryptocompare.com/media/33434220/rqwcvdzw_400x400.jpg')
    ZMR = Coin(currency='ZMR', full_name='Monero 0', id='ZMR', url='https://www.cryptocompare.com/media/33434221/zmr.jpg')
    XMV = Coin(currency='XMV', full_name='MoneroV', id='XMV', url='https://www.cryptocompare.com/media/33434222/xmv.jpg')
    NKN = Coin(currency='NKN', full_name='NKN', id='NKN', url='https://www.cryptocompare.com/media/33434229/nkn.jpg')
    ELY = Coin(currency='ELY', full_name='Elysian', id='ELY', url='https://www.cryptocompare.com/media/33434230/ely.png')
    HER = Coin(currency='HER', full_name='Hero Node', id='HER', url='https://www.cryptocompare.com/media/33434231/her.jpg')
    PAR = Coin(currency='PAR', full_name='Parlay', id='PAR', url='https://www.cryptocompare.com/media/33434252/par.jpg')
    SLX = Coin(currency='SLX', full_name='Slate', id='SLX', url='https://www.cryptocompare.com/media/33434266/slx.jpg')
    LTCC = Coin(currency='LTCC', full_name='Listerclassic Coin', id='LTCC', url='https://www.cryptocompare.com/media/33434267/ltcc.jpg')
    RST = Coin(currency='RST', full_name='REGA Risk Sharing Token', id='RST', url='https://www.cryptocompare.com/media/33434268/rst.jpg')
    XBB = Coin(currency='XBB', full_name='BrickBlock', id='XBB', url='https://www.cryptocompare.com/media/34478343/brickblock.png')
    AMX = Coin(currency='AMX', full_name='Amero', id='AMX', url='https://www.cryptocompare.com/media/33434270/amx.jpg')
    TFC = Coin(currency='TFC', full_name='The Freedom Coin', id='TFC', url='https://www.cryptocompare.com/media/33434271/tfc.jpg')
    REPO = Coin(currency='REPO', full_name='Repo Coin', id='REPO', url='https://www.cryptocompare.com/media/33434275/repo.jpg')
    IRC = Coin(currency='IRC', full_name='IRONCOIN', id='IRC', url='https://www.cryptocompare.com/media/33434281/irc.jpg')
    OIO = Coin(currency='OIO', full_name='Online', id='OIO', url='https://www.cryptocompare.com/media/33434284/oio.png')
    ANGL = Coin(currency='ANGL', full_name='Angel Token', id='ANGL', url='https://www.cryptocompare.com/media/33434286/angl.jpg')
    ANTS = Coin(currency='ANTS', full_name='ANTS Reloaded', id='ANTS', url='https://www.cryptocompare.com/media/33434287/ants.jpg')
    KNG = Coin(currency='KNG', full_name='BetKings', id='KNG', url='https://www.cryptocompare.com/media/33434289/kng.jpg')
    CMM = Coin(currency='CMM', full_name='Commercium ', id='CMM', url='https://www.cryptocompare.com/media/33434296/commercium.jpg')
    STT = Coin(currency='STT', full_name='Staramba', id='STT', url='https://www.cryptocompare.com/media/33434302/stt.jpg')
    WYS = Coin(currency='WYS', full_name='Wysker', id='WYS', url='https://www.cryptocompare.com/media/33434303/wys.jpg')
    COG = Coin(currency='COG', full_name='Cognitio', id='COG', url='https://www.cryptocompare.com/media/33434304/cog.jpg')
    ZIPT = Coin(currency='ZIPT', full_name='Zippie', id='ZIPT', url='https://www.cryptocompare.com/media/33434305/zipt.jpg')
    QKC = Coin(currency='QKC', full_name='QuarkChain', id='QKC', url='https://www.cryptocompare.com/media/33434307/qkc.jpg')
    OSA = Coin(currency='OSA', full_name='Optimal Shelf Availability Token', id='OSA', url='https://www.cryptocompare.com/media/33434309/osa.jpg')
    EXC = Coin(currency='EXC', full_name='Eximchain', id='EXC', url='https://www.cryptocompare.com/media/33434310/exc.jpg')
    BEN = Coin(currency='BEN', full_name='BitCOEN', id='BEN', url='https://www.cryptocompare.com/media/33752288/ben.jpg')
    BCIO = Coin(currency='BCIO', full_name='Blockchain.io', id='BCIO', url='https://www.cryptocompare.com/media/33752293/blockchainio.png')
    BMK = Coin(currency='BMK', full_name='Benchmark', id='BMK', url='https://www.cryptocompare.com/media/33752294/bmk.png')
    ROC = Coin(currency='ROC', full_name='Rasputin Online Coin', id='ROC', url='https://www.cryptocompare.com/media/33842903/roc.jpg')
    BZNT = Coin(currency='BZNT', full_name='Bezant', id='BZNT', url='https://www.cryptocompare.com/media/33842907/bznt.jpg')
    LYL = Coin(currency='LYL', full_name='LoyalCoin', id='LYL', url='https://www.cryptocompare.com/media/33842908/lyl.jpg')
    FT = Coin(currency='FT', full_name='Fabric Token', id='FT', url='https://www.cryptocompare.com/media/33842909/ft.jpg')
    BMX = Coin(currency='BMX', full_name='BitMart Coin', id='BMX', url='https://www.cryptocompare.com/media/33842910/bmx.jpg')
    PHI = Coin(currency='PHI', full_name='PHI Token', id='PHI', url='https://www.cryptocompare.com/media/33842914/phi.jpg')
    PMNT = Coin(currency='PMNT', full_name='Paymon', id='PMNT', url='https://www.cryptocompare.com/media/33842921/pmnt.jpg')
    BNTN = Coin(currency='BNTN', full_name='Blocnation', id='BNTN', url='https://www.cryptocompare.com/media/33842923/bntn.png')
    HYT = Coin(currency='HYT', full_name='HoryouToken', id='HYT', url='https://www.cryptocompare.com/media/33842924/hyt.jpg')
    GRMD = Coin(currency='GRMD', full_name='GreenMed', id='GRMD', url='https://www.cryptocompare.com/media/33842930/grmd.jpg')
    SSC = Coin(currency='SSC', full_name='SelfSell', id='SSC', url='https://www.cryptocompare.com/media/33842931/ssc.jpg')
    LOKI = Coin(currency='LOKI', full_name='Loki', id='LOKI', url='https://www.cryptocompare.com/media/33842932/loki.jpg')
    BKT = Coin(currency='BKT', full_name='Blocktrade token', id='BKT', url='https://www.cryptocompare.com/media/35284307/btt.png')
    NCP = Coin(currency='NCP', full_name='Newton Coin', id='NCP', url='https://www.cryptocompare.com/media/33842936/ncp.jpg')
    MPT = Coin(currency='MPT', full_name='Media Protocol Token', id='MPT', url='https://www.cryptocompare.com/media/33842938/mpt1.png')
    STAX = Coin(currency='STAX', full_name='Staxcoin', id='STAX', url='https://www.cryptocompare.com/media/33842943/stax.png')
    MRN = Coin(currency='MRN', full_name='Mercoin', id='MRN', url='https://www.cryptocompare.com/media/33842946/mrn.png')
    FOPA = Coin(currency='FOPA', full_name='Fopacoin', id='FOPA', url='https://www.cryptocompare.com/media/33842947/fopa.jpg')
    CBC = Coin(currency='CBC', full_name='CashBet Coin', id='CBC', url='https://www.cryptocompare.com/media/33842951/cbc.jpg')
    OOT = Coin(currency='OOT', full_name='Utrum', id='OOT', url='https://www.cryptocompare.com/media/33842952/oot.jpg')
    NBC = Coin(currency='NBC', full_name='Niobium', id='NBC', url='https://www.cryptocompare.com/media/33842955/nbc.jpg')
    SIC = Coin(currency='SIC', full_name='Swisscoin', id='SIC', url='https://www.cryptocompare.com/media/33842956/sic.jpg')
    ALG = Coin(currency='ALG', full_name='Algory', id='ALG', url='https://www.cryptocompare.com/media/33842957/alg.jpg')
    PAI = Coin(currency='PAI', full_name='PCHAIN', id='PAI', url='https://www.cryptocompare.com/media/33842959/pai.png')
    EXCC = Coin(currency='EXCC', full_name='ExchangeCoin', id='EXCC', url='https://www.cryptocompare.com/media/33842976/excc.jpg')
    REL = Coin(currency='REL', full_name='Reliance', id='REL', url='https://www.cryptocompare.com/media/33842979/rel.jpg')
    BTCN = Coin(currency='BTCN', full_name='BitcoiNote', id='BTCN', url='https://www.cryptocompare.com/media/33957375/6g4_k7_o_400x400.jpg')
    HERO = Coin(currency='HERO', full_name='Hero', id='HERO', url='https://www.cryptocompare.com/media/33957376/hero.jpg')
    SEELE = Coin(currency='SEELE', full_name='Seele', id='SEELE', url='https://www.cryptocompare.com/media/33957378/seele.jpg')
    EJAC = Coin(currency='EJAC', full_name='EJA Coin', id='EJAC', url='https://www.cryptocompare.com/media/33957381/eja.jpg')
    APIS = Coin(currency='APIS', full_name='APIS', id='APIS', url='https://www.cryptocompare.com/media/33957383/apis.png')
    UPP = Coin(currency='UPP', full_name='Sentinel Protocol', id='UPP', url='https://www.cryptocompare.com/media/33957387/upp.jpg')
    XT3 = Coin(currency='XT3', full_name='Xt3ch', id='XT3', url='https://www.cryptocompare.com/media/33957391/8exrkue2_400x400.jpg')
    MGD = Coin(currency='MGD', full_name='MassGrid', id='MGD', url='https://www.cryptocompare.com/media/33957397/obltargr_400x400.jpg')
    PLURA = Coin(currency='PLURA', full_name='PluraCoin', id='PLURA', url='https://www.cryptocompare.com/media/33957400/plura.jpg')
    SWACH = Coin(currency='SWACH', full_name='Swachhcoin', id='SWACH', url='https://www.cryptocompare.com/media/33957403/scx.jpg')
    NWCN = Coin(currency='NWCN', full_name='NowCoin', id='NWCN', url='https://www.cryptocompare.com/media/33957401/nwcn.jpg')
    ICST = Coin(currency='ICST', full_name='ICST', id='ICST', url='https://www.cryptocompare.com/media/34077390/icst.png')
    PURK = Coin(currency='PURK', full_name='Purk', id='PURK', url='https://www.cryptocompare.com/media/34155611/purk.png')
    ROE = Coin(currency='ROE', full_name='Rover Coin', id='ROE', url='https://www.cryptocompare.com/media/34077407/roe.jpg')
    LTCP = Coin(currency='LTCP', full_name='LitecoinPro', id='LTCP', url='https://www.cryptocompare.com/media/34077408/ltcp.jpg')
    DKD = Coin(currency='DKD', full_name='Dekado', id='DKD', url='https://www.cryptocompare.com/media/34077409/dkd.png')
    LYNX = Coin(currency='LYNX', full_name='Lynx', id='LYNX', url='https://www.cryptocompare.com/media/34077410/lynx.jpg')
    POSQ = Coin(currency='POSQ', full_name='Poseidon Quark', id='POSQ', url='https://www.cryptocompare.com/media/34077414/posq.jpg')
    YCE = Coin(currency='YCE', full_name='MYCE', id='YCE', url='https://www.cryptocompare.com/media/34077420/yce.jpg')
    OCC = Coin(currency='OCC', full_name='Original Crypto Coin', id='OCC', url='https://www.cryptocompare.com/media/34077421/occ.jpg')
    STOR = Coin(currency='STOR', full_name='Self Storage Coin', id='STOR', url='https://www.cryptocompare.com/media/34077422/stor.jpg')
    ARO = Coin(currency='ARO', full_name='Arionum', id='ARO', url='https://www.cryptocompare.com/media/34077423/aro.jpg')
    BWS = Coin(currency='BWS', full_name='BitcoinWSpectrum', id='BWS', url='https://www.cryptocompare.com/media/34077424/bws.jpg')
    BTCC = Coin(currency='BTCC', full_name='Bitcoin Core', id='BTCC', url='https://www.cryptocompare.com/media/34077427/btcc.png')
    GOLF = Coin(currency='GOLF', full_name='GolfCoin', id='GOLF', url='https://www.cryptocompare.com/media/34077431/tb5eoz00_400x400.jpeg')
    MUSE = Coin(currency='MUSE', full_name='Muse', id='MUSE', url='https://www.cryptocompare.com/media/34077432/muse.jpg')
    OCT = Coin(currency='OCT', full_name='OracleChain', id='OCT', url='https://www.cryptocompare.com/media/34077434/oct.jpg')
    XCEL = Coin(currency='XCEL', full_name='XcelTrip', id='XCEL', url='https://www.cryptocompare.com/media/34077435/xcel.jpg')
    ECH = Coin(currency='ECH', full_name='EthereCash', id='ECH', url='https://www.cryptocompare.com/media/34077437/ech.jpg')
    XMN = Coin(currency='XMN', full_name='Motion', id='XMN', url='https://www.cryptocompare.com/media/34077439/xmn.jpg')
    PLUS1 = Coin(currency='PLUS1', full_name='PlusOneCoin', id='PLUS1', url='https://www.cryptocompare.com/media/34077441/plus1.jpg')
    COI = Coin(currency='COI', full_name='Coinnec', id='COI', url='https://www.cryptocompare.com/media/34077446/coi.jpg')
    CANDY = Coin(currency='CANDY', full_name='UnicornGo Candy', id='CANDY', url='https://www.cryptocompare.com/media/34077448/candy.jpg')
    SHARD = Coin(currency='SHARD', full_name='ShardCoin', id='SHARD', url='https://www.cryptocompare.com/media/34835945/shard.png')
    GMCN = Coin(currency='GMCN', full_name='GambleCoin', id='GMCN', url='https://www.cryptocompare.com/media/34077455/gmcn.jpg')
    TRVC = Coin(currency='TRVC', full_name='Trivecoin', id='TRVC', url='https://www.cryptocompare.com/media/34077456/trvc.jpg')
    KRX = Coin(currency='KRX', full_name='RAVN Korrax ', id='KRX', url='https://www.cryptocompare.com/media/34077460/krx.png')
    BITX = Coin(currency='BITX', full_name='BitScreener', id='BITX', url='https://www.cryptocompare.com/media/34155487/bitx.png')
    HFT = Coin(currency='HFT', full_name='Hirefreehands', id='HFT', url='https://www.cryptocompare.com/media/34155494/hft.png')
    DTEM = Coin(currency='DTEM', full_name='Dystem', id='DTEM', url='https://www.cryptocompare.com/media/34478163/dtem.png')
    TIP = Coin(currency='TIP', full_name='Tip Blockchain', id='TIP', url='https://www.cryptocompare.com/media/34155504/tip.png')
    SOUND = Coin(currency='SOUND', full_name='Inmusik', id='SOUND', url='https://www.cryptocompare.com/media/34155506/sound.png')
    HB = Coin(currency='HB', full_name='HeartBout', id='HB', url='https://www.cryptocompare.com/media/34155514/hb.jpg')
    TRW = Coin(currency='TRW', full_name='Triwer', id='TRW', url='https://www.cryptocompare.com/media/34155516/trw.png')
    IQN = Coin(currency='IQN', full_name='IQeon', id='IQN', url='https://www.cryptocompare.com/media/34155518/iqn.jpg')
    GIC = Coin(currency='GIC', full_name='Giant', id='GIC', url='https://www.cryptocompare.com/media/34478386/gic.png')
    BGL = Coin(currency='BGL', full_name='Buglab', id='BGL', url='https://www.cryptocompare.com/media/34155533/buglab-token-listing-transparent.png')
    EPIK = Coin(currency='EPIK', full_name='EPIK Token', id='EPIK', url='https://www.cryptocompare.com/media/34155525/epik.png')
    ZMN = Coin(currency='ZMN', full_name='ZMINE', id='ZMN', url='https://www.cryptocompare.com/media/34155539/zmine.jpg')
    PNY = Coin(currency='PNY', full_name='Peony Coin', id='PNY', url='https://www.cryptocompare.com/media/34155540/pny.jpg')
    SAFE = Coin(currency='SAFE', full_name='SafeCoin', id='SAFE', url='https://www.cryptocompare.com/media/35521075/safecoinlogo_300x300.jpg')
    COU = Coin(currency='COU', full_name='Couchain', id='COU', url='https://www.cryptocompare.com/media/34155542/cou.jpg')
    BID = Coin(currency='BID', full_name='BidCoin', id='BID', url='https://www.cryptocompare.com/media/34155544/bidcoin.jpg')
    ATH = Coin(currency='ATH', full_name='Atheios', id='ATH', url='https://www.cryptocompare.com/media/34155545/ath.jpg')
    ABS = Coin(currency='ABS', full_name='Absolute Coin', id='ABS', url='https://www.cryptocompare.com/media/34155546/abs.jpg')
    VITAE = Coin(currency='VITAE', full_name='Vitae', id='VITAE', url='https://www.cryptocompare.com/media/34155548/vitae.jpg')
    XET = Coin(currency='XET', full_name='Eternal Token', id='XET', url='https://www.cryptocompare.com/media/34155549/xet.jpg')
    TDP = Coin(currency='TDP', full_name='TrueDeck', id='TDP', url='https://www.cryptocompare.com/media/34155558/tdp.jpg')
    XGS = Coin(currency='XGS', full_name='GenesisX', id='XGS', url='https://www.cryptocompare.com/media/34155559/xgs.jpg')
    XUEZ = Coin(currency='XUEZ', full_name='XUEZ', id='XUEZ', url='https://www.cryptocompare.com/media/34155560/xuez.jpg')
    BIM = Coin(currency='BIM', full_name='BitminerCoin', id='BIM', url='https://www.cryptocompare.com/media/34155562/bim.png')
    Dow = Coin(currency='Dow', full_name='DowCoin', id='Dow', url='https://www.cryptocompare.com/media/34155564/dow.jpg')
    HEX = Coin(currency='HEX', full_name='HexCoin', id='HEX', url='https://www.cryptocompare.com/media/34155565/hex.png')
    EMN = Coin(currency='EMN', full_name='Eminent Token ', id='EMN', url='https://www.cryptocompare.com/media/34155587/beepbeepnation_com-emn-vert-2.png')
    PYT = Coin(currency='PYT', full_name='Payther', id='PYT', url='https://www.cryptocompare.com/media/34155579/pyt.jpg')
    DEI = Coin(currency='DEI', full_name='Deimos', id='DEI', url='https://www.cryptocompare.com/media/34155582/dei.jpg')
    TPC = Coin(currency='TPC', full_name='TPCash', id='TPC', url='https://www.cryptocompare.com/media/34155583/tpc.png')
    OYS = Coin(currency='OYS', full_name='Oyster Platform', id='OYS', url='https://www.cryptocompare.com/media/34155584/oys.jpg')
    JEX = Coin(currency='JEX', full_name='JEX Token', id='JEX', url='https://www.cryptocompare.com/media/34155588/jex.jpg')
    ILK = Coin(currency='ILK', full_name='Inlock', id='ILK', url='https://www.cryptocompare.com/media/34155594/inlock.jpg')
    RYO = Coin(currency='RYO', full_name='Ryo', id='RYO', url='https://www.cryptocompare.com/media/34155598/ryo.jpg')
    MUSD = Coin(currency='MUSD', full_name='MUSDcoin', id='MUSD', url='https://www.cryptocompare.com/media/34155599/musd.jpg')
    MIC = Coin(currency='MIC', full_name='Mindexcoin', id='MIC', url='https://www.cryptocompare.com/media/34155601/mic.jpg')
    URALS = Coin(currency='URALS', full_name='Urals Coin', id='URALS', url='https://www.cryptocompare.com/media/34155602/urals.jpg')
    QWC = Coin(currency='QWC', full_name='Qwertycoin', id='QWC', url='https://www.cryptocompare.com/media/34155603/qwc.jpg')
    WAB = Coin(currency='WAB', full_name='WABnetwork', id='WAB', url='https://www.cryptocompare.com/media/34155604/wab.jpg')
    BTN = Coin(currency='BTN', full_name='Bitcoin Nova', id='BTN', url='https://www.cryptocompare.com/media/34155606/btn.jpg')
    ARE = Coin(currency='ARE', full_name='ARENON', id='ARE', url='https://www.cryptocompare.com/media/34155607/are.jpg')
    DAC = Coin(currency='DAC', full_name='DACash', id='DAC', url='https://www.cryptocompare.com/media/34155608/dac.jpg')
    EUNO = Coin(currency='EUNO', full_name='EUNO', id='EUNO', url='https://www.cryptocompare.com/media/34155610/euno.jpg')
    KAAS = Coin(currency='KAAS', full_name='KAASY.AI', id='KAAS', url='https://www.cryptocompare.com/media/34333411/kaas.jpg')
    MMO = Coin(currency='MMO', full_name='MMOCoin', id='MMO', url='https://www.cryptocompare.com/media/34333412/mmo.jpg')
    MVP = Coin(currency='MVP', full_name='Merculet', id='MVP', url='https://www.cryptocompare.com/media/34333413/mvp.jpg')
    DASC = Coin(currency='DASC', full_name='DasCoin', id='DASC', url='https://www.cryptocompare.com/media/34333414/dasc.jpg')
    EGT = Coin(currency='EGT', full_name='Egretia', id='EGT', url='https://www.cryptocompare.com/media/34333415/egt.jpg')
    PGT = Coin(currency='PGT', full_name='Puregold token', id='PGT', url='https://www.cryptocompare.com/media/34333417/pgt.png')
    MEDX = Coin(currency='MEDX', full_name='Mediblock', id='MEDX', url='https://www.cryptocompare.com/media/34333418/medx.jpg')
    CET = Coin(currency='CET', full_name='CoinEx token', id='CET', url='https://www.cryptocompare.com/media/30002253/coinex.png')
    SLST = Coin(currency='SLST', full_name='SmartLands', id='SLST', url='https://www.cryptocompare.com/media/34333419/slt.jpg')
    TGAME = Coin(currency='TGAME', full_name='TrueGame', id='TGAME', url='https://www.cryptocompare.com/media/34333421/tgame.jpg')
    ZINC = Coin(currency='ZINC', full_name='ZINC', id='ZINC', url='https://www.cryptocompare.com/media/34333420/zinc.png')
    KETAN = Coin(currency='KETAN', full_name='Ketan', id='KETAN', url='https://www.cryptocompare.com/media/34333423/ketan.jpg')
    KBC = Coin(currency='KBC', full_name='Karatgold coin', id='KBC', url='https://www.cryptocompare.com/media/34333424/kbc.png')
    MFT = Coin(currency='MFT', full_name='Mainframe', id='MFT', url='https://www.cryptocompare.com/media/34333427/mft.jpg')
    INSUR = Coin(currency='INSUR', full_name='InsurChain Coin', id='INSUR', url='https://www.cryptocompare.com/media/34333428/insur.jpg')
    NIX = Coin(currency='NIX', full_name='NIX', id='NIX', url='https://www.cryptocompare.com/media/34333430/nix.jpg')
    ZCN = Coin(currency='ZCN', full_name='0chain', id='ZCN', url='https://www.cryptocompare.com/media/34333431/zcn.jpg')
    FIN = Coin(currency='FIN', full_name='Finom FIN Token', id='FIN', url='https://www.cryptocompare.com/media/34333437/fin.jpg')
    RPM = Coin(currency='RPM', full_name='Render Payment', id='RPM', url='https://www.cryptocompare.com/media/34333441/rpm.jpg')
    DGX = Coin(currency='DGX', full_name='Digix Gold token', id='DGX', url='https://www.cryptocompare.com/media/34477706/dgx.png')
    ITA = Coin(currency='ITA', full_name='Italocoin', id='ITA', url='https://www.cryptocompare.com/media/34477708/ita.jpg')
    NOM = Coin(currency='NOM', full_name='Finom NOM Token', id='NOM', url='https://www.cryptocompare.com/media/34333437/fin.jpg')
    XSTC = Coin(currency='XSTC', full_name='Safe Trade Coin', id='XSTC', url='https://www.cryptocompare.com/media/34477716/xstc.png')
    U42 = Coin(currency='U42', full_name='You42', id='U42', url='https://www.cryptocompare.com/media/34477718/u42.png')
    EGCC = Coin(currency='EGCC', full_name='Engine', id='EGCC', url='https://www.cryptocompare.com/media/34477732/egcc.jpg')
    FREC = Coin(currency='FREC', full_name='Freyrchain', id='FREC', url='https://www.cryptocompare.com/media/34477733/frec.jpg')
    AOA = Coin(currency='AOA', full_name='Aurora ', id='AOA', url='https://www.cryptocompare.com/media/34477737/aoa.jpg')
    LET = Coin(currency='LET', full_name='LinkEye', id='LET', url='https://www.cryptocompare.com/media/34477738/let.jpg')
    MEET = Coin(currency='MEET', full_name='CoinMeet', id='MEET', url='https://www.cryptocompare.com/media/34477746/meet.jpg')
    BOE = Coin(currency='BOE', full_name='Bodhi ', id='BOE', url='https://www.cryptocompare.com/media/34477747/boe.jpg')
    RTE = Coin(currency='RTE', full_name='Rate3 ', id='RTE', url='https://www.cryptocompare.com/media/34477748/rte.jpg')
    CAR = Coin(currency='CAR', full_name='CarBlock ', id='CAR', url='https://www.cryptocompare.com/media/34477749/car.jpg')
    CPT = Coin(currency='CPT', full_name='Cryptaur', id='CPT', url='https://www.cryptocompare.com/media/34477750/cpt.jpg')
    PCO = Coin(currency='PCO', full_name='Pecunio', id='PCO', url='https://www.cryptocompare.com/media/34477751/pco.jpg')
    XPST = Coin(currency='XPST', full_name='PokerSports', id='XPST', url='https://www.cryptocompare.com/media/34477752/xpts.jpg')
    HSC = Coin(currency='HSC', full_name='HashCoin ', id='HSC', url='https://www.cryptocompare.com/media/34477757/hashfuture.png')
    MCV = Coin(currency='MCV', full_name='MCV Token', id='MCV', url='https://www.cryptocompare.com/media/34477762/mcv.png')
    SCRL = Coin(currency='SCRL', full_name='Scroll', id='SCRL', url='https://www.cryptocompare.com/media/34477763/scrl.jpg')
    CONI = Coin(currency='CONI', full_name='CoinBene', id='CONI', url='https://www.cryptocompare.com/media/34477765/coni.png')
    XPAT = Coin(currency='XPAT', full_name='Bitnation Pangea', id='XPAT', url='https://www.cryptocompare.com/media/34477766/xpat.jpg')
    MBLC = Coin(currency='MBLC', full_name='Mont Blanc', id='MBLC', url='https://www.cryptocompare.com/media/34477768/montblanc.png')
    DIW = Coin(currency='DIW', full_name='DIWtoken', id='DIW', url='https://www.cryptocompare.com/media/34477769/diw.png')
    JOINT = Coin(currency='JOINT', full_name='Joint Ventures', id='JOINT', url='https://www.cryptocompare.com/media/34477771/joint.jpg')
    IDXM = Coin(currency='IDXM', full_name='IDEX Membership', id='IDXM', url='https://www.cryptocompare.com/media/34477770/idxm.png')
    CCO = Coin(currency='CCO', full_name='Ccore', id='CCO', url='https://www.cryptocompare.com/media/34477773/cco.png')
    ATMI = Coin(currency='ATMI', full_name='Atonomi', id='ATMI', url='https://www.cryptocompare.com/media/34477778/atmi.jpg')
    TKA = Coin(currency='TKA', full_name='Tokia', id='TKA', url='https://www.cryptocompare.com/media/34477777/tka.png')
    RMT = Coin(currency='RMT', full_name='SureRemit', id='RMT', url='https://www.cryptocompare.com/media/34477782/rmt.jpg')
    OLT = Coin(currency='OLT', full_name='OneLedger', id='OLT', url='https://www.cryptocompare.com/media/34477783/olt.jpg')
    GETX = Coin(currency='GETX', full_name='Guaranteed Ethurance Token Extra', id='GETX', url='https://www.cryptocompare.com/media/34477784/getx.png')
    IQ = Coin(currency='IQ', full_name='Everipedia', id='IQ', url='https://www.cryptocompare.com/media/34477786/iq.png')
    BWT = Coin(currency='BWT', full_name='Bittwatt', id='BWT', url='https://www.cryptocompare.com/media/34477785/bwt.png')
    LST = Coin(currency='LST', full_name='Lendroid Support Token', id='LST', url='https://www.cryptocompare.com/media/34477788/lst.jpg')
    EMV = Coin(currency='EMV', full_name='Ethereum Movie Venture', id='EMV', url='https://www.cryptocompare.com/media/34477791/emv.jpg')
    ESZ = Coin(currency='ESZ', full_name='EtherSportz', id='ESZ', url='https://www.cryptocompare.com/media/34477790/esz.png')
    TRAK = Coin(currency='TRAK', full_name='TrakInvest', id='TRAK', url='https://www.cryptocompare.com/media/34477792/trak-2.jpg')
    ZXC = Coin(currency='ZXC', full_name='Oxcert', id='ZXC', url='https://www.cryptocompare.com/media/34477794/zxc.jpg')
    BTRN = Coin(currency='BTRN', full_name='Biotron', id='BTRN', url='https://www.cryptocompare.com/media/34477795/btrn.png')
    XMX = Coin(currency='XMX', full_name='XMax', id='XMX', url='https://www.cryptocompare.com/media/34477796/xmx.png')
    VME = Coin(currency='VME', full_name='VeriME', id='VME', url='https://www.cryptocompare.com/media/34477799/vme.png')
    VITE = Coin(currency='VITE', full_name='VITE', id='VITE', url='https://www.cryptocompare.com/media/34477806/vite.jpg')
    RNT = Coin(currency='RNT', full_name='OneRoot Network', id='RNT', url='https://www.cryptocompare.com/media/34477807/rnt.jpg')
    BBO = Coin(currency='BBO', full_name='Bigbom', id='BBO', url='https://www.cryptocompare.com/media/34477808/bbo.jpg')
    YUP = Coin(currency='YUP', full_name='Crowdholding', id='YUP', url='https://www.cryptocompare.com/media/34477809/yup.jpg')
    SNIP = Coin(currency='SNIP', full_name='SnipCoin', id='SNIP', url='https://www.cryptocompare.com/media/34477802/snip.png')
    XDNA = Coin(currency='XDNA', full_name='XDNA', id='XDNA', url='https://www.cryptocompare.com/media/34477810/xdna.png')
    SAL = Coin(currency='SAL', full_name='SalPay', id='SAL', url='https://www.cryptocompare.com/media/34477811/sal.png')
    CARD = Coin(currency='CARD', full_name='Cardstack', id='CARD', url='https://www.cryptocompare.com/media/34477813/card.png')
    LIKE = Coin(currency='LIKE', full_name='LikeCoin', id='LIKE', url='https://www.cryptocompare.com/media/34477816/like.png')
    THRT = Coin(currency='THRT', full_name='ThriveToken', id='THRT', url='https://www.cryptocompare.com/media/34477817/thrt.png')
    SKRP = Coin(currency='SKRP', full_name='Skraps', id='SKRP', url='https://www.cryptocompare.com/media/35521091/skrp.png')
    AVH = Coin(currency='AVH', full_name='Animation Vision Cash', id='AVH', url='https://www.cryptocompare.com/media/34477819/avh.png')
    SCC = Coin(currency='SCC', full_name='StockChain Coin', id='SCC', url='https://www.cryptocompare.com/media/34477823/scc.png')
    HALO = Coin(currency='HALO', full_name='Halo Platform', id='HALO', url='https://www.cryptocompare.com/media/34477824/halo.jpg')
    BSTN = Coin(currency='BSTN', full_name='BitStation', id='BSTN', url='https://www.cryptocompare.com/media/34477825/bstn.png')
    PITCH = Coin(currency='PITCH', full_name='PITCH', id='PITCH', url='https://www.cryptocompare.com/media/34477826/pitch.jpg')
    NANJ = Coin(currency='NANJ', full_name='NANJCOIN', id='NANJ', url='https://www.cryptocompare.com/media/34477827/nanj.png')
    PAXEX = Coin(currency='PAXEX', full_name='PAXEX', id='PAXEX', url='https://www.cryptocompare.com/media/34477830/paxex.png')
    DIT = Coin(currency='DIT', full_name='Ditcoin', id='DIT', url='https://www.cryptocompare.com/media/34477834/dit.jpg')
    AZART = Coin(currency='AZART', full_name='Azart', id='AZART', url='https://www.cryptocompare.com/media/34477835/azart.png')
    CENNZ = Coin(currency='CENNZ', full_name='Centrality Token', id='CENNZ', url='https://www.cryptocompare.com/media/34477833/cennz.png')
    RDC = Coin(currency='RDC', full_name='Ordocoin', id='RDC', url='https://www.cryptocompare.com/media/34477836/rdc.jpg')
    TTU = Coin(currency='TTU', full_name='TaTaTu', id='TTU', url='https://www.cryptocompare.com/media/34477837/ttu.png')
    FREE = Coin(currency='FREE', full_name='FREE coin', id='FREE', url='https://www.cryptocompare.com/media/34477838/free.jpg')
    AOP = Coin(currency='AOP', full_name='Averopay', id='AOP', url='https://www.cryptocompare.com/media/34477839/aop.jpg')
    XAP = Coin(currency='XAP', full_name='Apollon', id='XAP', url='https://www.cryptocompare.com/media/34477840/xap.png')
    INTO = Coin(currency='INTO', full_name='Influ Token', id='INTO', url='https://www.cryptocompare.com/media/34477844/into.jpg')
    AIMS = Coin(currency='AIMS', full_name='HighCastle Token', id='AIMS', url='https://www.cryptocompare.com/media/34477845/aims.jpg')
    TSC = Coin(currency='TSC', full_name='ThunderStake', id='TSC', url='https://www.cryptocompare.com/media/34477872/tsc.jpg')
    SPLB = Coin(currency='SPLB', full_name='SimpleBank', id='SPLB', url='https://www.cryptocompare.com/media/34477873/splb.jpg')
    CMZ = Coin(currency='CMZ', full_name='CRYPTOMAGZ', id='CMZ', url='https://www.cryptocompare.com/media/34477875/cmz.jpg')
    NOBS = Coin(currency='NOBS', full_name='No BS Crypto', id='NOBS', url='https://www.cryptocompare.com/media/34478232/nobs.png')
    HMN = Coin(currency='HMN', full_name='Harvest Masternode Coin', id='HMN', url='https://www.cryptocompare.com/media/34477880/hc.png')
    MHP = Coin(currency='MHP', full_name='MedicoHealth', id='MHP', url='https://www.cryptocompare.com/media/34477884/mhp.png')
    HMD = Coin(currency='HMD', full_name='Homelend', id='HMD', url='https://www.cryptocompare.com/media/34477886/hmd.jpg')
    JSE = Coin(currency='JSE', full_name='JSEcoin', id='JSE', url='https://www.cryptocompare.com/media/34477889/jse.png')
    IMGZ = Coin(currency='IMGZ', full_name='Imigize', id='IMGZ', url='https://www.cryptocompare.com/media/34477890/imgz.jpg')
    NYN = Coin(currency='NYN', full_name='NYNJA', id='NYN', url='https://www.cryptocompare.com/media/34477892/nynja.jpg')
    IAM = Coin(currency='IAM', full_name='IAME Identity', id='IAM', url='https://www.cryptocompare.com/media/34477894/iam.jpg')
    URB = Coin(currency='URB', full_name='Urbit Data', id='URB', url='https://www.cryptocompare.com/media/34477891/urb.png')
    CHART = Coin(currency='CHART', full_name='BetOnChart', id='CHART', url='https://www.cryptocompare.com/media/34477895/chart.jpg')
    WHEN = Coin(currency='WHEN', full_name='WhenHub', id='WHEN', url='https://www.cryptocompare.com/media/34477896/when.png')
    SFT = Coin(currency='SFT', full_name='SportsFix', id='SFT', url='https://www.cryptocompare.com/media/34477898/stf.png')
    ITR = Coin(currency='ITR', full_name='INTRO', id='ITR', url='https://www.cryptocompare.com/media/34477903/intro.png')
    CHE = Coin(currency='CHE', full_name='Cache', id='CHE', url='https://www.cryptocompare.com/media/34477904/che.png')
    ZEEW = Coin(currency='ZEEW', full_name='Zeew', id='ZEEW', url='https://www.cryptocompare.com/media/34477905/zeew.jpg')
    QUA = Coin(currency='QUA', full_name='Quasa', id='QUA', url='https://www.cryptocompare.com/media/34477909/qua.png')
    RSC = Coin(currency='RSC', full_name='Ronaldinho Soccer Coin', id='RSC', url='https://www.cryptocompare.com/media/34477988/rsc1.png')
    ENTRY = Coin(currency='ENTRY', full_name='ENTRY', id='ENTRY', url='https://www.cryptocompare.com/media/34477912/entry.jpg')
    PHTC = Coin(currency='PHTC', full_name='Photochain', id='PHTC', url='https://www.cryptocompare.com/media/34477911/pht.png')
    WORK = Coin(currency='WORK', full_name='Aworker', id='WORK', url='https://www.cryptocompare.com/media/34477913/work.png')
    ORC = Coin(currency='ORC', full_name='Organicco', id='ORC', url='https://www.cryptocompare.com/media/34477914/orc.jpg')
    ZAZA = Coin(currency='ZAZA', full_name='ZAZA', id='ZAZA', url='https://www.cryptocompare.com/media/34477917/zaza.png')
    IDAP = Coin(currency='IDAP', full_name='IDAP', id='IDAP', url='https://www.cryptocompare.com/media/34477918/idap.jpg')
    HEAL = Coin(currency='HEAL', full_name='Etheal', id='HEAL', url='https://www.cryptocompare.com/media/34477921/heal.jpg')
    OFCR = Coin(currency='OFCR', full_name='OfficerCoin', id='OFCR', url='https://www.cryptocompare.com/media/34477920/ofcr.png')
    SHPT = Coin(currency='SHPT', full_name='Shipit', id='SHPT', url='https://www.cryptocompare.com/media/34477922/shpt.png')
    LED = Coin(currency='LED', full_name='Terawatt', id='LED', url='https://www.cryptocompare.com/media/34477925/led.png')
    PRLPAY = Coin(currency='PRLPAY', full_name='PearlPay', id='PRLPAY', url='https://www.cryptocompare.com/media/34477931/prlpay.png')
    RBDT = Coin(currency='RBDT', full_name='RoBust Defense Token', id='RBDT', url='https://www.cryptocompare.com/media/34477932/rbdt.png')
    SKYFT = Coin(currency='SKYFT', full_name='SKYFchain', id='SKYFT', url='https://www.cryptocompare.com/media/34477941/skyft.png')
    FLEX = Coin(currency='FLEX', full_name='TrustedCars FLEX', id='FLEX', url='https://www.cryptocompare.com/media/34477942/flex.png')
    STRY = Coin(currency='STRY', full_name='STRYKZ', id='STRY', url='https://www.cryptocompare.com/media/34477947/stry.jpg')
    FAN = Coin(currency='FAN', full_name='Fan360', id='FAN', url='https://www.cryptocompare.com/media/34477946/fan.png')
    GBTC = Coin(currency='GBTC', full_name='GigTricks', id='GBTC', url='https://www.cryptocompare.com/media/34477950/gbtc.jpg')
    NBOX = Coin(currency='NBOX', full_name='Unboxed', id='NBOX', url='https://www.cryptocompare.com/media/34477952/nbox.png')
    BUD = Coin(currency='BUD', full_name='Buddy', id='BUD', url='https://www.cryptocompare.com/media/34477958/bud.png')
    DBCCOIN = Coin(currency='DBCCOIN', full_name='Datablockchain', id='DBCCOIN', url='https://www.cryptocompare.com/media/34477959/dbccoin.png')
    K2G = Coin(currency='K2G', full_name='Kasko2go', id='K2G', url='https://www.cryptocompare.com/media/34477966/k2g.jpg')
    ARR = Coin(currency='ARR', full_name='ARROUND', id='ARR', url='https://www.cryptocompare.com/media/34477967/arr.png')
    GMB = Coin(currency='GMB', full_name='GAMB', id='GMB', url='https://www.cryptocompare.com/media/34477970/gmb.jpg')
    SPOT = Coin(currency='SPOT', full_name='Spotcoin', id='SPOT', url='https://www.cryptocompare.com/media/34477969/spot.png')
    VTUUR = Coin(currency='VTUUR', full_name='VTUUR', id='VTUUR', url='https://www.cryptocompare.com/media/34477971/vtuur.jpg')
    Pakka = Coin(currency='Pakka', full_name='NextPakk', id='Pakka', url='https://www.cryptocompare.com/media/34477972/pakka.png')
    ETI = Coin(currency='ETI', full_name='EtherInc', id='ETI', url='https://www.cryptocompare.com/media/34477975/eti.jpg')
    FRECN = Coin(currency='FRECN', full_name='Freldo', id='FRECN', url='https://www.cryptocompare.com/media/34477978/frecn.jpg')
    NOIA = Coin(currency='NOIA', full_name='NOIA Network', id='NOIA', url='https://www.cryptocompare.com/media/34477984/noia.jpg')
    LAX = Coin(currency='LAX', full_name='LAPO', id='LAX', url='https://www.cryptocompare.com/media/34477986/lax.jpg')
    LPC = Coin(currency='LPC', full_name='Little Phil', id='LPC', url='https://www.cryptocompare.com/media/34477991/lpc.jpg')
    DYNO = Coin(currency='DYNO', full_name='DYNO', id='DYNO', url='https://www.cryptocompare.com/media/34477997/dyno.png')
    MFX = Coin(currency='MFX', full_name='MFChain', id='MFX', url='https://www.cryptocompare.com/media/34478000/mfx.png')
    SPIKE = Coin(currency='SPIKE', full_name='Spiking', id='SPIKE', url='https://www.cryptocompare.com/media/34478001/spike.png')
    SGO = Coin(currency='SGO', full_name='Selfie GO', id='SGO', url='https://www.cryptocompare.com/media/34478003/sgo.jpg')
    RAWG = Coin(currency='RAWG', full_name='RAWG', id='RAWG', url='https://www.cryptocompare.com/media/34478004/rawg.png')
    BDB = Coin(currency='BDB', full_name='Big Data Block', id='BDB', url='https://www.cryptocompare.com/media/34478007/bdb.png')
    MNR = Coin(currency='MNR', full_name='Monoreto', id='MNR', url='https://www.cryptocompare.com/media/34478010/mnr.jpg')
    ZNAQ = Coin(currency='ZNAQ', full_name='ZNAQ', id='ZNAQ', url='https://www.cryptocompare.com/media/34478018/znaq.jpg')
    YBT = Coin(currency='YBT', full_name='YellowBetter', id='YBT', url='https://www.cryptocompare.com/media/34478022/ybt.png')
    OPET = Coin(currency='OPET', full_name='ÕpetFoundation', id='OPET', url='https://www.cryptocompare.com/media/34478025/opet.jpg')
    PSK = Coin(currency='PSK', full_name='Pool of Stake', id='PSK', url='https://www.cryptocompare.com/media/34478024/psk.png')
    KVT = Coin(currency='KVT', full_name='Kinesis Velocity Token ', id='KVT', url='https://www.cryptocompare.com/media/34478026/kvt.png')
    COT = Coin(currency='COT', full_name='CoTrader', id='COT', url='https://www.cryptocompare.com/media/34478031/cot.png')
    WPT = Coin(currency='WPT', full_name='Worldopoly', id='WPT', url='https://www.cryptocompare.com/media/34478032/wpt.png')
    ABELE = Coin(currency='ABELE', full_name='Abele', id='ABELE', url='https://www.cryptocompare.com/media/34478035/abele.png')
    XEP = Coin(currency='XEP', full_name='ephelants360', id='XEP', url='https://www.cryptocompare.com/media/34478036/xep.png')
    OMI = Coin(currency='OMI', full_name='ECOMI', id='OMI', url='https://www.cryptocompare.com/media/34478040/omi.png')
    BILL = Coin(currency='BILL', full_name='TillBilly', id='BILL', url='https://www.cryptocompare.com/media/34478043/bill.png')
    ST = Coin(currency='ST', full_name='Scienceroot', id='ST', url='https://www.cryptocompare.com/media/34478045/scienceroot.png')
    WBBC = Coin(currency='WBBC', full_name='World Bit Bank', id='WBBC', url='https://www.cryptocompare.com/media/34478046/wbbc.png')
    XDT = Coin(currency='XDT', full_name='Dataeum', id='XDT', url='https://www.cryptocompare.com/media/34478047/xdt.png')
    WPP = Coin(currency='WPP', full_name='Green Energy Token', id='WPP', url='https://www.cryptocompare.com/media/34478048/wpp.png')
    SLT = Coin(currency='SLT', full_name='Social Lending Network', id='SLT', url='https://www.cryptocompare.com/media/34478057/social-lending.png')
    APL = Coin(currency='APL', full_name='Apollo Currency', id='APL', url='https://www.cryptocompare.com/media/34478058/apl.png')
    MCB = Coin(currency='MCB', full_name='MyCryptoBank', id='MCB', url='https://www.cryptocompare.com/media/34478060/mycryptobank.jpg')
    HDAC = Coin(currency='HDAC', full_name='Hdac', id='HDAC', url='https://www.cryptocompare.com/media/34478062/hdac.png')
    CCCX = Coin(currency='CCCX', full_name='Clipper Coin Capital', id='CCCX', url='https://www.cryptocompare.com/media/34478063/cccx.png')
    VRH = Coin(currency='VRH', full_name='Virtual Rehab', id='VRH', url='https://www.cryptocompare.com/media/34478066/vrh.png')
    AEN = Coin(currency='AEN', full_name='Aenco', id='AEN', url='https://www.cryptocompare.com/media/34478067/aen.png')
    SOLID = Coin(currency='SOLID', full_name='Solidified', id='SOLID', url='https://www.cryptocompare.com/media/34478069/solid.png')
    VANIG = Coin(currency='VANIG', full_name='VANIG', id='VANIG', url='https://www.cryptocompare.com/media/34478070/vanig.png')
    AIRE = Coin(currency='AIRE', full_name='Tokenaire', id='AIRE', url='https://www.cryptocompare.com/media/34478072/aire.png')
    GMA = Coin(currency='GMA', full_name='Goldchip Mining Asset', id='GMA', url='https://www.cryptocompare.com/media/34478076/gma.png')
    WMB = Coin(currency='WMB', full_name='WatermelonBlock', id='WMB', url='https://www.cryptocompare.com/media/34478077/watermelon.png')
    MVU = Coin(currency='MVU', full_name='meVu', id='MVU', url='https://www.cryptocompare.com/media/34478081/mvu.jpg')
    TLNT = Coin(currency='TLNT', full_name='Talent Token', id='TLNT', url='https://www.cryptocompare.com/media/34478082/tlnt.jpg')
    GLDR = Coin(currency='GLDR', full_name='Golder Coin', id='GLDR', url='https://www.cryptocompare.com/media/35309169/gldr.png')
    IMU = Coin(currency='IMU', full_name='imusify', id='IMU', url='https://www.cryptocompare.com/media/34478083/imusify.png')
    TRT = Coin(currency='TRT', full_name='TuurnT', id='TRT', url='https://www.cryptocompare.com/media/34478084/trt.png')
    OLM = Coin(currency='OLM', full_name='Olam', id='OLM', url='https://www.cryptocompare.com/media/34478090/olm.jpg')
    CST = Coin(currency='CST', full_name='Casper API', id='CST', url='https://www.cryptocompare.com/media/34478091/cst.jpg')
    YON = Coin(currency='YON', full_name='YondoCoin', id='YON', url='https://www.cryptocompare.com/media/34478092/yon.png')
    URT = Coin(currency='URT', full_name='Universal Recognition Token', id='URT', url='https://www.cryptocompare.com/media/34478095/urt.jpg')
    QCX = Coin(currency='QCX', full_name='QuickX Protocol', id='QCX', url='https://www.cryptocompare.com/media/34478096/quickx.png')
    CRON = Coin(currency='CRON', full_name='Cryptocean', id='CRON', url='https://www.cryptocompare.com/media/34478098/cron.jpg')
    DIP = Coin(currency='DIP', full_name='Etherisc', id='DIP', url='https://www.cryptocompare.com/media/34478100/dip.png')
    REDC = Coin(currency='REDC', full_name='RedCab', id='REDC', url='https://www.cryptocompare.com/media/34478109/redc.png')
    TTV = Coin(currency='TTV', full_name='TV-TWO', id='TTV', url='https://www.cryptocompare.com/media/34478113/ttv.jpg')
    OICOIN = Coin(currency='OICOIN', full_name='Osmium Investment Coin', id='OICOIN', url='https://www.cryptocompare.com/media/34478112/osmium.png')
    ENQ = Coin(currency='ENQ', full_name='Enecuum', id='ENQ', url='https://www.cryptocompare.com/media/34478115/enq.png')
    EXPR = Coin(currency='EXPR', full_name='Expercoin', id='EXPR', url='https://www.cryptocompare.com/media/34478116/expr.jpg')
    DTN = Coin(currency='DTN', full_name='Datareum', id='DTN', url='https://www.cryptocompare.com/media/34478117/dtn.png')
    IDM = Coin(currency='IDM', full_name='IDM', id='IDM', url='https://www.cryptocompare.com/media/34478118/idm.jpg')
    SIDT = Coin(currency='SIDT', full_name='SID Token', id='SIDT', url='https://www.cryptocompare.com/media/34478120/sidt.jpg')
    ISR = Coin(currency='ISR', full_name='Insureum', id='ISR', url='https://www.cryptocompare.com/media/34478119/isr.png')
    CDPT = Coin(currency='CDPT', full_name='Creditor Data Platform', id='CDPT', url='https://www.cryptocompare.com/media/34478121/cdpt.png')
    CRGO = Coin(currency='CRGO', full_name='CargoCoin', id='CRGO', url='https://www.cryptocompare.com/media/34478122/cargocoin.png')
    AXIS = Coin(currency='AXIS', full_name='LaneAxis', id='AXIS', url='https://www.cryptocompare.com/media/34478123/axis.png')
    QRP = Coin(currency='QRP', full_name='Cryptics', id='QRP', url='https://www.cryptocompare.com/media/34478125/qrp.jpg')
    TIIM = Coin(currency='TIIM', full_name='TriipMiles', id='TIIM', url='https://www.cryptocompare.com/media/34478126/tiim.png')
    BNR = Coin(currency='BNR', full_name='BiNeuro', id='BNR', url='https://www.cryptocompare.com/media/34478129/bitneuro.png')
    VRT = Coin(currency='VRT', full_name='Virtual Reality Technology', id='VRT', url='https://www.cryptocompare.com/media/34478130/vrt.png')
    ZCC1 = Coin(currency='ZCC1', full_name='ZeroCarbon', id='ZCC1', url='https://www.cryptocompare.com/media/34478131/nrg.png')
    KRP = Coin(currency='KRP', full_name='Kryptoin', id='KRP', url='https://www.cryptocompare.com/media/34478133/krp.png')
    DAG = Coin(currency='DAG', full_name='Constellation ', id='DAG', url='https://www.cryptocompare.com/media/34478136/dag.png')
    OLE = Coin(currency='OLE', full_name='Olive', id='OLE', url='https://www.cryptocompare.com/media/34478139/ole.png')
    OKB = Coin(currency='OKB', full_name='Okex', id='OKB', url='https://www.cryptocompare.com/media/34478141/okb.png')
    AMLT = Coin(currency='AMLT', full_name='AMLT', id='AMLT', url='https://www.cryptocompare.com/media/34478140/amlt.png')
    HGO = Coin(currency='HGO', full_name='HireGo', id='HGO', url='https://www.cryptocompare.com/media/34478142/hgo.png')
    TCOIN = Coin(currency='TCOIN', full_name='Talenthon', id='TCOIN', url='https://www.cryptocompare.com/media/34478144/tcoin.png')
    BZ = Coin(currency='BZ', full_name='Bit-Z', id='BZ', url='https://www.cryptocompare.com/media/34478146/bz.png')
    PRA = Coin(currency='PRA', full_name='ProChain', id='PRA', url='https://www.cryptocompare.com/media/34478149/prochain.png')
    VLP = Coin(currency='VLP', full_name='Volpo', id='VLP', url='https://www.cryptocompare.com/media/34478150/vlp.png')
    ZIP = Coin(currency='ZIP', full_name='Zipper', id='ZIP', url='https://www.cryptocompare.com/media/34478152/zipper.png')
    KCASH = Coin(currency='KCASH', full_name='Kcash', id='KCASH', url='https://www.cryptocompare.com/media/34478174/kcash.png')
    ZT = Coin(currency='ZT', full_name='ZB Global', id='ZT', url='https://www.cryptocompare.com/media/34478181/zb.png')
    BOUTS = Coin(currency='BOUTS', full_name='BoutsPro', id='BOUTS', url='https://www.cryptocompare.com/media/34478186/bouts.png')
    EST = Coin(currency='EST', full_name='ESports Chain', id='EST', url='https://www.cryptocompare.com/media/34478188/est.png')
    MODEX = Coin(currency='MODEX', full_name='MODEX Token', id='MODEX', url='https://www.cryptocompare.com/media/34478207/mdx1.png')
    OGT = Coin(currency='OGT', full_name='One Game', id='OGT', url='https://www.cryptocompare.com/media/34478196/ogt.png')
    PLA = Coin(currency='PLA', full_name='PlayChip', id='PLA', url='https://www.cryptocompare.com/media/34478199/pla.png')
    NPER = Coin(currency='NPER', full_name='NPER', id='NPER', url='https://www.cryptocompare.com/media/34478200/nper.png')
    ATON = Coin(currency='ATON', full_name='Further Network', id='ATON', url='https://www.cryptocompare.com/media/34478201/aton.png')
    EURS = Coin(currency='EURS', full_name='STASIS EURS', id='EURS', url='https://www.cryptocompare.com/media/34478204/stasis.png')
    XCG = Coin(currency='XCG', full_name='Xchange', id='XCG', url='https://www.cryptocompare.com/media/34478205/xcg.jpg')
    PCH = Coin(currency='PCH', full_name='POPCHAIN', id='PCH', url='https://www.cryptocompare.com/media/34478208/popchain.png')
    ECOM = Coin(currency='ECOM', full_name='Omnitude', id='ECOM', url='https://www.cryptocompare.com/media/34478210/ecom.png')
    WIT = Coin(currency='WIT', full_name='Witcoin', id='WIT', url='https://www.cryptocompare.com/media/34478213/witcoin.png')
    OPU = Coin(currency='OPU', full_name='Opu Coin', id='OPU', url='https://www.cryptocompare.com/media/34478214/opu.png')
    MOF = Coin(currency='MOF', full_name='Molecular Future', id='MOF', url='https://www.cryptocompare.com/media/34478215/mof.png')
    BOX = Coin(currency='BOX', full_name='ContentBox', id='BOX', url='https://www.cryptocompare.com/media/34478217/contentbox.png')
    COTI = Coin(currency='COTI', full_name='COTI', id='COTI', url='https://www.cryptocompare.com/media/34478216/coti.png')
    ETALON = Coin(currency='ETALON', full_name='Etalon', id='ETALON', url='https://www.cryptocompare.com/media/34478218/etalon.png')
    TICS = Coin(currency='TICS', full_name='CargoConX', id='TICS', url='https://www.cryptocompare.com/media/34478225/tics.png')
    ZPR = Coin(currency='ZPR', full_name='ZPER', id='ZPR', url='https://www.cryptocompare.com/media/34478221/zper.png')
    AAC = Coin(currency='AAC', full_name='Acute Angle Cloud', id='AAC', url='https://www.cryptocompare.com/media/34478227/acuteangle.png')
    ESTATE = Coin(currency='ESTATE', full_name='AgentMile', id='ESTATE', url='https://www.cryptocompare.com/media/34478230/estate.png')
    BLV = Coin(currency='BLV', full_name='Blockvest', id='BLV', url='https://www.cryptocompare.com/media/34478231/blv.png')
    RRC = Coin(currency='RRC', full_name='Recycling Regeneration Chain', id='RRC', url='https://www.cryptocompare.com/media/34478235/rrc.png')
    MPG = Coin(currency='MPG', full_name='Max Property Group', id='MPG', url='https://www.cryptocompare.com/media/35309444/mpg.png')
    QNTU = Coin(currency='QNTU', full_name='Quanta', id='QNTU', url='https://www.cryptocompare.com/media/34478240/quanta.png')
    IG = Coin(currency='IG', full_name='IG Token ', id='IG', url='https://www.cryptocompare.com/media/34478241/ig.png')
    FML = Coin(currency='FML', full_name='FormulA', id='FML', url='https://www.cryptocompare.com/media/34478316/fml-nav-logo.png')
    TLU = Coin(currency='TLU', full_name='Irene Energy', id='TLU', url='https://www.cryptocompare.com/media/34478242/tlu.png')
    PSM = Coin(currency='PSM', full_name='Prasm', id='PSM', url='https://www.cryptocompare.com/media/34478246/prasm.png')
    MON = Coin(currency='MON', full_name='MilionCoin', id='MON', url='https://www.cryptocompare.com/media/34478247/mon.png')
    KAN = Coin(currency='KAN', full_name='Bitkan', id='KAN', url='https://www.cryptocompare.com/media/34478254/bitkan.png')
    NMH = Coin(currency='NMH', full_name='Namahe', id='NMH', url='https://www.cryptocompare.com/media/34478259/nmh.png')
    KST = Coin(currency='KST', full_name='StarKST', id='KST', url='https://www.cryptocompare.com/media/34478260/starkst.png')
    DEL = Coin(currency='DEL', full_name='DelChain', id='DEL', url='https://www.cryptocompare.com/media/34478261/delchain.png')
    HIT = Coin(currency='HIT', full_name='HitChain', id='HIT', url='https://www.cryptocompare.com/media/34478267/hitchain.png')
    PBLK = Coin(currency='PBLK', full_name='PayBlock', id='PBLK', url='https://www.cryptocompare.com/media/34478268/pblk.png')
    MDN = Coin(currency='MDN', full_name='MADANA', id='MDN', url='https://www.cryptocompare.com/media/34478302/pax1.png')
    TMTG = Coin(currency='TMTG', full_name='Digital Gold Exchange', id='TMTG', url='https://www.cryptocompare.com/media/34478274/tmtg.png')
    SGC = Coin(currency='SGC', full_name='Sudan Gold Coin', id='SGC', url='https://www.cryptocompare.com/media/34478275/sgc.png')
    PRT = Coin(currency='PRT', full_name='Papusha', id='PRT', url='https://www.cryptocompare.com/media/34478276/prt.png')
    COSM = Coin(currency='COSM', full_name='CosmoChain', id='COSM', url='https://www.cryptocompare.com/media/34478279/cosmochain.png')
    GPPT = Coin(currency='GPPT', full_name='Pluto Project Coin', id='GPPT', url='https://www.cryptocompare.com/media/34478323/gppt.png')
    LNL = Coin(currency='LNL', full_name='LunarLink', id='LNL', url='https://www.cryptocompare.com/media/34478281/lnl.png')
    VRN = Coin(currency='VRN', full_name='Vernam', id='VRN', url='https://www.cryptocompare.com/media/34478284/vrn.png')
    NEX = Coin(currency='NEX', full_name='Neonexchange ', id='NEX', url='https://www.cryptocompare.com/media/34478288/nex.png')
    BRNX = Coin(currency='BRNX', full_name='Bronix', id='BRNX', url='https://www.cryptocompare.com/media/34478289/brnx.png')
    SRCOIN = Coin(currency='SRCOIN', full_name='SRCoin', id='SRCOIN', url='https://www.cryptocompare.com/media/34478290/srcoin.png')
    RFT = Coin(currency='RFT', full_name='RYFTS', id='RFT', url='https://www.cryptocompare.com/media/34478291/rft.png')
    ET = Coin(currency='ET', full_name='ENDO ', id='ET', url='https://www.cryptocompare.com/media/34478294/et.png')
    MMTM = Coin(currency='MMTM', full_name='Momentum', id='MMTM', url='https://www.cryptocompare.com/media/34478297/mmtm.png')
    XGH = Coin(currency='XGH', full_name='Golden Hash', id='XGH', url='https://www.cryptocompare.com/media/34478300/xgh.png')
    FXP = Coin(currency='FXP', full_name='FXPay', id='FXP', url='https://www.cryptocompare.com/media/34478303/fxp.png')
    PASS = Coin(currency='PASS', full_name='Blockpass', id='PASS', url='https://www.cryptocompare.com/media/34478307/blockpass.png')
    HRO = Coin(currency='HRO', full_name='HEROIC.com', id='HRO', url='https://www.cryptocompare.com/media/34478308/hro.png')
    DGTX = Coin(currency='DGTX', full_name='Digitex Futures', id='DGTX', url='https://www.cryptocompare.com/media/34478311/dgtx.png')
    BSCH = Coin(currency='BSCH', full_name='BitSchool', id='BSCH', url='https://www.cryptocompare.com/media/34478312/bsch.png')
    TRVR = Coin(currency='TRVR', full_name='Trivver', id='TRVR', url='https://www.cryptocompare.com/media/34478313/trivver.png')
    PESA = Coin(currency='PESA', full_name='Credible', id='PESA', url='https://www.cryptocompare.com/media/34478315/pesa.png')
    CLPX = Coin(currency='CLPX', full_name='Chynge.net', id='CLPX', url='https://www.cryptocompare.com/media/34478326/xclp.png')
    GLN = Coin(currency='GLN', full_name='Galion Token', id='GLN', url='https://www.cryptocompare.com/media/34478329/gln.png')
    AUK = Coin(currency='AUK', full_name='Aukcecoin', id='AUK', url='https://www.cryptocompare.com/media/34478330/auk.png')
    PCCM = Coin(currency='PCCM', full_name='Poseidon Chain', id='PCCM', url='https://www.cryptocompare.com/media/34478336/pccm.png')
    TOPC = Coin(currency='TOPC', full_name='Topchain', id='TOPC', url='https://www.cryptocompare.com/media/34478338/topchain.png')
    PLAN = Coin(currency='PLAN', full_name='Plancoin', id='PLAN', url='https://www.cryptocompare.com/media/34478346/plancoin.png')
    EVER = Coin(currency='EVER', full_name='EverLife.AI', id='EVER', url='https://www.cryptocompare.com/media/34478347/ever.png')
    TRAID = Coin(currency='TRAID', full_name='Traid', id='TRAID', url='https://www.cryptocompare.com/media/34478353/traid.png')
    TRIO = Coin(currency='TRIO', full_name='Tripio', id='TRIO', url='https://www.cryptocompare.com/media/34478359/tripio.png')
    BNTE = Coin(currency='BNTE', full_name='Bountie', id='BNTE', url='https://www.cryptocompare.com/media/34478360/bnte.png')
    DPY = Coin(currency='DPY', full_name='Delphy', id='DPY', url='https://www.cryptocompare.com/media/34478363/delphy.png')
    FUNDZ = Coin(currency='FUNDZ', full_name='FundFantasy', id='FUNDZ', url='https://www.cryptocompare.com/media/34478364/fundz.png')
    MIB = Coin(currency='MIB', full_name='Mobile Integrated Blockchain', id='MIB', url='https://www.cryptocompare.com/media/34478367/mib.png')
    BAAS = Coin(currency='BAAS', full_name='BaaSid', id='BAAS', url='https://www.cryptocompare.com/media/34478383/baas.png')
    LYNK = Coin(currency='LYNK', full_name='Lynked.World', id='LYNK', url='https://www.cryptocompare.com/media/34478384/lynk.png')
    CCL = Coin(currency='CCL', full_name='CyClean', id='CCL', url='https://www.cryptocompare.com/media/34478392/ccl.png')
    HYC = Coin(currency='HYC', full_name='HYCON', id='HYC', url='https://www.cryptocompare.com/media/34478394/hyc.png')
    TCX = Coin(currency='TCX', full_name='T-Coin', id='TCX', url='https://www.cryptocompare.com/media/34478395/tcx.png')
    HLD = Coin(currency='HLD', full_name='HyperLending', id='HLD', url='https://www.cryptocompare.com/media/34478398/hyperlending.png')
    DACC = Coin(currency='DACC', full_name='Decentralized Accessible Content Chain ', id='DACC', url='https://www.cryptocompare.com/media/34478399/dacc.png')
    NUSD = Coin(currency='NUSD', full_name='Nomin USD', id='NUSD', url='https://www.cryptocompare.com/media/34478400/havven.png')
    TCHB = Coin(currency='TCHB', full_name='Teachers Blockchain', id='TCHB', url='https://www.cryptocompare.com/media/34478401/tch.png')
    DAX = Coin(currency='DAX', full_name='DAEX', id='DAX', url='https://www.cryptocompare.com/media/34478404/dax.png')
    BEC = Coin(currency='BEC', full_name='Beauty Chain', id='BEC', url='https://www.cryptocompare.com/media/35521067/bec.png')
    VEEN = Coin(currency='VEEN', full_name='LIVEEN', id='VEEN', url='https://www.cryptocompare.com/media/34478410/veen.png')
    CIC = Coin(currency='CIC', full_name='CIChain', id='CIC', url='https://www.cryptocompare.com/media/34478411/cic.png')
    MIODIO = Coin(currency='MIODIO', full_name='MIODIOCOIN', id='MIODIO', url='https://www.cryptocompare.com/media/34478412/mio-dio.png')
    MOV = Coin(currency='MOV', full_name='MovieCoin', id='MOV', url='https://www.cryptocompare.com/media/34478422/mov.png')
    IHF = Coin(currency='IHF', full_name='Invictus Hyperion Fund', id='IHF', url='https://www.cryptocompare.com/media/34478456/ihf.png')
    CNAB = Coin(currency='CNAB', full_name='Cannabium', id='CNAB', url='https://www.cryptocompare.com/media/34478424/cnab.png')
    SGP = Coin(currency='SGP', full_name='SGPay', id='SGP', url='https://www.cryptocompare.com/media/34478426/sgp.png')
    HANA = Coin(currency='HANA', full_name='Hanacoin', id='HANA', url='https://www.cryptocompare.com/media/34478431/hana.png')
    BTV = Coin(currency='BTV', full_name='Bitvote', id='BTV', url='https://www.cryptocompare.com/media/34478436/bitvote.png')
    URP = Coin(currency='URP', full_name='Universal Reward Protocol', id='URP', url='https://www.cryptocompare.com/media/34478437/urp.png')
    SHE = Coin(currency='SHE', full_name='Shine Chain', id='SHE', url='https://www.cryptocompare.com/media/34478438/she.png')
    IVN = Coin(currency='IVN', full_name='IVN Security', id='IVN', url='https://www.cryptocompare.com/media/34478446/ivn.png')
    ZAT = Coin(currency='ZAT', full_name='ZatGo', id='ZAT', url='https://www.cryptocompare.com/media/34478455/zat.png')
    IMT = Coin(currency='IMT', full_name='MoneyToken', id='IMT', url='https://www.cryptocompare.com/media/34478458/moneytoken.png')
    MHC = Coin(currency='MHC', full_name='MetaHash', id='MHC', url='https://www.cryptocompare.com/media/34478465/metahash.png')
    ROBET = Coin(currency='ROBET', full_name='RoBet', id='ROBET', url='https://www.cryptocompare.com/media/34478469/robet.png')
    CRYP = Coin(currency='CRYP', full_name='CrypticCoin', id='CRYP', url='https://www.cryptocompare.com/media/34478470/cryp.png')
    BDT = Coin(currency='BDT', full_name='Blockonix', id='BDT', url='https://www.cryptocompare.com/media/34478472/bdt.png')
    BTXC = Coin(currency='BTXC', full_name='Bettex coin', id='BTXC', url='https://www.cryptocompare.com/media/34478473/btxc.png')
    DAPS = Coin(currency='DAPS', full_name='DAPS Token', id='DAPS', url='https://www.cryptocompare.com/media/34478477/daps.png')
    ETE = Coin(currency='ETE', full_name='EXTRADECOIN', id='ETE', url='https://www.cryptocompare.com/media/34478483/extradecoin.png')
    NHCT = Coin(currency='NHCT', full_name='Nano Healthcare Token', id='NHCT', url='https://www.cryptocompare.com/media/34478484/nhct.png')
    SWA = Coin(currency='SWA', full_name='Swace', id='SWA', url='https://www.cryptocompare.com/media/34478487/swace.png')
    USDCT = Coin(currency='USDCT', full_name='USDCT', id='USDCT', url='https://www.cryptocompare.com/media/34478491/usdc.png')
    IAG = Coin(currency='IAG', full_name='IAGON', id='IAG', url='https://www.cryptocompare.com/media/34478492/iagon.png')
    STRS = Coin(currency='STRS', full_name='STARS ', id='STRS', url='https://www.cryptocompare.com/media/34478504/strs.png')
    MTCMN = Coin(currency='MTCMN', full_name='MTC Mesh', id='MTCMN', url='https://www.cryptocompare.com/media/34478521/mtcmn.png')
    AAA = Coin(currency='AAA', full_name='AAA Reserve Currency', id='AAA', url='https://www.cryptocompare.com/media/34478522/aaa.png')
    ZEST = Coin(currency='ZEST', full_name='ZestCoin', id='ZEST', url='https://www.cryptocompare.com/media/34478523/zest.png')
    MOAC = Coin(currency='MOAC', full_name='MOAC', id='MOAC', url='https://www.cryptocompare.com/media/34478526/moac.png')
    HLM = Coin(currency='HLM', full_name='Helium', id='HLM', url='https://www.cryptocompare.com/media/34478534/hlm.png')
    CSP = Coin(currency='CSP', full_name='Caspian', id='CSP', url='https://www.cryptocompare.com/media/34478535/csp.png')
    USDC = Coin(currency='USDC', full_name='USD Coin', id='USDC', url='https://www.cryptocompare.com/media/34835941/usdc.png')
    ONGAS = Coin(currency='ONGAS', full_name='Ontology Gas', id='ONGAS', url='https://www.cryptocompare.com/media/30001663/ont.jpg')
    NRVE = Coin(currency='NRVE', full_name='Narrative', id='NRVE', url='https://www.cryptocompare.com/media/34478540/nrve.png')
    BIP = Coin(currency='BIP', full_name='Minter', id='BIP', url='https://www.cryptocompare.com/media/34835659/bip.png')
    XCASH = Coin(currency='XCASH', full_name='X-CASH', id='XCASH', url='https://www.cryptocompare.com/media/34478544/xcash.png')
    RMESH = Coin(currency='RMESH', full_name='RightMesh', id='RMESH', url='https://www.cryptocompare.com/media/34478546/rightmesh.png')
    HAND = Coin(currency='HAND', full_name='ShowHand', id='HAND', url='https://www.cryptocompare.com/media/34478547/showhand.png')
    GBXT = Coin(currency='GBXT', full_name='Globitex Token', id='GBXT', url='https://www.cryptocompare.com/media/34835645/gbx.png')
    AT = Coin(currency='AT', full_name='ABCC Token', id='AT', url='https://www.cryptocompare.com/media/34835646/abcc.png')
    BASIS = Coin(currency='BASIS', full_name='Basis', id='BASIS', url='https://www.cryptocompare.com/media/34835648/basis.png')
    JIB = Coin(currency='JIB', full_name='Jibbit', id='JIB', url='https://www.cryptocompare.com/media/34835647/jib.png')
    PMTN = Coin(currency='PMTN', full_name='Peer Mountain', id='PMTN', url='https://www.cryptocompare.com/media/34835649/pmtn.png')
    SGA = Coin(currency='SGA', full_name='SAGA', id='SGA', url='https://www.cryptocompare.com/media/34835650/saga.png')
    PHM = Coin(currency='PHM', full_name='Phomeum', id='PHM', url='https://www.cryptocompare.com/media/34835651/phm.png')
    CUSD = Coin(currency='CUSD', full_name='Carbon', id='CUSD', url='https://www.cryptocompare.com/media/34835652/carbon.png')
    QUANT = Coin(currency='QUANT', full_name='Quantler', id='QUANT', url='https://www.cryptocompare.com/media/34835653/quant.png')
    KUSD = Coin(currency='KUSD', full_name='Kowala', id='KUSD', url='https://www.cryptocompare.com/media/34835656/kowala.png')
    VEOT = Coin(currency='VEOT', full_name='Viewo', id='VEOT', url='https://www.cryptocompare.com/media/34835655/veo.png')
    GGR = Coin(currency='GGR', full_name='GGRocket', id='GGR', url='https://www.cryptocompare.com/media/34835658/ggr.png')
    VEST = Coin(currency='VEST', full_name='VestChain', id='VEST', url='https://www.cryptocompare.com/media/34835661/vestchain.png')
    MCN = Coin(currency='MCN', full_name='mCoin', id='MCN', url='https://www.cryptocompare.com/media/34835665/mcn.png')
    TCH = Coin(currency='TCH', full_name='TigerCash', id='TCH', url='https://www.cryptocompare.com/media/34835667/cointiger.png')
    DEPO = Coin(currency='DEPO', full_name='Depository Network', id='DEPO', url='https://www.cryptocompare.com/media/34835668/depo.png')
    ONE = Coin(currency='ONE', full_name='Menlo One', id='ONE', url='https://www.cryptocompare.com/media/34835672/one.png')
    TVA = Coin(currency='TVA', full_name='Terra Virtua', id='TVA', url='https://www.cryptocompare.com/media/34835675/terra.png')
    METM = Coin(currency='METM', full_name='MetaMorph', id='METM', url='https://www.cryptocompare.com/media/34835689/metamorph.png')
    PAX = Coin(currency='PAX', full_name='Paxos Standard', id='PAX', url='https://www.cryptocompare.com/media/34835691/pax.png')
    ARAW = Coin(currency='ARAW', full_name='Araw', id='ARAW', url='https://www.cryptocompare.com/media/34835694/araw.png')
    BRAZ = Coin(currency='BRAZ', full_name='Brazio', id='BRAZ', url='https://www.cryptocompare.com/media/34835697/brazio.png')
    TALAO = Coin(currency='TALAO', full_name='Talao', id='TALAO', url='https://www.cryptocompare.com/media/34835706/talao.png')
    IZX = Coin(currency='IZX', full_name='IZX', id='IZX', url='https://www.cryptocompare.com/media/34835714/izx.png')
    DIVI = Coin(currency='DIVI', full_name='Divi Project', id='DIVI', url='https://www.cryptocompare.com/media/34835734/divi.png')
    HQT = Coin(currency='HQT', full_name='HyperQuant', id='HQT', url='https://www.cryptocompare.com/media/34835733/hq.png')
    W12 = Coin(currency='W12', full_name='W12 Protocol', id='W12', url='https://www.cryptocompare.com/media/34835736/w12.png')
    NBAR = Coin(currency='NBAR', full_name='NOBAR', id='NBAR', url='https://www.cryptocompare.com/media/34835735/nbar.png')
    HC = Coin(currency='HC', full_name='HyperCash', id='HC', url='https://www.cryptocompare.com/media/34835738/hcash.png')
    KBX = Coin(currency='KBX', full_name='KuBitX', id='KBX', url='https://www.cryptocompare.com/media/34835743/kbx.png')
    MYDFS = Coin(currency='MYDFS', full_name='MyDFS', id='MYDFS', url='https://www.cryptocompare.com/media/34835747/mydfs.png')
    VTHO = Coin(currency='VTHO', full_name='VeChainThor ', id='VTHO', url='https://www.cryptocompare.com/media/34835748/vtho.png')
    BHPC = Coin(currency='BHPC', full_name='BHPCash', id='BHPC', url='https://www.cryptocompare.com/media/34835749/bhpc.png')
    VTOS = Coin(currency='VTOS', full_name='VTOS', id='VTOS', url='https://www.cryptocompare.com/media/34835750/vtos.png')
    M2O = Coin(currency='M2O', full_name='M2O Token', id='M2O', url='https://www.cryptocompare.com/media/34835757/m2o.png')
    SLY = Coin(currency='SLY', full_name='SELFLLERY', id='SLY', url='https://www.cryptocompare.com/media/34835758/selfllery.png')
    UEC = Coin(currency='UEC', full_name='United Emirates Coin', id='UEC', url='https://www.cryptocompare.com/media/34835766/uec.png')
    BEAT = Coin(currency='BEAT', full_name='BEAT Token', id='BEAT', url='https://www.cryptocompare.com/media/34835768/beat.png')
    MOLK = Coin(currency='MOLK', full_name='Mobilink Token', id='MOLK', url='https://www.cryptocompare.com/media/34835769/molk.png')
    MSD = Coin(currency='MSD', full_name='MSD', id='MSD', url='https://www.cryptocompare.com/media/34835777/main_image.png')
    SEED = Coin(currency='SEED', full_name='Superbloom', id='SEED', url='https://www.cryptocompare.com/media/34835779/seed.png')
    SEAL = Coin(currency='SEAL', full_name='Seal Network', id='SEAL', url='https://www.cryptocompare.com/media/34835782/seal.png')
    GBO = Coin(currency='GBO', full_name='Gabro.io', id='GBO', url='https://www.cryptocompare.com/media/34835786/gabro.png')
    ACM = Coin(currency='ACM', full_name='Actinium', id='ACM', url='https://www.cryptocompare.com/media/34835897/acm.png')
    DFXT = Coin(currency='DFXT', full_name='DigiFinexToken', id='DFXT', url='https://www.cryptocompare.com/media/34835898/digifinextoken.png')
    BF = Coin(currency='BF', full_name='BitForex Token', id='BF', url='https://www.cryptocompare.com/media/34835899/bf.png')
    NWP = Coin(currency='NWP', full_name='NWPSolution', id='NWP', url='https://www.cryptocompare.com/media/34835900/nwp.png')
    BCDT = Coin(currency='BCDT', full_name='Blockchain Certified Data Token', id='BCDT', url='https://www.cryptocompare.com/media/34835902/bcdt.png')
    EVOS = Coin(currency='EVOS', full_name='EVOS', id='EVOS', url='https://www.cryptocompare.com/media/34835916/evos.png')
    DEEX = Coin(currency='DEEX', full_name='DEEX', id='DEEX', url='https://www.cryptocompare.com/media/34835923/deex.png')
    ANON = Coin(currency='ANON', full_name='ANON', id='ANON', url='https://www.cryptocompare.com/media/34835929/anon.png')
    LTZ = Coin(currency='LTZ', full_name='Litecoinz', id='LTZ', url='https://www.cryptocompare.com/media/34835930/ltz.png')
    MTZ = Coin(currency='MTZ', full_name='Monetizr', id='MTZ', url='https://www.cryptocompare.com/media/34835943/monetizr.png')
    TBL = Coin(currency='TBL', full_name='Tombola', id='TBL', url='https://www.cryptocompare.com/media/34835944/tombola.png')
    BXY = Coin(currency='BXY', full_name='Beaxy', id='BXY', url='https://www.cryptocompare.com/media/34835951/beaxy.png')
    KUE = Coin(currency='KUE', full_name='Kuende', id='KUE', url='https://www.cryptocompare.com/media/34835959/kuende.png')
    ESN = Coin(currency='ESN', full_name='Ethersocial', id='ESN', url='https://www.cryptocompare.com/media/34835960/esn.png')
    H3O = Coin(currency='H3O', full_name='Hydrominer', id='H3O', url='https://www.cryptocompare.com/media/34835961/hidrominer.png')
    BETHER = Coin(currency='BETHER', full_name='Bethereum', id='BETHER', url='https://www.cryptocompare.com/media/34835962/bether.png')
    ETHO = Coin(currency='ETHO', full_name='ETHER-1', id='ETHO', url='https://www.cryptocompare.com/media/34835963/etho.png')
    WTL = Coin(currency='WTL', full_name='Welltrado', id='WTL', url='https://www.cryptocompare.com/media/34835966/wlt.png')
    HIH = Coin(currency='HIH', full_name='HiHealth', id='HIH', url='https://www.cryptocompare.com/media/34835971/hih.png')
    ANGEL = Coin(currency='ANGEL', full_name='Crypto Angel', id='ANGEL', url='https://www.cryptocompare.com/media/34835972/cryptoangel.png')
    P2PS = Coin(currency='P2PS', full_name='P2P Solutions Foundation', id='P2PS', url='https://www.cryptocompare.com/media/34835974/p2ps.png')
    GXT = Coin(currency='GXT', full_name='Game Protocol', id='GXT', url='https://www.cryptocompare.com/media/34835973/gxt.png')
    AIM = Coin(currency='AIM', full_name='Aimedis', id='AIM', url='https://www.cryptocompare.com/media/34835975/aim.png')
    TWISTR = Coin(currency='TWISTR', full_name='TWIST', id='TWISTR', url='https://www.cryptocompare.com/media/34835983/twist.png')
    CXA = Coin(currency='CXA', full_name='CryptovationX', id='CXA', url='https://www.cryptocompare.com/media/34835985/cryptovationx.png')
    BITTO = Coin(currency='BITTO', full_name='BITTO', id='BITTO', url='https://www.cryptocompare.com/media/34835984/bitto.png')
    HNY = Coin(currency='HNY', full_name='BitFence', id='HNY', url='https://www.cryptocompare.com/media/34835986/hny.png')
    QEY = Coin(currency='QEY', full_name='AQwire', id='QEY', url='https://www.cryptocompare.com/media/34835989/qey.png')
    UMK = Coin(currency='UMK', full_name='UMKA', id='UMK', url='https://www.cryptocompare.com/media/34835990/umk.png')
    VNX = Coin(currency='VNX', full_name='VisionX', id='VNX', url='https://www.cryptocompare.com/media/34835996/visionx.png')
    WMK = Coin(currency='WMK', full_name='Wemark', id='WMK', url='https://www.cryptocompare.com/media/34835998/wmk.png')
    OJX = Coin(currency='OJX', full_name='Ojooo', id='OJX', url='https://www.cryptocompare.com/media/34836001/ojx.png')
    CHW = Coin(currency='CHW', full_name='Chrysalis Coin', id='CHW', url='https://www.cryptocompare.com/media/34836005/chw.png')
    ABBC = Coin(currency='ABBC', full_name='Alibabacoin', id='ABBC', url='https://www.cryptocompare.com/media/34836013/abbc_ticker.png')
    CATT = Coin(currency='CATT', full_name='Catex', id='CATT', url='https://www.cryptocompare.com/media/34835995/catex.png')
    VEX = Coin(currency='VEX', full_name='Vexanium', id='VEX', url='https://www.cryptocompare.com/media/34836014/vexanium.png')
    LQDN = Coin(currency='LQDN', full_name='Liquidity Network', id='LQDN', url='https://www.cryptocompare.com/media/34836015/lqdn.png')
    BIOC = Coin(currency='BIOC', full_name='BioCrypt', id='BIOC', url='https://www.cryptocompare.com/media/34836016/bioc.png')
    FOREX = Coin(currency='FOREX', full_name='FOREXCOIN', id='FOREX', url='https://www.cryptocompare.com/media/34836020/forexcoin.png')
    CPLO = Coin(currency='CPLO', full_name='Cpollo', id='CPLO', url='https://www.cryptocompare.com/media/34836023/cpl.png')
    XPX = Coin(currency='XPX', full_name='ProximaX', id='XPX', url='https://www.cryptocompare.com/media/34836026/xpx.png')
    RIPAX = Coin(currency='RIPAX', full_name='RipaEx', id='RIPAX', url='https://www.cryptocompare.com/media/34836028/ripax.png')
    HETA = Coin(currency='HETA', full_name='HetaChain', id='HETA', url='https://www.cryptocompare.com/media/34836029/heta.png')
    NOW = Coin(currency='NOW', full_name='NOW Token', id='NOW', url='https://www.cryptocompare.com/media/34836031/now.png')
    ADAB = Coin(currency='ADAB', full_name='Adab Solutions', id='ADAB', url='https://www.cryptocompare.com/media/34836043/adab.png')
    CIX100 = Coin(currency='CIX100', full_name='Cryptoindex', id='CIX100', url='https://www.cryptocompare.com/media/34836044/cryptoindex.png')
    MINX = Coin(currency='MINX', full_name='InnovaMinex', id='MINX', url='https://www.cryptocompare.com/media/34836046/inx.png')
    MOBU = Coin(currency='MOBU', full_name='MOBU', id='MOBU', url='https://www.cryptocompare.com/media/34836047/mobu.png')
    NVDX = Coin(currency='NVDX', full_name='Nodvix', id='NVDX', url='https://www.cryptocompare.com/media/34836048/nvdx.png')
    COVEX = Coin(currency='COVEX', full_name='CoVEX', id='COVEX', url='https://www.cryptocompare.com/media/34836051/covex.png')
    TAL = Coin(currency='TAL', full_name='Talentico', id='TAL', url='https://www.cryptocompare.com/media/34836050/tal.png')
    ATT = Coin(currency='ATT', full_name='Aeternum', id='ATT', url='https://www.cryptocompare.com/media/34836055/att.png')
    F2K = Coin(currency='F2K', full_name='Farm2Kitchen', id='F2K', url='https://www.cryptocompare.com/media/34836057/f2k.png')
    GTX = Coin(currency='GTX', full_name='GALLACTIC', id='GTX', url='https://www.cryptocompare.com/media/34836056/gtx.png')
    B21 = Coin(currency='B21', full_name='B21', id='B21', url='https://www.cryptocompare.com/media/34836059/b21.png')
    LK = Coin(currency='LK', full_name='Liker', id='LK', url='https://www.cryptocompare.com/media/34836060/liker.png')
    QOBI = Coin(currency='QOBI', full_name='Qobit', id='QOBI', url='https://www.cryptocompare.com/media/34836072/qobit.png')
    BVO = Coin(currency='BVO', full_name='BRAVO Pay', id='BVO', url='https://www.cryptocompare.com/media/34836070/bvo.png')
    VENA = Coin(currency='VENA', full_name='Vena Network', id='VENA', url='https://www.cryptocompare.com/media/34836073/vena.png')
    CDRX = Coin(currency='CDRX', full_name='CDRX', id='CDRX', url='https://www.cryptocompare.com/media/34836074/cdrx.png')
    CRF = Coin(currency='CRF', full_name='CrowdForce ', id='CRF', url='https://www.cryptocompare.com/media/34836083/crf.png')
    ELES = Coin(currency='ELES', full_name='Elements Estates', id='ELES', url='https://www.cryptocompare.com/media/34836088/eles.png')
    GEON = Coin(currency='GEON', full_name='Geon', id='GEON', url='https://www.cryptocompare.com/media/34836090/geon.png')
    TZO = Coin(currency='TZO', full_name='TANZŌ', id='TZO', url='https://www.cryptocompare.com/media/34836092/tzo.png')
    WLME = Coin(currency='WLME', full_name='Wellmee', id='WLME', url='https://www.cryptocompare.com/media/34836096/wlme.png')
    INVX = Coin(currency='INVX', full_name='Investx', id='INVX', url='https://www.cryptocompare.com/media/34836100/investx.png')
    AWT = Coin(currency='AWT', full_name='WhatsOnPic', id='AWT', url='https://www.cryptocompare.com/media/34836101/awt.png')
    ABX = Coin(currency='ABX', full_name='AutoBay', id='ABX', url='https://www.cryptocompare.com/media/34836103/abx.png')
    LNKC = Coin(currency='LNKC', full_name='LINKCHAIN', id='LNKC', url='https://www.cryptocompare.com/media/34836108/linkchain.png')
    BFC = Coin(currency='BFC', full_name='Betform', id='BFC', url='https://www.cryptocompare.com/media/34836109/bfc.png')
    IMPCN = Coin(currency='IMPCN', full_name='Brain Space', id='IMPCN', url='https://www.cryptocompare.com/media/34836110/ipm.png')
    XPT = Coin(currency='XPT', full_name='Plata', id='XPT', url='https://www.cryptocompare.com/media/34836111/xpt.png')
    NMK = Coin(currency='NMK', full_name='Namek', id='NMK', url='https://www.cryptocompare.com/media/35264123/namek.png')
    OUT = Coin(currency='OUT', full_name='Netscouters', id='OUT', url='https://www.cryptocompare.com/media/35264124/out.png')
    LPT = Coin(currency='LPT', full_name='Livepeer', id='LPT', url='https://www.cryptocompare.com/media/35264132/lpt.png')
    RAINC  = Coin(currency='RAINC ', full_name='RainCheck', id='RAINC ', url='https://www.cryptocompare.com/media/35264136/rain.png')
    IOV = Coin(currency='IOV', full_name='IOV', id='IOV', url='https://www.cryptocompare.com/media/35264141/iov.png')
    MYO = Coin(currency='MYO', full_name='Mycro', id='MYO', url='https://www.cryptocompare.com/media/35264142/myo.png')
    ORET = Coin(currency='ORET', full_name='ORET Token', id='ORET', url='https://www.cryptocompare.com/media/35264143/oret.png')
    SEC = Coin(currency='SEC', full_name='SecureCryptoPayments', id='SEC', url='https://www.cryptocompare.com/media/35264144/securepayments.png')
    QUIZ = Coin(currency='QUIZ', full_name='Quizando', id='QUIZ', url='https://www.cryptocompare.com/media/35264145/quiz.png')
    CYRS = Coin(currency='CYRS', full_name='Cyrus Token', id='CYRS', url='https://www.cryptocompare.com/media/35264146/cyrs.png')
    UTL = Coin(currency='UTL', full_name='Utile Network', id='UTL', url='https://www.cryptocompare.com/media/35264147/utl.png')
    JOYS = Coin(currency='JOYS', full_name='JOYS', id='JOYS', url='https://www.cryptocompare.com/media/35264149/joys.png')
    DACH = Coin(currency='DACH', full_name='DACH Coin', id='DACH', url='https://www.cryptocompare.com/media/35264153/dach.png')
    MNVM = Coin(currency='MNVM', full_name='Novam', id='MNVM', url='https://www.cryptocompare.com/media/35264154/mnvm.png')
    PLTX = Coin(currency='PLTX', full_name='PlutusX', id='PLTX', url='https://www.cryptocompare.com/media/35264155/pltx.png')
    BTMG = Coin(currency='BTMG', full_name='Bitcademy Football', id='BTMG', url='https://www.cryptocompare.com/media/35264156/btmg.png')
    BRIK = Coin(currency='BRIK', full_name='BrikBit', id='BRIK', url='https://www.cryptocompare.com/media/35264157/brik.png')
    XTN = Coin(currency='XTN', full_name='XEND token', id='XTN', url='https://www.cryptocompare.com/media/35264158/xnt.png')
    LUMA = Coin(currency='LUMA', full_name='LUMA Token', id='LUMA', url='https://www.cryptocompare.com/media/35264159/luma.png')
    BTZN = Coin(currency='BTZN', full_name='Bitzon', id='BTZN', url='https://www.cryptocompare.com/media/35264161/btz.png')
    CLRTY = Coin(currency='CLRTY', full_name='Clarity', id='CLRTY', url='https://www.cryptocompare.com/media/35264162/clrty.png')
    CGT = Coin(currency='CGT', full_name='Coingrid', id='CGT', url='https://www.cryptocompare.com/media/35264163/cgt.png')
    NAVIB = Coin(currency='NAVIB', full_name='Navibration', id='NAVIB', url='https://www.cryptocompare.com/media/35264167/navib.png')
    ATHK = Coin(currency='ATHK', full_name='AntiHACK.me', id='ATHK', url='https://www.cryptocompare.com/media/35264169/athk.png')
    ATP = Coin(currency='ATP', full_name='ArtPro', id='ATP', url='https://www.cryptocompare.com/media/35264171/atp.png')
    PLEO = Coin(currency='PLEO', full_name='Empleos', id='PLEO', url='https://www.cryptocompare.com/media/35264174/pleo.png')
    GDX = Coin(currency='GDX', full_name='Gamedex', id='GDX', url='https://www.cryptocompare.com/media/35264175/gdx.png')
    EGDC = Coin(currency='EGDC', full_name='EasyGuide', id='EGDC', url='https://www.cryptocompare.com/media/35264176/egdc.png')
    ENTT = Coin(currency='ENTT', full_name='Presale Ventures', id='ENTT', url='https://www.cryptocompare.com/media/35264178/entt.png')
    RWD = Coin(currency='RWD', full_name='Reward Vision', id='RWD', url='https://www.cryptocompare.com/media/35264179/rwd.png')
    AURUM = Coin(currency='AURUM', full_name='Aurum', id='AURUM', url='https://www.cryptocompare.com/media/35264181/aurum.png')
    WRL = Coin(currency='WRL', full_name='WHIRL', id='WRL', url='https://www.cryptocompare.com/media/35264182/wrl.png')
    CRWD = Coin(currency='CRWD', full_name='CRWD Network', id='CRWD', url='https://www.cryptocompare.com/media/35264185/crwt.png')
    ENCN = Coin(currency='ENCN', full_name='EndChain', id='ENCN', url='https://www.cryptocompare.com/media/35264186/encn.png')
    TAURI = Coin(currency='TAURI', full_name='Extauri', id='TAURI', url='https://www.cryptocompare.com/media/35264189/tauri.png')
    EYE = Coin(currency='EYE', full_name='EYE Token', id='EYE', url='https://www.cryptocompare.com/media/35264190/eye.png')
    GTR = Coin(currency='GTR', full_name='Gturbo', id='GTR', url='https://www.cryptocompare.com/media/35264191/gtr.png')
    OPEX = Coin(currency='OPEX', full_name='Optherium Token', id='OPEX', url='https://www.cryptocompare.com/media/35264193/opex.jpg')
    SKYM = Coin(currency='SKYM', full_name='SkyMap', id='SKYM', url='https://www.cryptocompare.com/media/35264194/skim.png')
    SCIA = Coin(currency='SCIA', full_name='Stem Cell', id='SCIA', url='https://www.cryptocompare.com/media/35264195/scia.png')
    TXP = Coin(currency='TXP', full_name='Trade Pharma Network', id='TXP', url='https://www.cryptocompare.com/media/35264196/txp.png')
    GPS = Coin(currency='GPS', full_name='Triffic', id='GPS', url='https://www.cryptocompare.com/media/35264197/gps.png')
    WTXH = Coin(currency='WTXH', full_name='WTX HUB', id='WTXH', url='https://www.cryptocompare.com/media/35264198/wtxh.png')
    BBG = Coin(currency='BBG', full_name='BigBang', id='BBG', url='https://www.cryptocompare.com/media/35264199/bbg.png')
    NZE = Coin(currency='NZE', full_name='Nagezeni', id='NZE', url='https://www.cryptocompare.com/media/35264204/nze.png')
    EQY = Coin(currency='EQY', full_name='Eqwity', id='EQY', url='https://www.cryptocompare.com/media/35264206/eqy.png')
    FLC = Coin(currency='FLC', full_name='Fieldcoin', id='FLC', url='https://www.cryptocompare.com/media/35264207/flc.png')
    SHKG = Coin(currency='SHKG', full_name='SharkGate', id='SHKG', url='https://www.cryptocompare.com/media/35264208/shkg.png')
    TENZ = Coin(currency='TENZ', full_name='Tenzorum', id='TENZ', url='https://www.cryptocompare.com/media/35264209/tenz.png')
    TWC = Coin(currency='TWC', full_name='Twilight', id='TWC', url='https://www.cryptocompare.com/media/35264211/twc.png')
    WUG = Coin(currency='WUG', full_name='WatchUGot', id='WUG', url='https://www.cryptocompare.com/media/35264215/wug.png')
    CAND = Coin(currency='CAND', full_name='Canlead', id='CAND', url='https://www.cryptocompare.com/media/35264218/cand.png')
    CTW = Coin(currency='CTW', full_name='Citowise', id='CTW', url='https://www.cryptocompare.com/media/35264219/ctw.png')
    CRV = Coin(currency='CRV', full_name='Cravy', id='CRV', url='https://www.cryptocompare.com/media/35264220/crv.png')
    XIM = Coin(currency='XIM', full_name='Impresso', id='XIM', url='https://www.cryptocompare.com/media/35264222/xim.png')
    NAM = Coin(currency='NAM', full_name='Namacoin ', id='NAM', url='https://www.cryptocompare.com/media/35264223/nam.png')
    UFT = Coin(currency='UFT', full_name='ufoodo', id='UFT', url='https://www.cryptocompare.com/media/35264224/uft.png')
    BZKY = Coin(currency='BZKY', full_name='Bizkey', id='BZKY', url='https://www.cryptocompare.com/media/35264226/bzky.png')
    CARAT = Coin(currency='CARAT', full_name='Carats Token', id='CARAT', url='https://www.cryptocompare.com/media/35264227/carat.png')
    ZILLA = Coin(currency='ZILLA', full_name='ChainZilla', id='ZILLA', url='https://www.cryptocompare.com/media/35264228/zilla.png')
    TCJ = Coin(currency='TCJ', full_name='Coinshare', id='TCJ', url='https://www.cryptocompare.com/media/35264229/tcj.png')
    MAP = Coin(currency='MAP', full_name='Maester Protocol', id='MAP', url='https://www.cryptocompare.com/media/35264230/map.png')
    DN8 = Coin(currency='DN8', full_name='Pldgr', id='DN8', url='https://www.cryptocompare.com/media/35264231/dn8.png')
    XNT = Coin(currency='XNT', full_name='Exenium', id='XNT', url='https://www.cryptocompare.com/media/35264232/xnt.png')
    PPOVR = Coin(currency='PPOVR', full_name='POVR', id='PPOVR', url='https://www.cryptocompare.com/media/35264233/ppovr.png')
    LX = Coin(currency='LX', full_name='Moonlight', id='LX', url='https://www.cryptocompare.com/media/35264237/lx.png')
    AWAX = Coin(currency='AWAX', full_name='AWAX', id='AWAX', url='https://www.cryptocompare.com/media/35264240/awax.png')
    VAR = Coin(currency='VAR', full_name='VARcrypt', id='VAR', url='https://www.cryptocompare.com/media/35264241/var.png')
    TKD = Coin(currency='TKD', full_name='Tokedo', id='TKD', url='https://www.cryptocompare.com/media/35264349/tokedo.png')
    VTAG = Coin(currency='VTAG', full_name='veriTAG Token', id='VTAG', url='https://www.cryptocompare.com/media/35264296/vtag.png')
    WBY = Coin(currency='WBY', full_name='WeBuy', id='WBY', url='https://www.cryptocompare.com/media/35264434/wby.png')
    BBOS = Coin(currency='BBOS', full_name='Blackbox Foundation', id='BBOS', url='https://www.cryptocompare.com/media/35264517/blackbox.png')
    BFEX = Coin(currency='BFEX', full_name='BFEX', id='BFEX', url='https://www.cryptocompare.com/media/35280491/bfex.png')
    HUS = Coin(currency='HUS', full_name='HUSSY', id='HUS', url='https://www.cryptocompare.com/media/35280492/hus.png')
    MENU = Coin(currency='MENU', full_name='MenuBuzz', id='MENU', url='https://www.cryptocompare.com/media/35280495/menu.png')
    APXT = Coin(currency='APXT', full_name='ApolloX', id='APXT', url='https://www.cryptocompare.com/media/35280506/apollo.png')
    IDORU = Coin(currency='IDORU', full_name='Vip2Fan', id='IDORU', url='https://www.cryptocompare.com/media/35280507/idoru.png')
    WOM = Coin(currency='WOM', full_name='WOM', id='WOM', url='https://www.cryptocompare.com/media/35280508/wom.png')
    BONA = Coin(currency='BONA', full_name='Bonafi', id='BONA', url='https://www.cryptocompare.com/media/35280518/bonafi.png')
    HLDY = Coin(currency='HLDY', full_name='HOLIDAY', id='HLDY', url='https://www.cryptocompare.com/media/35280509/hldy.png')
    COS = Coin(currency='COS', full_name='Contentos', id='COS', url='https://www.cryptocompare.com/media/35280522/contentos.png')
    BLACK = Coin(currency='BLACK', full_name='eosBLACK', id='BLACK', url='https://www.cryptocompare.com/media/35280523/black.png')
    HORUS = Coin(currency='HORUS', full_name='HorusPay', id='HORUS', url='https://www.cryptocompare.com/media/35280529/horus.png')
    MEETONE = Coin(currency='MEETONE', full_name='MEET.ONE', id='MEETONE', url='https://www.cryptocompare.com/media/35280532/meetone.png')
    IOTW = Coin(currency='IOTW', full_name='IOTW', id='IOTW', url='https://www.cryptocompare.com/media/35280534/iotw.png')
    EMPR = Coin(currency='EMPR', full_name='empowr', id='EMPR', url='https://www.cryptocompare.com/media/35284298/empr.png')
    MPAY = Coin(currency='MPAY', full_name='Menapay', id='MPAY', url='https://www.cryptocompare.com/media/35284306/menapay.jpg')
    AGM = Coin(currency='AGM', full_name='Argoneum', id='AGM', url='https://www.cryptocompare.com/media/35284310/agm.png')
    MTCN = Coin(currency='MTCN', full_name='Multiven', id='MTCN', url='https://www.cryptocompare.com/media/35284312/multiven.png')
    PTO = Coin(currency='PTO', full_name='Patentico', id='PTO', url='https://www.cryptocompare.com/media/35284315/pto.png')
    AS = Coin(currency='AS', full_name='AmaStar', id='AS', url='https://www.cryptocompare.com/media/35284316/as.png')
    OSF = Coin(currency='OSF', full_name='One Solution', id='OSF', url='https://www.cryptocompare.com/media/35284317/osf.png')
    DPT = Coin(currency='DPT', full_name='Deliverers Power Token', id='DPT', url='https://www.cryptocompare.com/media/35284318/dpt.png')
    GTN = Coin(currency='GTN', full_name='Greentoken', id='GTN', url='https://www.cryptocompare.com/media/35284319/gtn.png')
    VIDI = Coin(currency='VIDI', full_name='Vidion', id='VIDI', url='https://www.cryptocompare.com/media/35284320/vidi.png')
    SUQA = Coin(currency='SUQA', full_name='SUQA', id='SUQA', url='https://www.cryptocompare.com/media/35284324/suqa.png')
    OPQ = Coin(currency='OPQ', full_name='Opacity', id='OPQ', url='https://www.cryptocompare.com/media/35284326/opq.png')
    ZYM = Coin(currency='ZYM', full_name='Enzym', id='ZYM', url='https://www.cryptocompare.com/media/35284330/zym.png')
    RPB = Coin(currency='RPB', full_name='Republia', id='RPB', url='https://www.cryptocompare.com/media/35284332/republia.png')
    DYNCOIN = Coin(currency='DYNCOIN', full_name='Dyncoin', id='DYNCOIN', url='https://www.cryptocompare.com/media/35284331/dyncoin.png')
    MIT = Coin(currency='MIT', full_name='MiMiner', id='MIT', url='https://www.cryptocompare.com/media/35284333/mit.png')
    VANM = Coin(currency='VANM', full_name='VANM', id='VANM', url='https://www.cryptocompare.com/media/35284334/vanm.jpg')
    PSF = Coin(currency='PSF', full_name='Prime Shipping Foundation', id='PSF', url='https://www.cryptocompare.com/media/35284335/psf.png')
    LITION = Coin(currency='LITION', full_name='Lition', id='LITION', url='https://www.cryptocompare.com/media/35284337/lition.png')
    NEW = Coin(currency='NEW', full_name='Newton', id='NEW', url='https://www.cryptocompare.com/media/35284336/new.png')
    TITAN = Coin(currency='TITAN', full_name='Titan', id='TITAN', url='https://www.cryptocompare.com/media/35284338/titan.png')
    MZG = Coin(currency='MZG', full_name='Moozicore', id='MZG', url='https://www.cryptocompare.com/media/35284347/moozi.png')
    VIAZ = Coin(currency='VIAZ', full_name='Viaz', id='VIAZ', url='https://www.cryptocompare.com/media/35284348/viaz.png')
    BTZC = Coin(currency='BTZC', full_name='BeatzCoin', id='BTZC', url='https://www.cryptocompare.com/media/35284350/btzc.png')
    ECR = Coin(currency='ECR', full_name='EcoVerse', id='ECR', url='https://www.cryptocompare.com/media/35284351/ecr.png')
    RF = Coin(currency='RF', full_name='Raido Financial', id='RF', url='https://www.cryptocompare.com/media/35284352/raido.png')
    ARMS = Coin(currency='ARMS', full_name='2Acoin', id='ARMS', url='https://www.cryptocompare.com/media/35284353/arms.png')
    STIPS = Coin(currency='STIPS', full_name='Stips', id='STIPS', url='https://www.cryptocompare.com/media/35284354/stips.png')
    MPXT = Coin(currency='MPXT', full_name='Myplacex', id='MPXT', url='https://www.cryptocompare.com/media/35284358/mpxt.png')
    XELS = Coin(currency='XELS', full_name='XELS Coin', id='XELS', url='https://www.cryptocompare.com/media/35284360/xels.png')
    PGF7T = Coin(currency='PGF7T', full_name='PGF500', id='PGF7T', url='https://www.cryptocompare.com/media/35284361/pgf.png')
    IDAC  = Coin(currency='IDAC ', full_name='IDAC ', id='IDAC ', url='https://www.cryptocompare.com/media/35284362/idac.png')
    ZUUM = Coin(currency='ZUUM', full_name='Zuum', id='ZUUM', url='https://www.cryptocompare.com/media/35284363/zuum.png')
    UCOINT = Coin(currency='UCOINT', full_name='UCOIN', id='UCOINT', url='https://www.cryptocompare.com/media/35284364/ucoin.png')
    YDY = Coin(currency='YDY', full_name='Ydentity', id='YDY', url='https://www.cryptocompare.com/media/35284365/ydy.png')
    FTUM = Coin(currency='FTUM', full_name='Fatum ', id='FTUM', url='https://www.cryptocompare.com/media/35284367/ftm.png')
    SPON = Coin(currency='SPON', full_name='Instant Sponsor Token', id='SPON', url='https://www.cryptocompare.com/media/35284368/spon.png')
    DLXV = Coin(currency='DLXV', full_name='Delta-X', id='DLXV', url='https://www.cryptocompare.com/media/35284370/dlxv.png')
    OCEAN = Coin(currency='OCEAN', full_name='Poseidon Foundation', id='OCEAN', url='https://www.cryptocompare.com/media/35284371/poseidon.png')
    TECO = Coin(currency='TECO', full_name='TerraEcoCoin', id='TECO', url='https://www.cryptocompare.com/media/35284373/ecos.png')
    GOALS = Coin(currency='GOALS', full_name='UnitedFans', id='GOALS', url='https://www.cryptocompare.com/media/35284374/goals.png')
    ETHIX = Coin(currency='ETHIX', full_name='EthicHub', id='ETHIX', url='https://www.cryptocompare.com/media/35284375/ethix.png')
    CDP = Coin(currency='CDP', full_name='CrowdPrecision', id='CDP', url='https://www.cryptocompare.com/media/35284376/cp.png')
    TTB = Coin(currency='TTB', full_name='TrustaBit', id='TTB', url='https://www.cryptocompare.com/media/35284378/ttb.png')
    CHK = Coin(currency='CHK', full_name='Chek', id='CHK', url='https://www.cryptocompare.com/media/35284379/one.png')
    PRPL = Coin(currency='PRPL', full_name='Purple Token', id='PRPL', url='https://www.cryptocompare.com/media/35284381/prpl.png')
    OASC = Coin(currency='OASC', full_name='Oasis City', id='OASC', url='https://www.cryptocompare.com/media/35284382/oasc.png')
    TREE = Coin(currency='TREE', full_name='HyperionX', id='TREE', url='https://www.cryptocompare.com/media/35284383/hyper.png')
    GDL = Coin(currency='GDL', full_name='GodlyCoin', id='GDL', url='https://www.cryptocompare.com/media/35284386/gdl.png')
    LNT = Coin(currency='LNT', full_name='Litenett', id='LNT', url='https://www.cryptocompare.com/media/35284387/litenet.png')
    FTRC = Coin(currency='FTRC', full_name='FutureCoin', id='FTRC', url='https://www.cryptocompare.com/media/35284388/ftrc.png')
    HBX = Coin(currency='HBX', full_name='Hyperbridge', id='HBX', url='https://www.cryptocompare.com/media/35284390/hyperbridge.png')
    LAO = Coin(currency='LAO', full_name='LC Token', id='LAO', url='https://www.cryptocompare.com/media/35284389/lao.png')
    GOVT = Coin(currency='GOVT', full_name='The Government Network', id='GOVT', url='https://www.cryptocompare.com/media/35284392/govt.png')
    TBRS = Coin(currency='TBRS', full_name='Tiberius', id='TBRS', url='https://www.cryptocompare.com/media/35284391/tbrs.png')
    COGEN = Coin(currency='COGEN', full_name='Cogenero', id='COGEN', url='https://www.cryptocompare.com/media/35284393/cogen.png')
    DAILY = Coin(currency='DAILY', full_name='Coindaily', id='DAILY', url='https://www.cryptocompare.com/media/35284395/daily.png')
    SREUR = Coin(currency='SREUR', full_name='SocialRemit', id='SREUR', url='https://www.cryptocompare.com/media/35284396/social.jpg')
    MAZC = Coin(currency='MAZC', full_name='MyMazzu', id='MAZC', url='https://www.cryptocompare.com/media/35284397/mazc.png')
    TGTC = Coin(currency='TGTC', full_name='Tokensgate', id='TGTC', url='https://www.cryptocompare.com/media/35284398/tgtc.png')
    NRG = Coin(currency='NRG', full_name='Energi', id='NRG', url='https://www.cryptocompare.com/media/35284400/nrg.png')
    PLNX = Coin(currency='PLNX', full_name='Planumex', id='PLNX', url='https://www.cryptocompare.com/media/35284401/pex.png')
    IPT = Coin(currency='IPT', full_name='Crypt-ON', id='IPT', url='https://www.cryptocompare.com/media/35284413/crypton.png')
    IGTT = Coin(currency='IGTT', full_name='IGT', id='IGTT', url='https://www.cryptocompare.com/media/35284414/igt.png')
    SRXIO = Coin(currency='SRXIO', full_name='Securix', id='SRXIO', url='https://www.cryptocompare.com/media/35284417/securix.png')
    GZB = Coin(currency='GZB', full_name='Gigzi', id='GZB', url='https://www.cryptocompare.com/media/35284416/gzb.png')
    FNX = Coin(currency='FNX', full_name='FinanceX', id='FNX', url='https://www.cryptocompare.com/media/35284419/financex.png')
    GGP = Coin(currency='GGP', full_name='GGPro', id='GGP', url='https://www.cryptocompare.com/media/35284422/ggpro.png')
    IFUM = Coin(currency='IFUM', full_name='Infleum', id='IFUM', url='https://www.cryptocompare.com/media/35284424/infleum.jpg')
    ATC = Coin(currency='ATC', full_name='AutoBlock', id='ATC', url='https://www.cryptocompare.com/media/35284425/atc.png')
    DOOH = Coin(currency='DOOH', full_name='Bidooh', id='DOOH', url='https://www.cryptocompare.com/media/35284426/bidooh.png')
    IOUX = Coin(currency='IOUX', full_name='IOU', id='IOUX', url='https://www.cryptocompare.com/media/35284428/ioux.png')
    BQTX = Coin(currency='BQTX', full_name='BQT', id='BQTX', url='https://www.cryptocompare.com/media/35284429/bqt.png')
    NVOY = Coin(currency='NVOY', full_name='Envoy', id='NVOY', url='https://www.cryptocompare.com/media/35284432/nvoy.png')
    CYBR = Coin(currency='CYBR', full_name='CYBR', id='CYBR', url='https://www.cryptocompare.com/media/35284433/cybr.png')
    LLG = Coin(currency='LLG', full_name='Loligo', id='LLG', url='https://www.cryptocompare.com/media/35284435/loligo.png')
    LCR = Coin(currency='LCR', full_name='Lucre', id='LCR', url='https://www.cryptocompare.com/media/35284434/lcr.png')
    SNPC = Coin(currency='SNPC', full_name='SnapCoin', id='SNPC', url='https://www.cryptocompare.com/media/35284436/snpc.png')
    VTM = Coin(currency='VTM', full_name='Victorieum', id='VTM', url='https://www.cryptocompare.com/media/35284438/vtm.png')
    NRX = Coin(currency='NRX', full_name='Neironix', id='NRX', url='https://www.cryptocompare.com/media/35284440/neironix.png')
    BTSG = Coin(currency='BTSG', full_name='BitSong', id='BTSG', url='https://www.cryptocompare.com/media/35284441/btsg.png')
    BXM = Coin(currency='BXM', full_name='Bixtrim', id='BXM', url='https://www.cryptocompare.com/media/35284442/bxm.png')
    CINX = Coin(currency='CINX', full_name='CINDX', id='CINX', url='https://www.cryptocompare.com/media/35284445/cinx.png')
    CCIN = Coin(currency='CCIN', full_name='Cryptocoin Insurance', id='CCIN', url='https://www.cryptocompare.com/media/35284446/ccin.png')
    CCI = Coin(currency='CCI', full_name='Cyber Capital Invest', id='CCI', url='https://www.cryptocompare.com/media/35284447/cci.png')
    RDS = Coin(currency='RDS', full_name='Reger Diamond', id='RDS', url='https://www.cryptocompare.com/media/35284449/rds.png')
    GMS = Coin(currency='GMS', full_name='Gemstra', id='GMS', url='https://www.cryptocompare.com/media/35284448/gms.png')
    SGAT = Coin(currency='SGAT', full_name='SGAT', id='SGAT', url='https://www.cryptocompare.com/media/35284450/sga.png')
    SILKT = Coin(currency='SILKT', full_name='SilkChain', id='SILKT', url='https://www.cryptocompare.com/media/35284452/silk.png')
    BITM = Coin(currency='BITM', full_name='BitMoney', id='BITM', url='https://www.cryptocompare.com/media/35284451/bitm.png')
    TCHN = Coin(currency='TCHN', full_name='Tachain', id='TCHN', url='https://www.cryptocompare.com/media/35284453/tachain.png')
    ICHN = Coin(currency='ICHN', full_name='i-chain', id='ICHN', url='https://www.cryptocompare.com/media/35284456/ichn.png')
    LVX = Coin(currency='LVX', full_name='LVX', id='LVX', url='https://www.cryptocompare.com/media/35284457/lvx.png')
    AENT = Coin(currency='AENT', full_name='AEN', id='AENT', url='https://www.cryptocompare.com/media/35284458/aen.png')
    MBN = Coin(currency='MBN', full_name='Membrana', id='MBN', url='https://www.cryptocompare.com/media/35284459/mbn.png')
    LYFE = Coin(currency='LYFE', full_name='Lyfe', id='LYFE', url='https://www.cryptocompare.com/media/35307330/lyfe.png')
    REMCO = Coin(currency='REMCO', full_name='Remco', id='REMCO', url='https://www.cryptocompare.com/media/35307329/remco.png')
    SaTT = Coin(currency='SaTT', full_name='SaTT', id='SaTT', url='https://www.cryptocompare.com/media/35307331/satt.png')
    GEMA = Coin(currency='GEMA', full_name='Gemera', id='GEMA', url='https://www.cryptocompare.com/media/35307335/gema.png')
    SCH = Coin(currency='SCH', full_name='Sia Cash Coin', id='SCH', url='https://www.cryptocompare.com/media/35307336/sch.png')
    VTEX = Coin(currency='VTEX', full_name='Vertex', id='VTEX', url='https://www.cryptocompare.com/media/35307342/vertex.png')
    SRV = Coin(currency='SRV', full_name='ServAdvisor', id='SRV', url='https://www.cryptocompare.com/media/35307341/srv.png')
    DSLA = Coin(currency='DSLA', full_name='Stacktical', id='DSLA', url='https://www.cryptocompare.com/media/35307343/dsla.png')
    SYLO = Coin(currency='SYLO', full_name='Sylo', id='SYLO', url='https://www.cryptocompare.com/media/35307344/sylo.png')
    YMZ = Coin(currency='YMZ', full_name='Yamzu', id='YMZ', url='https://www.cryptocompare.com/media/35307345/yamzu.png')
    AER = Coin(currency='AER', full_name='Aeryus', id='AER', url='https://www.cryptocompare.com/media/35307346/aeryus.png')
    AIBB = Coin(currency='AIBB', full_name='AiBB ', id='AIBB', url='https://www.cryptocompare.com/media/35307348/aibb.png')
    META = Coin(currency='META', full_name='Metadium', id='META', url='https://www.cryptocompare.com/media/35521068/meta.png')
    ASQT = Coin(currency='ASQT', full_name='ASQ Protocol', id='ASQT', url='https://www.cryptocompare.com/media/35307351/asqt.png')
    AXC = Coin(currency='AXC', full_name='autoXchange', id='AXC', url='https://www.cryptocompare.com/media/35307352/axc.png')
    BLKD = Coin(currency='BLKD', full_name='Blinked', id='BLKD', url='https://www.cryptocompare.com/media/35307353/blkd.png')
    CYS = Coin(currency='CYS', full_name='BlooCYS', id='CYS', url='https://www.cryptocompare.com/media/35307354/cys.png')
    ATTR = Coin(currency='ATTR', full_name='Attrace', id='ATTR', url='https://www.cryptocompare.com/media/35307355/attrace.png')
    CTY = Coin(currency='CTY', full_name='Connecty', id='CTY', url='https://www.cryptocompare.com/media/35307356/cty.png')
    BC = Coin(currency='BC', full_name='Beverage.cash', id='BC', url='https://www.cryptocompare.com/media/35307358/bc.png')
    DDL = Coin(currency='DDL', full_name='Donocle', id='DDL', url='https://www.cryptocompare.com/media/35307357/ddl.png')
    EZX = Coin(currency='EZX', full_name='EZ Exchange', id='EZX', url='https://www.cryptocompare.com/media/35307360/ezx.png')
    COY = Coin(currency='COY', full_name='Coin Analyst', id='COY', url='https://www.cryptocompare.com/media/35307364/coinanalyst.png')
    FNL = Coin(currency='FNL', full_name='Finlocale', id='FNL', url='https://www.cryptocompare.com/media/35307365/fnl.png')
    B2G = Coin(currency='B2G', full_name='Bitcoiin2Gen', id='B2G', url='https://www.cryptocompare.com/media/35307366/b2g.png')
    CSQ = Coin(currency='CSQ', full_name='cosquare', id='CSQ', url='https://www.cryptocompare.com/media/35307368/cosquare.png')
    HBE = Coin(currency='HBE', full_name='healthbank ', id='HBE', url='https://www.cryptocompare.com/media/35307369/hbe.png')
    HV = Coin(currency='HV', full_name='HighVibe.Network', id='HV', url='https://www.cryptocompare.com/media/35307370/hv.png')
    ICT = Coin(currency='ICT', full_name='Intrachain', id='ICT', url='https://www.cryptocompare.com/media/35307371/ict.png')
    TOS = Coin(currency='TOS', full_name='KRATOS', id='TOS', url='https://www.cryptocompare.com/media/35307373/tos.png')
    CPROP = Coin(currency='CPROP', full_name='CPROP', id='CPROP', url='https://www.cryptocompare.com/media/35307374/crop.png')
    MOOLYA = Coin(currency='MOOLYA', full_name='moolyacoin', id='MOOLYA', url='https://www.cryptocompare.com/media/35307375/moolya.png')
    PON = Coin(currency='PON', full_name='Ponder', id='PON', url='https://www.cryptocompare.com/media/35307376/pon.png')
    CREV = Coin(currency='CREV', full_name='CryptoRevolution', id='CREV', url='https://www.cryptocompare.com/media/35307377/crypto.png')
    VAD = Coin(currency='VAD', full_name='Varanida', id='VAD', url='https://www.cryptocompare.com/media/35307378/vad.png')
    IDC = Coin(currency='IDC', full_name='IdealCoin', id='IDC', url='https://www.cryptocompare.com/media/35307379/idl.png')
    LBR = Coin(currency='LBR', full_name='LaborCrypto', id='LBR', url='https://www.cryptocompare.com/media/35307380/lbr.png')
    EMX = Coin(currency='EMX', full_name='EMX', id='EMX', url='https://www.cryptocompare.com/media/35308827/emx.png')
    XBASE = Coin(currency='XBASE', full_name='ETERBASE', id='XBASE', url='https://www.cryptocompare.com/media/35308828/eterbase.png')
    LEN = Coin(currency='LEN', full_name='Liqnet', id='LEN', url='https://www.cryptocompare.com/media/35308829/len.png')
    KUBO = Coin(currency='KUBO', full_name='KUBO', id='KUBO', url='https://www.cryptocompare.com/media/35308833/kbg.png')
    FABA = Coin(currency='FABA', full_name='Faba Invest', id='FABA', url='https://www.cryptocompare.com/media/35308835/faba.png')
    LQ8 = Coin(currency='LQ8', full_name='Liquid8', id='LQ8', url='https://www.cryptocompare.com/media/35308834/lq8.png')
    GC = Coin(currency='GC', full_name='Gric Coin', id='GC', url='https://www.cryptocompare.com/media/35308838/gric.png')
    INFLR = Coin(currency='INFLR', full_name='Inflr', id='INFLR', url='https://www.cryptocompare.com/media/35308842/inflr.png')
    LIB = Coin(currency='LIB', full_name='Libellum', id='LIB', url='https://www.cryptocompare.com/media/35308844/libellum.png')
    XPR = Coin(currency='XPR', full_name='Permian', id='XPR', url='https://www.cryptocompare.com/media/35308845/xpr.png')
    PETL = Coin(currency='PETL', full_name='Petlife ', id='PETL', url='https://www.cryptocompare.com/media/35308850/petl.png')
    XDMC = Coin(currency='XDMC', full_name='MPCX', id='XDMC', url='https://www.cryptocompare.com/media/35308852/mpcx.png')
    PPS = Coin(currency='PPS', full_name='PopulStay', id='PPS', url='https://www.cryptocompare.com/media/35308853/pps.png')
    SMILO = Coin(currency='SMILO', full_name='Smilo', id='SMILO', url='https://www.cryptocompare.com/media/35308866/smilo.png')
    BCV = Coin(currency='BCV', full_name='BCV Blue Chip', id='BCV', url='https://www.cryptocompare.com/media/35308867/bcv.png')
    TREX = Coin(currency='TREX', full_name='TreeBlock', id='TREX', url='https://www.cryptocompare.com/media/35308874/trex.png')
    VNS = Coin(currency='VNS', full_name='Venus', id='VNS', url='https://www.cryptocompare.com/media/35308877/vns.png')
    VRF = Coin(currency='VRF', full_name='Verifier', id='VRF', url='https://www.cryptocompare.com/media/35308878/vrf.png')
    AUX = Coin(currency='AUX', full_name='Auxilium', id='AUX', url='https://www.cryptocompare.com/media/35308893/auxilium.png')
    LYQD = Coin(currency='LYQD', full_name='eLYQD', id='LYQD', url='https://www.cryptocompare.com/media/35309055/lyqd.png')
    CBP = Coin(currency='CBP', full_name='ComBox', id='CBP', url='https://www.cryptocompare.com/media/35309069/combox.png')
    SMOKE = Coin(currency='SMOKE', full_name='Smoke', id='SMOKE', url='https://www.cryptocompare.com/media/35309073/smoke.png')
    EDN = Coin(currency='EDN', full_name='EdenChain', id='EDN', url='https://www.cryptocompare.com/media/35309078/eden.png')
    AVALA = Coin(currency='AVALA', full_name='Travala', id='AVALA', url='https://www.cryptocompare.com/media/35309080/avala.png')
    NOS = Coin(currency='NOS', full_name='nOS', id='NOS', url='https://www.cryptocompare.com/media/35309081/nos.png')
    DT1 = Coin(currency='DT1', full_name='Dollar Token 1', id='DT1', url='https://www.cryptocompare.com/media/34478379/icoinbay.png')
    FTT = Coin(currency='FTT', full_name='FarmaTrust', id='FTT', url='https://www.cryptocompare.com/media/35309088/farma.png')
    STACS = Coin(currency='STACS', full_name='STACS Token', id='STACS', url='https://www.cryptocompare.com/media/35309089/stacs.png')
    JMC = Coin(currency='JMC', full_name='Junson Ming Chan Coin', id='JMC', url='https://www.cryptocompare.com/media/35309090/jmc.png')
    FOAM = Coin(currency='FOAM', full_name='Foam', id='FOAM', url='https://www.cryptocompare.com/media/35309092/foam.png')
    FRED = Coin(currency='FRED', full_name='FREDEnergy', id='FRED', url='https://www.cryptocompare.com/media/35309096/fred.png')
    CNCT = Coin(currency='CNCT', full_name='CONNECT', id='CNCT', url='https://www.cryptocompare.com/media/35309098/cnct.png')
    ENGT = Coin(currency='ENGT', full_name='Engagement Token', id='ENGT', url='https://www.cryptocompare.com/media/35309105/logo_engagementtoken.png')
    VRTY = Coin(currency='VRTY', full_name='Verity', id='VRTY', url='https://www.cryptocompare.com/media/35309106/vrty.png')
    TEAMT = Coin(currency='TEAMT', full_name='TokenStars TEAM Token', id='TEAMT', url='https://www.cryptocompare.com/media/35309107/teamt.png')
    ZND = Coin(currency='ZND', full_name='Zenad', id='ZND', url='https://www.cryptocompare.com/media/35309117/zenad.png')
    FPC = Coin(currency='FPC', full_name='Futurepia', id='FPC', url='https://www.cryptocompare.com/media/35309119/fpc.png')
    SYNCO = Coin(currency='SYNCO', full_name='Synco', id='SYNCO', url='https://www.cryptocompare.com/media/35309121/synco.png')
    SPY = Coin(currency='SPY', full_name='Verifier', id='SPY', url='https://www.cryptocompare.com/media/35309120/spy.png')
    HIDU = Coin(currency='HIDU', full_name='H-Education World', id='HIDU', url='https://www.cryptocompare.com/media/35309123/hidu.png')
    USE = Coin(currency='USE', full_name='Usechain Token', id='USE', url='https://www.cryptocompare.com/media/35309131/use.png')
    NGIN = Coin(currency='NGIN', full_name='Ngin', id='NGIN', url='https://www.cryptocompare.com/media/35309139/ngin.png')
    KOTO = Coin(currency='KOTO', full_name='Koto', id='KOTO', url='https://www.cryptocompare.com/media/35309140/koto.png')
    SUSD = Coin(currency='SUSD', full_name='sUSD', id='SUSD', url='https://www.cryptocompare.com/media/35309161/susd.png')
    GENX = Coin(currency='GENX', full_name='Genesis Network', id='GENX', url='https://www.cryptocompare.com/media/35309163/genx.png')
    HPSP = Coin(currency='HPSP', full_name='Hyperspace', id='HPSP', url='https://www.cryptocompare.com/media/35309164/hpsp.png')
    VTL = Coin(currency='VTL', full_name='Vertical', id='VTL', url='https://www.cryptocompare.com/media/35309165/vtl.png')
    SECI = Coin(currency='SECI', full_name='Seci', id='SECI', url='https://www.cryptocompare.com/media/35309167/seci.png')
    SPRTZ = Coin(currency='SPRTZ', full_name='SpritzCoin', id='SPRTZ', url='https://www.cryptocompare.com/media/35309168/sprtz.png')
    C25 = Coin(currency='C25', full_name='C25 Coin', id='C25', url='https://www.cryptocompare.com/media/35309170/c25.png')
    MVL = Coin(currency='MVL', full_name='MVL', id='MVL', url='https://www.cryptocompare.com/media/35309171/mvl.png')
    STASH = Coin(currency='STASH', full_name='BitStash', id='STASH', url='https://www.cryptocompare.com/media/35309203/bitstash-logo.png')
    HERB = Coin(currency='HERB', full_name='HerbCoin', id='HERB', url='https://www.cryptocompare.com/media/35309192/herb.png')
    AQUA = Coin(currency='AQUA', full_name='Aquachain', id='AQUA', url='https://www.cryptocompare.com/media/35309193/aqua.png')
    XQR = Coin(currency='XQR', full_name='Qredit', id='XQR', url='https://www.cryptocompare.com/media/35309195/qredit.png')
    URX = Coin(currency='URX', full_name='URANIUMX', id='URX', url='https://www.cryptocompare.com/media/35309204/logo.png')
    FTM = Coin(currency='FTM', full_name='Fantom', id='FTM', url='https://www.cryptocompare.com/media/35309205/ftm.png')
    HASH = Coin(currency='HASH', full_name='Hashbon', id='HASH', url='https://www.cryptocompare.com/media/35309209/hash.png')
    KSYS = Coin(currency='KSYS', full_name='K-Systems', id='KSYS', url='https://www.cryptocompare.com/media/35309210/ksys.png')
    MTEL = Coin(currency='MTEL', full_name='MEDoctor', id='MTEL', url='https://www.cryptocompare.com/media/35309214/med.png')
    MTT = Coin(currency='MTT', full_name='MulTra', id='MTT', url='https://www.cryptocompare.com/media/35309215/multra.png')
    MITC = Coin(currency='MITC', full_name='MusicLife', id='MITC', url='https://www.cryptocompare.com/media/35309217/music.png')
    BBTC = Coin(currency='BBTC', full_name='BlakeBitcoin', id='BBTC', url='https://www.cryptocompare.com/media/35309220/bbtc.png')
    UMO = Coin(currency='UMO', full_name='Universal Molecule', id='UMO', url='https://www.cryptocompare.com/media/35309221/umo.png')
    LIT = Coin(currency='LIT', full_name='Lithium', id='LIT', url='https://www.cryptocompare.com/media/35309222/lit.png')
    MUST = Coin(currency='MUST', full_name='MUST Protocol', id='MUST', url='https://www.cryptocompare.com/media/35309223/must.png')
    ELT = Coin(currency='ELT', full_name='Electron', id='ELT', url='https://www.cryptocompare.com/media/35309224/elt.png')
    TIOX = Coin(currency='TIOX', full_name='Trade Token X', id='TIOX', url='https://www.cryptocompare.com/media/35309225/tiox.png')
    XNB = Coin(currency='XNB', full_name='Xeonbit', id='XNB', url='https://www.cryptocompare.com/media/35309231/xnb.png')
    XRN = Coin(currency='XRN', full_name='Saronite', id='XRN', url='https://www.cryptocompare.com/media/35309232/xnr.png')
    RBTC = Coin(currency='RBTC', full_name='Smart Bitcoin', id='RBTC', url='https://www.cryptocompare.com/media/35309233/rbtc.png')
    BXC = Coin(currency='BXC', full_name='BtcEX', id='BXC', url='https://www.cryptocompare.com/media/35309234/bxc.jpg')
    PIRATE = Coin(currency='PIRATE', full_name='PirateCash', id='PIRATE', url='https://www.cryptocompare.com/media/35309249/pirate.png')
    EXO = Coin(currency='EXO', full_name='Exosis', id='EXO', url='https://www.cryptocompare.com/media/35309251/exo.png')
    ONAM = Coin(currency='ONAM', full_name='ONAM', id='ONAM', url='https://www.cryptocompare.com/media/35309252/oman.png')
    BIH = Coin(currency='BIH', full_name='BitHostCoin', id='BIH', url='https://www.cryptocompare.com/media/35309256/bih.png')
    KARMA = Coin(currency='KARMA', full_name='Karma', id='KARMA', url='https://www.cryptocompare.com/media/35309260/karma.png')
    CJR = Coin(currency='CJR', full_name='Conjure', id='CJR', url='https://www.cryptocompare.com/media/35309264/cjr.png')
    BLTG = Coin(currency='BLTG', full_name='Block-Logic', id='BLTG', url='https://www.cryptocompare.com/media/35309272/bltg.png')
    AGVC = Coin(currency='AGVC', full_name='AgaveCoin', id='AGVC', url='https://www.cryptocompare.com/media/35521095/agvc.png')
    ASGC = Coin(currency='ASGC', full_name='ASG', id='ASGC', url='https://www.cryptocompare.com/media/35309342/asgc.png')
    MIMI = Coin(currency='MIMI', full_name='MIMI Money', id='MIMI', url='https://www.cryptocompare.com/media/35309346/mimi.png')
    PXG = Coin(currency='PXG', full_name='PlayGame', id='PXG', url='https://www.cryptocompare.com/media/35309350/pxg.png')
    ORM = Coin(currency='ORM', full_name='ORIUM', id='ORM', url='https://www.cryptocompare.com/media/35309351/orm.png')
    TRET = Coin(currency='TRET', full_name='Tourist Review', id='TRET', url='https://www.cryptocompare.com/media/35309353/tret.png')
    SET = Coin(currency='SET', full_name='Securosys', id='SET', url='https://www.cryptocompare.com/media/35309354/set.png')
    BEER = Coin(currency='BEER', full_name='BEER Coin', id='BEER', url='https://www.cryptocompare.com/media/35309359/beer.jpg')
    AERGO = Coin(currency='AERGO', full_name='AERGO ', id='AERGO', url='https://www.cryptocompare.com/media/35309360/aergo.jpg')
    TIMI = Coin(currency='TIMI', full_name='Timicoin', id='TIMI', url='https://www.cryptocompare.com/media/35309363/tmc.jpg')
    NRP = Coin(currency='NRP', full_name='Neural Protocol', id='NRP', url='https://www.cryptocompare.com/media/35309366/nrp.jpg')
    SNTVT = Coin(currency='SNTVT', full_name='Sentivate', id='SNTVT', url='https://www.cryptocompare.com/media/35309367/sntvt.jpg')
    CEN = Coin(currency='CEN', full_name='Coinsuper Ecosystem Network', id='CEN', url='https://www.cryptocompare.com/media/35309368/cen.jpg')
    GARD = Coin(currency='GARD', full_name='Hashgard', id='GARD', url='https://www.cryptocompare.com/media/35309371/gard.jpg')
    UNX = Coin(currency='UNX', full_name='UNEOX', id='UNX', url='https://www.cryptocompare.com/media/35309374/unx.jpg')
    OWC = Coin(currency='OWC', full_name='Oduwa', id='OWC', url='https://www.cryptocompare.com/media/35309375/owc.jpg')
    WOWX = Coin(currency='WOWX', full_name='WOWX', id='WOWX', url='https://www.cryptocompare.com/media/35309384/wowx.png')
    THO = Coin(currency='THO', full_name='Athero', id='THO', url='https://www.cryptocompare.com/media/35309386/tho.png')
    TOSS = Coin(currency='TOSS', full_name='PROOF OF TOSS', id='TOSS', url='https://www.cryptocompare.com/media/35309395/toss.png')
    KMX = Coin(currency='KMX', full_name='KiMex', id='KMX', url='https://www.cryptocompare.com/media/35309396/kmx.png')
    SKI = Coin(currency='SKI', full_name='Skillchain', id='SKI', url='https://www.cryptocompare.com/media/35309397/ski.png')
    SG = Coin(currency='SG', full_name='SocialGood', id='SG', url='https://www.cryptocompare.com/media/35309398/sg.png')
    SUNEX = Coin(currency='SUNEX', full_name='The Sun Exchange', id='SUNEX', url='https://www.cryptocompare.com/media/35309400/sunex.jpg')
    VIDY = Coin(currency='VIDY', full_name='Vidy', id='VIDY', url='https://www.cryptocompare.com/media/35309399/vidy.png')
    XRBT = Coin(currency='XRBT', full_name='Xtribe', id='XRBT', url='https://www.cryptocompare.com/media/35309401/xrbt.png')
    ALUX = Coin(currency='ALUX', full_name='Alux Bank', id='ALUX', url='https://www.cryptocompare.com/media/35309403/alux.png')
    XBOND = Coin(currency='XBOND', full_name='Bitacium', id='XBOND', url='https://www.cryptocompare.com/media/35309402/xbond.png')
    BOSE = Coin(currency='BOSE', full_name='Bitbose', id='BOSE', url='https://www.cryptocompare.com/media/35309407/bose.png')
    GRIN = Coin(currency='GRIN', full_name='Grin', id='GRIN', url='https://www.cryptocompare.com/media/35309420/grin.png')
    JOY = Coin(currency='JOY', full_name='Joycoin', id='JOY', url='https://www.cryptocompare.com/media/35309421/joy.png')
    WETH = Coin(currency='WETH', full_name='WETH', id='WETH', url='https://www.cryptocompare.com/media/35309422/weth.png')
    GBE = Coin(currency='GBE', full_name='Godbex', id='GBE', url='https://www.cryptocompare.com/media/35309424/gbe.png')
    HRBE = Coin(currency='HRBE', full_name='Harambee Token', id='HRBE', url='https://www.cryptocompare.com/media/35309425/hrbe.png')
    BEAM = Coin(currency='BEAM', full_name='Beam', id='BEAM', url='https://www.cryptocompare.com/media/35309429/v3jr4j6q_400x400.jpg')
    MILC = Coin(currency='MILC', full_name='MIcro Licensing Coin', id='MILC', url='https://www.cryptocompare.com/media/35309432/milc.jpg')
    PINMO = Coin(currency='PINMO', full_name='Pinmo', id='PINMO', url='https://www.cryptocompare.com/media/35309433/pinmo.jpg')
    RGT = Coin(currency='RGT', full_name='Retail.Global', id='RGT', url='https://www.cryptocompare.com/media/35309436/rgt.jpg')
    BMG = Coin(currency='BMG', full_name='Borneo', id='BMG', url='https://www.cryptocompare.com/media/35309438/bmg.jpg')
    OXY2 = Coin(currency='OXY2', full_name='Cryptoxygen', id='OXY2', url='https://www.cryptocompare.com/media/35309441/oxy2.jpg')
    FAIRC = Coin(currency='FAIRC', full_name='Faireum Token', id='FAIRC', url='https://www.cryptocompare.com/media/35309445/fairc.jpg')
    BPN = Coin(currency='BPN', full_name='beepnow', id='BPN', url='https://www.cryptocompare.com/media/35309448/bpn.png')
    DYC = Coin(currency='DYC', full_name='Dycoin', id='DYC', url='https://www.cryptocompare.com/media/35309450/dyc.jpg')
    DUSK = Coin(currency='DUSK', full_name='Dusk Network', id='DUSK', url='https://www.cryptocompare.com/media/35309449/dusk.png')
    LN = Coin(currency='LN', full_name='LINK', id='LN', url='https://www.cryptocompare.com/media/35309453/ln.png')
    FTR = Coin(currency='FTR', full_name='FactR', id='FTR', url='https://www.cryptocompare.com/media/35309455/ftr.jpg')
    RWE = Coin(currency='RWE', full_name='Real-World Evidence', id='RWE', url='https://www.cryptocompare.com/media/35309454/rwe.png')
    YSH = Coin(currency='YSH', full_name='Yoshi', id='YSH', url='https://www.cryptocompare.com/media/35309456/ysh.png')
    TASH = Coin(currency='TASH', full_name='Smart Trip Platform', id='TASH', url='https://www.cryptocompare.com/media/35309457/tash.jpg')
    TXM = Coin(currency='TXM', full_name='TMONEY', id='TXM', url='https://www.cryptocompare.com/media/35309458/tmoney.png')
    TRAVEL = Coin(currency='TRAVEL', full_name='Travelvee', id='TRAVEL', url='https://www.cryptocompare.com/media/35309459/travel.jpg')
    ACA = Coin(currency='ACA', full_name='ACA Token', id='ACA', url='https://www.cryptocompare.com/media/35309460/aca.png')
    AUPC = Coin(currency='AUPC', full_name='Authpaper', id='AUPC', url='https://www.cryptocompare.com/media/35309463/aupc.png')
    COSX = Coin(currency='COSX', full_name='Cosmecoin', id='COSX', url='https://www.cryptocompare.com/media/35309464/cosx.jpg')
    DNTX = Coin(currency='DNTX', full_name='DNAtix', id='DNTX', url='https://www.cryptocompare.com/media/35309465/dntx.png')
    HART = Coin(currency='HART', full_name='HARA', id='HART', url='https://www.cryptocompare.com/media/35309466/hart.jpg')
    KSS = Coin(currency='KSS', full_name='Krosscoin', id='KSS', url='https://www.cryptocompare.com/media/35309467/kss.png')
    LIPS = Coin(currency='LIPS', full_name='LipChain', id='LIPS', url='https://www.cryptocompare.com/media/35309468/lips.jpg')
    MIBO = Coin(currency='MIBO', full_name='miBoodle', id='MIBO', url='https://www.cryptocompare.com/media/35309470/mibo.jpg')
    BRIX = Coin(currency='BRIX', full_name='OpenBrix', id='BRIX', url='https://www.cryptocompare.com/media/35309472/brix.jpg')
    NZO = Coin(currency='NZO', full_name='NonZero', id='NZO', url='https://www.cryptocompare.com/media/35309471/nzo.png')
    PTT = Coin(currency='PTT', full_name='Pink Taxi Token', id='PTT', url='https://www.cryptocompare.com/media/35309477/ptt.jpg')
    XRK = Coin(currency='XRK', full_name='RecordsKeeper', id='XRK', url='https://www.cryptocompare.com/media/35309478/xrk.jpg')
    RMOB = Coin(currency='RMOB', full_name='RewardMob', id='RMOB', url='https://www.cryptocompare.com/media/35309485/rmob.jpg')
    XRF = Coin(currency='XRF', full_name='Sarf', id='XRF', url='https://www.cryptocompare.com/media/35309486/xrf.png')
    POD = Coin(currency='POD', full_name='Smart League', id='POD', url='https://www.cryptocompare.com/media/35309488/pod.jpg')
    SUT = Coin(currency='SUT', full_name='Suapp', id='SUT', url='https://www.cryptocompare.com/media/35309489/sut.jpg')
    WHO = Coin(currency='WHO', full_name='Truwho', id='WHO', url='https://www.cryptocompare.com/media/35309493/who.jpg')
    ID = Coin(currency='ID', full_name='TrigID', id='ID', url='https://www.cryptocompare.com/media/35309494/id.png')
    WDX = Coin(currency='WDX', full_name='WeiDex', id='WDX', url='https://www.cryptocompare.com/media/35309497/wdx.png')
    AIOT = Coin(currency='AIOT', full_name='AIOT Token', id='AIOT', url='https://www.cryptocompare.com/media/35309499/aiot.png')
    AMOS = Coin(currency='AMOS', full_name='Amos', id='AMOS', url='https://www.cryptocompare.com/media/35309502/amos.png')
    XBANK = Coin(currency='XBANK', full_name='Bancryp', id='XBANK', url='https://www.cryptocompare.com/media/35309509/xbank.png')
    OX = Coin(currency='OX', full_name='betbox', id='OX', url='https://www.cryptocompare.com/media/35309516/ox.jpg')
    KRO = Coin(currency='KRO', full_name='Betoken', id='KRO', url='https://www.cryptocompare.com/media/35309517/kro.png')
    CAID = Coin(currency='CAID', full_name='ClearAid', id='CAID', url='https://www.cryptocompare.com/media/35309518/caid.png')
    LTE = Coin(currency='LTE', full_name='Local Token Exchange', id='LTE', url='https://www.cryptocompare.com/media/35309522/lte.jpg')
    HLX = Coin(currency='HLX', full_name='Helix3', id='HLX', url='https://www.cryptocompare.com/media/35309521/hlx.png')
    MEL = Coin(currency='MEL', full_name='Melior AI', id='MEL', url='https://www.cryptocompare.com/media/35309523/mel.png')
    NEXXO = Coin(currency='NEXXO', full_name='Nexxo', id='NEXXO', url='https://www.cryptocompare.com/media/35309525/nexxo.jpg')
    QNTR = Coin(currency='QNTR', full_name='Quantor', id='QNTR', url='https://www.cryptocompare.com/media/35309526/qnt.png')
    BTCUS = Coin(currency='BTCUS', full_name='Bitcoinus', id='BTCUS', url='https://www.cryptocompare.com/media/35309533/bits-2.jpg')
    RAYS = Coin(currency='RAYS', full_name='Rays Network', id='RAYS', url='https://www.cryptocompare.com/media/35309536/rays.png')
    MOL = Coin(currency='MOL', full_name='Molecule', id='MOL', url='https://www.cryptocompare.com/media/35309537/mol.jpg')
    RENC = Coin(currency='RENC', full_name='RENC', id='RENC', url='https://www.cryptocompare.com/media/35309540/renc.png')
    TLT = Coin(currency='TLT', full_name='Travelertoken', id='TLT', url='https://www.cryptocompare.com/media/35309542/tlt.jpg')
    EMOT = Coin(currency='EMOT', full_name='Sentigraph.io', id='EMOT', url='https://www.cryptocompare.com/media/35309541/emot.png')
    USAT = Coin(currency='USAT', full_name='USAT', id='USAT', url='https://www.cryptocompare.com/media/35309546/usat-2.jpg')
    VOL = Coin(currency='VOL', full_name='VolAir', id='VOL', url='https://www.cryptocompare.com/media/35309548/vol.jpg')
    AIRT = Coin(currency='AIRT', full_name='Aircraft', id='AIRT', url='https://www.cryptocompare.com/media/35309549/airt.png')
    VTRD = Coin(currency='VTRD', full_name='VTradeExchange', id='VTRD', url='https://www.cryptocompare.com/media/35309552/vtrd.jpg')
    BTT = Coin(currency='BTT', full_name='BitTorrent', id='BTT', url='https://www.cryptocompare.com/media/35309593/btt.jpg')
    GALI = Coin(currency='GALI', full_name='Galilel', id='GALI', url='https://www.cryptocompare.com/media/35309733/gali.png')
    PLAI = Coin(currency='PLAI', full_name='Plair', id='PLAI', url='https://www.cryptocompare.com/media/35309554/pla.jpg')
    BGG = Coin(currency='BGG', full_name='Bgogo Token', id='BGG', url='https://www.cryptocompare.com/media/35309562/bgogo.png')
    HEDG = Coin(currency='HEDG', full_name='HedgeTrade', id='HEDG', url='https://www.cryptocompare.com/media/35309585/hedg.png')
    WBTC = Coin(currency='WBTC', full_name='Wrapped Bitcoin', id='WBTC', url='https://www.cryptocompare.com/media/35309588/wbtc.png')
    ERE = Coin(currency='ERE', full_name='Erecoin', id='ERE', url='https://www.cryptocompare.com/media/35309590/ere.png')
    BTU = Coin(currency='BTU', full_name='BTU Protocol', id='BTU', url='https://www.cryptocompare.com/media/35309595/btu.jpg')
    APS = Coin(currency='APS', full_name='APRES', id='APS', url='https://www.cryptocompare.com/media/35309596/aps.jpg')
    XBX = Coin(currency='XBX', full_name='BiteX', id='XBX', url='https://www.cryptocompare.com/media/35309597/xbx.jpg')
    QNT = Coin(currency='QNT', full_name='Quant', id='QNT', url='https://www.cryptocompare.com/media/35309600/qnt.jpg')
    FFUEL = Coin(currency='FFUEL', full_name='getFIFO', id='FFUEL', url='https://www.cryptocompare.com/media/35309603/ffuel.jpg')
    NSP = Coin(currency='NSP', full_name='NOMAD.space', id='NSP', url='https://www.cryptocompare.com/media/35309607/nsp.png')
    PTNX = Coin(currency='PTNX', full_name='Platin', id='PTNX', url='https://www.cryptocompare.com/media/35309608/ptnx.jpg')
    SNcoin = Coin(currency='SNcoin', full_name='ScientificCoin', id='SNcoin', url='https://www.cryptocompare.com/media/35309610/sncoin.png')
    TTN = Coin(currency='TTN', full_name='TITA Project', id='TTN', url='https://www.cryptocompare.com/media/35309611/ttn.jpg')
    BWT2 = Coin(currency='BWT2', full_name='Bitwin 2.0', id='BWT2', url='https://www.cryptocompare.com/media/35309628/bwt.jpg')
    OATH = Coin(currency='OATH', full_name='OATH Protocol', id='OATH', url='https://www.cryptocompare.com/media/35309629/oath.jpg')
    SBA = Coin(currency='SBA', full_name='simplyBrand', id='SBA', url='https://www.cryptocompare.com/media/35309630/sba.jpg')
    DXG = Coin(currency='DXG', full_name='DexAge', id='DXG', url='https://www.cryptocompare.com/media/35309632/dxg.png')
    EXTP = Coin(currency='EXTP', full_name='TradePlace', id='EXTP', url='https://www.cryptocompare.com/media/35309633/extp.jpg')
    ZEX = Coin(currency='ZEX', full_name='Zaddex', id='ZEX', url='https://www.cryptocompare.com/media/35309634/zex.png')
    XCZ = Coin(currency='XCZ', full_name='XCOYNZ', id='XCZ', url='https://www.cryptocompare.com/media/35309635/xcz.jpg')
    CBUK = Coin(currency='CBUK', full_name='CurveBlock', id='CBUK', url='https://www.cryptocompare.com/media/35309636/cbuk.png')
    HIX = Coin(currency='HIX', full_name='HELIX Orange', id='HIX', url='https://www.cryptocompare.com/media/35309641/hix.jpg')
    TGN = Coin(currency='TGN', full_name='TerraGreen', id='TGN', url='https://www.cryptocompare.com/media/35309643/tgn.png')
    COGS = Coin(currency='COGS', full_name='Cogmento', id='COGS', url='https://www.cryptocompare.com/media/35309642/cogs.jpg')
    XRM = Coin(currency='XRM', full_name='Aerum', id='XRM', url='https://www.cryptocompare.com/media/35309644/xrm.jpg')
    CCOIN = Coin(currency='CCOIN', full_name='Creditcoin', id='CCOIN', url='https://www.cryptocompare.com/media/35309645/ccoin.png')
    ICHX = Coin(currency='ICHX', full_name='IceChain', id='ICHX', url='https://www.cryptocompare.com/media/35309656/ichx.jpg')
    FORCE = Coin(currency='FORCE', full_name='TriForce Tokens', id='FORCE', url='https://www.cryptocompare.com/media/35309658/force.jpg')
    BTMX = Coin(currency='BTMX', full_name='BitMax Token', id='BTMX', url='https://www.cryptocompare.com/media/35309667/btmx.jpg')
    LTO = Coin(currency='LTO', full_name='LTO Network', id='LTO', url='https://www.cryptocompare.com/media/35309668/lto.png')
    QUSD = Coin(currency='QUSD', full_name='QUSD', id='QUSD', url='https://www.cryptocompare.com/media/35309698/qusd.png')
    BTH = Coin(currency='BTH', full_name='Bithereum', id='BTH', url='https://www.cryptocompare.com/media/35309700/bth.png')
    PLG = Coin(currency='PLG', full_name='Pledgecamp', id='PLG', url='https://www.cryptocompare.com/media/35309723/plg.jpg')
    PVP = Coin(currency='PVP', full_name='PVPChain', id='PVP', url='https://www.cryptocompare.com/media/35309734/pvp.png')
    EMANATE = Coin(currency='EMANATE', full_name='EMANATE', id='EMANATE', url='https://www.cryptocompare.com/media/35309742/emanate.jpg')
    CP = Coin(currency='CP', full_name='CryptoProfile', id='CP', url='https://www.cryptocompare.com/media/35309767/cp.png')
    DAYTA = Coin(currency='DAYTA', full_name='Dayta', id='DAYTA', url='https://www.cryptocompare.com/media/35520952/dayta.png')
    ORV = Coin(currency='ORV', full_name='Orvium', id='ORV', url='https://www.cryptocompare.com/media/35520955/orv.png')
    CWT = Coin(currency='CWT', full_name='Coinware', id='CWT', url='https://www.cryptocompare.com/media/35520956/cwt.png')
    AQU = Coin(currency='AQU', full_name='aQuest', id='AQU', url='https://www.cryptocompare.com/media/35520957/aqu.png')
    CXG = Coin(currency='CXG', full_name='Coinxes', id='CXG', url='https://www.cryptocompare.com/media/35520958/cxg.png')
    CHFT = Coin(currency='CHFT', full_name='CustomCoin', id='CHFT', url='https://www.cryptocompare.com/media/35520959/chft.png')
    VNTY = Coin(currency='VNTY', full_name='VENOTY', id='VNTY', url='https://www.cryptocompare.com/media/35520960/vnty.png')
    MAI = Coin(currency='MAI', full_name='Mindsync', id='MAI', url='https://www.cryptocompare.com/media/35520961/mai.png')
    BTR = Coin(currency='BTR', full_name='Bither', id='BTR', url='https://www.cryptocompare.com/media/35520962/btr.png')
    SSX = Coin(currency='SSX', full_name='SOMESING', id='SSX', url='https://www.cryptocompare.com/media/35520963/ssx.jpg')
    KLK = Coin(currency='KLK', full_name='Klickzie', id='KLK', url='https://www.cryptocompare.com/media/35520966/klk.png')
    LVN = Coin(currency='LVN', full_name='LivenPay', id='LVN', url='https://www.cryptocompare.com/media/35520970/lvn.png')
    AZU = Coin(currency='AZU', full_name='Azultec', id='AZU', url='https://www.cryptocompare.com/media/35520972/azu.png')
    ARQ = Coin(currency='ARQ', full_name='ArQmA', id='ARQ', url='https://www.cryptocompare.com/media/35520985/arq.png')
    WU = Coin(currency='WU', full_name='WULET', id='WU', url='https://www.cryptocompare.com/media/35520988/wu.png')
    ZUC = Coin(currency='ZUC', full_name='Zeux', id='ZUC', url='https://www.cryptocompare.com/media/35520989/zuc.png')
    FFM = Coin(currency='FFM', full_name='Files.fm Library', id='FFM', url='https://www.cryptocompare.com/media/35520991/ffm.png')
    DRF = Coin(currency='DRF', full_name='Drife', id='DRF', url='https://www.cryptocompare.com/media/35520992/drf.png')
    GTIB = Coin(currency='GTIB', full_name='Global Trust Coin', id='GTIB', url='https://www.cryptocompare.com/media/35520995/gtib.png')
    CR = Coin(currency='CR', full_name='CryptoRiyal', id='CR', url='https://www.cryptocompare.com/media/35520996/cr.png')
    VEO = Coin(currency='VEO', full_name='Amoveo', id='VEO', url='https://www.cryptocompare.com/media/35520997/veo.png')
    DLA = Coin(currency='DLA', full_name='Dolla', id='DLA', url='https://www.cryptocompare.com/media/35520998/dla.png')
    AFO = Coin(currency='AFO', full_name='AllForOneBusiness', id='AFO', url='https://www.cryptocompare.com/media/35520999/afo.png')
    FET = Coin(currency='FET', full_name='Fetch.AI', id='FET', url='https://www.cryptocompare.com/media/35521002/fet.png')
    DAGT = Coin(currency='DAGT', full_name='Digital Asset Guarantee Token', id='DAGT', url='https://www.cryptocompare.com/media/35521003/dagt.png')
    GVE = Coin(currency='GVE', full_name='Globalvillage Ecosystem', id='GVE', url='https://www.cryptocompare.com/media/35521004/gve.png')
    IDT = Coin(currency='IDT', full_name='InvestDigital', id='IDT', url='https://www.cryptocompare.com/media/35521005/itd.png')
    KUV = Coin(currency='KUV', full_name='Kuverit', id='KUV', url='https://www.cryptocompare.com/media/35521006/kuv.png')
    ARCX = Coin(currency='ARCX', full_name='ArcadierX', id='ARCX', url='https://www.cryptocompare.com/media/35521009/arcx.png')
    YACHTCO = Coin(currency='YACHTCO', full_name='Yachtco', id='YACHTCO', url='https://www.cryptocompare.com/media/35521014/yachtco.png')
    BOLTT = Coin(currency='BOLTT', full_name='BolttCoin', id='BOLTT', url='https://www.cryptocompare.com/media/35521013/boltt.png')
    ENCX = Coin(currency='ENCX', full_name='Encrybit', id='ENCX', url='https://www.cryptocompare.com/media/35521017/encx.png')
    VALID = Coin(currency='VALID', full_name='Validator Token', id='VALID', url='https://www.cryptocompare.com/media/35521018/valid.png')
    TYM = Coin(currency='TYM', full_name='Tryvium', id='TYM', url='https://www.cryptocompare.com/media/35521023/tym.png')
    VENUS = Coin(currency='VENUS', full_name='VenusEnergy', id='VENUS', url='https://www.cryptocompare.com/media/35521026/venus.png')
    HYGH = Coin(currency='HYGH', full_name='HYGH', id='HYGH', url='https://www.cryptocompare.com/media/35521025/hygh.png')
    NODIS = Coin(currency='NODIS', full_name='Nodis', id='NODIS', url='https://www.cryptocompare.com/media/35521028/nodis.png')
    MNC = Coin(currency='MNC', full_name='MainCoin', id='MNC', url='https://www.cryptocompare.com/media/35521031/mnc.png')
    USDS = Coin(currency='USDS', full_name='StableUSD', id='USDS', url='https://www.cryptocompare.com/media/35521034/usds.png')
    HVE = Coin(currency='HVE', full_name='UHIVE', id='HVE', url='https://www.cryptocompare.com/media/35521035/hve.png')
    XR = Coin(currency='XR', full_name='Gofind XR', id='XR', url='https://www.cryptocompare.com/media/35521036/xr.png')
    VALOR = Coin(currency='VALOR', full_name='Smart Valor', id='VALOR', url='https://www.cryptocompare.com/media/35521038/valor.png')
    ALP = Coin(currency='ALP', full_name='Alphacon', id='ALP', url='https://www.cryptocompare.com/media/35521037/alp.png')
    EMU = Coin(currency='EMU', full_name='eMusic', id='EMU', url='https://www.cryptocompare.com/media/35521039/emu.png')
    GST = Coin(currency='GST', full_name='GameStars', id='GST', url='https://www.cryptocompare.com/media/35521040/gst.png')
    ARS = Coin(currency='ARS', full_name='Artcoin', id='ARS', url='https://www.cryptocompare.com/media/35521047/ars.png')
    NRM = Coin(currency='NRM', full_name='Neuromachine', id='NRM', url='https://www.cryptocompare.com/media/35521051/nrm.png')
    APOD = Coin(currency='APOD', full_name='AirPod', id='APOD', url='https://www.cryptocompare.com/media/35521052/apod.png')
    AX = Coin(currency='AX', full_name='AlphaX', id='AX', url='https://www.cryptocompare.com/media/35521053/ax.png')
    CWEX = Coin(currency='CWEX', full_name='Crypto Wine Exchange', id='CWEX', url='https://www.cryptocompare.com/media/35521061/cwex.png')
    CLDX = Coin(currency='CLDX', full_name='Cloverdex', id='CLDX', url='https://www.cryptocompare.com/media/35521069/cldx.png')
    LABX = Coin(currency='LABX', full_name='Stakinglab', id='LABX', url='https://www.cryptocompare.com/media/35521071/labx.png')
    GGC = Coin(currency='GGC', full_name='Gingr', id='GGC', url='https://www.cryptocompare.com/media/35521083/ggc.png')
    AGT = Coin(currency='AGT', full_name='AGATE', id='AGT', url='https://www.cryptocompare.com/media/35521084/agt.png')
    ENV = Coin(currency='ENV', full_name='Envienta', id='ENV', url='https://www.cryptocompare.com/media/35521085/env.png')
    ANKR = Coin(currency='ANKR', full_name='Ankr Network', id='ANKR', url='https://www.cryptocompare.com/media/35521086/ankr.png')
    GEP = Coin(currency='GEP', full_name='Gaia', id='GEP', url='https://www.cryptocompare.com/media/35521093/gep.png')
    IZA = Coin(currency='IZA', full_name='Inzura', id='IZA', url='https://www.cryptocompare.com/media/35521096/iza.png')
    GBA = Coin(currency='GBA', full_name='Geeba', id='GBA', url='https://www.cryptocompare.com/media/35521097/gba.png')
    ITU = Coin(currency='ITU', full_name='iTrue', id='ITU', url='https://www.cryptocompare.com/media/35521098/itu.png')
    FANZ = Coin(currency='FANZ', full_name='FanChain', id='FANZ', url='https://www.cryptocompare.com/media/35521101/fanz.png')
    CSPN = Coin(currency='CSPN', full_name='Crypto Sports', id='CSPN', url='https://www.cryptocompare.com/media/35521102/cspn.png')
    CCH = Coin(currency='CCH', full_name='Coinchase', id='CCH', url='https://www.cryptocompare.com/media/35521105/cch.png')
    HAVEN = Coin(currency='HAVEN', full_name='Safe Haven', id='HAVEN', url='https://www.cryptocompare.com/media/35521107/sha.png')
    XOV = Coin(currency='XOV', full_name='XOVBank', id='XOV', url='https://www.cryptocompare.com/media/35521109/xov.png')
    eQUAD = Coin(currency='eQUAD', full_name='Quadrant Protocol', id='eQUAD', url='https://www.cryptocompare.com/media/35521110/equad.png')
    CUR = Coin(currency='CUR', full_name='Cura Network', id='CUR', url='https://www.cryptocompare.com/media/35521111/cur.png')
    CREDIT = Coin(currency='CREDIT', full_name='Credit', id='CREDIT', url='https://www.cryptocompare.com/media/35521112/credit.png')
    ERA = Coin(currency='ERA', full_name='ETHA', id='ERA', url='https://www.cryptocompare.com/media/35521113/era.png')
    MAKE = Coin(currency='MAKE', full_name='MAKE', id='MAKE', url='https://www.cryptocompare.com/media/35521116/make.png')
    KIBIS = Coin(currency='KIBIS', full_name='KIBIS', id='KIBIS', url='https://www.cryptocompare.com/media/35521117/kibis.png')
    SPKZ = Coin(currency='SPKZ', full_name='Spokkz', id='SPKZ', url='https://www.cryptocompare.com/media/35521119/spkz.png')
    OGO = Coin(currency='OGO', full_name='VogoV', id='OGO', url='https://www.cryptocompare.com/media/35521120/ogo.png')
    AWC = Coin(currency='AWC', full_name='Atomic Wallet Coin', id='AWC', url='https://www.cryptocompare.com/media/35521121/awc.png')
    DIS = Coin(currency='DIS', full_name='DiscoveryIoT', id='DIS', url='https://www.cryptocompare.com/media/35521122/dis.png')
    SCRIBE = Coin(currency='SCRIBE', full_name='Scribe Network', id='SCRIBE', url='https://www.cryptocompare.com/media/35521125/scribe.png')
    INX = Coin(currency='INX', full_name='InMax', id='INX', url='https://www.cryptocompare.com/media/35521126/inx.png')
    SQR = Coin(currency='SQR', full_name='Squeezer', id='SQR', url='https://www.cryptocompare.com/media/35521134/sqr.png')
    PHT = Coin(currency='PHT', full_name='Photon Token', id='PHT', url='https://www.cryptocompare.com/media/35521139/pht.png')
    CRO = Coin(currency='CRO', full_name='Crypto.com Chain Token', id='CRO', url='https://www.cryptocompare.com/media/34478435/mco.png')
    LYTX = Coin(currency='LYTX', full_name='LYTIX', id='LYTX', url='https://www.cryptocompare.com/media/35521149/lytx.png')
    TJA = Coin(currency='TJA', full_name='TapJets', id='TJA', url='https://www.cryptocompare.com/media/35521150/tja.png')
    InBit = Coin(currency='InBit', full_name='PrepayWay', id='InBit', url='https://www.cryptocompare.com/media/35521151/inbit.png')
    DIO = Coin(currency='DIO', full_name='Decimated', id='DIO', url='https://www.cryptocompare.com/media/35521152/dio-2.png')
    LIC = Coin(currency='LIC', full_name='Ligercoin', id='LIC', url='https://www.cryptocompare.com/media/35521153/lic.png')
    SCA = Coin(currency='SCA', full_name='SiaClassic', id='SCA', url='https://www.cryptocompare.com/media/35521154/sc.png')
    XOS = Coin(currency='XOS', full_name='Excalibur OS', id='XOS', url='https://www.cryptocompare.com/media/35521155/xos.png')
    VSYS = Coin(currency='VSYS', full_name='V Systems', id='VSYS', url='https://www.cryptocompare.com/media/35521163/vsys.png')
    LAC = Coin(currency='LAC', full_name='LOVE Air Coffee', id='LAC', url='https://www.cryptocompare.com/media/35521164/lac.png')
    QCP = Coin(currency='QCP', full_name='Crypto Potential', id='QCP', url='https://www.cryptocompare.com/media/35521165/qcp.png')
    UGT = Coin(currency='UGT', full_name='Universal Games Token', id='UGT', url='https://www.cryptocompare.com/media/35521169/ugt.png')
    BWL = Coin(currency='BWL', full_name='Bitwala Token', id='BWL', url='https://www.cryptocompare.com/media/35521170/btw.png')
    WATT = Coin(currency='WATT', full_name='WorkChain.io', id='WATT', url='https://www.cryptocompare.com/media/35521175/watt.png')
    XRX = Coin(currency='XRX', full_name='Global Property Register', id='XRX', url='https://www.cryptocompare.com/media/35521173/xrx.png')
    TFF = Coin(currency='TFF', full_name='TheFaustFlick', id='TFF', url='https://www.cryptocompare.com/media/35521185/tff.png')
    ANY = Coin(currency='ANY', full_name='Anything App', id='ANY', url='https://www.cryptocompare.com/media/35521186/any.png')
    ELOC = Coin(currency='ELOC', full_name='eLocations', id='ELOC', url='https://www.cryptocompare.com/media/35521187/ecol.png')
    IZZY = Coin(currency='IZZY', full_name='Izzy', id='IZZY', url='https://www.cryptocompare.com/media/35521189/izzy.png')
    SONT = Coin(currency='SONT', full_name='Sonata.ai', id='SONT', url='https://www.cryptocompare.com/media/35521190/sont.png')
    SWI = Coin(currency='SWI', full_name='Swinca', id='SWI', url='https://www.cryptocompare.com/media/35521192/swi.png')
    LUNES = Coin(currency='LUNES', full_name='Lunes', id='LUNES', url='https://www.cryptocompare.com/media/35521195/lunes.png')
    EDEXA = Coin(currency='EDEXA', full_name='edeXa Security Token', id='EDEXA', url='https://www.cryptocompare.com/media/35521196/edexa.png')
    PPI = Coin(currency='PPI', full_name='Primpy', id='PPI', url='https://www.cryptocompare.com/media/35521204/ppi.png')
    ANTE = Coin(currency='ANTE', full_name='ANTE', id='ANTE', url='https://www.cryptocompare.com/media/35521205/ante.png')
    TRXDICE = Coin(currency='TRXDICE', full_name='TRONdice', id='TRXDICE', url='https://www.cryptocompare.com/media/35521207/trxdice.png')
    AFTT = Coin(currency='AFTT', full_name='Africa Trading Chain', id='AFTT', url='https://www.cryptocompare.com/media/35521208/aftt.png')
    TRXWIN = Coin(currency='TRXWIN', full_name='TronWin', id='TRXWIN', url='https://www.cryptocompare.com/media/35521210/trxwin.png')
    TWJ = Coin(currency='TWJ', full_name='TronWeeklyJournal', id='TWJ', url='https://www.cryptocompare.com/media/35521211/twj.png')
    IGG = Coin(currency='IGG', full_name='IG Gold', id='IGG', url='https://www.cryptocompare.com/media/35521212/xkar9bf6_400x400.jpg')
    DARB = Coin(currency='DARB', full_name='Darb Token', id='DARB', url='https://www.cryptocompare.com/media/35521222/darb.png')
    MBTX = Coin(currency='MBTX', full_name='MinedBlock', id='MBTX', url='https://www.cryptocompare.com/media/35521223/mbtx.png')
    CFun = Coin(currency='CFun', full_name='CFun', id='CFun', url='https://www.cryptocompare.com/media/35521237/cfun.png')
    ECTE = Coin(currency='ECTE', full_name='EurocoinToken', id='ECTE', url='https://www.cryptocompare.com/media/35521248/ecte.png')
    BUY = Coin(currency='BUY', full_name='Buying.com', id='BUY', url='https://www.cryptocompare.com/media/35521249/buy.png')
    LWA = Coin(currency='LWA', full_name='Leap With Alice', id='LWA', url='https://www.cryptocompare.com/media/35521251/lwa.png')
    INR = Coin(currency='INR', full_name='Insure Network', id='INR', url='https://www.cryptocompare.com/media/35521253/inr.png')
    REDi = Coin(currency='REDi', full_name='REDI', id='REDi', url='https://www.cryptocompare.com/media/35521254/redi.png')
    AAS = Coin(currency='AAS', full_name='aassio', id='AAS', url='https://www.cryptocompare.com/media/35521241/aas.png')
    PCC = Coin(currency='PCC', full_name='PCORE', id='PCC', url='https://www.cryptocompare.com/media/35521219/pcc.png')
    IPUX = Coin(currency='IPUX', full_name='IPUX', id='IPUX', url='https://www.cryptocompare.com/media/35521217/ipux.png')
    BWN = Coin(currency='BWN', full_name='BitWings', id='BWN', url='https://www.cryptocompare.com/media/35521215/bwn.png')
    MIG = Coin(currency='MIG', full_name='Migranet', id='MIG', url='https://www.cryptocompare.com/media/35521213/mig.png')
    T4M = Coin(currency='T4M', full_name='Tap4.Menu', id='T4M', url='https://www.cryptocompare.com/media/35521184/t4m.png')
    ZEON = Coin(currency='ZEON', full_name='Zeon Network', id='ZEON', url='https://www.cryptocompare.com/media/35521171/zeon.png')
    WHY = Coin(currency='WHY', full_name='Whisky Token', id='WHY', url='https://www.cryptocompare.com/media/35521255/why.png')
    SLC = Coin(currency='SLC', full_name='SLICE', id='SLC', url='https://www.cryptocompare.com/media/35521240/slc.png')
    VOLLAR = Coin(currency='VOLLAR', full_name='Vollar', id='VOLLAR', url='https://www.cryptocompare.com/media/35521259/vollar.png')
    URIS = Coin(currency='URIS', full_name='Uris', id='URIS', url='https://www.cryptocompare.com/media/35521258/uris.png')
    MBTC = Coin(currency='MBTC', full_name='MicroBitcoin', id='MBTC', url='https://www.cryptocompare.com/media/34836000/mbc.png')
    HRD = Coin(currency='HRD', full_name='Hoard', id='HRD', url='https://www.cryptocompare.com/media/35521262/hrd.png')
    SHER = Coin(currency='SHER', full_name='Shercoin', id='SHER', url='https://www.cryptocompare.com/media/35521263/sher.png')
    QCO = Coin(currency='QCO', full_name='Qravity', id='QCO', url='https://www.cryptocompare.com/media/35521264/qco.png')
    ZB = Coin(currency='ZB', full_name='ZeroBank', id='ZB', url='https://www.cryptocompare.com/media/35521265/zb.png')
    ISG = Coin(currency='ISG', full_name='ISG', id='ISG', url='https://www.cryptocompare.com/media/35521266/isg.png')
    GEC = Coin(currency='GEC', full_name='Geco.one', id='GEC', url='https://www.cryptocompare.com/media/35521267/gec.png')
    TAGZ = Coin(currency='TAGZ', full_name='TAGZ', id='TAGZ', url='https://www.cryptocompare.com/media/35521268/tagz.png')
    SKP = Coin(currency='SKP', full_name='Skelpy', id='SKP', url='https://www.cryptocompare.com/media/35521269/skp.png')
    MCC = Coin(currency='MCC', full_name='MyCreditChain', id='MCC', url='https://www.cryptocompare.com/media/35521270/mcc.png')
    CELR = Coin(currency='CELR', full_name='Celer Network', id='CELR', url='https://www.cryptocompare.com/media/35521202/celr.png')
    XGN = Coin(currency='XGN', full_name='Golden Currency', id='XGN', url='https://www.cryptocompare.com/media/35521279/xgn.png')
    YPTO = Coin(currency='YPTO', full_name='YPTOspace', id='YPTO', url='https://www.cryptocompare.com/media/35521283/ypto.png')
    UBE = Coin(currency='UBE', full_name='Ubecoin', id='UBE', url='https://www.cryptocompare.com/media/35521284/ube.png')
    XLM = Coin(currency='XLM', full_name='Stellar', id='XLM', url='https://www.cryptocompare.com/media/35521289/xlm.png')
    VRA = Coin(currency='VRA', full_name='Verasity', id='VRA', url='https://www.cryptocompare.com/media/33187836/vra.jpg')
    ETGP = Coin(currency='ETGP', full_name='Ethereum Gold Project', id='ETGP', url='https://www.cryptocompare.com/media/35521290/etgp.png')
    GFCS = Coin(currency='GFCS', full_name='Global Funeral Care', id='GFCS', url='https://www.cryptocompare.com/media/35521292/gfcs.png')
    IX = Coin(currency='IX', full_name='X-Block', id='IX', url='https://www.cryptocompare.com/media/35521293/ix.png')
    RDT = Coin(currency='RDT', full_name='Reindeer', id='RDT', url='https://www.cryptocompare.com/media/35521294/rdt.png')
    ALIC = Coin(currency='ALIC', full_name='AliCoin', id='ALIC', url='https://www.cryptocompare.com/media/35521296/alic.png')
    HCXP = Coin(currency='HCXP', full_name='HCX PAY', id='HCXP', url='https://www.cryptocompare.com/media/35521297/hcxp.png')
    AGRO = Coin(currency='AGRO', full_name='Bit Agro', id='AGRO', url='https://www.cryptocompare.com/media/35521298/agro.png')
    TFUEL = Coin(currency='TFUEL', full_name='Theta Fuel', id='TFUEL', url='https://www.cryptocompare.com/media/35521299/tfuel.png')
    BYTS = Coin(currency='BYTS', full_name='Bytus', id='BYTS', url='https://www.cryptocompare.com/media/35521303/byts.png')
    GRT = Coin(currency='GRT', full_name='GoRecruit', id='GRT', url='https://www.cryptocompare.com/media/35521304/grt.png')
    MYTV = Coin(currency='MYTV', full_name='MyTVchain', id='MYTV', url='https://www.cryptocompare.com/media/35521305/mytv.png')
    EUCX = Coin(currency='EUCX', full_name='EUCX', id='EUCX', url='https://www.cryptocompare.com/media/35521306/eucx.png')
    DRG = Coin(currency='DRG', full_name='Dragon Coin', id='DRG', url='https://www.cryptocompare.com/media/25792571/drg.png')
    DXN = Coin(currency='DXN', full_name='DEXON', id='DXN', url='https://www.cryptocompare.com/media/35521250/dex.png')
    AML = Coin(currency='AML', full_name='AMANPURI', id='AML', url='https://www.cryptocompare.com/media/35521318/aml.png')
    B66 = Coin(currency='B66', full_name='Block66', id='B66', url='https://www.cryptocompare.com/media/35521319/b66.png')
    LEVL = Coin(currency='LEVL', full_name='Levolution', id='LEVL', url='https://www.cryptocompare.com/media/35521321/levl.png')
    DHC = Coin(currency='DHC', full_name='dClinic', id='DHC', url='https://www.cryptocompare.com/media/35521324/dhc.png')
    UGAS = Coin(currency='UGAS', full_name='Ultrain', id='UGAS', url='https://www.cryptocompare.com/media/35521325/ugas.png')
    PNP = Coin(currency='PNP', full_name='LogisticsX', id='PNP', url='https://www.cryptocompare.com/media/35521327/pnp.png')
    EDO = Coin(currency='EDO', full_name='Eidoo', id='EDO', url='https://www.cryptocompare.com/media/35521333/eidoo.jpg')
    ORS = Coin(currency='ORS', full_name='ORS Group', id='ORS', url='https://www.cryptocompare.com/media/30002247/orst.png')
    FCT = Coin(currency='FCT', full_name='Factoids', id='FCT', url='https://www.cryptocompare.com/media/1382863/fct1.png')
    PRY = Coin(currency='PRY', full_name='PRIMARY', id='PRY', url='https://www.cryptocompare.com/media/35521337/pry.png')
    MXM = Coin(currency='MXM', full_name='Maximine', id='MXM', url='https://www.cryptocompare.com/media/35521338/mxm.png')
    TITC = Coin(currency='TITC', full_name='TitCoin', id='TITC', url='https://www.cryptocompare.com/media/20069/tit.png')
    TTC = Coin(currency='TTC', full_name='TTC PROTOCOL', id='TTC', url='https://www.cryptocompare.com/media/35521339/ttc.png')
    BCNX = Coin(currency='BCNX', full_name='BCNEX', id='BCNX', url='https://www.cryptocompare.com/media/35521340/bcnx.png')
    SWG = Coin(currency='SWG', full_name='Swing', id='SWG', url='https://www.cryptocompare.com/media/35521343/swg.png')
    HTER = Coin(currency='HTER', full_name='Biogen', id='HTER', url='https://www.cryptocompare.com/media/35521344/hter.png')
    EVED = Coin(currency='EVED', full_name='Evedo', id='EVED', url='https://www.cryptocompare.com/media/35521342/eved.png')
    GSE = Coin(currency='GSE', full_name='Gese', id='GSE', url='https://www.cryptocompare.com/media/35521345/gse.png')
    BZRX = Coin(currency='BZRX', full_name='bZx', id='BZRX', url='https://www.cryptocompare.com/media/35521346/bzrx.png')
    GIF = Coin(currency='GIF', full_name='Gift Token', id='GIF', url='https://www.cryptocompare.com/media/35521350/gif.png')
    YBK = Coin(currency='YBK', full_name='YourBlock', id='YBK', url='https://www.cryptocompare.com/media/35521347/ybk.png')
    STG = Coin(currency='STG', full_name='STAYGE', id='STG', url='https://www.cryptocompare.com/media/35521355/stg.png')
    DEVX = Coin(currency='DEVX', full_name='Developeo', id='DEVX', url='https://www.cryptocompare.com/media/35521357/devx.png')
    TMB = Coin(currency='TMB', full_name='Teambrella', id='TMB', url='https://www.cryptocompare.com/media/35521358/tmb.png')
    HBRS = Coin(currency='HBRS', full_name='HubrisOne', id='HBRS', url='https://www.cryptocompare.com/media/35521359/hbrs.png')
    XPL = Coin(currency='XPL', full_name='Exclusive Platform', id='XPL', url='https://www.cryptocompare.com/media/35521360/xpl.png')
    MTSH = Coin(currency='MTSH', full_name='Mitoshi', id='MTSH', url='https://www.cryptocompare.com/media/35521363/mtsh.png')
    DAGO = Coin(currency='DAGO', full_name='Dago Mining', id='DAGO', url='https://www.cryptocompare.com/media/35521364/dago.png')
    EMI = Coin(currency='EMI', full_name='EIPlatform', id='EMI', url='https://www.cryptocompare.com/media/35521369/emi.png')
    TEMPO = Coin(currency='TEMPO', full_name='Tempo', id='TEMPO', url='https://www.cryptocompare.com/media/35521370/tempo.png')
    PPR = Coin(currency='PPR', full_name='Papyrus', id='PPR', url='https://www.cryptocompare.com/media/35521371/ppr.png')
    REW = Coin(currency='REW', full_name='Review.Network', id='REW', url='https://www.cryptocompare.com/media/35521372/rew.png')
    ORBIS = Coin(currency='ORBIS', full_name='Orbis', id='ORBIS', url='https://www.cryptocompare.com/media/34477897/orbs.jpg')
    ORBS = Coin(currency='ORBS', full_name='Orbs', id='ORBS', url='https://www.cryptocompare.com/media/35521373/orbs.png')
    STE = Coin(currency='STE', full_name='Streamex', id='STE', url='https://www.cryptocompare.com/media/35521376/ste.png')
    TPLAY = Coin(currency='TPLAY', full_name='TruePlay', id='TPLAY', url='https://www.cryptocompare.com/media/35521377/tplay.png')
    GYM = Coin(currency='GYM', full_name='Gym Rewards', id='GYM', url='https://www.cryptocompare.com/media/35521379/gym.png')
    VIDT = Coin(currency='VIDT', full_name='V-ID', id='VIDT', url='https://www.cryptocompare.com/media/34155586/vid.png')
    UDOO = Coin(currency='UDOO', full_name='Howdoo', id='UDOO', url='https://www.cryptocompare.com/media/35521381/udoo.png')
    FAT = Coin(currency='FAT', full_name='Fatcoin', id='FAT', url='https://www.cryptocompare.com/media/35521380/fatbtc.png')
    TAN = Coin(currency='TAN', full_name='Taklimakan', id='TAN', url='https://www.cryptocompare.com/media/35521383/tkln.png')
    KICKS = Coin(currency='KICKS', full_name='SESSIA', id='KICKS', url='https://www.cryptocompare.com/media/35650281/qqt0pvlv_400x400.png')
    LYM = Coin(currency='LYM', full_name='Lympo', id='LYM', url='https://www.cryptocompare.com/media/27010755/lym.png')
    SPORTG = Coin(currency='SPORTG', full_name='SportGift', id='SPORTG', url='https://www.cryptocompare.com/media/35650283/sportg.png')
    CRES = Coin(currency='CRES', full_name='Cresio', id='CRES', url='https://www.cryptocompare.com/media/35650284/cres.png')
    NOKU = Coin(currency='NOKU', full_name='NOKU Master token', id='NOKU', url='https://www.cryptocompare.com/media/30002224/noku.jpg')
    BINC = Coin(currency='BINC', full_name='BINCOIN', id='BINC', url='https://www.cryptocompare.com/media/35521261/bin.png')
    RIF = Coin(currency='RIF', full_name='RIF Token', id='RIF', url='https://www.cryptocompare.com/media/35309430/rif.jpg')
    PERU = Coin(currency='PERU', full_name='PeruCoin', id='PERU', url='https://www.cryptocompare.com/media/34477804/peru.png')
    FIII = Coin(currency='FIII', full_name='Fiii', id='FIII', url='https://www.cryptocompare.com/media/35284455/fiii.png')
    FIH = Coin(currency='FIH', full_name='Fidelity House', id='FIH', url='https://www.cryptocompare.com/media/34836045/fih.png')
    GNC = Coin(currency='GNC', full_name='Greencoin', id='GNC', url='https://www.cryptocompare.com/media/35521135/gnc.png')
    WHN = Coin(currency='WHN', full_name='Windhan Energy', id='WHN', url='https://www.cryptocompare.com/media/35521140/whn.png')
    VC = Coin(currency='VC', full_name='Vecap', id='VC', url='https://www.cryptocompare.com/media/35309443/vc.png')
    SRX = Coin(currency='SRX', full_name='Solarex', id='SRX', url='https://www.cryptocompare.com/media/35309543/srx.png')
    GUAR = Coin(currency='GUAR', full_name='Guarium', id='GUAR', url='https://www.cryptocompare.com/media/35309520/guar.jpg')
    AFCT = Coin(currency='AFCT', full_name='Allforcrypto', id='AFCT', url='https://www.cryptocompare.com/media/35521252/afct.png')
    JVY = Coin(currency='JVY', full_name='Javvy', id='JVY', url='https://www.cryptocompare.com/media/34835970/javvy-blockchain-icon-rgb_550x550_transparent_v2-dark-blue-copy-copy.png')
    VLTX = Coin(currency='VLTX', full_name='Volentix', id='VLTX', url='https://www.cryptocompare.com/media/35284380/vltx.png')
    LYN = Coin(currency='LYN', full_name='LYNCHPIN Token', id='LYN', url='https://www.cryptocompare.com/media/35309173/lyn.png')
    HXC = Coin(currency='HXC', full_name='HexanCoin', id='HXC', url='https://www.cryptocompare.com/media/35264192/hxc.png')
    BB1 = Coin(currency='BB1', full_name='Bitbond', id='BB1', url='https://www.cryptocompare.com/media/35521001/bb1.png')
    eSwitch = Coin(currency='eSwitch', full_name='ShareMeAll', id='eSwitch', url='https://www.cryptocompare.com/media/35309508/eswitch.jpg')
    PARQ = Coin(currency='PARQ', full_name='PARQ', id='PARQ', url='https://www.cryptocompare.com/media/35521181/parq.png')
    ALCE = Coin(currency='ALCE', full_name='Alcedo', id='ALCE', url='https://www.cryptocompare.com/media/35521027/alce.png')
    ADUX = Coin(currency='ADUX', full_name='Adult X Token', id='ADUX', url='https://www.cryptocompare.com/media/35521260/adux.png')
    IMP = Coin(currency='IMP', full_name='CoinIMP', id='IMP', url='https://www.cryptocompare.com/media/35309657/imp.jpg')
    BCNA = Coin(currency='BCNA', full_name='BitCanna', id='BCNA', url='https://www.cryptocompare.com/media/35284439/bcna.png')
    AZ = Coin(currency='AZ', full_name='Azbit', id='AZ', url='https://www.cryptocompare.com/media/34478502/az.png')
    APZ = Coin(currency='APZ', full_name='Alprockz', id='APZ', url='https://www.cryptocompare.com/media/35309646/apz.jpg')
    WVR = Coin(currency='WVR', full_name='Weave', id='WVR', url='https://www.cryptocompare.com/media/35521138/wvr.png')
    FFCT = Coin(currency='FFCT', full_name='FortFC', id='FFCT', url='https://www.cryptocompare.com/media/35520971/ffct.png')
    TELE = Coin(currency='TELE', full_name='Miracle Tele', id='TELE', url='https://www.cryptocompare.com/media/35521378/tele.png')
    REME = Coin(currency='REME', full_name='REME-Coin', id='REME', url='https://www.cryptocompare.com/media/35309538/reme.jpg')
    RAIZER = Coin(currency='RAIZER', full_name='RAIZER', id='RAIZER', url='https://www.cryptocompare.com/media/35309766/raizer.jpg')
    BTMK = Coin(currency='BTMK', full_name='BitMark', id='BTMK', url='https://www.cryptocompare.com/media/20084/btm.png')
    AES = Coin(currency='AES', full_name='Artis Aes Evolution', id='AES', url='https://www.cryptocompare.com/media/35650299/aes.png')
    AIBK = Coin(currency='AIBK', full_name='AIB Utility Token', id='AIBK', url='https://www.cryptocompare.com/media/35650301/aibk.png')
    XDN = Coin(currency='XDN', full_name='DigitalNote ', id='XDN', url='https://www.cryptocompare.com/media/35650302/xdn.png')
    NCC = Coin(currency='NCC', full_name='NeuroChain', id='NCC', url='https://www.cryptocompare.com/media/35650303/ncc.png')
    AION = Coin(currency='AION', full_name='Aion', id='AION', url='https://www.cryptocompare.com/media/35650307/aion.jpg')
    WAN = Coin(currency='WAN', full_name='Wanchain', id='WAN', url='https://www.cryptocompare.com/media/9350742/wan.jpg')
    POLY = Coin(currency='POLY', full_name='Polymath Network', id='POLY', url='https://www.cryptocompare.com/media/27010571/poly.png')
    XTZ = Coin(currency='XTZ', full_name='Tezos', id='XTZ', url='https://www.cryptocompare.com/media/1383651/xbt.png')
    DAI = Coin(currency='DAI', full_name='Dai', id='DAI', url='https://www.cryptocompare.com/media/27010778/dai.jpg')
    STONE = Coin(currency='STONE', full_name='DataBloc', id='STONE', url='https://www.cryptocompare.com/media/35650308/stone.png')
    OILD = Coin(currency='OILD', full_name='OilWellCoin', id='OILD', url='https://www.cryptocompare.com/media/35650310/oild.png')
    VLM = Coin(currency='VLM', full_name='Volum', id='VLM', url='https://www.cryptocompare.com/media/35650311/vlm.png')
    BSV = Coin(currency='BSV', full_name='Bitcoin SV', id='BSV', url='https://www.cryptocompare.com/media/35309257/bsv1.png')
    BCH = Coin(currency='BCH', full_name='Bitcoin Cash', id='BCH', url='https://www.cryptocompare.com/media/1383919/12-bitcoin-cash-square-crop-small-grn.png')
    BCD = Coin(currency='BCD', full_name='Bitcoin Diamond', id='BCD', url='https://www.cryptocompare.com/media/16404872/bcd.png')
    ZEN = Coin(currency='ZEN', full_name='Horizen', id='ZEN', url='https://www.cryptocompare.com/media/34478457/horizen.png')
    LOL = Coin(currency='LOL', full_name='LOL Coin', id='LOL', url='https://www.cryptocompare.com/media/35650312/lol.png')
    AUDC = Coin(currency='AUDC', full_name='Aussie Digital', id='AUDC', url='https://www.cryptocompare.com/media/34478256/aud.png')
    PART = Coin(currency='PART', full_name='Particl', id='PART', url='https://www.cryptocompare.com/media/35650315/part.png')
    TTT = Coin(currency='TTT', full_name='Tap Project', id='TTT', url='https://www.cryptocompare.com/media/35650348/ttt.png')
    PRL = Coin(currency='PRL', full_name='Oyster Pearl', id='PRL', url='https://www.cryptocompare.com/media/16746488/prl.png')
    EDUC = Coin(currency='EDUC', full_name='EducoinV', id='EDUC', url='https://www.cryptocompare.com/media/351066/edc.png')
    EDC = Coin(currency='EDC', full_name='EDC Blockchain', id='EDC', url='https://www.cryptocompare.com/media/35650352/edc.png')
    RFOX = Coin(currency='RFOX', full_name='RedFOX Labs', id='RFOX', url='https://www.cryptocompare.com/media/35650353/rfox.png')
    CTLX = Coin(currency='CTLX', full_name='Cash Telex', id='CTLX', url='https://www.cryptocompare.com/media/35650354/ctlx.png')
    CSM = Coin(currency='CSM', full_name='Consentium', id='CSM', url='https://www.cryptocompare.com/media/35650355/csm.png')
    BTNY = Coin(currency='BTNY', full_name='Bitney', id='BTNY', url='https://www.cryptocompare.com/media/35650356/btny.png')
    MINT = Coin(currency='MINT', full_name='MintCoin', id='MINT', url='https://www.cryptocompare.com/media/35650359/mint.png')
    GBYTE = Coin(currency='GBYTE', full_name='Obyte', id='GBYTE', url='https://www.cryptocompare.com/media/35650360/gbyte.png')
    GUSD = Coin(currency='GUSD', full_name='Gemini Dollar', id='GUSD', url='https://www.cryptocompare.com/media/34478391/gusd.png')
    NOIZ = Coin(currency='NOIZ', full_name='NOIZ', id='NOIZ', url='https://www.cryptocompare.com/media/34478002/noiz.jpg')
    GX = Coin(currency='GX', full_name='GameX', id='GX', url='https://www.cryptocompare.com/media/20780801/gamex.png')
    TOKC = Coin(currency='TOKC', full_name='Tokyo Coin', id='TOKC', url='https://www.cryptocompare.com/media/27010853/tokc.jpg')
    BLITZ = Coin(currency='BLITZ', full_name='BlitzCoin', id='BLITZ', url='https://www.cryptocompare.com/media/350612/blitz.png')
    XEN = Coin(currency='XEN', full_name='XenixCoin', id='XEN', url='https://www.cryptocompare.com/media/352119/xen.jpg')
    ACH = Coin(currency='ACH', full_name='AchieveCoin', id='ACH', url='https://www.cryptocompare.com/media/30002098/ach.jpg')
    FORK = Coin(currency='FORK', full_name='Gastro Advisor Token', id='FORK', url='https://www.cryptocompare.com/media/34836112/fork.png')
    VIG = Coin(currency='VIG', full_name='TheVig', id='VIG', url='https://www.cryptocompare.com/media/33957398/vig.jpg')
    BTG = Coin(currency='BTG', full_name='Bitcoin Gold', id='BTG', url='https://www.cryptocompare.com/media/27011062/btg.png')

    transaction3 = Transaction(user=stephano, buy=1000, buy_quantity=5, coin=ETH, timestamp='2015-03-18')
    transaction2 = Transaction(user=stephano, sell=500, sell_quantity=2, coin=LTC, timestamp='2015-02-18')
    transaction13 = Transaction(user=stephano, sell=500, sell_quantity=2, coin=BTC, timestamp='2015-02-18')
    transaction14 = Transaction(user=stephano, sell=500, sell_quantity=2, coin=BTC, timestamp='2015-02-18')
    transaction1 = Transaction(user=stephano, buy=1000, buy_quantity=13, coin=BTC, timestamp='2015-01-18')
    transaction5 = Transaction(user=stephano, buy=1000, buy_quantity=6, coin=LTC, timestamp='2015-05-18')
    transaction6 = Transaction(user=stephano, sell=500, sell_quantity=2, coin=LTC, timestamp='2015-06-18')
    transaction15 = Transaction(user=stephano, sell=500, sell_quantity=2, coin=ETH, timestamp='2015-06-18')
    transaction16 = Transaction(user=stephano, sell=500, sell_quantity=2, coin=BTC, timestamp='2015-06-18')
    transaction17 = Transaction(user=stephano, sell=500, sell_quantity=2, coin=XRP, timestamp='2015-06-18')
    transaction8 = Transaction(user=stephano, sell=500, sell_quantity=1, coin=XRP, timestamp='2015-08-18')
    transaction4 = Transaction(user=stephano, sell=500, sell_quantity=3, coin=ETH, timestamp='2015-04-18')
    transaction9 = Transaction(user=stephano, sell=500, buy_quantity=3, coin=LTC, timestamp='2015-09-18')
    transaction7 = Transaction(user=stephano, buy=1000, buy_quantity=8, coin=XRP, timestamp='2015-07-18')
    transaction10 = Transaction(user=stephano, sell=500, coin=LTC, timestamp='2015-10-18')
    transaction11 = Transaction(user=stephano, sell=500, coin=BTC, timestamp='2015-11-18')
    transaction12 = Transaction(user=stephano, sell=500, sell_quantity=6, coin=BTC, timestamp='2015-12-18')

    transaction20 = Transaction(user=sabo, buy=200, buy_quantity=6, coin=BTC, timestamp='2016-12-18')
    transaction21 = Transaction(user=sabo, buy=2, buy_quantity=6, coin=LTC, timestamp='2015-12-18')
    transaction22 = Transaction(user=sabo, sell=10, sell_quantity=6, coin=ETH, timestamp='2013-12-18')
    transaction23 = Transaction(user=sabo, sell=2, sell_quantity=3, coin=LTC, timestamp='2015-2-18')
    transaction24 = Transaction(user=sabo, buy=10, buy_quantity=6, coin=XRP, timestamp='2015-9-18')

    db.session.add_all([transaction1,
     transaction2, transaction3, transaction4, transaction5, transaction6, transaction7,
     transaction8, transaction9, transaction10, transaction11, transaction12, transaction13, transaction14,
     transaction15, transaction16, transaction17, transaction20, transaction21, transaction22, transaction23, transaction24,


BTC,
ETH,
LTC,
DASH,
XMR,
NXT,
ETC,
DOGE,
ZEC,
BTS,
DGB,
XRP,
BTCD,
PPC,
CRAIG,
XBS,
XPY,
PRC,
YBC,
DANK,
GIVE,
KOBO,
DT,
CETI,
SUP,
XPD,
GEO,
CHASH,
SPR,
NXTI,
WOLF,
XDP,
AC,
ACOIN,
AERO,
ALF,
AGS,
AMC,
ALN,
APEX,
ARCH,
ARG,
ARI,
AUR,
AXR,
BCX,
BET,
BEAN,
BLU,
BLK,
BOST,
BQC,
XMY,
MOON,
ZET,
SXC,
QTL,
ENRG,
QRK,
RIC,
DGC,
LIMX,
BTB,
CAIX,
BTE,
BUK,
CACH,
CANN,
CAP,
CASH,
CAT,
CBX,
CCN,
CIN,
CINNI,
CXC,
CLAM,
CLOAK,
CLR,
CMC,
CNC,
CNL,
COMM,
COOL,
CRACK,
CRYPT,
CSC,
DEM,
DMD,
XVG,
DRKC,
DSB,
DVC,
EAC,
EFL,
ELC,
EMC2,
EMD,
EXCL,
EXE,
EZC,
FLAP,
FC2,
FFC,
FIBRE,
FRC,
FLT,
FRK,
FRAC,
FST,
FTC,
GDC,
GLC,
GLD,
GLX,
GLYPH,
GML,
GUE,
HAL,
HBN,
HUC,
HVC,
HYP,
ICB,
IFC,
IOC,
IXC,
JBS,
JKC,
JUDGE,
KDC,
KGC,
LK7,
LKY,
LSD,
LTB,
LTCD,
LTCX,
LXC,
LYC,
MAX,
MEC,
MED,
MIN,
MN,
MINC,
MRY,
MZC,
NAN,
NAUT,
NAV,
NBL,
NEC,
NET,
NMB,
NRB,
NOBL,
NRS,
NVC,
NMC,
NYAN,
OPAL,
ORB,
OSC,
PHS,
POINTS,
POT,
PSEUD,
PXC,
PYC,
RDD,
RIPO,
RPC,
RT2,
RYC,
RZR,
SAT2,
SBC,
SDC,
SFR,
SHADE,
SHLD,
SILK,
SLG,
SMC,
SOLE,
SPA,
SPT,
SRC,
SSV,
SUPER,
SWIFT,
SYNC,
SYS,
TAG,
TAK,
TES,
TGC,
TIT,
TOR,
TRC,
ULTC,
UNB,
UNO,
URO,
USDE,
UTC,
UTIL,
VDO,
VIA,
VOOT,
VRC,
VTC,
WC,
WDC,
XAI,
XBOT,
XC,
XCSH,
XCR,
XJO,
XLB,
XPM,
XST,
XXX,
YAC,
ZCC,
ZED,
BCN,
EKN,
XAU,
TMC,
XEM,
BURST,
NBT,
SJCX,
START,
HUGE,
XCP,
MAID,
NSR,
MONA,
CELL,
TEK,
BAY,
NTRN,
SLING,
XVC,
CRAVE,
BLOCK,
XSI,
BYC,
GRC,
GEMZ,
KTK,
HZ,
FAIR,
QORA,
NLG,
RBY,
PTC,
KORE,
WBB,
SSD,
XTC,
NOTE,
FLO,
MMXIV,
STV,
EBS,
AM,
XMG,
AMBER,
NKT,
J,
GHC,
ABY,
LDOGE,
MTR,
TRI,
SWARM,
BBR,
BTCRY,
BCR,
XPB,
XDQ,
FLDC,
SLR,
SMAC,
TRK,
U,
UIS,
CYP,
UFO,
ASN,
OC,
GSM,
FSC,
NXTTY,
QBK,
BLC,
MARYJ,
OMC,
GIG,
CC,
BITS,
LTBC,
NEOS,
HYPER,
VTR,
METAL,
PINK,
GRE,
XG,
CHILD,
MINE,
ROS,
UNAT,
SLM,
GAIA,
TRUST,
FCN,
XCN,
CURE,
GMC,
MMC,
XBC,
CYC,
OCTO,
MSC,
EGG,
C2,
GSX,
CAM,
RBR,
XQN,
ICASH,
NODE,
SOON,
BTMI,
EVENT,
VIOR,
XCO,
VMC,
MRS,
VIRAL,
EQM,
ISL,
QSLV,
XWT,
XNA,
RDN,
SKB,
BSTY,
FCS,
GAM,
NXS,
CESC,
TWLV,
EAGS,
MWC,
ADC,
MARS,
XMS,
SPHR,
SIGU,
DCC,
M1,
DB,
CTO,
EDGE,
FUTC,
GLOBE,
TAM,
MRP,
CREVA,
XFC,
NANAS,
LOG,
XCE,
ACP,
DRZ,
BSC,
DRKT,
CIRC,
NKA,
VERSA,
EPY,
SQL,
PIGGY,
CHA,
MIL,
CRW,
GEN,
XPH,
GRM,
QTZ,
ARB,
LTS,
SPC,
GP,
BITZ,
DUB,
GRAV,
MNV,
QCN,
HEDGE,
SONG,
XSEED,
CRE,
AXIOM,
SMLY,
RBT,
CHIP,
SPEC,
UNC,
SPRTS,
ZNY,
BTQ,
PKB,
SNRG,
GHOUL,
HNC,
DIGS,
EXP,
GCR,
MAPC,
MI,
CON,
TX,
GRS,
SC,
CLV,
LYB,
BST,
PXI,
CPC,
AMS,
OBITS,
CLUB,
RADS,
EMC,
EGC,
MND,
I0C,
BTA,
DCR,
NAS2,
PAK,
CRB,
DOGED,
REP,
OK,
RVR,
AMP,
HODL,
DGD,
EDRC,
LSK,
WAVES,
HTC,
GAME,
DSH,
DBIC,
XHI,
SPOTS,
BIOS,
CAB,
DIEM,
GBT,
RCX,
PWR,
TRUMP,
PRM,
BCY,
RBIES,
STEEM,
BLRY,
XWC,
DOT,
SCOT,
DNET,
BAC,
TCR,
POST,
INFX,
ETHS,
PXL,
NUM,
SOUL,
ION,
GROW,
UNITY,
OLDSF,
SSTC,
NETC,
GPU,
TAGR,
HMP,
ADZ,
GAP,
MYC,
IVZ,
VTA,
SLS,
SOIL,
CUBE,
YOC,
VPRC,
APC,
STEPS,
DBTC,
UNIT,
AEON,
MOIN,
SIB,
ERC,
AIB,
PRIME,
BERN,
BIGUP,
KR,
XRE,
MEME,
XDB,
ANTI,
BRK,
COLX,
MNM,
ADCN,
ZEIT,
CGA,
SWING,
SAFEX,
NEBU,
AEC,
FRN,
ADN,
PULSE,
N7,
CYG,
LGBTQ,
UTH,
MPRO,
KAT,
SPM,
MOJO,
BELA,
FLX,
BOLI,
CLUD,
DIME,
FLY,
HVCO,
GIZ,
GREXIT,
CARBON,
DEUR,
TUR,
LEMON,
STS,
DISK,
NEVA,
CYT,
FUZZ,
NKC,
SCRT,
XRA,
XNX,
STHR,
DBG,
BON,
WMC,
GOTX,
FLVR,
SHREK,
RISE,
REV,
PBC,
OBS,
EXIT,
CLINT,
CKC,
VIP,
NXE,
ZOOM,
DRACO,
YOVI,
ORLY,
KUBOS,
INCP,
SAK,
EVIL,
OMA,
MUE,
COX,
BNT,
BSD,
DES,
BIT16,
PDC,
CMTC,
CHESS,
SPACE,
REE,
LQD,
MARV,
XDE2,
VEC2,
OMNI,
GSY,
LIR,
MMNXT,
SCRPT,
LBC,
SPX,
CJ,
PUT,
KRAK,
DLISK,
IBANK,
STRAT,
VOYA,
ENTER,
WGC,
BM,
FRWC,
PSY,
XT,
RUST,
NZC,
SNGLS,
XAUR,
BFX,
UNIQ,
CRX,
DCT,
XPOKE,
MUDRA,
WARP,
CNMT,
PIZZA,
LC,
HEAT,
ICN,
EXB,
WINGS,
RBIT,
KMD,
GB,
NEO,
ANC,
SYNX,
MC,
JWL,
WAY,
TAB,
TRIG,
BITCNY,
BITUSD,
STO,
SNS,
CTC,
TOT,
BTD,
BOTS,
MDC,
FTP,
ZET2,
KRB,
TELL,
ENE,
TDFB,
BLOCKPAY,
BXT,
ZYD,
MST,
GOON,
VLT,
ZNE,
DCK,
COVAL,
DGDC,
TODAY,
VRM,
ROOT,
GPL,
DOPE,
FX,
PIO,
PROUD,
SMSR,
UBIQ,
ARM,
RING,
ERB,
LAZ,
FONZ,
BTCR,
SANDG,
PNK,
MOOND,
DLC,
SEN,
SCN,
WEX,
LTH,
BRONZ,
SH,
BUZZ,
MG,
PSI,
XPO,
NLC,
PSB,
XBTS,
FIT,
PINKX,
FIRE,
UNF,
SPORT,
PPY,
NTC,
EGO,
X2,
MT,
TIA,
GBRC,
XUP,
HALLO,
BBCC,
EMIGR,
BHC,
CRAFT,
INV,
OLYMP,
DPAY,
ATOM,
HKG,
ANTC,
JOBS,
DGORE,
THC,
TRA,
RMS,
FJC,
VAPOR,
SDP,
RRT,
XZC,
PRE,
CALC,
LEA,
CF,
CRNK,
CFC,
VTY,
ARDR,
BS,
JIF,
CRAB,
HILL,
MONETA,
EC,
RUBIT,
HCC,
BRAIN,
VTX,
KRC,
ROYAL,
LFC,
ZUR,
NUBIS,
TENNET,
PEC,
GMX,
GNJ,
TEAM,
SCT,
LANA,
ELE,
GCC,
AND,
EQUAL,
SWEET,
DKC,
COC,
CHOOF,
CSH,
ZCL,
RYCN,
PCS,
NBIT,
WINE,
DAR,
ARK,
IFLT,
ZECD,
ZXT,
WASH,
TESLA,
LUCKY,
VSL,
TPG,
LEO,
MDT,
CBD,
PEX,
INSANE,
GNT,
BASH,
FAME,
LIV,
SP,
MEGA,
VRS,
ALC,
DOGETH,
KLC,
HUSH,
BTLC,
DRM8,
FIST,
EBZ,
DRS,
FGZ,
BOSON,
ATX,
PNC,
BRDD,
TIME,
BIPC,
XNC,
EMB,
BTTF,
DLR,
CSMIC,
FIRST,
SCASH,
JIO,
IW,
JNS,
TRICK,
DCRE,
FRE,
NPC,
PLNC,
DGMS,
ICOB,
ARCO,
KURT,
XCRE,
ENT,
UR,
MTLM3,
ODNT,
EUC,
CCX,
BCF,
SEEDS,
XSN,
TKS,
BCCOIN,
SHORTY,
PCM,
KC,
CORAL,
BamitCoin,
NXC,
MONEY,
BSTAR,
HSP,
HZT,
CS,
XSP,
CCRB,
BULLS,
INCNT,
ICON,
NIC,
ACN,
XNG,
XCI,
LOOK,
LOC,
MMXVI,
TRST,
MIS,
WOP,
CQST,
IMPS,
IN,
CHIEF,
GOAT,
ANAL,
RC,
PND,
PX,
OPTION,
AV,
LTD,
UNITS,
HEEL,
GAKH,
GAIN,
SHIFT,
S8C,
LVG,
DRA,
ASAFE2,
LTCR,
QBC,
XPRO,
GIFT,
VIDZ,
INC,
PTA,
ACID,
ZLQ,
RADI,
RNC,
GOLOS,
PASC,
TWIST,
PAYP,
DETH,
YAY,
YES,
LENIN,
MRSA,
OS76,
BOSS,
MKR,
BIC,
CRPS,
MOTO,
NTCC,
HXX,
SPKTR,
MAC,
SEL,
NOO,
CHAO,
XGB,
YMC,
JOK,
GBIT,
TEC,
BOMB,
RIDE,
PIVX,
KED,
CNO,
WEALTH,
IOP,
XSPEC,
PEPECASH,
CLICK,
ELS,
KUSH,
ERY,
PLU,
PRES,
BTZ,
OPES,
WCT,
UBQ,
RATIO,
BAN,
NICE,
SMF,
CWXT,
TECH,
CIR,
LEPEN,
ROUND,
MAR,
MARX,
TAT,
HAZE,
PRX,
NRC,
PAC,
IMPCH,
ERR,
TIC,
NUKE,
EOC,
SFC,
JANE,
PARA,
MM,
CTL,
NDOGE,
ZBC,
MLN,
FRST,
PAY,
ORO,
ALEX,
TBCX,
MCAR,
THS,
ACES,
UAEC,
EA,
PIE,
CREA,
WISC,
BVC,
FIND,
MLITE,
STALIN,
TSE,
VLTC,
BIOB,
SWT,
PASL,
ZER,
CHAT,
CDN,
NETKO,
ZOI,
HONEY,
MXT,
MUSIC,
DTB,
VEG,
MBIT,
VOLT,
EDG,
BEST,
CHC,
ZENI,
PLANET,
DUCK,
BNX,
BSTK,
RNS,
DBIX,
AMIS,
KAYI,
XVP,
BOAT,
TAJ,
IMX,
CJC,
AMY,
QBT,
EB3,
XVE,
FAZZ,
APT,
BLAZR,
ARPA,
UNI,
ECO,
XLR,
DARK,
DON,
MER,
WGO,
RLC,
ATMOS,
ETT,
VISIO,
HPC,
GOT,
CXT,
EMPC,
GNO,
LGD,
TAAS,
BUCKS,
XBY,
GUP,
MCRN,
LUN,
RAIN,
WSX,
IEC,
IMS,
ARGUS,
CNT,
LMC,
TKN,
BTCS,
PROC,
XGR,
BENJI,
HMQ,
BCAP,
DUO,
RBX,
GRW,
APX,
MILO,
OLV,
ILC,
MRT,
IOU,
PZM,
PHR,
ANT,
PUPA,
RICE,
XCT,
DEA,
RED,
ZSE,
CTIC,
TAP,
BITOK,
PBT,
MUU,
INF8,
HTML5,
MNE,
DICE,
USC,
DUX,
XPS,
EQT,
INSN,
BAT,
F16,
HAMS,
QTUM,
NEF,
BOS,
QWARK,
IOT,
QRL,
ADL,
PTOY,
ZRC,
LKK,
ESP,
DYN,
SEQ,
MCAP,
MYST,
VERI,
SNM,
SKY,
CFI,
SNT,
AVT,
CVC,
IXT,
DENT,
ETHOS,
STA,
TFL,
EFYT,
EOS,
MCO,
NMR,
ADX,
QAU,
ECOB,
PLBT,
USDT,
NANO,
AHT,
ATB,
TIX,
CHAN,
CMP,
RVT,
HRB,
NIM,
CDT,
ACT,
DNT,
SUR,
PING,
MIV,
SAN,
KIN,
WGR,
XEL,
NVST,
FUN,
FUNC,
PQT,
WTT,
MTL,
HVN,
MYB,
PPT,
SNC,
STAR,
COR,
XRL,
OROC,
OAX,
MBI,
DDF,
DIM,
GGS,
DNA,
FYN,
FND,
DCY,
CFT,
DNR,
DP,
VUC,
BTPL,
UNIFY,
IPC,
BRIT,
AMMO,
SOCC,
MASS,
LA,
IML,
XUC,
STU,
PLR,
GUNS,
IFT,
PRO,
SYC,
IND,
TRIBE,
ZRX,
TNT,
COSS,
STORM,
NPX,
STORJ,
SCORE,
OMG,
OTX,
EQB,
VOISE,
ETBS,
CVCOIN,
DRP,
ARC,
BOG,
NDC,
POE,
ADT,
AE,
UET,
AGRS,
SAND,
DMT,
DAS,
ADST,
BCAT,
XCJ,
RKC,
NLC2,
LINDA,
KING,
ANCP,
RCC,
ROOTS,
SNK,
CABS,
OPT,
ZNT,
BITSD,
XLC,
SKIN,
MSP,
HIRE,
REAL,
DFBT,
EQ,
WLK,
VIB,
ONION,
BTX,
ICE,
XID,
GCN,
MANA,
ICOO,
TME,
SMART,
SIGT,
ONX,
COE,
ARENA,
WINK,
CRM,
DGPT,
MOBI,
CSNO,
KICK,
SDAO,
STX,
BNB,
CORE,
KEN,
QVT,
TIE,
AUT,
CTT,
GRWI,
MNY,
MTH,
CCC,
UMC,
BMXT,
GAS,
FIL,
OCL,
BNC,
TOM,
XAS,
SMNX,
DCN,
DLT,
MRV,
MBRS,
SUB,
MET,
NEBL,
PGL,
XMCC,
AUN,
CMPCO,
DTCT,
CTR,
WNET,
PRG,
THNX,
WORM,
FUCK,
VNT,
SIFT,
IGNIS,
IWT,
JDC,
ITT,
LNC,
AIX,
EVX,
XEC,
ENTRP,
ICOS,
PIX,
MEDI,
HGT,
LTA,
NIMFA,
SCOR,
MLS,
KEX,
COB,
BRO,
MINEX,
ATL,
DFT,
VET,
UTK,
LAT,
SOJ,
HDG,
STCN,
SQP,
RIYA,
LNK,
AMB,
MNTP,
ALTOCAR,
BLX,
BKX,
BOU,
OXY,
AMT,
GIM,
NYC,
LBTC,
FRAZ,
EMT,
GXC,
HBT,
KRONE,
SRT,
AVA,
BT,
ACC,
Z2,
LINX,
XCXT,
BLAS,
GOOD,
SCL,
TRV,
CRTM,
EON,
PST,
MTX,
PRIX,
CTX,
ENJ,
CNX,
DRC,
FUEL,
ACE,
WRC,
WTC,
BRX,
UCASH,
WRT,
ORME,
DEEP,
CCT,
WSH,
ABC,
PRP,
BMC,
PYN,
KAPU,
SENSE,
CAPP,
VEE,
FC,
RCN,
NRN,
EVC,
LINK,
WIZ,
ATKN,
KNC,
RUSTBITS,
REX,
ETHD,
SUMO,
TRX,
H2O,
TKT,
RHEA,
ART,
DRT,
SNOV,
DREAM,
MTN,
STOCKBET,
PLM,
SALT,
SND,
XP,
LRC,
HSR,
GLA,
ZNA,
EZM,
ODN,
POLL,
MTK,
CAS,
MAT,
GJC,
WIC,
WEB,
WAND,
ELIX,
EBTC,
HAC,
ADA,
YOYOW,
REC,
BIS,
OPP,
ROCK2,
EARTH,
ICX,
VSX,
FLASH,
GRFT,
BTCZ,
CZC,
PPP,
GUESS,
CAN,
ETP,
CIX,
ERT,
FLIK,
TRIP,
MBT,
ALIS,
LEV,
ARBI,
REQ,
ARN,
DAT,
VIBE,
ROK,
XRED,
DAY,
AST,
FLP,
HXT,
CND,
NTM,
TZC,
ENG,
MCI,
COV,
WAX,
AIR,
NTO,
ATCC,
KOLION,
WILD,
ELTC2,
ILCT,
POWR,
C20,
RYZ,
ELM,
TER,
XCS,
BQ,
CAV,
CLOUT,
WABI,
EVR,
TOA,
MNZ,
VIVO,
PHX,
MDA,
ZSC,
AURS,
CAG,
PKT,
ECHT,
INXT,
ATS,
RGC,
EBET,
R,
MOD,
CPAY,
RUP,
APPC,
WHL,
UP,
ETG,
WOMEN,
MAY,
RNDR,
EDDIE,
NAMO,
KCS,
GAT,
BLUE,
FLLW,
WYR,
VZT,
INDI,
LUX,
BAR,
PIRL,
ECASH,
WPR,
DRGN,
ODMC,
BRAT,
DTR,
TKR,
KEY,
ELITE,
XIOS,
DOV,
ETN,
REA,
AVE,
XNN,
BTDX,
ZAB,
BT1,
BT2,
JCR,
XSB,
ATM,
EBST,
KEK,
AID,
ALTCOM,
OST,
DATA,
UGC,
DTC,
PLAY,
PURE,
CLD,
OTN,
POS,
REBL,
NEOG,
EXN,
INS,
TRCT,
UKG,
BTCRED,
CPEX,
JTX,
AXT,
NEU,
RUPX,
BDR,
XIN,
DUTCH,
TIO,
PURA,
INN,
HST,
BCPT,
BDL,
CMS,
XBL,
ZEPH,
ATFS,
GES,
NULS,
LCASH,
CFD,
SPHTX,
PLC,
SRN,
WSC,
DBET,
XGOX,
NEWB,
LIFE,
RMC,
CREDO,
MSR,
CJT,
EVN,
BNK,
ELLA,
BPL,
COIN,
DRXNE,
SKR,
GRID,
XPTX,
GVT,
ETK,
ASTRO,
GMT,
SOAR,
EXY,
ISH,
MNX,
CRDS,
VIU,
DBR,
GFT,
STAC,
QSP,
RIPT,
BBT,
GBX,
CSTL,
ICC,
JNT,
QASH,
ALQO,
TRIA,
PBL,
MAG,
STEX,
UFR,
LOCI,
TAU,
LAB,
DEB,
FLIXX,
FRD,
PFR,
ECA,
LDM,
LTG,
STP,
SPANK,
WISH,
AERM,
PLX,
ETHB,
CDX,
FOOD,
DEC,
VOT,
UQC,
LEND,
SETH,
ABYSS,
XSH,
GEA,
DSR,
BDG,
ONG,
BTCM,
ETBT,
ZCG,
MUT,
MEOW,
DIVX,
CNBC,
RHOC,
XUN,
RFL,
COFI,
ELTCOIN,
GRX,
NTK,
ERO,
CMT,
RLX,
MAN,
CWV,
NRO,
SEND,
GLT,
X8X,
COAL,
DAXX,
BWK,
FNTB,
XMRG,
BTCE,
FYP,
BOXY,
NGC,
UTNP,
EGAS,
DPP,
ADB,
TGT,
XDCE,
BMT,
BIO,
MTRC,
BTCL,
PCN,
PYP,
CRED,
SBTC,
KLKS,
AC3,
GTO,
TNB,
HKN,
B2B,
LTHN,
GER,
LTCU,
MGO,
BTCA,
HQX,
ETF,
STAK,
BCOIN,
CCOS,
BNTY,
BRD,
HAT,
ELF,
VLR,
CWX,
DBC,
ZP,
POP,
PNX,
BAS,
UTT,
HBC,
AMM,
DAV,
XCPO,
GET,
ERC20,
ITC,
HTML,
GENE,
NMS,
PHO,
XTRA,
NTWK,
SUCR,
GNX,
NAS,
ACCO,
BYTHER,
REM,
TOK,
EREAL,
CPN,
XFT,
QLC,
BTSE,
OMGC,
Q2C,
BLT,
SPF,
TDS,
ORE,
SPK,
GOA,
FLS,
WAGE,
GUN,
DFS,
POLIS,
WELL,
FLOT,
CL,
SHND,
AUA,
DNN,
SAGA,
GXS,
TSL,
IRL,
BOT,
PMA,
TROLL,
FOR,
SGR,
JET,
MDS,
LCP,
GTC,
IETH,
SDRN,
INK,
KBR,
HPB,
MONK,
JINN,
MGN,
KZC,
GNR,
LWF,
BRC,
WCG,
HIVE,
LCK,
MFG,
ETL,
TEL,
ONL,
ZAP,
AIDOC,
ECC,
ET4,
LCT,
EBC,
VST,
INT,
CPY,
STN,
SFU,
PCOIN,
LUC,
EDT,
CYDER,
SRNT,
MLT,
EKO,
UBTC,
BTO,
DOC,
ARCT,
IMVR,
AURA,
IDH,
CBT,
ITZ,
XBP,
EXRN,
AGI,
BFT,
LGO,
CRPT,
SGL,
TNC,
FSBT,
CFTY,
DTA,
CV,
DTX,
MCU,
OCN,
THETA,
PRPS,
DUBI,
BPT,
SGN,
IOST,
TCT,
TRAC,
MOT,
ZIL,
HORSE,
QUN,
SWFTC,
SENT,
IPL,
OPC,
SAF,
SHA,
PYLNT,
GRLC,
EVE,
YEE,
REPUX,
JOYT,
XCD,
BTW,
AXPR,
FOTA,
DDD,
SPEND,
NPXS,
ZPT,
CROAT,
REF,
SXDT,
SXUT,
LDC,
VAL,
BCDN,
STK,
MZX,
SPICE,
Q1S,
XTO,
RUFF,
ELA,
CXO,
WT,
HGS,
SISA,
EBIT,
RCT,
CUZ,
HLC,
BETR,
GMR,
ING,
LHC,
BLZ,
CHSB,
EQUI,
MCT,
HHEM,
CWIS,
MBC,
GRO,
SWM,
WOBTC,
DNO,
eFIC,
TKY,
BANCA,
TRTL,
BIX,
ABT,
HBZ,
DRPU,
DOR,
PRFT,
PARETO,
DTRC,
IQB,
BEE,
MUN,
TIG,
LYK,
NYX,
DXT,
SAT,
CRL,
ORI,
USX,
LGR,
BCA,
B2X,
EXMR,
FSN,
UETL,
NBR,
ARY,
RAVE,
ILT,
SCOOBY,
CEFS,
BUN,
BSR,
SKULL,
TRDT,
XBTY,
JC,
BTCP,
SKC,
MWAT,
JEW,
KRM,
HT,
CDY,
SSS,
CRDNC,
BIFI,
BTF,
SHOW,
STC,
AIT,
STQ,
ALT,
TRF,
KB3,
FDX,
KREDS,
EQL,
GAI,
VULC,
DADI,
UNRC,
BBP,
NOX,
HYS,
LCWP,
NAVI,
ADI,
TEN,
VVI,
ANK,
IVC,
HLP,
VIN,
SHPING,
PTR,
LCC,
VANY,
TFD,
NBX,
BAX,
BERRY,
FLIP,
CLIN,
DHT,
ENK,
ALX,
REN,
DTH,
SOC,
TDX,
LOT,
FUNK,
LEAF,
COMP,
BITCAR,
CLN,
NIHL,
BASHC,
DIGIF,
DGM,
CBS,
TERN,
SVD,
PROOF,
BTCH,
redBUX,
AUC,
LIZ,
CIF,
NCASH,
SPD,
CMCT,
FILL,
POA,
RVN,
XNK,
XYO,
RFR,
PROPS,
CEDEX,
FUND,
CEL,
PUSHI,
BINS,
POKER,
AXYS,
BOLD,
EXTN,
DIG,
ETS,
LIPC,
HELL,
ELP,
ACAT,
RKT,
ELI,
CO2,
INVOX,
VLX,
ACTN,
LTCH,
ZUP,
HMT,
ONT,
USCOIN,
KIND,
BCT,
CLO,
CRU,
MOAT,
BBI,
BEZ,
ENTRC,
BTCGO,
XTROPTIONS,
KNW,
PGC,
BIT,
DATX,
PKC,
SQOIN,
TBAR,
CPL,
TUBE,
AUTO,
OMX,
TRCK,
SNX,
TOMO,
CHI,
W3C,
DIN,
INSTAR,
CHP,
PSD,
J8T,
LELE,
DROP,
AKA,
SHIP,
IHT,
LCS,
LALA,
LEDU,
FOXT,
ETKN,
ROX,
ADM,
AMBT,
MEE,
BTRM,
MANNA,
PROD,
ePRX,
HMC,
ZIX,
ELEC,
ORGT,
LOOM,
PAN,
BOTC,
GO,
VIEW,
OKOIN,
ADK,
GRAM,
ESS,
VIT,
SERA,
AET,
CMOS,
PGN,
BMH,
TT,
REDN,
TLP,
BSX,
BBN,
TDZ,
PAVO,
TUSD,
LDN,
BUBO,
USOAMIC,
FLUZ,
IPSX,
MIO,
AIC,
MITH,
FNO,
PAS,
XSG,
CVTC,
PLMT,
FARM,
NEXT,
RNTB,
XCLR,
SWTH,
FDZ,
VTN,
LION,
MASP,
XTL,
UCN,
HUR,
BRIA,
IC,
LATX,
ROI,
ETHPR,
MNB,
BTL,
GOAL,
RAC,
BEX,
HOLD,
EZT,
SOL,
VIC,
XCM,
NFN,
CEEK,
WIIX,
EOSDAC,
BCI,
MEDIC,
BBC,
KWH,
CTXC,
VLD,
FTX,
GSI,
BDP,
FLM,
ALPS,
ZEL,
BKC,
BITG,
DEV,
CHT,
GEX,
ABJ,
FTW,
RAP,
ARTE,
ANI,
PHC,
ETHM,
UBC,
SENC,
PAT,
LIGER,
CHFN,
EURN,
LEU,
SWC,
SEM,
DARX,
BBK,
NCT,
UWC,
UUU,
XHV,
CPX,
DOCK,
EQC,
ADH,
ZLA,
LIF,
EFX,
LND,
FTO,
HPAY,
SIG,
CARE,
NZL,
TBT,
XMC,
OAK,
DML,
GEM,
TIPS,
MOS,
TBX,
PNT,
WIN,
CHARM,
PROTON,
CRS,
DERO,
DEAL,
JUMP,
ZCO,
KRL,
NEXO,
CHX,
SS,
IFX,
XMO,
EDU,
PCL,
MITX,
APH,
NBAI,
CVT,
TUT,
BETT,
NOAH,
PAL,
ENU,
BFDT,
KEP,
RUBY,
CTKN,
YUM,
GSC,
DESI,
FNP,
VLUX,
MTC,
SSH,
XBI,
TRUE,
MRK,
FRV,
WINS,
XES,
RTB,
FXT,
HYDRO,
DXC,
CHBR,
OWD,
ELLI,
AXS,
DAN,
UBT,
AMO,
LBA,
LIVE,
GBG,
CNN,
SHL,
ETZ,
SKM,
SHR,
UBEX,
IVY,
KEC,
ODE,
HOT,
AMN,
SABR,
HWC,
BITGOLD,
BITSILVER,
GIN,
OPEN,
NLX,
FACE,
MRPH,
IOTX,
STM,
ITL,
AITT,
ITM,
VID,
UCT,
SNTR,
ZMR,
XMV,
NKN,
ELY,
HER,
PAR,
SLX,
LTCC,
RST,
XBB,
AMX,
TFC,
REPO,
IRC,
OIO,
ANGL,
ANTS,
KNG,
CMM,
STT,
WYS,
COG,
ZIPT,
QKC,
OSA,
EXC,
BEN,
BCIO,
BMK,
ROC,
BZNT,
LYL,
FT,
BMX,
PHI,
PMNT,
BNTN,
HYT,
GRMD,
SSC,
LOKI,
BKT,
NCP,
MPT,
STAX,
MRN,
FOPA,
CBC,
OOT,
NBC,
SIC,
ALG,
PAI,
EXCC,
REL,
BTCN,
HERO,
SEELE,
EJAC,
APIS,
UPP,
XT3,
MGD,
PLURA,
SWACH,
NWCN,
ICST,
PURK,
ROE,
LTCP,
DKD,
LYNX,
POSQ,
YCE,
OCC,
STOR,
ARO,
BWS,
BTCC,
GOLF,
MUSE,
OCT,
XCEL,
ECH,
XMN,
PLUS1,
COI,
CANDY,
SHARD,
GMCN,
TRVC,
KRX,
BITX,
HFT,
DTEM,
TIP,
SOUND,
HB,
TRW,
IQN,
GIC,
BGL,
EPIK,
ZMN,
PNY,
SAFE,
COU,
BID,
ATH,
ABS,
VITAE,
XET,
TDP,
XGS,
XUEZ,
BIM,
Dow,
HEX,
EMN,
PYT,
DEI,
TPC,
OYS,
JEX,
ILK,
RYO,
MUSD,
MIC,
URALS,
QWC,
WAB,
BTN,
ARE,
DAC,
EUNO,
KAAS,
MMO,
MVP,
DASC,
EGT,
PGT,
MEDX,
CET,
SLST,
TGAME,
ZINC,
KETAN,
KBC,
MFT,
INSUR,
NIX,
ZCN,
FIN,
RPM,
DGX,
ITA,
NOM,
XSTC,
U42,
EGCC,
FREC,
AOA,
LET,
MEET,
BOE,
RTE,
CAR,
CPT,
PCO,
XPST,
HSC,
MCV,
SCRL,
CONI,
XPAT,
MBLC,
DIW,
JOINT,
IDXM,
CCO,
ATMI,
TKA,
RMT,
OLT,
GETX,
IQ,
BWT,
LST,
EMV,
ESZ,
TRAK,
ZXC,
BTRN,
XMX,
VME,
VITE,
RNT,
BBO,
YUP,
SNIP,
XDNA,
SAL,
CARD,
LIKE,
THRT,
SKRP,
AVH,
SCC,
HALO,
BSTN,
PITCH,
NANJ,
PAXEX,
DIT,
AZART,
CENNZ,
RDC,
TTU,
FREE,
AOP,
XAP,
INTO,
AIMS,
TSC,
SPLB,
CMZ,
NOBS,
HMN,
MHP,
HMD,
JSE,
IMGZ,
NYN,
IAM,
URB,
CHART,
WHEN,
SFT,
ITR,
CHE,
ZEEW,
QUA,
RSC,
ENTRY,
PHTC,
WORK,
ORC,
ZAZA,
IDAP,
HEAL,
OFCR,
SHPT,
LED,
PRLPAY,
RBDT,
SKYFT,
FLEX,
STRY,
FAN,
GBTC,
NBOX,
BUD,
DBCCOIN,
K2G,
ARR,
GMB,
SPOT,
VTUUR,
Pakka,
ETI,
FRECN,
NOIA,
LAX,
LPC,
DYNO,
MFX,
SPIKE,
SGO,
RAWG,
BDB,
MNR,
ZNAQ,
YBT,
OPET,
PSK,
KVT,
COT,
WPT,
ABELE,
XEP,
OMI,
BILL,
ST,
WBBC,
XDT,
WPP,
SLT,
APL,
MCB,
HDAC,
CCCX,
VRH,
AEN,
SOLID,
VANIG,
AIRE,
GMA,
WMB,
MVU,
TLNT,
GLDR,
IMU,
TRT,
OLM,
CST,
YON,
URT,
QCX,
CRON,
DIP,
REDC,
TTV,
OICOIN,
ENQ,
EXPR,
DTN,
IDM,
SIDT,
ISR,
CDPT,
CRGO,
AXIS,
QRP,
TIIM,
BNR,
VRT,
ZCC1,
KRP,
DAG,
OLE,
OKB,
AMLT,
HGO,
TCOIN,
BZ,
PRA,
VLP,
ZIP,
KCASH,
ZT,
BOUTS,
EST,
MODEX,
OGT,
PLA,
NPER,
ATON,
EURS,
XCG,
PCH,
ECOM,
WIT,
OPU,
MOF,
BOX,
COTI,
ETALON,
TICS,
ZPR,
AAC,
ESTATE,
BLV,
RRC,
MPG,
QNTU,
IG,
FML,
TLU,
PSM,
MON,
KAN,
NMH,
KST,
DEL,
HIT,
PBLK,
MDN,
TMTG,
SGC,
PRT,
COSM,
GPPT,
LNL,
VRN,
NEX,
BRNX,
SRCOIN,
RFT,
ET,
MMTM,
XGH,
FXP,
PASS,
HRO,
DGTX,
BSCH,
TRVR,
PESA,
CLPX,
GLN,
AUK,
PCCM,
TOPC,
PLAN,
EVER,
TRAID,
TRIO,
BNTE,
DPY,
FUNDZ,
MIB,
BAAS,
LYNK,
CCL,
HYC,
TCX,
HLD,
DACC,
NUSD,
TCHB,
DAX,
BEC,
VEEN,
CIC,
MIODIO,
MOV,
IHF,
CNAB,
SGP,
HANA,
BTV,
URP,
SHE,
IVN,
ZAT,
IMT,
MHC,
ROBET,
CRYP,
BDT,
BTXC,
DAPS,
ETE,
NHCT,
SWA,
USDCT,
IAG,
STRS,
MTCMN,
AAA,
ZEST,
MOAC,
HLM,
CSP,
USDC,
ONGAS,
NRVE,
BIP,
XCASH,
RMESH,
HAND,
GBXT,
AT,
BASIS,
JIB,
PMTN,
SGA,
PHM,
CUSD,
QUANT,
KUSD,
VEOT,
GGR,
VEST,
MCN,
TCH,
DEPO,
ONE,
TVA,
METM,
PAX,
ARAW,
BRAZ,
TALAO,
IZX,
DIVI,
HQT,
W12,
NBAR,
HC,
KBX,
MYDFS,
VTHO,
BHPC,
VTOS,
M2O,
SLY,
UEC,
BEAT,
MOLK,
MSD,
SEED,
SEAL,
GBO,
ACM,
DFXT,
BF,
NWP,
BCDT,
EVOS,
DEEX,
ANON,
LTZ,
MTZ,
TBL,
BXY,
KUE,
ESN,
H3O,
BETHER,
ETHO,
WTL,
HIH,
ANGEL,
P2PS,
GXT,
AIM,
TWISTR,
CXA,
BITTO,
HNY,
QEY,
UMK,
VNX,
WMK,
OJX,
CHW,
ABBC,
CATT,
VEX,
LQDN,
BIOC,
FOREX,
CPLO,
XPX,
RIPAX,
HETA,
NOW,
ADAB,
CIX100,
MINX,
MOBU,
NVDX,
COVEX,
TAL,
ATT,
F2K,
GTX,
B21,
LK,
QOBI,
BVO,
VENA,
CDRX,
CRF,
ELES,
GEON,
TZO,
WLME,
INVX,
AWT,
ABX,
LNKC,
BFC,
IMPCN,
XPT,
NMK,
OUT,
LPT,
RAINC ,
IOV,
MYO,
ORET,
SEC,
QUIZ,
CYRS,
UTL,
JOYS,
DACH,
MNVM,
PLTX,
BTMG,
BRIK,
XTN,
LUMA,
BTZN,
CLRTY,
CGT,
NAVIB,
ATHK,
ATP,
PLEO,
GDX,
EGDC,
ENTT,
RWD,
AURUM,
WRL,
CRWD,
ENCN,
TAURI,
EYE,
GTR,
OPEX,
SKYM,
SCIA,
TXP,
GPS,
WTXH,
BBG,
NZE,
EQY,
FLC,
SHKG,
TENZ,
TWC,
WUG,
CAND,
CTW,
CRV,
XIM,
NAM,
UFT,
BZKY,
CARAT,
ZILLA,
TCJ,
MAP,
DN8,
XNT,
PPOVR,
LX,
AWAX,
VAR,
TKD,
VTAG,
WBY,
BBOS,
BFEX,
HUS,
MENU,
APXT,
IDORU,
WOM,
BONA,
HLDY,
COS,
BLACK,
HORUS,
MEETONE,
IOTW,
EMPR,
MPAY,
AGM,
MTCN,
PTO,
AS,
OSF,
DPT,
GTN,
VIDI,
SUQA,
OPQ,
ZYM,
RPB,
DYNCOIN,
MIT,
VANM,
PSF,
LITION,
NEW,
TITAN,
MZG,
VIAZ,
BTZC,
ECR,
RF,
ARMS,
STIPS,
MPXT,
XELS,
PGF7T,
IDAC ,
ZUUM,
UCOINT,
YDY,
FTUM,
SPON,
DLXV,
OCEAN,
TECO,
GOALS,
ETHIX,
CDP,
TTB,
CHK,
PRPL,
OASC,
TREE,
GDL,
LNT,
FTRC,
HBX,
LAO,
GOVT,
TBRS,
COGEN,
DAILY,
SREUR,
MAZC,
TGTC,
NRG,
PLNX,
IPT,
IGTT,
SRXIO,
GZB,
FNX,
GGP,
IFUM,
ATC,
DOOH,
IOUX,
BQTX,
NVOY,
CYBR,
LLG,
LCR,
SNPC,
VTM,
NRX,
BTSG,
BXM,
CINX,
CCIN,
CCI,
RDS,
GMS,
SGAT,
SILKT,
BITM,
TCHN,
ICHN,
LVX,
AENT,
MBN,
LYFE,
REMCO,
SaTT,
GEMA,
SCH,
VTEX,
SRV,
DSLA,
SYLO,
YMZ,
AER,
AIBB,
META,
ASQT,
AXC,
BLKD,
CYS,
ATTR,
CTY,
BC,
DDL,
EZX,
COY,
FNL,
B2G,
CSQ,
HBE,
HV,
ICT,
TOS,
CPROP,
MOOLYA,
PON,
CREV,
VAD,
IDC,
LBR,
EMX,
XBASE,
LEN,
KUBO,
FABA,
LQ8,
GC,
INFLR,
LIB,
XPR,
PETL,
XDMC,
PPS,
SMILO,
BCV,
TREX,
VNS,
VRF,
AUX,
LYQD,
CBP,
SMOKE,
EDN,
AVALA,
NOS,
DT1,
FTT,
STACS,
JMC,
FOAM,
FRED,
CNCT,
ENGT,
VRTY,
TEAMT,
ZND,
FPC,
SYNCO,
SPY,
HIDU,
USE,
NGIN,
KOTO,
SUSD,
GENX,
HPSP,
VTL,
SECI,
SPRTZ,
C25,
MVL,
STASH,
HERB,
AQUA,
XQR,
URX,
FTM,
HASH,
KSYS,
MTEL,
MTT,
MITC,
BBTC,
UMO,
LIT,
MUST,
ELT,
TIOX,
XNB,
XRN,
RBTC,
BXC,
PIRATE,
EXO,
ONAM,
BIH,
KARMA,
CJR,
BLTG,
AGVC,
ASGC,
MIMI,
PXG,
ORM,
TRET,
SET,
BEER,
AERGO,
TIMI,
NRP,
SNTVT,
CEN,
GARD,
UNX,
OWC,
WOWX,
THO,
TOSS,
KMX,
SKI,
SG,
SUNEX,
VIDY,
XRBT,
ALUX,
XBOND,
BOSE,
GRIN,
JOY,
WETH,
GBE,
HRBE,
BEAM,
MILC,
PINMO,
RGT,
BMG,
OXY2,
FAIRC,
BPN,
DYC,
DUSK,
LN,
FTR,
RWE,
YSH,
TASH,
TXM,
TRAVEL,
ACA,
AUPC,
COSX,
DNTX,
HART,
KSS,
LIPS,
MIBO,
BRIX,
NZO,
PTT,
XRK,
RMOB,
XRF,
POD,
SUT,
WHO,
ID,
WDX,
AIOT,
AMOS,
XBANK,
OX,
KRO,
CAID,
LTE,
HLX,
MEL,
NEXXO,
QNTR,
BTCUS,
RAYS,
MOL,
RENC,
TLT,
EMOT,
USAT,
VOL,
AIRT,
VTRD,
BTT,
GALI,
PLAI,
BGG,
HEDG,
WBTC,
ERE,
BTU,
APS,
XBX,
QNT,
FFUEL,
NSP,
PTNX,
SNcoin,
TTN,
BWT2,
OATH,
SBA,
DXG,
EXTP,
ZEX,
XCZ,
CBUK,
HIX,
TGN,
COGS,
XRM,
CCOIN,
ICHX,
FORCE,
BTMX,
LTO,
QUSD,
BTH,
PLG,
PVP,
EMANATE,
CP,
DAYTA,
ORV,
CWT,
AQU,
CXG,
CHFT,
VNTY,
MAI,
BTR,
SSX,
KLK,
LVN,
AZU,
ARQ,
WU,
ZUC,
FFM,
DRF,
GTIB,
CR,
VEO,
DLA,
AFO,
FET,
DAGT,
GVE,
IDT,
KUV,
ARCX,
YACHTCO,
BOLTT,
ENCX,
VALID,
TYM,
VENUS,
HYGH,
NODIS,
MNC,
USDS,
HVE,
XR,
VALOR,
ALP,
EMU,
GST,
ARS,
NRM,
APOD,
AX,
CWEX,
CLDX,
LABX,
GGC,
AGT,
ENV,
ANKR,
GEP,
IZA,
GBA,
ITU,
FANZ,
CSPN,
CCH,
HAVEN,
XOV,
eQUAD,
CUR,
CREDIT,
ERA,
MAKE,
KIBIS,
SPKZ,
OGO,
AWC,
DIS,
SCRIBE,
INX,
SQR,
PHT,
CRO,
LYTX,
TJA,
InBit,
DIO,
LIC,
SCA,
XOS,
VSYS,
LAC,
QCP,
UGT,
BWL,
WATT,
XRX,
TFF,
ANY,
ELOC,
IZZY,
SONT,
SWI,
LUNES,
EDEXA,
PPI,
ANTE,
TRXDICE,
AFTT,
TRXWIN,
TWJ,
IGG,
DARB,
MBTX,
CFun,
ECTE,
BUY,
LWA,
INR,
REDi,
AAS,
PCC,
IPUX,
BWN,
MIG,
T4M,
ZEON,
WHY,
SLC,
VOLLAR,
URIS,
MBTC,
HRD,
SHER,
QCO,
ZB,
ISG,
GEC,
TAGZ,
SKP,
MCC,
CELR,
XGN,
YPTO,
UBE,
XLM,
VRA,
ETGP,
GFCS,
IX,
RDT,
ALIC,
HCXP,
AGRO,
TFUEL,
BYTS,
GRT,
MYTV,
EUCX,
DRG,
DXN,
AML,
B66,
LEVL,
DHC,
UGAS,
PNP,
EDO,
ORS,
FCT,
PRY,
MXM,
TITC,
TTC,
BCNX,
SWG,
HTER,
EVED,
GSE,
BZRX,
GIF,
YBK,
STG,
DEVX,
TMB,
HBRS,
XPL,
MTSH,
DAGO,
EMI,
TEMPO,
PPR,
REW,
ORBIS,
ORBS,
STE,
TPLAY,
GYM,
VIDT,
UDOO,
FAT,
TAN,
KICKS,
LYM,
SPORTG,
CRES,
NOKU,
BINC,
RIF,
PERU,
FIII,
FIH,
GNC,
WHN,
VC,
SRX,
GUAR,
AFCT,
JVY,
VLTX,
LYN,
HXC,
BB1,
eSwitch,
PARQ,
ALCE,
ADUX,
IMP,
BCNA,
AZ,
APZ,
WVR,
FFCT,
TELE,
REME,
RAIZER,
BTMK,
AES,
AIBK,
XDN,
NCC,
AION,
WAN,
POLY,
XTZ,
DAI,
STONE,
OILD,
VLM,
BSV,
BCH,
BCD,
ZEN,
LOL,
AUDC,
PART,
TTT,
PRL,
EDUC,
EDC,
RFOX,
CTLX,
CSM,
BTNY,
MINT,
GBYTE,
GUSD,
NOIZ,
GX,
TOKC,
BLITZ,
XEN,
ACH,
FORK,
VIG,
BTG,
     ])

    db.session.commit()
