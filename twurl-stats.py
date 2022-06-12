import json
import subprocess

parks = [
    ("acad",	"https://twitter.com/AcadiaNPS",),
    ("npsa",	"https://twitter.com/NPamericansamoa",),
    ("arch",	"https://twitter.com/ArchesNPS",),
    ("badl",	"https://twitter.com/BadlandsNPS",),
    ("bibe",	"https://twitter.com/BigBendNPS",),
    ("bisc",	"https://twitter.com/BiscayneNPS",),
    ("blca",	"https://twitter.com/BlackCanyonNPS",),
    ("brca",	"https://twitter.com/BryceCanyonNPS",),
    ("cany",	"https://twitter.com/CanyonlandsNPS",),
    ("care",	"https://twitter.com/CapitolReefNPS",),
    ("cave",	"https://twitter.com/CavernsNPS",),
    ("chis",	"https://twitter.com/CHISNPS",),
    ("cong",	"https://twitter.com/CongareeNPS",),
    ("crla",	"https://twitter.com/CraterLakeNPS",),
    ("cuva",	"https://twitter.com/CVNPNPS",),
    ("deva",	"https://twitter.com/DeathValleyNPS",),
    ("dena",	"https://twitter.com/DenaliNPS",),
    ("drto",	"https://twitter.com/DryTortugasNPS",),
    ("ever",	"https://twitter.com/EvergladesNPS",),
    ("gaar",	"https://twitter.com/GatesArcticNPS",),
    ("jeff",	"https://twitter.com/GatewayArchNPS",),
    ("glac",	"https://twitter.com/GlacierNPS",),
    ("glba",	"https://twitter.com/GlacierBayNPS",),
    ("grca",	"https://twitter.com/GrandCanyonNPS",),
    ("grte",	"https://twitter.com/GrandTetonNPS",),
    ("grba",	"https://twitter.com/GreatBasinNPS",),
    ("grsa",	"https://twitter.com/GreatDunesNPS",),
    ("grsm",	"https://twitter.com/GreatSmokyNPS",),
    ("gumo",	"https://twitter.com/GuadalupeMtnsNP",),
    ("hale",	"https://twitter.com/HaleakalaNPS",),
    ("havo",	"https://twitter.com/Volcanoes_NPS",),
    ("hosp",	"",),
    ("indu",	"https://twitter.com/IndianaDunesNPS",),
    ("isro",	"",),
    ("jotr",	"https://twitter.com/JoshuaTreeNPS",),
    ("katm",	"https://twitter.com/KatmaiNPS",),
    ("kefj",	"https://twitter.com/KenaiFjordsNPS",),
    ("seki",	"https://twitter.com/SequoiaKingsNPS",),
    ("kova",	"",),
    ("lacl",	"https://twitter.com/LakeClarkNPS",),
    ("lavo",	"https://twitter.com/LassenNPS",),
    ("maca",	"https://twitter.com/MammothCaveNP",),
    ("meve",	"",),
    ("mora",	"https://twitter.com/MountRainierNPS",),
    ("neri",	"https://twitter.com/NewRiverNPS",),
    ("noca",	"https://twitter.com/NCascadesNPS",),
    ("olym",	"https://twitter.com/OlympicNP",),
    ("pefo",	"https://twitter.com/PetrifiedNPS",),
    ("pinn",	"https://twitter.com/PinnaclesNPS",),
    ("redw",	"https://twitter.com/RedwoodNPS",),
    ("romo",	"https://twitter.com/rockynps",),
    ("sagu",	"https://twitter.com/SaguaroNPS",),
    ("seki",	"https://twitter.com/SequoiaKingsNPS",),
    ("shen",	"https://twitter.com/ShenandoahNPS",),
    ("thro",	"https://twitter.com/TRooseveltNPS",),
    ("viis",	"",),
    ("voya",	"https://twitter.com/VoyageursNPS",),
    ("whsa",	"https://twitter.com/WhiteSandNps",),
    ("wica",	"https://twitter.com/WindCaveNPS",),
    ("wrst",	"https://twitter.com/WrangellStENPS",),
    ("yell",	"https://twitter.com/YellowstoneNPS",),
    ("yose",	"https://twitter.com/YosemiteNPS",),
    ("zion",	"https://twitter.com/ZionNPS",),
]

if __name__ == "__main__":
    for park_code, tw_url in parks:
        if tw_url == "":
            print("")
            continue 

        twitter_username = tw_url.split('/')[-1]
        proc_result = subprocess.run(
            [
                'twurl',
                '-j',
                f'/2/users/by/username/{twitter_username}?user.fields=public_metrics,verified',
            ], 
            capture_output=True,
        )
        stdout = json.loads(proc_result.stdout.decode())
        metrics = stdout.get("data", {}).get("public_metrics", {})
        verified = stdout.get("data", {}).get("verified", "")
        print(f'{park_code},{metrics.get("followers_count")},{metrics.get("tweet_count")},{verified}')



# {                                  
#   "data": {                        
#     "id": "44984641",              
#     "public_metrics": {            
#       "followers_count": 37957,    
#       "following_count": 299,      
#       "tweet_count": 2971,         
#       "listed_count": 788          
#     },                             
#     "name": "SaguaroNationalPark", 
#     "username": "SaguaroNPS"       
#   }                                
# }