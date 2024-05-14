#Source: https://stackoverflow.com/questions/62538951/nameerror-name-jam-is-not-defined
# Initialize variables
cnt_row = -1
cnt_col = 0
cnt_zero = 0

# Grab all relevant MIDI data (available in MIDI_dat)
for i in range(0, len(jam['annotations'])):
    if jam['annotations'][int(i)]['namespace'] == 'note_midi':
        for j in range(0, len(sorted(jam['annotations'][int(i)]['data']))):
            cnt_row = cnt_row + 1
            for k in range(0, len(sorted(jam['annotations'][int(i)]['data'])[int(j)]) - 1):
                if cnt_zero == 0:
                    MIDI_arr = np.zeros((len(sorted(jam['annotations'][int(i)]['data'])), len(sorted(jam['annotations'][int(i)]['data'])[int(j)]) - 1), dtype = np.float32)
                    cnt_zero = cnt_zero + 1
                if cnt_zero > 0:
                    MIDI_arr = np.vstack((MIDI_arr, np.zeros((len(sorted(jam['annotations'][int(i)]['data'])), len(sorted(jam['annotations'][int(i)]['data'])[int(j)]) - 1), dtype = np.float32)))
                    cnt_zero = cnt_zero + 1  # Keep
                if cnt_col > 2:
                    cnt_col = 0
                MIDI_arr[cnt_row, cnt_col] = sorted(jam['annotations'][int(i)]['data'])[int(j)][int(k)]
                cnt_col = cnt_col + 1
MIDI_dat = np.zeros((cnt_row + 1, cnt_col), dtype = np.float32)
cnt_col2 = 0
for n in range(0, cnt_row + 1):
    for m in range(0, cnt_col):
        if cnt_col2 > 2:
            cnt_col2 = 0
        MIDI_dat[n, cnt_col2] = MIDI_arr[n, cnt_col2]
        cnt_col2 = cnt_col2 + 1
        
 # Return the unique MIDI notes played (available in MIDI_val)
MIDI_dat_dur = np.copy(MIDI_dat)
for r in range(0, len(MIDI_dat[:, 0])):
    MIDI_dat_dur[r, 0] = MIDI_dat[r, 0] + MIDI_dat[r, 1]
tab_1, = np.where(np.logical_and(MIDI_dat[:, 0] >= start, MIDI_dat[:, 0] <= stop))
tab_2, = np.where(np.logical_and(MIDI_dat_dur[:, 0] >= start, MIDI_dat_dur[:, 0] <= stop))
tab_3, = np.where(np.logical_and(np.logical_and(MIDI_dat[:, 0] < start, MIDI_dat_dur[:, 0] > stop), MIDI_dat[:, 1] > int(stop-start)))
if tab_1.size != 0 and tab_2.size == 0 and tab_3.size == 0:
    tab_ind = tab_1
if tab_1.size == 0 and tab_2.size != 0 and tab_3.size == 0:
    tab_ind = tab_2
if tab_1.size == 0 and tab_2.size == 0 and tab_3.size != 0:
        tab_ind = tab_3
if tab_1.size != 0 and tab_2.size != 0 and tab_3.size == 0:
    tab_ind = np.concatenate([tab_1, tab_2])
if tab_1.size != 0 and tab_2.size == 0 and tab_3.size != 0:
    tab_ind = np.concatenate([tab_1, tab_3])
if tab_1.size == 0 and tab_2.size != 0 and tab_3.size != 0:
    tab_ind = np.concatenate([tab_2, tab_3])
if tab_1.size != 0 and tab_2.size != 0 and tab_3.size != 0:
    tab_ind = np.concatenate([tab_1, tab_2, tab_3])
if tab_1.size == 0 and tab_2.size == 0 and tab_3.size == 0:
    tab_ind = []
if len(tab_ind) != 0:
    MIDI_val = np.zeros((len(tab_ind), 1), dtype = np.float32)
    for z in range(0, len(tab_ind)):
        MIDI_val[z, 0] = int(round(MIDI_dat[tab_ind[z], 2]))
elif len(tab_ind) == 0:
    MIDI_val = []
MIDI_val = np.unique(MIDI_val)
if MIDI_val.size >= 6:
    MIDI_val = np.delete(MIDI_val, np.s_[6::])