'''
Script to use the search software to simply run the search
'''

import os
import pickle
from util.gen_charging_net import GenerateChargingNetwork

def main():

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', help='in file path', required=True)
    args = parser.parse_args()

    stateName = os.path.split(args.infile)[-1].replace('-latest.osm', '')
    s = GenerateChargingNetwork(args.infile, stateName, mp=1)
    
    print(s.data)
    
    goodNodes = s.genChargingNetwork()

    # write goodNodes to a pickle file

    out = list(zip(s.gridCoordCenters.values(), goodNodes))
    print(out)
    outpath = os.path.join(os.path.split(args.infile)[0], f'{stateName}-out.pkl')
    with open(outpath, 'wb') as f:
        pickle.dump(out, f, pickle.HIGHEST_PROTOCOL)
    
if __name__ == '__main__':
    main()
