import pickle
import org.opensim.utils as utils
import os

model = getCurrentModel()
s = model.getWorkingState()
c = model.getCoordinateSet()
coords = []
for i in range(model.getNumCoordinates()):
    coords.append(c.get(i).getValue(s))

file_name = "lol.lol"
if not os.path.exists(file_name):
    file_name = utils.FileUtils.getInstance().browseForFilenameToSave(".pose", "Save Pose", 1, "default.pose")

f = open(file_name, "wb")
pickle.dump(coords, f)
f.close()
