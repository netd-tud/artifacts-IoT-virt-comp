# import micropython

SCALE_FACTOR = 1

LOCAL_SCALE_FACTOR = 3330

Bitlist = []

active_KINDERSICHERUNG_CTRL_IDX = 10
active_KINDERSICHERUNG_CTRL_copy_IDX = 11
active_KINDERSICHERUNG_CTRL_old_IDX = 12
active_FH_TUERMODUL_CTRL_IDX = 13
active_FH_TUERMODUL_CTRL_copy_IDX = 14
active_FH_TUERMODUL_CTRL_old_IDX = 15
active_EINKLEMMSCHUTZ_CTRL_IDX = 16
active_EINKLEMMSCHUTZ_CTRL_copy_IDX = 17
active_EINKLEMMSCHUTZ_CTRL_old_IDX = 18
active_BLOCK_ERKENNUNG_CTRL_IDX = 19
active_BLOCK_ERKENNUNG_CTRL_copy_IDX = 20
active_BLOCK_ERKENNUNG_CTRL_old_IDX = 21
entered_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRL_IDX = 0
entered_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRL_copy_IDX = 1
tm_entered_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRLch_BLOCK_ERKENNUNG_CTRL__N_copy = 0
entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_IDX = 4
entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_copy_IDX = 5
exited_BEREIT_FH_TUERMODUL_CTRL_IDX = 6
exited_BEREIT_FH_TUERMODUL_CTRL_copy_IDX = 7
tm_entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRLexited_BEREIT_FH_TUERMODUL_CTRL = 0
tm_entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL = 0
sc_FH_TUERMODUL_CTRL_2375_2 = 0
sc_FH_TUERMODUL_CTRL_2352_1 = 0
sc_FH_TUERMODUL_CTRL_2329_1 = 0
FH_TUERMODUL_CTRL__N = 0
FH_TUERMODUL_CTRL__N_copy = 0
FH_TUERMODUL_CTRL__N_old = 0
sc_FH_TUERMODUL_CTRL_1781_10 = 0
sc_FH_TUERMODUL_CTRL_1739_10 = 0
FH_TUERMODUL__POSITION = 0
FH_TUERMODUL__I_EIN = 0
FH_TUERMODUL__I_EIN_old = 0
FH_DU__MFH = 0
FH_DU__MFH_copy = 0
FH_DU__POSITION = 0
FH_DU__I_EIN = 0
FH_DU__I_EIN_old = 0
BLOCK_ERKENNUNG_CTRL__I_EIN_MAX = 0
BLOCK_ERKENNUNG_CTRL__I_EIN_MAX_copy = 0
BLOCK_ERKENNUNG_CTRL__N = 0
BLOCK_ERKENNUNG_CTRL__N_copy = 0
BLOCK_ERKENNUNG_CTRL__N_old = 0
FH_TUERMODUL_CTRL__INREVERS2 = 0
FH_TUERMODUL_CTRL__INREVERS2_copy = 0
FH_TUERMODUL_CTRL__INREVERS1 = 0
FH_TUERMODUL_CTRL__INREVERS1_copy = 0
FH_TUERMODUL_CTRL__FT = 0
FH_TUERMODUL__SFHZ_ZENTRAL = 0
FH_TUERMODUL__SFHZ_ZENTRAL_old = 0
FH_TUERMODUL__SFHZ_MEC = 0
FH_TUERMODUL__SFHZ_MEC_old = 0
FH_TUERMODUL__SFHA_ZENTRAL = 0
FH_TUERMODUL__SFHA_ZENTRAL_old = 0
FH_TUERMODUL__SFHA_MEC = 0
FH_TUERMODUL__SFHA_MEC_old = 0
FH_TUERMODUL__KL_50 = 0
FH_TUERMODUL__BLOCK = 0
FH_TUERMODUL__BLOCK_copy = 0
FH_TUERMODUL__BLOCK_old = 0
FH_TUERMODUL__FT = 0
FH_TUERMODUL__SFHZ = 0
FH_TUERMODUL__SFHZ_copy = 0
FH_TUERMODUL__SFHZ_old = 0
FH_TUERMODUL__SFHA = 0
FH_TUERMODUL__SFHA_copy = 0
FH_TUERMODUL__SFHA_old = 0
FH_TUERMODUL__MFHZ = 0
FH_TUERMODUL__MFHZ_copy = 0
FH_TUERMODUL__MFHZ_old = 0
FH_TUERMODUL__MFHA = 0
FH_TUERMODUL__MFHA_copy = 0
FH_TUERMODUL__MFHA_old = 0
FH_TUERMODUL__EKS_LEISTE_AKTIV = 0
FH_TUERMODUL__EKS_LEISTE_AKTIV_old = 0
FH_TUERMODUL__COM_OPEN = 0
FH_TUERMODUL__COM_CLOSE = 0
FH_DU__KL_50 = 0
FH_DU__S_FH_FTZU = 0
FH_DU__S_FH_FTAUF = 0
FH_DU__FT = 0
FH_DU__EKS_LEISTE_AKTIV = 0
FH_DU__EKS_LEISTE_AKTIV_old = 0
FH_DU__S_FH_TMBFAUFCAN = 0
FH_DU__S_FH_TMBFAUFCAN_copy = 0
FH_DU__S_FH_TMBFAUFCAN_old = 0
FH_DU__S_FH_TMBFZUCAN = 0
FH_DU__S_FH_TMBFZUCAN_copy = 0
FH_DU__S_FH_TMBFZUCAN_old = 0
FH_DU__S_FH_TMBFZUDISC = 0
FH_DU__S_FH_TMBFZUDISC_old = 0
FH_DU__S_FH_TMBFAUFDISC = 0
FH_DU__S_FH_TMBFAUFDISC_old = 0
FH_DU__S_FH_ZUDISC = 0
FH_DU__S_FH_AUFDISC = 0
FH_DU__DOOR_ID = 0
FH_DU__BLOCK = 0
FH_DU__BLOCK_copy = 0
FH_DU__BLOCK_old = 0
FH_DU__MFHZ = 0
FH_DU__MFHZ_copy = 0
FH_DU__MFHZ_old = 0
FH_DU__MFHA = 0
FH_DU__MFHA_copy = 0
FH_DU__MFHA_old = 0
FH_TUERMODUL_CTRL__END_REVERS_IDX = 22
FH_TUERMODUL_CTRL__END_REVERS_copy_IDX = 23
FH_TUERMODUL__EINKLEMMUNG_IDX = 24

time = 0
stable = 0
step = 0

NICHT_INITIALISIERT_NICHT_INITIALISIERT_next_state = 0
ZENTRAL_KINDERSICHERUNG_CTRL_next_state = 0
MEC_KINDERSICHERUNG_CTRL_next_state = 0
KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_next_state = 0
B_FH_TUERMODUL_CTRL_next_state = 0
A_FH_TUERMODUL_CTRL_next_state = 0
WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_next_state = 0
INITIALISIERT_FH_TUERMODUL_CTRL_next_state = 0
TIPP_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state = 0
MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state = 0
OEFFNEN_FH_TUERMODUL_CTRL_next_state = 0
SCHLIESSEN_FH_TUERMODUL_CTRL_next_state = 0
FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_next_state = 0
EINKLEMMSCHUTZ_CTRL_EINKLEMMSCHUTZ_CTRL_next_state = 0
BEWEGUNG_BLOCK_ERKENNUNG_CTRL_next_state = 0
BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_next_state = 0


