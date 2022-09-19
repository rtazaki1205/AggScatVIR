

def get_sizelist(agg,amon=None):
    """
    Get a list of available ``size`` arguments, which is necessary to call the ``dustmodel`` class.
    
    Examples:
        >>> print(get_nlist('FA19','100nm'))
        ['8', '16', '32', '64', '128', '256', '512', '1024', '2048', '4096']

        >>> print(get_nlist('CAHP','400nm'))
        ['8', '16', '32', '64']

        >>> print(get_nlist('grs'))
        ['0_2000', '0_2520', '0_3175', '0_4000', '0_5040', '0_6350', '0_8000', '1_0079', '1_2699', '1_6000']
    """
    
    #
    # safety checks
    #
    if agg in ['CALP','CAMP','CAHP']:
        amon_list=['100nm','200nm','400nm']
    elif agg in ['FA11','FA13','FA15','FA19']:
        amon_list=['100nm','150nm','200nm','300nm','400nm']
    elif agg=='grs':
        amon=None
    else:
        print('error in get_sizelist: incorrect partype type')
        print(' inputted value     = ',agg)
        print(" while available values are= 'FA11', 'FA13', 'FA15', 'FA19', 'CAHP', 'CAMP', 'CALP', 'grs'")
        exit()

    # check amon
    if amon is not None and amon not in amon_list:
        print('error in get_sizelist: incorrect monomer radius')
        print(' inputted value     = ',amon)
        print(' while available values are= ',amon_list)
        exit()

    #
    #
    nlist=[]
    if(agg=='FA11'):
        if(amon=='100nm'):
            nlist=['8','16','32','64','128','256']
        elif(amon=='150nm'):
            nlist=['8','16','32','64']
        elif(amon=='200nm'):
            nlist=['8','16','32','64']
        elif(amon=='300nm'):
            nlist=['8','16','32']
        elif(amon=='400nm'):
            nlist=['8','16']
    elif(agg=='FA13'):
        if(amon=='100nm'):
            nlist=['8','16','32','64','128','256','512']
        elif(amon=='150nm'):
            nlist=['8','16','32','64','128']
        elif(amon=='200nm'):
            nlist=['8','16','32','64','128']
        elif(amon=='300nm'):
            nlist=['8','16','32','64']
        elif(amon=='400nm'):
            nlist=['8','16','32']

    elif(agg=='FA15'):
        if(amon=='100nm'):
            nlist=['8','16','32','64','128','256','512','1024']
        elif(amon=='150nm'):
            nlist=['8','16','32','64','128','256']
        elif(amon=='200nm'):
            nlist=['8','16','32','64','128','256']
        elif(amon=='300nm'):
            nlist=['8','16','32','64','128']
        elif(amon=='400nm'):
            nlist=['8','16','32','64']

    elif(agg=='FA19'):
        if(amon=='100nm'):
            nlist=['8','16','32','64','128','256','512','1024','2048','4096']
        elif(amon=='150nm'):
            nlist=['8','16','32','64','128','256','512']
        elif(amon=='200nm'):
            nlist=['8','16','32','64','128','256','512']
        elif(amon=='300nm'):
            nlist=['8','16','32','64','128','256']
        elif(amon=='400nm'):
            nlist=['8','16','32','64','128']

    elif(agg=='CAHP' or agg=='CAMP' or agg=='CALP'):
        if(amon=='100nm'):
            nlist=['8','16','32','64','128','256','512','1024','2048','4096']
        elif(amon=='200nm'):
            nlist=['8','16','32','64','128','256','512']
        elif(amon=='400nm'):
            nlist=['8','16','32','64']

    elif(agg=='grs'):
        nlist=['0_2000','0_2520','0_3175','0_4000','0_5040','0_6350','0_8000','1_0079','1_2699','1_6000']

    return nlist


