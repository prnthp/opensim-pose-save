import pickle
import org.opensim.utils as utils
import os

model = getCurrentModel()
s = model.getWorkingState()
c = model.getCoordinateSet()


file_name = utils.FileUtils.getInstance().browseForFilename(".pose", "Load Pose", 1)

f = open(file_name, "r")
coords = pickle.load(f)
f.close()


for i in range(len(coords)):
    c.get(i).setValue(s, coords[i])

updateDisplay()
