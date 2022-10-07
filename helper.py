# Countries Where Military Coups Have Occurred
def CountriesWhereMilitaryCoupsHaveOccured(cam_list):
    countries_coups = cam_list.country.value_counts().reset_index()
    countries_coups.rename(columns={'index':'Country', 'country':'How Many Times Have Coups Occurred'}, inplace=True)
    return countries_coups

# region
def Region(cam_list):
    regi = cam_list.region.value_counts().reset_index()
    regi.rename(columns={'index':'Region', 'region':'How Many Countries Fall in this Region'}, inplace=True)
    return regi

# SuccessfulCoups
def SuccessfulCoups(cam_list):
    sc = cam_list.successful.value_counts().reset_index()
    sc.rename(columns={'index':'Successful_Coups', 'successful':'Total Number of Successful Coups'}, inplace=True)
    return sc

# combat
def Combat(cam_list):
    co = cam_list.combat.value_counts().reset_index()
    co.rename(columns={'index':'combat', 'combat':'Whether combat happened during Coups'}, inplace=True)
    return co

# country per combat
def CountryCombat(cam_list):
    cc = cam_list.groupby('country')['combat'].size().reset_index()
    return cc

# SuccessfulCountry
def SuccessfulCountry(cam_list):
    ycs = cam_list.groupby(['year', 'country'])['successful'].size().reset_index()
    return ycs

# RegionPerCoup
def RegionPerCoup(cam_list):
    rc = cam_list.groupby(['region','country'])['coup'].size().reset_index()
    return rc