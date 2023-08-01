import tifffile
import argparse
import os.path

def open_tif_with_properties(path):
    try:
        with tifffile.TiffFile(path) as tif:
            properties_full = {}
            for tag in tif.pages[0].tags.values():
                name, value = tag.name, tag.value
                properties_full[name] = value
        try:
            magnification = properties_full['OlympusSIS']['magnification']
            pixelsize = properties_full['OlympusSIS']['pixelsizex']
            properties = {'magnification': magnification, 'pixelsize': pixelsize, 'path': path}
        except:
            print("WARNING:: could not extract main properties.")
            properties = {}
        return properties, properties_full
    except: 
        print("ERROR::Could not read properties of file. Make sure the file is in .tif format.")

if __name__ == "__main__":

    print("******************************")
    print("Reading tif properties")
    print("******************************")

    # Args Parser
    parser = argparse.ArgumentParser(description='Read Header')
    
    #Training Parameters
    parser.add_argument('--path', type = str, default="", help='path to .tif')

    
    args = parser.parse_args()
    if(not os.path.isfile(args.path)): 
        print("ERROR::Could not find the file specified.")
    else: 
        properties, properties_full = open_tif_with_properties(args.path)

        print("MAIN PROPERTIES: ")
        [print(p,properties[p]) for p in properties.keys()]
        print()
        print("ALL PROPERTIES: ")
        [print(p,properties_full[p]) for p in properties_full.keys()]
        print()


