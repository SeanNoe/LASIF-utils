# Run this script from lasif root directory, so the lasif project
import pyasdf
import glob
import tqdm
import os
import toml
# Make folder
dir_name = "./coordinate_info"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
all_events = glob.glob("LASIF_PROJECT/DATA/EARTHQUAKES/*.h5")
# loop over all events and dump info to a file
for event in tqdm.tqdm(all_events):
    event_name = ".".join(event.split("/")[-1].split(".")[0:-1])
    with pyasdf.ASDFDataSet(event) as ds:
        src_lat = ds.events[0].origins[0].latitude
        src_lon = ds.events[0].origins[0].longitude
        src_depth = ds.events[0].origins[0].depth
        src_info = {"src_lat": src_lat, "src_lon": src_lon,
                    "src_depth": src_depth,
                    "receiver_coords": ds.get_all_coordinates()}
        with open(os.path.join(dir_name, event_name + ".toml"), "w") as fh:
            toml.dump(src_info, fh)
