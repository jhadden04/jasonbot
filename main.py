import praw
import time

reddit = praw.Reddit(client_id='2WHqLvf5aRq3tQ',
                     client_secret='J1WHeJffj_QlK5pvom_qKPJUYsVA4Q',
                     user_agent='a reddit instance',
                     username='FranchescaScola',
                     password='mnkjoi09M)')


def subspam():
    misctext = """John here, original owner of thcdelivery, https://www.realthcdelivery.com/
messaging you all of you to let you know that the
REAL THC DELIVERY Will be doing a Friday Flash Sale :

SITE WIDE 50% OFF SALE

Use Coupon Code :
RealTHCD
At Checkout"""

    subname = 'CanadianMOMs+canadients'  # obviously you can add more subreddits to this
    usedusernames = ['ruglescdn', 'Bone-Juice', 'canuck883', 'AI-Pharma', 'klinklonfoonyak', 'rottenpupil', 'math4829', 'ohwell2hell', 'the3b', 'Renegade_Punk', 'PrincePatty', 'VegetableOk4039', 'dontcallmeray', 'SkidRowTrash', 'TheStonedCelestial', 'Superficial_Charm', 'zcewaunt', 'byebyeblackmarket', 'cherbo123', 'Rifter0876', 'digitalunperson', 'BrownTown456', 'berocksteady', 'dontThrowAwayDabs', 'Hobbes710', 'alt717', 'montegue144', 'Sudosu2020', 'bacondamagecontroll', 'Not_Me25', 'xXxBEAVISxXx', 'cmcshane95', 'xhowlinx', 'ElPayt', 'radbradman12', 'Kruder420', 'bombrah', 'FindYourVapeDOTcom', 'TurbulentHovercraft0', 'coop3r187', 'NightlyOwl9999', 'eternalboom3r', 'SpiffyLynn', 'Spocks-Nephew', 'dildosandwhiches', 'west_coast_ghost', 'HQV701E', 'Yeahnahyeahnahyeah1', 'GaiasGardenMedicinal', 'misterbaboon1', 'xqou', 'dope_smoker_pro', 'Cops_on_Drops', 'LeGeantVert', 'SonicBacon', 'Drkushmaster', 'omgwtdbbq420lol', 'punctualjohn', 'cannadatrees', 'Imryannoimryan', 'InfinitelyCheeched', 'atarikid', 'LOOP2112', 'treedibles', 'FatHomerSimpson', 'GreggoireLeOeuf', 'Wescuddles', 'tunaliker', 'IamDonaldJTrumpAMA', 'Turndownforwhot', 'HHVN', 'bgc2420', 'Toastysweedaccount', '26AWi', 'Catmandingo', 'Undergrowth709', 'CannaKwn', 'lukeCRASH', 'Parking-Ad-1088', 'RonanBuh', 'CraftFlowers', 'wutangfather36', 'blueleaves-greensky', '777asap', 'AimOrDie', 'initialdjp', 'casualt11', 'xenochrist420', 'ElysiumCraft1', 'WeedRichards', 'arrow399', 'bassdrop30', 'redditjged', 'haloguysm1th', 'MD74', 'periodicsheep', 'ceman_yeumis', 'mcchubby', 'sudo-nymph', 'sympleton', 'phaze_d', 'Arctiumsp', 'MasaharuMorimoto', 'TheNickelGuy', 'Len_Zefflin', 'FluSH31', 'Jaktumurmu1', 'publicbigguns', 'Third_Eye78', 'longshortwsb', 'MOMThrowawaywhynot', 'actrix', 'watermelon-4-lyf', 'WTFCannabis', 'converter-bot', 'cezariobirbiglio', 'BarracudaDouble7760', 'SoupOrSandwich', 'Abby_Sciuto', 'mrking604', 'W33DMEN5000', 'benjotdeluxe', 'Swisstimelate', 'RockIslander2018', 'MartyV78', 'Drizznit1221', '7eastgenetics', 'lovelikecyanide', 'prairiefarmer', 'Devank90', 'moregoo', 'BlazeStarGaze', 'blue_solid', 'crazy4ski', 'Rat-Tricks', 'CalyxPro', 'BrilliantRat', 'residentialninja', 'PaJeppy', 'EnclG4me', 'Takenotes420', 'pakkflipper420', 'Bert666Six', 'mistern8d', 'v-dubb', 'brodok2000', 'Rara-Randy', 'Highskylife', 'Rabbi_Mohamed', 'bubbleguys', 'Traditional_Safe7480', 'Under_the_Milky_Way', 'sensismoke420', 'oldbastage', 'puttinthe-oo-incool', 'GrabbaDelta9', 'PoopGalaxyLord', 'FourthLvlSpicyMeme', 'DougFromWpg', 'Gr84Skin', 'Seaeend', 'kushyushy', 'Ifoughttheguardrail', 'Mysterious-Coyote-40', 'BulimicPlatypus', 'DeepCultureCast', 'thenoblenacho', 'Rarefindofthemind', 'purplezamboni', 'Bewitcherr', 'Lostinbinary', 'Martin_Di_Stasio', 'Billy_Ray_Valentine', 'trichomeking94', 'EastcoastvaporCDN', 'ThaCza', 'TheGuvnur', 'jjofort79', 'kiefblaster', 'Topdime1', 'GarySanduchi', 'Northernlighter', 'apercu_consulting', 'FractalParadigm', 'ExtraGloria', 'Cannannannnnada', 'twentypastfour11', 'kgbdemon90', 'marfewj1313', 'PicklesBC', 'ClearSkyPraisin', 'pilapodapostache', 'olafsoncole95', 'Secretbud121', 'kellanist', 'scify420', 'prawndavid', 'HipsterSamuraiJack', 'ityaboycannapenis', 'Dabs2Review', 'tet5uo', 'jfl_cmmnts', 'cannabisblogger420', 'coonytunes', 'IncognitoBudz', 'NiklasChronwall', 'jerkface900', 'Buss_Conductah', 'LtSoundwave', 'tommytw0time', 'bringme5', 'iamdperfectone', 'HighRandomthoughts', 'keepaway430', 'GCPMAN', 'thegoodrichard', 'gunzanrozes', 'SuperSoper3', 'El_le_va_te', 'Snoo21193', 'Select_Relation_7848', 'Danktator', 'Delphic10', 'nevertoomany', 'MarcusXL']
    while True:
        for comment in reddit.subreddit(subname).stream.comments():
            name = comment.author.name
            title = f'Dear, {name}'
            nametxt = f'{name}\n'
            if name in usedusernames:
                continue
            b = open("names.txt", "r")
            if nametxt in b:
                continue
            try:
                text = misctext
                reddit.redditor(name).message(title, text)
            except:
                continue
            usedusernames.append(name)
            f = open("names.txt", "a")
            f.write(nametxt)
            print(f'u/{name} r/{comment.subreddit.display_name}')
            print(usedusernames)
            time.sleep(40)
            break


subspam()
