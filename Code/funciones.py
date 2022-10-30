import pandas as pd
import numpy as np
from numpy import nan
import re

def limpiar_act(x):
    
    x = x.lower()
    
    if 'surf' in x:
        return 'Surfing'
    elif 'boarding' in x:
        return 'Surfing'
    elif 'paddle' in x:
        return 'Surfing'
    elif 'windsurf' in x:
        return 'Surfing'
    elif 'body' in x:
        return 'Surfing'
    elif 'paddle' in x:
        return 'Surfing'
    elif 'boogie' in x:
        return 'Surfing'
    elif 'skim' in x:
        return 'Surfing'
    
    elif 'swim' in x:
        return 'Swimming'
    elif 'wading' in x:
        return 'Swimming'
    elif 'float' in x:
        return 'Swimming'
    elif 'treading water' in x:
        return 'Swimming'
    elif 'bath' in x:
        return 'Swimming'
    elif 'lying' in x:
        return 'Swimming'
    elif 'swam' in x:
        return 'Swimming'
    elif 'skiff' in x:
        return 'Swimming'
    elif 'water' in x:
        return 'Swimming'
    elif 'search' in x:
        return 'Swimming'
    elif 'sea' in x:
        return 'Swimming'
    elif 'shallows' in x:
        return 'Swimming'
    elif 'rest' in x:
        return 'Swimming'
    elif 'net' in x:
        return 'Swimming'
    elif 'sit' in x:
        return 'Swimming'
    elif 'waist' in x:
        return 'Swimming'
    elif 'knee-deep' in x:
        return 'Swimming'
    elif 'free' in x:
        return 'Swimming'
    elif 'sit' in x:
        return 'Swimming'
    
    elif 'fishing' in x:
        return 'Fishing'
    elif 'aquarium' in x:
        return 'Fishing'
    elif 'hunt' in x:
        return 'Fishing'
    elif 'trap' in x:
        return 'Fishing'
    elif 'pull' in x:
        return 'Fishing'
    elif 'pick' in x:
        return 'Fishing'
    elif 'fish' in x:
        return 'Fishing'
    elif 'pulling' in x:
        return 'Fishing'
    elif 'cleaning' in x:
        return 'Fishing'
    elif 'spear' in x:
        return 'Fishing'
    elif 'crayfish' in x:
        return 'Fishing'
    elif 'lobster' in x:
        return 'Fishing'
    elif 'hunt' in x:
        return 'Fishing'
    elif 'catch' in x:
        return 'Fishing'
    
    elif 'walk' in x:
        return 'Walking'
    elif 'shell' in x:
        return 'Walking'
    elif 'stand' in x:
        return 'Walking'
    elif 'see' in x:
        return 'Walking'
    elif 'diving' in x:
        return 'Diving'
    elif 'snorkel' in x:
        return 'Diving'
    elif 'clean' in x:
        return 'Diving'
    elif 'dive' in x:
        return 'Diving'
    elif 'underwater' in x:
        return 'Diving'
    elif 'photo' in x:
        return 'Photographing'
    
    elif 'film' in x:
        return 'Filming'
    
    elif 'wash' in x:
        return 'Washing'
    elif 'help' in x:
        return 'Helping'
    elif 'air' in x:
        return 'Flying'
    elif 'crashed' in x:
        return 'Flying'
    elif 'plane' in x:
        return 'Flying'
    
    elif 'vehicle' in x:
        return 'Driving'
    
    elif 'play' in x:
        return 'Playing'
    elif 'skiing' in x:
        return 'Playing'
    elif 'kayak' in x:
        return 'Playing'
    elif 'rowing' in x:
        return 'Playing'
    elif 'cage' in x:
        return 'Playing'
    elif 'scuba' in x:
        return 'Playing'
    elif 'snorkeling' in x:
        return 'Playing'
    
    
    elif 'shark' in x:
        return 'Fighting'
    elif 'feeding' in x:
        return 'Fighting'
    elif 'hand' in x:
        return 'Fighting'
    elif 'touch' in x:
        return 'Fighting'
    elif 'bitt' in x:
        return 'Fighting'
    
    elif 'sail' in x:
        return 'Sailing'
    elif 'ship' in x:
        return 'Sailing'
    elif 'boat' in x:
        return 'Sailing'
    elif 'aboard' in x:
        return 'Sailing'
    elif 'sink' in x:
        return 'Sailing'
    elif 'cruise' in x:
        return 'Sailing'
    elif 'tanker' in x:
        return 'Sailing'
    elif 'overboard' in x:
        return 'Sailing'
    elif 'marine' in x:
        return 'Sailing'
    elif 'raft' in x:
        return 'Sailing'
    elif 'storm' in x:
        return 'Sailing'
    elif 'launch' in x:
        return 'Sailing'
    elif 'ski' in x:
        return 'Sailing'
    elif 'wreck' in x:
        return 'Sailing'
    elif 'zodiac' in x:
        return 'Sailing'
    elif 'capsized' in x:
        return 'Sailing'
    elif 'ton' in x:
        return 'Sailing'
    elif 'sink' in x:
        return 'Sailing'
    elif 'dinghy' in x:
        return 'Sailing'
    elif 'canoe' in x:
        return 'Sailing'
    elif 'yacht' in x:
        return 'Sailing'
    elif 'crew' in x:
        return 'Sailing'
    elif 'submarine' in x:
        return 'Sailing'
    elif 'adrift' in x:
        return 'Sailing'
    elif 'sank' in x:
        return 'Sailing'
    elif 'ferry' in x:
        return 'Sailing'
    elif 'sunk' in x:
        return 'Sailing'
    elif 'founde' in x:
        return 'Sailing'
    elif 'freighter' in x:
        return 'Sailing'
    elif 'into' in x:
        return 'Sailing'
    elif 'fell' in x:
        return 'Sailing'
    
    elif 'unknown' in x:
        return 'Unknown'
    
    else:
        return 'Other'