def interface():
    global Bitlist, tm_entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL, tm_entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRLexited_BEREIT_FH_TUERMODUL_CTRL, sc_FH_TUERMODUL_CTRL_2375_2, FH_TUERMODUL__MFHA_copy, sc_FH_TUERMODUL_CTRL_2352_1, FH_TUERMODUL__MFHZ_copy, sc_FH_TUERMODUL_CTRL_2329_1, sc_FH_TUERMODUL_CTRL_1781_10, sc_FH_TUERMODUL_CTRL_1739_10, tm_entered_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRLch_BLOCK_ERKENNUNG_CTRL__N_copy
    if Bitlist[entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_IDX]:
        tm_entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL = time
    if Bitlist[entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_IDX] or Bitlist[exited_BEREIT_FH_TUERMODUL_CTRL_IDX]:
        tm_entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRLexited_BEREIT_FH_TUERMODUL_CTRL = time
    if (sc_FH_TUERMODUL_CTRL_2375_2 != 0) and (time - sc_FH_TUERMODUL_CTRL_2375_2 >= 1):
        FH_TUERMODUL__MFHA_copy = 0
        sc_FH_TUERMODUL_CTRL_2375_2 = 0
    if (sc_FH_TUERMODUL_CTRL_2375_2 != 0) and (time - sc_FH_TUERMODUL_CTRL_2352_1 >= 1):
        FH_TUERMODUL__MFHZ_copy = 0
        sc_FH_TUERMODUL_CTRL_2352_1 = 0
    if (sc_FH_TUERMODUL_CTRL_2329_1 != 0) and (time - sc_FH_TUERMODUL_CTRL_2329_1 >= 1):
        FH_TUERMODUL__MFHZ_copy = 0
        sc_FH_TUERMODUL_CTRL_2329_1 = 0
    if (sc_FH_TUERMODUL_CTRL_1781_10 != 0) and (time - sc_FH_TUERMODUL_CTRL_1781_10 >= 1):
        sc_FH_TUERMODUL_CTRL_1781_10 = 0
    if (sc_FH_TUERMODUL_CTRL_1739_10 != 0) and (time - sc_FH_TUERMODUL_CTRL_1739_10 >= 1):
        sc_FH_TUERMODUL_CTRL_1739_10 = 0
    if Bitlist[entered_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRL_IDX] or BLOCK_ERKENNUNG_CTRL__N != BLOCK_ERKENNUNG_CTRL__N_old:
        tm_entered_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRLch_BLOCK_ERKENNUNG_CTRL__N_copy = time


def init():
    global tm_entered_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRLch_BLOCK_ERKENNUNG_CTRL__N_copy, tm_entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRLexited_BEREIT_FH_TUERMODUL_CTRL, tm_entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL, NICHT_INITIALISIERT_NICHT_INITIALISIERT_next_state, ZENTRAL_KINDERSICHERUNG_CTRL_next_state, MEC_KINDERSICHERUNG_CTRL_next_state, KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_next_state, B_FH_TUERMODUL_CTRL_next_state, A_FH_TUERMODUL_CTRL_next_state, WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_next_state, INITIALISIERT_FH_TUERMODUL_CTRL_next_state, TIPP_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state, MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state, OEFFNEN_FH_TUERMODUL_CTRL_next_state, SCHLIESSEN_FH_TUERMODUL_CTRL_next_state, FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_next_state, EINKLEMMSCHUTZ_CTRL_EINKLEMMSCHUTZ_CTRL_next_state, BEWEGUNG_BLOCK_ERKENNUNG_CTRL_next_state, BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_next_state

    tm_entered_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRLch_BLOCK_ERKENNUNG_CTRL__N_copy = 0
    tm_entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRLexited_BEREIT_FH_TUERMODUL_CTRL = 0
    tm_entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL = 0
    NICHT_INITIALISIERT_NICHT_INITIALISIERT_next_state = 0
    ZENTRAL_KINDERSICHERUNG_CTRL_next_state = 0
    MEC_KINDERSICHERUNG_CTRL_next_state = 0
    KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_next_state = 0
    B_FH_TUERMODUL_CTRL_next_state = 0
    A_FH_TUERMODUL_CTRL_next_state = 0
    WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_next_state = 0
    INITIALISIERT_FH_TUERMODUL_CTRL_next_state = 0
    TIPP_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state = 0
    MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state = 0
    OEFFNEN_FH_TUERMODUL_CTRL_next_state = 0
    SCHLIESSEN_FH_TUERMODUL_CTRL_next_state = 0
    FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_next_state = 0
    EINKLEMMSCHUTZ_CTRL_EINKLEMMSCHUTZ_CTRL_next_state = 0
    BEWEGUNG_BLOCK_ERKENNUNG_CTRL_next_state = 0
    BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_next_state = 0


def generic_KINDERSICHERUNG_CTRL():
    global Bitlist, active_KINDERSICHERUNG_CTRL_IDX, KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_next_state, ZENTRAL_KINDERSICHERUNG_CTRL_next_state, MEC_KINDERSICHERUNG_CTRL_next_state, FH_TUERMODUL__SFHA_ZENTRAL, FH_TUERMODUL__SFHZ_ZENTRAL, FH_TUERMODUL__SFHA_ZENTRAL_old, FH_TUERMODUL__SFHZ_ZENTRAL_old, FH_TUERMODUL__SFHA_MEC, FH_TUERMODUL__SFHZ_MEC, FH_TUERMODUL__SFHA_MEC_old, FH_TUERMODUL__SFHZ_MEC_old, FH_TUERMODUL__SFHA_copy, FH_TUERMODUL__SFHZ_copy, FH_TUERMODUL__KL_50, stable
    if Bitlist[active_KINDERSICHERUNG_CTRL_IDX]:
        if KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_next_state == 1:
            if not (FH_TUERMODUL__SFHA_ZENTRAL or FH_TUERMODUL__SFHZ_ZENTRAL):
                stable = 0
                FH_TUERMODUL__SFHZ_copy = 0
                FH_TUERMODUL__SFHA_copy = 0

                KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_next_state = 3
                ZENTRAL_KINDERSICHERUNG_CTRL_next_state = 0
            else:
                if ZENTRAL_KINDERSICHERUNG_CTRL_next_state == 1:
                    if FH_TUERMODUL__SFHA_ZENTRAL and not FH_TUERMODUL__SFHA_ZENTRAL_old:
                        stable = 0
                        FH_TUERMODUL__SFHA_copy = 1

                        ZENTRAL_KINDERSICHERUNG_CTRL_next_state = 1

                    elif FH_TUERMODUL__SFHZ_ZENTRAL and not FH_TUERMODUL__SFHZ_ZENTRAL_old:
                        stable = 0
                        FH_TUERMODUL__SFHZ_copy = 1

                        ZENTRAL_KINDERSICHERUNG_CTRL_next_state = 1

                    elif not FH_TUERMODUL__SFHA_ZENTRAL and FH_TUERMODUL__SFHA_ZENTRAL_old:
                        stable = 0
                        FH_TUERMODUL__SFHA_copy = 0

                        ZENTRAL_KINDERSICHERUNG_CTRL_next_state = 1

                    elif not FH_TUERMODUL__SFHZ_ZENTRAL and FH_TUERMODUL__SFHZ_ZENTRAL_old:
                        stable = 0
                        FH_TUERMODUL__SFHZ_copy = 0

                        ZENTRAL_KINDERSICHERUNG_CTRL_next_state = 1

                else:
                    stable = 0

        elif KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_next_state == 2:
            if not (FH_TUERMODUL__SFHA_MEC or FH_TUERMODUL__SFHZ_MEC):
                stable = 0
                FH_TUERMODUL__SFHZ_copy = 0
                FH_TUERMODUL__SFHA_copy = 0

                KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_next_state = 3
                MEC_KINDERSICHERUNG_CTRL_next_state = 0
            else:
                if MEC_KINDERSICHERUNG_CTRL_next_state == 1:
                    if FH_TUERMODUL__SFHA_MEC and not FH_TUERMODUL__SFHA_MEC_old:
                        stable = 0
                        FH_TUERMODUL__SFHA_copy = 1

                        MEC_KINDERSICHERUNG_CTRL_next_state = 1

                    elif FH_TUERMODUL__SFHZ_MEC and not FH_TUERMODUL__SFHZ_MEC_old:
                        stable = 0
                        FH_TUERMODUL__SFHZ_copy = 1

                        MEC_KINDERSICHERUNG_CTRL_next_state = 1

                    elif not FH_TUERMODUL__SFHA_MEC and FH_TUERMODUL__SFHA_MEC_old:
                        stable = 0
                        FH_TUERMODUL__SFHA_copy = 0

                        MEC_KINDERSICHERUNG_CTRL_next_state = 1

                    elif not FH_TUERMODUL__SFHZ_MEC and FH_TUERMODUL__SFHZ_MEC_old:
                        stable = 0
                        FH_TUERMODUL__SFHZ_copy = 0

                        MEC_KINDERSICHERUNG_CTRL_next_state = 1

                else:
                    stable = 0

        elif KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_next_state == 3:
            if (not FH_TUERMODUL__KL_50) and (FH_TUERMODUL__SFHZ_MEC and FH_TUERMODUL__SFHA_MEC):
                stable = 0
                FH_TUERMODUL__SFHZ_copy = 1
                FH_TUERMODUL__SFHA_copy = 1

                KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_next_state = 2

            elif (not FH_TUERMODUL__KL_50) and (FH_TUERMODUL__SFHZ_MEC and not FH_TUERMODUL__SFHA_MEC):
                stable = 0
                FH_TUERMODUL__SFHZ_copy = 1

                KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_next_state = 2

            elif (not FH_TUERMODUL__KL_50) and (not FH_TUERMODUL__SFHZ_MEC and FH_TUERMODUL__SFHA_MEC):
                stable = 0
                FH_TUERMODUL__SFHA_copy = 1

                KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_next_state = 2

            elif not FH_TUERMODUL__SFHZ_ZENTRAL and FH_TUERMODUL__SFHA_ZENTRAL and not FH_TUERMODUL__KL_50:
                stable = 0
                FH_TUERMODUL__SFHA_copy = 1

                KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_next_state = 1

            elif FH_TUERMODUL__SFHZ_ZENTRAL and FH_TUERMODUL__SFHA_ZENTRAL:
                stable = 0
                FH_TUERMODUL__SFHA_copy = 1
                FH_TUERMODUL__SFHZ_copy = 1

                KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_next_state = 1

            elif FH_TUERMODUL__SFHZ_ZENTRAL and not FH_TUERMODUL__SFHA_ZENTRAL and not FH_TUERMODUL__KL_50:
                stable = 0
                FH_TUERMODUL__SFHZ_copy = 1

                KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_next_state = 1

        else:
            stable = 0
            KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_next_state = 3


