from prescription_data import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia"]

# Remove Warfarin and add Edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    if warfarin in prescription:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    else:
        print(f"Patient {patient} is not taking Warfaring."
              f" Please remove {patient} from the trial")
    print(patient, prescription)