def limpiar_spe(x):
    
    x = x.lower()
    
    if 'ree' in x:
        return 'Reef Shark'
    elif 'whit' in x:
        return 'White Shark'
    elif 'wobbegon' in x:
        return 'Wobbegong Shark'
    elif 'tawne' in x:
        return 'Tawney Shark'
    elif 'blackti' in x:
        return 'Blacktip Shark'
    elif 'bul' in x:
        return 'Bull Shark'
    elif 'tige' in x:
        return 'Tiger Shark'
    elif 'bronz' in x:
        return 'Bronze Whale'
    elif 'mak' in x:
        return 'Mako Shark'
    elif 'blue poin' in x:
        return 'Mako Shark'
    elif 'blu' in x:
        return 'Blue Shark'
    elif 'gre' in x:
        return 'Grey Nurse Shark'
    elif 'hammerhea' in x:
        return 'Hammerhead Shark'
    elif 'nurs' in x:
        return 'Nurse Shark'
    elif 'blac' in x:
        return 'Blacktip Shark'
    elif 'sandba' in x:
        return 'Sandbar Shark'
    elif 'silver' in x:
        return 'Silvertip Shark'
    elif 'graffe' in x:
        return 'Graffed Shark'
    elif 'soupfi' in x:
        return 'Soupfin Shark'
    elif 'lemo' in x:
        return 'Lemon Shark'
    elif 'spinne' in x:
        return 'Spinner Shark'
    elif 'sand' in x:
        return 'Sand Shark'
    elif 'leopar' in x:
        return 'Leopard Shark'
    elif 'unknow' in x:
        return 'Unknown'
    elif 'not confir' in x:
        return 'Unknown'
    elif 'invali' in x:
        return 'Unknown'
    else:
        return 'Other'

def limpiar_nom(x):
    
    x = x.lower()
    
    if 'female' in x:
        return 'Unknown'
    elif 'male' in x:
        return 'Unknown'
    elif 'boy' in x:
        return 'Unknown'
    elif 'boat' in x:
        return 'Unknown'
    elif 'child' in x:
        return 'Unknown'
    elif 'anonymous' in x:
        return 'Unknown'
    elif 'sailor' in x:
        return 'Unknown'
    elif 'unidentified' in x:
        return 'Unknown'
    elif 'fisherm' in x:
        return 'Unknown'
    elif 'girl' in x:
        return 'Unknown'
    elif 'diver' in x:
        return 'Unknown'
    elif 'soldier' in x:
        return 'Unknown'
    elif 'native' in x:
        return 'Unknown'
    elif 'dinghy' in x:
        return 'Unknown'
    elif 'native' in x:
        return 'Unknown'
    elif 'woman' in x or 'women' in x:
        return 'Unknown'
    else:
        x = x.title()
        return x

def limpiar_bc(x):
    
    if re.findall('(?i)B\.(?i)C', x):
        return x[:11]
    else:
        return x
    
def limpiar_case(x):
    y = re.findall('\d+.\d+.\d+', x)
    
    if y == []: 
        return x
    else:
        y = y[0].split('.')
        j = '-'.join(y)
        return j