def generic_FH_TUERMODUL_CTRL():
    global Bitlist, active_FH_TUERMODUL_CTRL_IDX, active_FH_TUERMODUL_CTRL_old_IDX, active_FH_TUERMODUL_CTRL_copy_IDX, entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_IDX, exited_BEREIT_FH_TUERMODUL_CTRL_IDX, active_KINDERSICHERUNG_CTRL_IDX, active_KINDERSICHERUNG_CTRL_copy_IDX, active_BLOCK_ERKENNUNG_CTRL_IDX, active_BLOCK_ERKENNUNG_CTRL_copy_IDX, entered_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRL_IDX, BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_next_state, KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_next_state, B_FH_TUERMODUL_CTRL_next_state, INITIALISIERT_FH_TUERMODUL_CTRL_next_state, NICHT_INITIALISIERT_NICHT_INITIALISIERT_next_state, OEFFNEN_FH_TUERMODUL_CTRL_next_state, SCHLIESSEN_FH_TUERMODUL_CTRL_next_state, TIPP_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state, MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state, A_FH_TUERMODUL_CTRL_next_state, WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_next_state, FH_TUERMODUL_CTRL__N, FH_TUERMODUL_CTRL__N_old, FH_TUERMODUL_CTRL__INREVERS1, FH_TUERMODUL_CTRL__INREVERS2, FH_TUERMODUL_CTRL__INREVERS1_copy, FH_TUERMODUL_CTRL__INREVERS2_copy, FH_TUERMODUL__BLOCK, FH_TUERMODUL__BLOCK_old, FH_TUERMODUL__MFHZ, FH_TUERMODUL__MFHA, FH_TUERMODUL__MFHZ_copy, FH_TUERMODUL__MFHA_copy, FH_TUERMODUL__SFHZ, FH_TUERMODUL__SFHZ_old, FH_TUERMODUL__SFHA, FH_TUERMODUL__SFHA_old, FH_TUERMODUL__POSITION, FH_TUERMODUL__KL_50, FH_TUERMODUL__EINKLEMMUNG_IDX, FH_TUERMODUL_CTRL__END_REVERS_IDX, FH_TUERMODUL_CTRL__END_REVERS_copy_IDX, active_EINKLEMMSCHUTZ_CTRL_copy_IDX, sc_FH_TUERMODUL_CTRL_2329_1, sc_FH_TUERMODUL_CTRL_2375_2, sc_FH_TUERMODUL_CTRL_2352_1, sc_FH_TUERMODUL_CTRL_1781_10, sc_FH_TUERMODUL_CTRL_1739_10, step, time, tm_entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL, tm_entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRLexited_BEREIT_FH_TUERMODUL_CTRL, stable
    if not Bitlist[active_FH_TUERMODUL_CTRL_IDX] and Bitlist[active_FH_TUERMODUL_CTRL_old_IDX] and not \
            Bitlist[active_FH_TUERMODUL_CTRL_copy_IDX]:
        Bitlist[entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_IDX] = 0
        Bitlist[exited_BEREIT_FH_TUERMODUL_CTRL_IDX] = 0
    if Bitlist[active_FH_TUERMODUL_CTRL_IDX]:
        if not Bitlist[active_KINDERSICHERUNG_CTRL_IDX]:
            KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_next_state = 3
        Bitlist[active_KINDERSICHERUNG_CTRL_copy_IDX] = 0
        if not Bitlist[active_BLOCK_ERKENNUNG_CTRL_IDX]:
            Bitlist[entered_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRL_IDX] = 0
            BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_next_state = 1
        Bitlist[active_BLOCK_ERKENNUNG_CTRL_copy_IDX] = 0
        Bitlist[active_KINDERSICHERUNG_CTRL_copy_IDX] = 1
        Bitlist[active_BLOCK_ERKENNUNG_CTRL_copy_IDX] = 1
        if B_FH_TUERMODUL_CTRL_next_state == 1:
            if FH_TUERMODUL_CTRL__N == 59 and not (FH_TUERMODUL_CTRL__N_old == 59):
                stable = 0

                B_FH_TUERMODUL_CTRL_next_state = 3
                INITIALISIERT_FH_TUERMODUL_CTRL_next_state = 3

        elif B_FH_TUERMODUL_CTRL_next_state == 2:
            if (FH_TUERMODUL__BLOCK and not FH_TUERMODUL__BLOCK_old) and FH_TUERMODUL__MFHZ:
                stable = 0
                FH_TUERMODUL__MFHZ_copy = 0
                sc_FH_TUERMODUL_CTRL_2329_1 = time

                B_FH_TUERMODUL_CTRL_next_state = 3
                INITIALISIERT_FH_TUERMODUL_CTRL_next_state = 3
            else:
                if NICHT_INITIALISIERT_NICHT_INITIALISIERT_next_state == 1:
                    if not FH_TUERMODUL__SFHZ:
                        stable = 0
                        FH_TUERMODUL__MFHZ_copy = 0

                        NICHT_INITIALISIERT_NICHT_INITIALISIERT_next_state = 3

                elif NICHT_INITIALISIERT_NICHT_INITIALISIERT_next_state == 2:
                    if not FH_TUERMODUL__SFHA:
                        stable = 0
                        FH_TUERMODUL__MFHA_copy = 0

                        NICHT_INITIALISIERT_NICHT_INITIALISIERT_next_state = 3

                elif NICHT_INITIALISIERT_NICHT_INITIALISIERT_next_state == 3:
                    if FH_TUERMODUL__SFHA:
                        stable = 0
                        FH_TUERMODUL__MFHA_copy = 1

                        NICHT_INITIALISIERT_NICHT_INITIALISIERT_next_state = 2

                    elif FH_TUERMODUL__SFHZ:
                        stable = 0
                        FH_TUERMODUL__MFHZ_copy = 1

                        NICHT_INITIALISIERT_NICHT_INITIALISIERT_next_state = 1

                else:
                    stable = 0
                    NICHT_INITIALISIERT_NICHT_INITIALISIERT_next_state = 3

        elif B_FH_TUERMODUL_CTRL_next_state == 3:
            if (FH_TUERMODUL_CTRL__N > 60 and not (FH_TUERMODUL_CTRL__N_old > 60)) and (
                    (not (FH_TUERMODUL_CTRL__INREVERS1 or FH_TUERMODUL_CTRL__INREVERS2))):
                stable = 0
                FH_TUERMODUL__MFHZ_copy = 0
                FH_TUERMODUL__MFHA_copy = 0

                B_FH_TUERMODUL_CTRL_next_state = 1

            elif (FH_TUERMODUL__BLOCK and not FH_TUERMODUL__BLOCK_old) and FH_TUERMODUL__MFHA:
                stable = 0
                FH_TUERMODUL__MFHA_copy = 0
                sc_FH_TUERMODUL_CTRL_2375_2 = time

                B_FH_TUERMODUL_CTRL_next_state = 2
                NICHT_INITIALISIERT_NICHT_INITIALISIERT_next_state = 3

            elif (FH_TUERMODUL__BLOCK and not FH_TUERMODUL__BLOCK_old) and FH_TUERMODUL__MFHZ:
                stable = 0
                FH_TUERMODUL__MFHZ_copy = 0
                sc_FH_TUERMODUL_CTRL_2352_1 = time

                B_FH_TUERMODUL_CTRL_next_state = 2
                NICHT_INITIALISIERT_NICHT_INITIALISIERT_next_state = 3

            else:
                if INITIALISIERT_FH_TUERMODUL_CTRL_next_state == 1:
                    if FH_TUERMODUL__POSITION >= 405:
                        stable = 0
                        FH_TUERMODUL__MFHA_copy = 0

                        INITIALISIERT_FH_TUERMODUL_CTRL_next_state = 3
                    else:
                        if OEFFNEN_FH_TUERMODUL_CTRL_next_state == 1:
                            if (FH_TUERMODUL__SFHZ and not FH_TUERMODUL__SFHZ_old) or (
                                    FH_TUERMODUL__SFHA and not FH_TUERMODUL__SFHA_old):
                                stable = 0
                                FH_TUERMODUL__MFHA_copy = 0

                                INITIALISIERT_FH_TUERMODUL_CTRL_next_state = 3
                                OEFFNEN_FH_TUERMODUL_CTRL_next_state = 0

                        elif OEFFNEN_FH_TUERMODUL_CTRL_next_state == 2:
                            if FH_TUERMODUL__SFHZ and not FH_TUERMODUL__SFHZ_old:
                                stable = 0

                                OEFFNEN_FH_TUERMODUL_CTRL_next_state = 1

                            elif not FH_TUERMODUL__SFHA and FH_TUERMODUL__SFHA_old:
                                stable = 0
                                FH_TUERMODUL__MFHA_copy = 0

                                INITIALISIERT_FH_TUERMODUL_CTRL_next_state = 3
                                OEFFNEN_FH_TUERMODUL_CTRL_next_state = 0

                        else:
                            stable = 0
                            OEFFNEN_FH_TUERMODUL_CTRL_next_state = 2

                elif INITIALISIERT_FH_TUERMODUL_CTRL_next_state == 2:
                    if FH_TUERMODUL__POSITION <= 0:
                        stable = 0
                        FH_TUERMODUL__MFHZ_copy = 0

                        INITIALISIERT_FH_TUERMODUL_CTRL_next_state = 3
                    else:
                        if SCHLIESSEN_FH_TUERMODUL_CTRL_next_state == 1:
                            if (FH_TUERMODUL__SFHA and not FH_TUERMODUL__SFHA_old) or (
                                    FH_TUERMODUL__SFHZ and not FH_TUERMODUL__SFHZ_old):
                                stable = 0
                                FH_TUERMODUL__MFHZ_copy = 0

                                INITIALISIERT_FH_TUERMODUL_CTRL_next_state = 3
                            else:
                                if TIPP_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state == 1:
                                    Bitlist[FH_TUERMODUL_CTRL__END_REVERS_copy_IDX] = 0
                                    if Bitlist[FH_TUERMODUL_CTRL__END_REVERS_IDX]:
                                        stable = 0
                                        FH_TUERMODUL__MFHZ_copy = 1
                                        FH_TUERMODUL_CTRL__INREVERS2_copy = 0

                                        TIPP_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state = 2
                                        FH_TUERMODUL__MFHA_copy = 0

                                        Bitlist[active_EINKLEMMSCHUTZ_CTRL_copy_IDX] = 1

                                elif TIPP_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state == 2:
                                    if Bitlist[FH_TUERMODUL__EINKLEMMUNG_IDX]:
                                        stable = 0
                                        FH_TUERMODUL_CTRL__INREVERS2_copy = 1

                                        Bitlist[FH_TUERMODUL_CTRL__END_REVERS_copy_IDX] = 1
                                        TIPP_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state = 1
                                        Bitlist[active_EINKLEMMSCHUTZ_CTRL_copy_IDX] = 0
                                        FH_TUERMODUL__MFHZ_copy = 0

                                        sc_FH_TUERMODUL_CTRL_1781_10 = time
                                        FH_TUERMODUL__MFHA_copy = 1

                                else:
                                    stable = 0
                                    TIPP_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state = 2
                                    Bitlist[active_EINKLEMMSCHUTZ_CTRL_copy_IDX] = 1

                        elif SCHLIESSEN_FH_TUERMODUL_CTRL_next_state == 2:
                            if not FH_TUERMODUL__SFHZ and FH_TUERMODUL__SFHZ_old:
                                stable = 0
                                FH_TUERMODUL__MFHZ_copy = 0

                                INITIALISIERT_FH_TUERMODUL_CTRL_next_state = 3
                            else:
                                if MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state == 1:
                                    Bitlist[FH_TUERMODUL_CTRL__END_REVERS_copy_IDX] = 0
                                    if Bitlist[FH_TUERMODUL_CTRL__END_REVERS_IDX]:
                                        stable = 0
                                        FH_TUERMODUL_CTRL__INREVERS1_copy = 0

                                        MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state = 2
                                        FH_TUERMODUL__MFHA_copy = 0

                                        Bitlist[active_EINKLEMMSCHUTZ_CTRL_copy_IDX] = 1
                                        FH_TUERMODUL__MFHZ_copy = 1

                                elif MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state == 2:
                                    if Bitlist[FH_TUERMODUL__EINKLEMMUNG_IDX]:
                                        stable = 0
                                        FH_TUERMODUL__MFHZ_copy = 0
                                        FH_TUERMODUL_CTRL__INREVERS1_copy = 1

                                        Bitlist[FH_TUERMODUL_CTRL__END_REVERS_copy_IDX] = 1
                                        MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state = 1
                                        Bitlist[active_EINKLEMMSCHUTZ_CTRL_copy_IDX] = 0

                                        sc_FH_TUERMODUL_CTRL_1739_10 = time
                                        FH_TUERMODUL__MFHA_copy = 1

                                    elif FH_TUERMODUL__SFHA and not FH_TUERMODUL__SFHA_old:
                                        stable = 0

                                        SCHLIESSEN_FH_TUERMODUL_CTRL_next_state = 1
                                        MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state = 0

                                else:
                                    stable = 0
                                    MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state = 2
                                    Bitlist[active_EINKLEMMSCHUTZ_CTRL_copy_IDX] = 1
                                    FH_TUERMODUL__MFHZ_copy = 1

                        else:
                            stable = 0
                            SCHLIESSEN_FH_TUERMODUL_CTRL_next_state = 2
                            MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state = 2
                            Bitlist[active_EINKLEMMSCHUTZ_CTRL_copy_IDX] = 1
                            FH_TUERMODUL__MFHZ_copy = 1

                elif INITIALISIERT_FH_TUERMODUL_CTRL_next_state == 3:
                    if (FH_TUERMODUL__SFHZ and not FH_TUERMODUL__SFHZ_old) and (FH_TUERMODUL__POSITION > 0):
                        stable = 0

                        INITIALISIERT_FH_TUERMODUL_CTRL_next_state = 2
                        SCHLIESSEN_FH_TUERMODUL_CTRL_next_state = 2
                        MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state = 2
                        Bitlist[active_EINKLEMMSCHUTZ_CTRL_copy_IDX] = 1
                        FH_TUERMODUL__MFHZ_copy = 1

                    elif (FH_TUERMODUL__SFHA and not FH_TUERMODUL__SFHA_old) and (FH_TUERMODUL__POSITION < 405):
                        stable = 0
                        FH_TUERMODUL__MFHA_copy = 1

                        INITIALISIERT_FH_TUERMODUL_CTRL_next_state = 1
                        OEFFNEN_FH_TUERMODUL_CTRL_next_state = 2

                else:
                    stable = 0
                    INITIALISIERT_FH_TUERMODUL_CTRL_next_state = 3

        else:
            stable = 0
            B_FH_TUERMODUL_CTRL_next_state = 2

        if A_FH_TUERMODUL_CTRL_next_state == 1:
            Bitlist[entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_copy_IDX] = 0
            if (step == 1 and tm_entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRLexited_BEREIT_FH_TUERMODUL_CTRL != 0 and (
                    time - tm_entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRLexited_BEREIT_FH_TUERMODUL_CTRL == 1)) and (
                    (FH_TUERMODUL__MFHZ or FH_TUERMODUL__MFHA)):
                stable = 0
                FH_TUERMODUL_CTRL__N = FH_TUERMODUL_CTRL__N + 1

                A_FH_TUERMODUL_CTRL_next_state = 1
                Bitlist[entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_copy_IDX] = 1
                WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_next_state = 1
            else:
                if WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_next_state == 1:
                    if (step == 1 and tm_entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL != 0 and (
                            time - tm_entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL == 3)) and (
                            ((not (FH_TUERMODUL__MFHZ or FH_TUERMODUL__MFHA)) and FH_TUERMODUL_CTRL__N > 0)):
                        stable = 0
                        FH_TUERMODUL_CTRL__N = FH_TUERMODUL_CTRL__N - 1

                        WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_next_state = 1

                else:
                    stable = 0
                    Bitlist[entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_copy_IDX] = 1
                    WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_next_state = 1

        else:
            stable = 0
            FH_TUERMODUL_CTRL__N = 0
            A_FH_TUERMODUL_CTRL_next_state = 1
            Bitlist[entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_copy_IDX] = 1
            WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_next_state = 1

        Bitlist[entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_copy_IDX] = Bitlist[
            entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_IDX]
        Bitlist[exited_BEREIT_FH_TUERMODUL_CTRL_copy_IDX] = Bitlist[exited_BEREIT_FH_TUERMODUL_CTRL_IDX]