# 
def get_radius_and_porosity(partype,amon,np):
    """
    Get the characteristic radius and porosity of an aggregate.
    
    Examples:
        >>> ac,por=get_radius_and_porosity('FA19','100nm','4096')
        >>> print('%-21s'%"characteristic radius",'= %5.3f um'%ac)
        >>> print('%-21s'%"porosity",'= %5.2f %%'%por)
        characteristic radius = 10.04 um
        porosity              = 99.60 %

        >>> ac,por=get_radius_and_porosity('CAHP','400nm','64')
        >>> print('%-21s'%"characteristic radius",'= %5.3f um'%ac)
        >>> print('%-21s'%"porosity",'= %5.2f %%'%por)
        characteristic radius =  3.12 um
        porosity              = 86.47 %
    """

    #
    # safety checks
    #
    # check partype
    partype_list=['CALP','CAMP','CAHP','FA19','FA15','FA13','FA11']
    if partype not in partype_list:
        print('error in get_radius_and_poroty: incorrect partype type')
        print(' inputted value     = ',partype)
        print(' while available values are= ',partype_list)
        exit()

    # check amon
    amon_list=['100nm','150nm','200nm','300nm','400nm']
    if amon not in amon_list:
        print('error in get_radius_and_poroty: incorrect monomer radius')
        print(' inputted value     = ',amon)
        print(' while available values are= ',amon_list)
        exit()

    # check np
    np_list=get_sizelist(partype,amon=amon)
    if np not in np_list:
        print('error in get_radius_and_poroty: incorrect number of monomers.')
        print('        inputted value     = ',np)
        print('        while available values are= ',np_list)
        exit()

    #
    # first store aggregate radius (normalized to amon=100 nm)
    #
    if partype=='FA11':
        if np=='8':
            rc=0.51170114E+01
            po=94.03
        elif np=='16':
            rc=0.98256942E+01
            po=98.31
        elif np=='32':
            rc=0.18565017E+02
            po=99.50
        elif np=='64':
            rc=0.34922949E+02
            po=99.85
        elif np=='128':
            rc=0.65612469E+02
            po=99.95
        elif np=='256':
            rc=0.12322839E+03
            po=99.99

    elif partype=='FA13':

        if np=='8':
            rc=0.44973857E+01
            po=91.21
        elif np=='16':
            rc=0.78695278E+01
            po=96.72
        elif np=='32':
            rc=0.13530396E+02
            po=98.71
        elif np=='64':
            rc=0.23129327E+02
            po=99.48
        elif np=='128':
            rc=0.39461053E+02
            po=99.79
        elif np=='256':
            rc=0.67279401E+02
            po=99.92
        elif np=='512':
            rc=0.11468214E+03
            po=99.97

    elif partype=='FA15':

        if np=='8':
            rc=0.39191880E+01
            po=86.71
        elif np=='16':
            rc=0.64216775E+01
            po=93.96
        elif np=='32':
            rc=0.10317279E+02
            po=97.09
        elif np=='64':
            rc=0.16454757E+02
            po=98.56
        elif np=='128':
            rc=0.26168845E+02
            po=99.29
        elif np=='256':
            rc=0.41570925E+02
            po=99.64
        elif np=='512':
            rc=0.66008933E+02
            po=99.82
        elif np=='1024':
            rc=0.10479467E+03
            po=99.91

    elif partype=='FA19':

        if np=='8':
            rc=0.35921630E+01
            po=82.74
        elif np=='16':
            rc=0.55369074E+01
            po=90.57
        elif np=='32':
            rc=0.76808037E+01
            po=92.94
        elif np=='64':
            rc=0.10549461E+02
            po=94.55
        elif np=='128':
            rc=0.15686970E+02
            po=96.68
        elif np=='256':
            rc=0.21807930E+02
            po=97.53
        elif np=='512':
            rc=0.32392439E+02
            po=98.49
        elif np=='1024':
            rc=0.49487722E+02
            po=99.16
        elif np=='2048':
            rc=0.67223888E+02
            po=99.33
        elif np=='4096':
            rc=0.10043553E+03
            po=99.60

    elif partype=='CAHP':

        if np=='8':
            rc=0.32514276E+01
            po=76.73
        elif np=='16':
            rc=0.44484377E+01
            po=81.82
        elif np=='32':
            rc=0.59977666E+01
            po=85.17
        elif np=='64':
            rc=0.77906738E+01
            po=86.47
        elif np=='128':
            rc=0.98686230E+01
            po=86.68
        elif np=='256':
            rc=0.12394360E+02
            po=86.55
        elif np=='512':
            rc=0.15560679E+02
            po=86.41
        elif np=='1024':
            rc=0.19615370E+02
            po=86.43
        elif np=='2048':
            rc=0.24804457E+02
            po=86.58
        elif np=='4096':
            rc=0.31440169E+02
            po=86.82
    
    elif partype=='CAMP':

        if np=='8':
            rc=0.25707121E+01
            po=52.91
        elif np=='16':
            rc=0.34233881E+01
            po=60.12
        elif np=='32':
            rc=0.46841991E+01
            po=68.87
        elif np=='64':
            rc=0.61717829E+01
            po=72.78
        elif np=='128':
            rc=0.79544462E+01
            po=74.57
        elif np=='256':
            rc=0.10207683E+02
            po=75.93
        elif np=='512':
            rc=0.12913911E+02
            po=76.23
        elif np=='1024':
            rc=0.16479447E+02
            po=77.12
        elif np=='2048':
            rc=0.20918822E+02
            po=77.63
        elif np=='4096':
            rc=0.26428819E+02
            po=77.81
    
    elif partype=='CALP':
        if np=='8':
            rc=0.22291601E+01
            po=27.78
        elif np=='16':
            rc=0.29659565E+01
            po=38.68
        elif np=='32':
            rc=0.39164124E+01
            po=46.73
        elif np=='64':
            rc=0.52142878E+01
            po=54.86
        elif np=='128':
            rc=0.67492996E+01
            po=58.37
        elif np=='256':
            rc=0.87215615E+01
            po=61.41
        elif np=='512':
            rc=0.11219171E+02
            po=63.74
        elif np=='1024':
            rc=0.14317935E+02
            po=65.11
        elif np=='2048':
            rc=0.18286614E+02
            po=66.51
        elif np=='4096':
            rc=0.23404664E+02
            po=68.05


    # convert str --> int
    a0=int(amon[0:3])/100
    
    # 0.1 is to convert [nm] --> [um]
    rc = rc * a0 * 0.1

    return rc,po

if __name__ == '__main__':

    print(get_sizelist('FA11','300nm'))
    print(get_sizelist('grs'))

    ac,por=get_radius_and_porosity('FA19','100nm','4096')
    print('%-21s'%"characteristic radius",'= %5.2f um'%ac)
    print('%-21s'%"porosity",'= %5.2f %%'%por)
   
    ac,por=get_radius_and_porosity('CAHP','400nm','64')
    print('%-21s'%"characteristic radius",'= %5.2f um'%ac)
    print('%-21s'%"porosity",'= %5.2f %%'%por)