def generic_EINKLEMMSCHUTZ_CTRL():
    global Bitlist, active_EINKLEMMSCHUTZ_CTRL_IDX, EINKLEMMSCHUTZ_CTRL_EINKLEMMSCHUTZ_CTRL_next_state, stable
    if Bitlist[active_EINKLEMMSCHUTZ_CTRL_IDX]:
        if EINKLEMMSCHUTZ_CTRL_EINKLEMMSCHUTZ_CTRL_next_state == 1:
            if (FH_TUERMODUL__EKS_LEISTE_AKTIV and not FH_TUERMODUL__EKS_LEISTE_AKTIV_old) and (
                    (not (FH_TUERMODUL__SFHZ and FH_TUERMODUL__SFHA))):
                stable = 0

                Bitlist[FH_TUERMODUL__EINKLEMMUNG_IDX] = 1
                EINKLEMMSCHUTZ_CTRL_EINKLEMMSCHUTZ_CTRL_next_state = 2

        elif EINKLEMMSCHUTZ_CTRL_EINKLEMMSCHUTZ_CTRL_next_state == 2:
            Bitlist[FH_TUERMODUL__EINKLEMMUNG_IDX] = 0
            if not FH_TUERMODUL__EKS_LEISTE_AKTIV and FH_TUERMODUL__EKS_LEISTE_AKTIV_old:
                stable = 0

                EINKLEMMSCHUTZ_CTRL_EINKLEMMSCHUTZ_CTRL_next_state = 1

        else:
            stable = 0
            EINKLEMMSCHUTZ_CTRL_EINKLEMMSCHUTZ_CTRL_next_state = 1


def generic_BLOCK_ERKENNUNG_CTRL():
    global Bitlist, active_BLOCK_ERKENNUNG_CTRL_IDX, active_BLOCK_ERKENNUNG_CTRL_old_IDX, active_BLOCK_ERKENNUNG_CTRL_copy_IDX, entered_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRL_IDX,BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_next_state, stable, FH_TUERMODUL__BLOCK_copy, BLOCK_ERKENNUNG_CTRL__N, BLOCK_ERKENNUNG_CTRL__I_EIN_MAX, BEWEGUNG_BLOCK_ERKENNUNG_CTRL_next_state
    if not Bitlist[active_BLOCK_ERKENNUNG_CTRL_IDX] and Bitlist[active_BLOCK_ERKENNUNG_CTRL_old_IDX] and not \
            Bitlist[active_BLOCK_ERKENNUNG_CTRL_copy_IDX]:
        Bitlist[entered_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRL_IDX] = 0
    if Bitlist[active_BLOCK_ERKENNUNG_CTRL_IDX]:
        if BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_next_state == 1:
            if (FH_TUERMODUL__I_EIN != FH_TUERMODUL__I_EIN_old) and (FH_TUERMODUL__I_EIN > 0):
                stable = 0
                FH_TUERMODUL__BLOCK_copy = 0

                BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_next_state = 2
                BLOCK_ERKENNUNG_CTRL__N = 0
                BLOCK_ERKENNUNG_CTRL__I_EIN_MAX = 2
                BEWEGUNG_BLOCK_ERKENNUNG_CTRL_next_state = 3
                Bitlist[entered_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRL_IDX] = 1

        elif BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_next_state == 2:
            if (not FH_TUERMODUL__MFHA and FH_TUERMODUL__MFHA_old) or (
                    not FH_TUERMODUL__MFHZ and FH_TUERMODUL__MFHZ_old):
                stable = 0

                BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_next_state = 1
                BEWEGUNG_BLOCK_ERKENNUNG_CTRL_next_state = 0
            else:
                if BEWEGUNG_BLOCK_ERKENNUNG_CTRL_next_state == 1:
                    pass
                elif BEWEGUNG_BLOCK_ERKENNUNG_CTRL_next_state == 2:
                    if FH_TUERMODUL__I_EIN > (BLOCK_ERKENNUNG_CTRL__I_EIN_MAX - 2):
                        stable = 0
                        FH_TUERMODUL__BLOCK_copy = 1

                        BEWEGUNG_BLOCK_ERKENNUNG_CTRL_next_state = 1

                elif BEWEGUNG_BLOCK_ERKENNUNG_CTRL_next_state == 3:
                    Bitlist[entered_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRL_IDX] = 0
                    if BLOCK_ERKENNUNG_CTRL__N == 11 and not (BLOCK_ERKENNUNG_CTRL__N_old == 11):
                        stable = 0

                        BEWEGUNG_BLOCK_ERKENNUNG_CTRL_next_state = 2

                    elif BEWEGUNG_BLOCK_ERKENNUNG_CTRL_next_state == 3:
                        if step == 1 and tm_entered_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRLch_BLOCK_ERKENNUNG_CTRL__N_copy != 0 and 0:
                            BLOCK_ERKENNUNG_CTRL__N = BLOCK_ERKENNUNG_CTRL__N + 1
                            if FH_TUERMODUL__I_EIN > BLOCK_ERKENNUNG_CTRL__I_EIN_MAX:
                                BLOCK_ERKENNUNG_CTRL__I_EIN_MAX = FH_TUERMODUL__I_EIN

                else:
                    stable = 0
                    BLOCK_ERKENNUNG_CTRL__N = 0
                    BLOCK_ERKENNUNG_CTRL__I_EIN_MAX = 2
                    BEWEGUNG_BLOCK_ERKENNUNG_CTRL_next_state = 3
                    Bitlist[entered_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRL_IDX] = 1

        else:
            stable = 0
            BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_next_state = 1


def FH_DU():
    global time, stable, step, Bitlist, FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_next_state, FH_DU__MFHZ, FH_DU__MFHZ_old, FH_DU__MFHA, FH_DU__MFHA_old, FH_DU__MFH, FH_DU__MFH_copy, FH_DU__I_EIN, FH_DU__I_EIN_old, FH_DU__EKS_LEISTE_AKTIV, FH_DU__EKS_LEISTE_AKTIV_old, FH_DU__POSITION, FH_DU__FT, FH_DU__KL_50, FH_DU__BLOCK, FH_DU__BLOCK_copy, FH_DU__BLOCK_old, FH_DU__DOOR_ID, FH_DU__S_FH_TMBFZUCAN, FH_DU__S_FH_TMBFZUCAN_old, FH_DU__S_FH_TMBFZUDISC, FH_DU__S_FH_TMBFZUDISC_old, FH_DU__S_FH_TMBFAUFCAN, FH_DU__S_FH_TMBFAUFCAN_old, FH_DU__S_FH_TMBFAUFDISC, FH_DU__S_FH_TMBFAUFDISC_old, FH_DU__S_FH_AUFDISC, FH_DU__S_FH_FTAUF, FH_DU__S_FH_ZUDISC, FH_DU__S_FH_FTZU, FH_TUERMODUL__MFHZ, FH_TUERMODUL__MFHZ_copy, FH_TUERMODUL__MFHZ_old, FH_TUERMODUL__MFHA, FH_TUERMODUL__MFHA_copy, FH_TUERMODUL__MFHA_old, FH_TUERMODUL__I_EIN, FH_TUERMODUL__I_EIN_old, FH_TUERMODUL__EKS_LEISTE_AKTIV, FH_TUERMODUL__EKS_LEISTE_AKTIV_old, FH_TUERMODUL__POSITION, FH_TUERMODUL__FT, FH_TUERMODUL__KL_50, FH_TUERMODUL__BLOCK, FH_TUERMODUL__BLOCK_copy, FH_TUERMODUL__BLOCK_old, FH_TUERMODUL__SFHA_MEC, FH_TUERMODUL__SFHA_MEC_old, FH_TUERMODUL__SFHA_ZENTRAL, FH_TUERMODUL__SFHA_ZENTRAL_old, FH_TUERMODUL__SFHZ_MEC, FH_TUERMODUL__SFHZ_MEC_old, FH_TUERMODUL__SFHZ_ZENTRAL, FH_TUERMODUL__SFHZ_ZENTRAL_old, FH_TUERMODUL__SFHZ, FH_TUERMODUL__SFHZ_copy, FH_TUERMODUL__SFHZ_old, FH_TUERMODUL__SFHA, FH_TUERMODUL__SFHA_copy, FH_TUERMODUL__SFHA_old, active_KINDERSICHERUNG_CTRL_IDX, active_KINDERSICHERUNG_CTRL_old_IDX, active_KINDERSICHERUNG_CTRL_copy_IDX, active_EINKLEMMSCHUTZ_CTRL_IDX, active_EINKLEMMSCHUTZ_CTRL_old_IDX, active_EINKLEMMSCHUTZ_CTRL_copy_IDX, active_BLOCK_ERKENNUNG_CTRL_IDX, active_BLOCK_ERKENNUNG_CTRL_old_IDX, active_BLOCK_ERKENNUNG_CTRL_copy_IDX, active_FH_TUERMODUL_CTRL_IDX, active_FH_TUERMODUL_CTRL_old_IDX, active_FH_TUERMODUL_CTRL_copy_IDX, entered_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRL_IDX, entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_IDX, entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_copy_IDX, exited_BEREIT_FH_TUERMODUL_CTRL_IDX, KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_next_state, EINKLEMMSCHUTZ_CTRL_EINKLEMMSCHUTZ_CTRL_next_state, BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_next_state, B_FH_TUERMODUL_CTRL_next_state, A_FH_TUERMODUL_CTRL_next_state, WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_next_state, FH_TUERMODUL_CTRL__N, FH_TUERMODUL_CTRL__N_old, BLOCK_ERKENNUNG_CTRL__N_old
    time = 1
    stable = 0
    step = 0
    while not stable:
        stable = 1
        step += 1
        if FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_next_state == 1:
            if not FH_DU__MFHZ and FH_DU__MFHZ_old:
                stable = 0
                FH_DU__MFH = 0

                FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_next_state = 2

        elif FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_next_state == 2:
            if FH_DU__MFHZ and not FH_DU__MFHZ_old:
                stable = 0
                FH_DU__MFH = -100

                FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_next_state = 1

            elif FH_DU__MFHA and not FH_DU__MFHA_old:
                stable = 0
                FH_DU__MFH = 100
                FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_next_state = 3

        elif FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_next_state == 3:
            if not FH_DU__MFHA and FH_DU__MFHA_old:
                stable = 0
                FH_DU__MFH = 0

                FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_next_state = 2

        else:
            stable = 0
            FH_DU__MFH = 0
            FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_next_state = 2

        if not Bitlist[active_KINDERSICHERUNG_CTRL_IDX]:
            KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_next_state = 3
        Bitlist[active_KINDERSICHERUNG_CTRL_copy_IDX] = 0
        if not Bitlist[active_EINKLEMMSCHUTZ_CTRL_IDX]:
            EINKLEMMSCHUTZ_CTRL_EINKLEMMSCHUTZ_CTRL_next_state = 1
        Bitlist[active_EINKLEMMSCHUTZ_CTRL_copy_IDX] = 0
        if not Bitlist[active_BLOCK_ERKENNUNG_CTRL_IDX]:
            Bitlist[entered_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRL_IDX] = 0
            BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_next_state = 1
        Bitlist[active_BLOCK_ERKENNUNG_CTRL_copy_IDX] = 0
        if not Bitlist[active_FH_TUERMODUL_CTRL_IDX]:
            Bitlist[entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_IDX] = 0
            Bitlist[exited_BEREIT_FH_TUERMODUL_CTRL_IDX] = 0
            B_FH_TUERMODUL_CTRL_next_state = 2
            FH_TUERMODUL_CTRL__N = 0
            A_FH_TUERMODUL_CTRL_next_state = 1
            Bitlist[entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_copy_IDX] = 1
            WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_next_state = 1
        Bitlist[active_FH_TUERMODUL_CTRL_copy_IDX] = 0
        Bitlist[active_KINDERSICHERUNG_CTRL_copy_IDX] = 1
        Bitlist[active_EINKLEMMSCHUTZ_CTRL_copy_IDX] = 1
        Bitlist[active_BLOCK_ERKENNUNG_CTRL_copy_IDX] = 1
        Bitlist[active_FH_TUERMODUL_CTRL_copy_IDX] = 1

        if FH_DU__S_FH_TMBFZUCAN != FH_DU__S_FH_TMBFZUCAN_old:
            if not FH_DU__DOOR_ID:
                FH_DU__S_FH_FTZU = FH_DU__S_FH_TMBFZUCAN
        if FH_DU__S_FH_TMBFZUDISC != FH_DU__S_FH_TMBFZUDISC_old:
            if FH_DU__DOOR_ID:
                FH_DU__S_FH_TMBFZUCAN = FH_DU__S_FH_TMBFZUDISC
        if FH_DU__S_FH_TMBFAUFCAN != FH_DU__S_FH_TMBFAUFCAN_old:
            if not FH_DU__DOOR_ID:
                FH_DU__S_FH_FTAUF = FH_DU__S_FH_TMBFAUFCAN
        if FH_DU__S_FH_TMBFAUFDISC != FH_DU__S_FH_TMBFAUFDISC_old:
            if FH_DU__DOOR_ID:
                FH_DU__S_FH_TMBFAUFCAN = FH_DU__S_FH_TMBFAUFDISC
        Bitlist[active_KINDERSICHERUNG_CTRL_IDX] = Bitlist[active_KINDERSICHERUNG_CTRL_old_IDX]
        Bitlist[active_FH_TUERMODUL_CTRL_IDX] = Bitlist[active_FH_TUERMODUL_CTRL_old_IDX]
        Bitlist[active_EINKLEMMSCHUTZ_CTRL_IDX] = Bitlist[active_EINKLEMMSCHUTZ_CTRL_old_IDX]
        Bitlist[active_BLOCK_ERKENNUNG_CTRL_IDX] = Bitlist[active_BLOCK_ERKENNUNG_CTRL_old_IDX]
        FH_TUERMODUL__SFHA_MEC = FH_DU__S_FH_AUFDISC
        FH_TUERMODUL__SFHA_ZENTRAL = FH_DU__S_FH_FTAUF
        FH_TUERMODUL__SFHZ_MEC = FH_DU__S_FH_ZUDISC
        FH_TUERMODUL__SFHZ_ZENTRAL = FH_DU__S_FH_FTZU

        generic_KINDERSICHERUNG_CTRL()

        FH_DU__MFHA = FH_TUERMODUL__MFHA
        FH_DU__MFHZ = FH_TUERMODUL__MFHZ
        FH_DU__I_EIN = FH_TUERMODUL__I_EIN
        FH_DU__EKS_LEISTE_AKTIV = FH_TUERMODUL__EKS_LEISTE_AKTIV
        FH_DU__POSITION = FH_TUERMODUL__POSITION
        FH_DU__FT = FH_TUERMODUL__FT
        FH_DU__S_FH_AUFDISC = FH_TUERMODUL__SFHA_MEC
        FH_DU__S_FH_FTAUF = FH_TUERMODUL__SFHA_ZENTRAL
        FH_DU__S_FH_ZUDISC = FH_TUERMODUL__SFHZ_MEC
        FH_DU__S_FH_FTZU = FH_TUERMODUL__SFHZ_ZENTRAL
        FH_DU__KL_50 = FH_TUERMODUL__KL_50
        FH_DU__BLOCK = FH_TUERMODUL__BLOCK

        FH_TUERMODUL__SFHA_MEC = FH_DU__S_FH_AUFDISC
        FH_TUERMODUL__SFHA_ZENTRAL = FH_DU__S_FH_FTAUF
        FH_TUERMODUL__SFHZ_MEC = FH_DU__S_FH_ZUDISC
        FH_TUERMODUL__SFHZ_ZENTRAL = FH_DU__S_FH_FTZU

        generic_FH_TUERMODUL_CTRL()

        FH_DU__MFHA = FH_TUERMODUL__MFHA
        FH_DU__MFHZ = FH_TUERMODUL__MFHZ
        FH_DU__I_EIN = FH_TUERMODUL__I_EIN
        FH_DU__EKS_LEISTE_AKTIV = FH_TUERMODUL__EKS_LEISTE_AKTIV
        FH_DU__POSITION = FH_TUERMODUL__POSITION
        FH_DU__FT = FH_TUERMODUL__FT
        FH_DU__S_FH_AUFDISC = FH_TUERMODUL__SFHA_MEC
        FH_DU__S_FH_FTAUF = FH_TUERMODUL__SFHA_ZENTRAL
        FH_DU__S_FH_ZUDISC = FH_TUERMODUL__SFHZ_MEC
        FH_DU__S_FH_FTZU = FH_TUERMODUL__SFHZ_ZENTRAL
        FH_DU__KL_50 = FH_TUERMODUL__KL_50
        FH_DU__BLOCK = FH_TUERMODUL__BLOCK

        FH_TUERMODUL__SFHA_MEC = FH_DU__S_FH_AUFDISC
        FH_TUERMODUL__SFHA_ZENTRAL = FH_DU__S_FH_FTAUF
        FH_TUERMODUL__SFHZ_MEC = FH_DU__S_FH_ZUDISC
        FH_TUERMODUL__SFHZ_ZENTRAL = FH_DU__S_FH_FTZU

        generic_EINKLEMMSCHUTZ_CTRL()

        FH_DU__MFHA = FH_TUERMODUL__MFHA
        FH_DU__MFHZ = FH_TUERMODUL__MFHZ
        FH_DU__I_EIN = FH_TUERMODUL__I_EIN
        FH_DU__EKS_LEISTE_AKTIV = FH_TUERMODUL__EKS_LEISTE_AKTIV
        FH_DU__POSITION = FH_TUERMODUL__POSITION
        FH_DU__FT = FH_TUERMODUL__FT
        FH_DU__S_FH_AUFDISC = FH_TUERMODUL__SFHA_MEC
        FH_DU__S_FH_FTAUF = FH_TUERMODUL__SFHA_ZENTRAL
        FH_DU__S_FH_ZUDISC = FH_TUERMODUL__SFHZ_MEC
        FH_DU__S_FH_FTZU = FH_TUERMODUL__SFHZ_ZENTRAL
        FH_DU__KL_50 = FH_TUERMODUL__KL_50
        FH_DU__BLOCK = FH_TUERMODUL__BLOCK

        FH_TUERMODUL__SFHA_MEC = FH_DU__S_FH_AUFDISC
        FH_TUERMODUL__SFHA_ZENTRAL = FH_DU__S_FH_FTAUF
        FH_TUERMODUL__SFHZ_MEC = FH_DU__S_FH_ZUDISC
        FH_TUERMODUL__SFHZ_ZENTRAL = FH_DU__S_FH_FTZU

        generic_BLOCK_ERKENNUNG_CTRL()

        FH_DU__MFHA = FH_TUERMODUL__MFHA
        FH_DU__MFHZ = FH_TUERMODUL__MFHZ
        FH_DU__I_EIN = FH_TUERMODUL__I_EIN
        FH_DU__EKS_LEISTE_AKTIV = FH_TUERMODUL__EKS_LEISTE_AKTIV
        FH_DU__POSITION = FH_TUERMODUL__POSITION
        FH_DU__FT = FH_TUERMODUL__FT
        FH_DU__S_FH_AUFDISC = FH_TUERMODUL__SFHA_MEC
        FH_DU__S_FH_FTAUF = FH_TUERMODUL__SFHA_ZENTRAL
        FH_DU__S_FH_ZUDISC = FH_TUERMODUL__SFHZ_MEC
        FH_DU__S_FH_FTZU = FH_TUERMODUL__SFHZ_ZENTRAL
        FH_DU__KL_50 = FH_TUERMODUL__KL_50
        FH_DU__BLOCK = FH_TUERMODUL__BLOCK

        Bitlist[active_KINDERSICHERUNG_CTRL_copy_IDX] = Bitlist[active_KINDERSICHERUNG_CTRL_IDX]
        Bitlist[active_FH_TUERMODUL_CTRL_copy_IDX] = Bitlist[active_FH_TUERMODUL_CTRL_IDX]
        Bitlist[active_EINKLEMMSCHUTZ_CTRL_copy_IDX] = Bitlist[active_EINKLEMMSCHUTZ_CTRL_IDX]
        Bitlist[active_BLOCK_ERKENNUNG_CTRL_copy_IDX] = Bitlist[active_BLOCK_ERKENNUNG_CTRL_IDX]
        FH_TUERMODUL_CTRL__N_old = FH_TUERMODUL_CTRL__N
        FH_TUERMODUL__I_EIN_old = FH_TUERMODUL__I_EIN
        FH_DU__MFH = FH_DU__MFH_copy
        FH_DU__I_EIN_old = FH_DU__I_EIN
        BLOCK_ERKENNUNG_CTRL__N_old = BLOCK_ERKENNUNG_CTRL__N
        FH_TUERMODUL__SFHZ_ZENTRAL_old = FH_TUERMODUL__SFHZ_ZENTRAL
        FH_TUERMODUL__SFHZ_MEC_old = FH_TUERMODUL__SFHZ_MEC
        FH_TUERMODUL__SFHA_ZENTRAL_old = FH_TUERMODUL__SFHA_ZENTRAL
        FH_TUERMODUL__SFHA_MEC_old = FH_TUERMODUL__SFHA_MEC
        FH_TUERMODUL__BLOCK = FH_TUERMODUL__BLOCK_copy
        FH_TUERMODUL__BLOCK_old = FH_TUERMODUL__BLOCK
        FH_TUERMODUL__SFHZ = FH_TUERMODUL__SFHZ_copy
        FH_TUERMODUL__SFHZ_old = FH_TUERMODUL__SFHZ
        FH_TUERMODUL__SFHA = FH_TUERMODUL__SFHA_copy
        FH_TUERMODUL__SFHA_old = FH_TUERMODUL__SFHA
        FH_TUERMODUL__MFHZ = FH_TUERMODUL__MFHZ_copy
        FH_TUERMODUL__MFHZ_old = FH_TUERMODUL__MFHZ
        FH_TUERMODUL__MFHA = FH_TUERMODUL__MFHA_copy
        FH_TUERMODUL__MFHA_old = FH_TUERMODUL__MFHA
        FH_TUERMODUL__EKS_LEISTE_AKTIV_old = FH_TUERMODUL__EKS_LEISTE_AKTIV
        FH_DU__EKS_LEISTE_AKTIV_old = FH_DU__EKS_LEISTE_AKTIV
        FH_DU__S_FH_TMBFAUFCAN_old = FH_DU__S_FH_TMBFAUFCAN
        FH_DU__S_FH_TMBFZUCAN_old = FH_DU__S_FH_TMBFZUCAN
        FH_DU__S_FH_TMBFZUDISC_old = FH_DU__S_FH_TMBFZUDISC
        FH_DU__S_FH_TMBFAUFDISC_old = FH_DU__S_FH_TMBFAUFDISC
        FH_DU__BLOCK = FH_DU__BLOCK_copy
        FH_DU__BLOCK_old = FH_DU__BLOCK
        FH_DU__MFHZ = FH_DU__MFHZ_copy
        FH_DU__MFHZ_old = FH_DU__MFHZ
        FH_DU__MFHA = FH_DU__MFHA_copy
        FH_DU__MFHA_old = FH_DU__MFHA


def benchmark():
    initialise_benchmark()
    result = benchmark_body(SCALE_FACTOR)
    # print("")
    # micropython.mem_info()
    return verify_benchmark(result)


def benchmark_body(lsf):
    global Bitlist
    for lsd_cnt in range(0, lsf):
        Bitlist = [0] * 64
        init()
        interface()
        FH_DU()
    return 0


def initialise_benchmark():
    return


def verify_benchmark(unused):
    global Bitlist, tm_entered_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRLch_BLOCK_ERKENNUNG_CTRL__N_copy, tm_entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRLexited_BEREIT_FH_TUERMODUL_CTRL, tm_entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL, NICHT_INITIALISIERT_NICHT_INITIALISIERT_next_state, ZENTRAL_KINDERSICHERUNG_CTRL_next_state, MEC_KINDERSICHERUNG_CTRL_next_state, KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_next_state, B_FH_TUERMODUL_CTRL_next_state, A_FH_TUERMODUL_CTRL_next_state, WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_next_state, INITIALISIERT_FH_TUERMODUL_CTRL_next_state, TIPP_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state, MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state, OEFFNEN_FH_TUERMODUL_CTRL_next_state, SCHLIESSEN_FH_TUERMODUL_CTRL_next_state, FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_next_state, EINKLEMMSCHUTZ_CTRL_EINKLEMMSCHUTZ_CTRL_next_state, BEWEGUNG_BLOCK_ERKENNUNG_CTRL_next_state, BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_next_state
    expected = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0]
    for (result, expected) in zip(Bitlist, expected):
        if result != expected:
            return False
    if tm_entered_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRLch_BLOCK_ERKENNUNG_CTRL__N_copy != 0 or tm_entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRLexited_BEREIT_FH_TUERMODUL_CTRL != 0 or tm_entered_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL != 0 or NICHT_INITIALISIERT_NICHT_INITIALISIERT_next_state != 0 or ZENTRAL_KINDERSICHERUNG_CTRL_next_state != 0 or MEC_KINDERSICHERUNG_CTRL_next_state != 0 or KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_next_state != 3 or B_FH_TUERMODUL_CTRL_next_state != 2 or A_FH_TUERMODUL_CTRL_next_state != 1 or WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_next_state != 1 or INITIALISIERT_FH_TUERMODUL_CTRL_next_state != 0 or TIPP_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state != 0 or MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_next_state != 0 or OEFFNEN_FH_TUERMODUL_CTRL_next_state != 0 or SCHLIESSEN_FH_TUERMODUL_CTRL_next_state != 0 or FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_next_state != 2 or EINKLEMMSCHUTZ_CTRL_EINKLEMMSCHUTZ_CTRL_next_state != 1 or BEWEGUNG_BLOCK_ERKENNUNG_CTRL_next_state != 0 or BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_next_state != 1:
        return False
    return True
